#!/usr/bin/env python3
"""appeal-maker: rebuild a shot list from a FINISHED video, for channels with no render pipeline.

Works with any production method (editor, AI video tool, human editor): it only needs the final
video file and ffmpeg. It finds the cuts, saves one frame per shot, and writes a manifest skeleton
that annotate-script.py reads. Claude then looks at the frames and fills each shot's "subject"
(from the image prompts if the user has them, else a short description of what is on screen) and
the "ov" overlay list (title / chapter / fact / quote cards seen on screen).

Usage:
  python3 shotlist-from-video.py --video final.mp4 --out <work dir> [--threshold 0.3] [--min-shot 1.5] [--sheets 5]

Writes:
  <work dir>/manifest.json   {"dur", "shots":[{id,start,end,subject:"",kind:"still"}], "ov":[], "chapters":""}
  <work dir>/frames/         "NNN sNNN.jpg", one frame from the middle of each shot (pass as --stills)
  <work dir>/sheets/         with --sheets N: contact sheets, one frame every N seconds, 4x3 tiles,
                             tile i of sheet k (both from 0) = second (k*12 + i) * N. Use them to spot
                             text cards that appear mid-shot.

Tuning: slow zooms and pans never trigger a cut. Crossfades can be missed: lower --threshold
(0.2) if shots are merged, raise it (0.4) if one shot is split in several.

Part of Appeal Maker by Enric (x.com/enricpedro) · factumclub.com
"""
import argparse, json, os, re, subprocess

ap = argparse.ArgumentParser()
ap.add_argument("--video", required=True)
ap.add_argument("--out", required=True)
ap.add_argument("--threshold", type=float, default=0.3)
ap.add_argument("--min-shot", type=float, default=1.5)
ap.add_argument("--sheets", type=float, default=0)
A = ap.parse_args()
os.makedirs(os.path.join(A.out, "frames"), exist_ok=True)

dur = float(subprocess.check_output(
    ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", A.video]).decode().strip())

log = subprocess.run(
    ["ffmpeg", "-hide_banner", "-i", A.video, "-an", "-vf",
     f"scale=320:-2,select='gt(scene,{A.threshold})',showinfo", "-f", "null", "-"],
    capture_output=True, text=True).stderr
cuts = [float(x) for x in re.findall(r"pts_time:([0-9.]+)", log)]

starts = [0.0]
for c in cuts:
    if c - starts[-1] >= A.min_shot and dur - c >= A.min_shot:
        starts.append(c)
shots = []
for i, s in enumerate(starts):
    e = starts[i + 1] if i + 1 < len(starts) else dur
    sid = f"s{i + 1:03d}"
    shots.append({"id": sid, "start": round(s, 3), "end": round(e, 3), "subject": "", "kind": "still"})
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{(s + e) / 2:.3f}", "-i", A.video,
                    "-frames:v", "1", "-q:v", "3", "-vf", "scale=960:-2",
                    os.path.join(A.out, "frames", f"{i + 1:03d} {sid}.jpg")], check=True)

if A.sheets:
    os.makedirs(os.path.join(A.out, "sheets"), exist_ok=True)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", A.video, "-vf",
                    f"fps=1/{A.sheets},scale=480:-2,tile=4x3", "-q:v", "4",
                    os.path.join(A.out, "sheets", "sheet%03d.jpg")], check=True)

json.dump({"dur": round(dur, 3), "shots": shots, "ov": [], "chapters": ""},
          open(os.path.join(A.out, "manifest.json"), "w"), indent=1)
print("duration", round(dur, 1), "cuts found", len(cuts), "shots", len(shots), "->", A.out)
