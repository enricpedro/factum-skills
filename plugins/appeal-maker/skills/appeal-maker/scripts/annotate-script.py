#!/usr/bin/env python3
"""appeal-maker: turn one finished episode into an annotated script (HTML for a Google Doc).

Every scene image, title/chapter card, quote, fact and subscribe prompt is written in as its own
line at the exact sentence where it appears, using the episode's own subtitle timing. The narration
is the real script; nothing is paraphrased.

Inputs (see SKILL.md step 3):
  --manifest  JSON with {"dur", "shots":[{id,start,end,subject,kind}], "ov":[{type,at,payload}], "chapters": "<chapter lines>"}
  --script    the narration script, .md or .txt (if it has a "## SCRIPT" heading, only the text after it
              is used; lines starting with "#" are treated as headings, not narration)
  --srt       the episode's subtitles .srt (editor caption export, YouTube captions, or Whisper)
  --stills    optional: the scene images folder, files named "NNN <shot id> <anything>.jpg"
              (shotlist-from-video.py writes frames/ in this form); without it shots are numbered in order
  --title     optional: the episode title (default: the script's first "# " line)
  --channel-line  e.g. "@YourHandle · https://www.youtube.com/channel/UC..."
  --episode   episode number or label
  --out       output .html

Prints the word-match ratio: it must be ~1.0. Lower means the srt and the script disagree (wrong
version of the script): use the version the video was made from.

Part of Appeal Maker by Enric (x.com/enricpedro) · factumclub.com
"""
import argparse, bisect, difflib, html as _h, json, os, re

ap = argparse.ArgumentParser()
for a in ("manifest", "script", "srt", "channel-line", "out"):
    ap.add_argument("--" + a, required=True)
ap.add_argument("--stills")
ap.add_argument("--title")
ap.add_argument("--episode", required=True)
A = ap.parse_args()
esc = lambda x: _h.escape(x, quote=False)
norm = lambda w: re.sub(r"[^a-z0-9]", "", w.lower())
mmss = lambda t: f"{int(t)//60}:{int(t)%60:02d}"

m = json.load(open(A.manifest))
txt = open(A.script).read()
body = (txt.split("## SCRIPT", 1)[1] if "## SCRIPT" in txt else txt).split("<!-- COMPLIANCE")[0].strip()
paras = [p.strip() for p in body.split("\n") if p.strip() and p.strip() != "---" and not p.strip().startswith("#")]
toks = [(norm(mt.group()), pi, mt.start()) for pi, p in enumerate(paras) for mt in re.finditer(r"\S+", p) if norm(mt.group())]

def tsec(s):
    h, mi, x = s.split(":"); return int(h) * 3600 + int(mi) * 60 + float(x.replace(",", "."))
sw = []
for blk in open(A.srt).read().strip().split("\n\n"):
    L = blk.split("\n"); a, b = L[1].split(" --> "); t0, t1 = tsec(a), tsec(b)
    ws = " ".join(L[2:]).split()
    sw += [(norm(w), t0 + (t1 - t0) * i / max(1, len(ws))) for i, w in enumerate(ws) if norm(w)]
sm = difflib.SequenceMatcher(None, [t[0] for t in toks], [w[0] for w in sw], autojunk=False)
s2t = {b + k: a + k for a, b, n in sm.get_matching_blocks() for k in range(n)}
times = [w[1] for w in sw]

def pos(t):
    j = bisect.bisect_left(times, t - 0.05)
    while j < len(sw) and j not in s2t: j += 1
    if j >= len(sw): return (len(paras) - 1, len(paras[-1]))
    _, pi, off = toks[s2t[j]]; p = paras[pi]
    cut = max([0] + [mm.end() for mm in re.finditer(r'[.!?]["”\']?\s+', p[:off + 1])])
    return (pi, cut)

if A.stills:
    stills = {os.path.splitext(f)[0].split(" ")[1]: f.split(" ")[0] for f in os.listdir(A.stills) if " " in f}
else:
    stills = {s["id"]: f"{i + 1:03d}" for i, s in enumerate(m["shots"])}
ins = {}
add = lambda t, o, h: ins.setdefault(pos(t), []).append((t, o, h))
for s in m["shots"]:
    subj = s.get("subject") or ""
    subj = subj if len(subj) < 170 else subj[:167].rsplit(" ", 1)[0] + "..."
    kind = s.get("kind")
    if kind == "presenter":
        add(s["start"], 2, f'<p style="color:#b45309"><b>[HOST ON CAMERA · {mmss(s["start"])}]</b> the presenter speaks this passage to camera</p>')
        continue
    if kind == "split":
        add(s["start"], 2, f'<p style="color:#b45309"><b>[HOST + IMAGE SPLIT · {mmss(s["start"])}]</b> presenter on one side, the image on the other{": <i>" + esc(subj) + "</i>" if subj else ""}</p>')
        continue
    anim = " (animated)" if kind in ("motion", "clip", "video") else ""
    add(s["start"], 2, f'<p style="color:#1a56db"><b>[IMAGE {stills.get(s["id"], "?")} · {mmss(s["start"])}{anim}]</b> <i>{esc(subj)}</i></p>')
chapters = [l.split(" ", 1) for l in m.get("chapters", "").strip().split("\n") if l.strip()]
for e in m.get("ov", []):
    t, p = e["at"], e.get("payload", {})
    ty = e["type"]
    if ty == "title_card":
        add(t, 0, f'<p style="color:#7c3aed"><b>[TITLE CARD · 0:00]</b> "{esc(p.get("title",""))}"{", with the line " + chr(34) + esc(p["kicker"]) + chr(34) if p.get("kicker") else ""}.</p>')
    elif ty == "chapter_card":
        add(t, 1, f'<h2>CHAPTER {p.get("n","")} · {mmss(t)} · {esc(p.get("title",""))}</h2><p style="color:#7c3aed"><b>[CHAPTER CARD]</b> "{esc(p.get("title",""))}"</p>')
    elif ty == "fact":
        add(t, 3, f'<p style="color:#047857"><b>[ON-SCREEN FACT · {mmss(t)}]</b> {esc(re.sub(r"[*][*](.+?)[*][*]", r"\1", p.get("text","")))}</p>')
    elif ty == "quote":
        add(t, 3, f'<p style="color:#7c3aed"><b>[ON-SCREEN QUOTE · {mmss(t)}]</b> "{esc(p.get("quote",""))}" ({esc(p.get("source",""))})</p>')
    elif ty == "name_tag":
        add(t, 3, f'<p style="color:#7c3aed"><b>[NAME TAG · {mmss(t)}]</b> {esc(p.get("name",""))}: {esc(p.get("line",""))}</p>')
    elif ty == "date":
        add(t, 3, f'<p style="color:#7c3aed"><b>[DATE CARD · {mmss(t)}]</b> {esc(str(p.get("year","")))}</p>')
    elif ty == "map":
        add(t, 3, f'<p style="color:#7c3aed"><b>[MAP · {mmss(t)}]</b> {esc(p.get("place",""))}</p>')
    elif ty == "highlight":
        add(t, 3, f'<p style="color:#7c3aed"><b>[HIGHLIGHT · {mmss(t)}]</b> {esc(p.get("shape","mark"))} drawn on {esc(p.get("target",""))}</p>')
    elif ty == "subscribe":
        add(t, 3, f'<p style="color:#7c3aed"><b>[SUBSCRIBE PROMPT · {mmss(t)}]</b></p>')
    else:
        add(t, 3, f'<p style="color:#7c3aed"><b>[{esc(ty.upper().replace("_"," "))} · {mmss(t)}]</b> {esc(" · ".join(str(v) for v in p.values() if isinstance(v, str))[:200])}</p>')
if chapters:
    add(0, 0.5, f'<h2>OPENING · 0:00 · {esc(chapters[0][1])}</h2>')

out = []
for pi, p in enumerate(paras):
    cuts = sorted({off for (q, off) in ins if q == pi}); segs, last = [], 0
    for c in cuts:
        if c > last: segs.append(("t", p[last:c]))
        segs.append(("c", c)); last = c
    segs.append(("t", p[last:])); buf = []
    for k, v in segs:
        if k == "t":
            if v.strip(): buf.append(esc(v.strip()))
        else:
            if buf: out.append("<p>" + " ".join(buf) + "</p>"); buf = []
            out += [h for _, _, h in sorted(ins[(pi, v)], key=lambda x: (x[0] if x[1] != 0.5 else -1, x[1]))]
    if buf: out.append("<p>" + " ".join(buf) + "</p>")

first = txt.split("\n", 1)[0]
title = A.title or (first.lstrip("# ").split(": ", 1)[-1] if first.startswith("# ") else "")
nfact = sum(1 for e in m.get("ov", []) if e["type"] == "fact")
head = f'''<h1>Episode {esc(A.episode)}</h1><h2>{esc(title)}</h2>
<p><b>Channel:</b> {esc(A.channel_line)}<br><b>Running time:</b> {mmss(m["dur"])} · <b>Script:</b> {len(" ".join(paras).split()):,} words · <b>Scenes:</b> {len(m["shots"])} images, {len(chapters)} chapters{f", {nfact} on-screen facts" if nfact else ""}</p>
<h3>Chapters</h3><p>{"<br>".join(esc(c[0] + " " + c[1]) for c in chapters if len(c) == 2)}</p>
<h3>Key</h3><p style="color:#1a56db"><b>[IMAGE nnn · time]</b> the scene image shown from this line on; the number matches the file in the episode's Stills folder, the italic text is the scene description it was made from. (animated) = a short moving clip made from that image.</p>
<p style="color:#b45309"><b>[HOST ON CAMERA] [HOST + IMAGE SPLIT]</b> the channel's presenter on screen (channels with a host).</p>
<p style="color:#7c3aed"><b>[TITLE CARD] [CHAPTER CARD] [NAME TAG] [DATE CARD] [MAP] [HIGHLIGHT] [ON-SCREEN QUOTE] [SUBSCRIBE PROMPT]</b> graphics laid over the picture.</p>
<p style="color:#047857"><b>[ON-SCREEN FACT]</b> a real fact shown on screen.</p><p>Plain text is the narration.</p><hr>'''
open(A.out, "w").write('<html><body style="font-family:Georgia">' + head + "\n".join(out) + "</body></html>")
print("match", round(len(s2t) / max(1, len(toks)), 3), "missing stills", sum(1 for s in m["shots"] if s["id"] not in stills and s.get("kind") not in ("presenter", "split")), "bytes", os.path.getsize(A.out))
