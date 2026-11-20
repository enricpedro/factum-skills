---
name: appeal-maker
description: Handle a YouTube Partner Program rejection or suspension for reused content, generic / repetitive content, or unsatisfying / off-putting content (the inauthentic-content branches), in any niche and with any production method - pick the right route (appeal or edit-and-reapply), build the appeal video script plus every Google Doc and media file it shows (channel bible, production rules, episode docs, range grid, story arcs or comparison, annotated script with image and card placement, voiceover MP3, layers demo), and say how to avoid that rejection in future. Use when the user says a channel was rejected, suspended or demonetized for reused, generic/repetitive or unsatisfying/off-putting content, asks for an appeal, an appeal video, an appeal script, or "appeal maker".
---

# Appeal maker

Made by Enric ([x.com/enricpedro](https://x.com/enricpedro)) · [factumclub.com](https://factumclub.com).
Latest version, install and usage guide: https://github.com/enricpedro/factum-skills

**Paths:** `<skill dir>` below is this skill's own folder, the base directory Claude Code shows when
the skill loads (`~/.claude/skills/appeal-maker` for a manual install, the plugin cache for a plugin
install). The two helper scripts are in `<skill dir>/scripts/`.

## Track record and what it means

| Rejection reason | Appeals made with this method | Outcome |
|---|---|---|
| Reused content (story channel, AI images, licensed TTS) | 1 | monetized |
| Reused content (history channels using public-domain archive photos) | 2 | both monetized |
| Generic or repetitive content (story channel) | 1 | refused |
| Unsatisfying or off-putting content | 0 | no track record yet |

**The reused-content recipe is proven (3 of 3). The same recipe has NOT worked for generic or
repetitive content.** Public creator reports agree: reused-content appeals on AI story channels often
win, generic/repetitive appeals on story or narration channels almost never do (0 wins in about 12
public cases found, Nov 2026). For unsatisfying or off-putting content no documented win was found
(Nov 2026): treat it like generic or repetitive. Pick the route and the argument by the rejection
reason, below, before building anything. When the user reports an outcome, tell them to add it to this table with one line
on what it teaches.

## Read the rejection screen first: which option, which policy

Studio shows two options. They are different strategies; never mix their logic.

- **Option 1, Appeal by sending a video.** YouTube's wording: "If you think we made a mistake, submit
  an appeal telling us why." The appeal DEFENDS THE CHANNEL AS IT STANDS. Only condition: "Only choose
  this option if you haven't deleted any videos since your channel was suspended." The screen also
  warns that if the appeal fails, "any other channels you may operate are also at risk of suspension
  from YPP." A deadline is shown.
- **Option 2, Edit your channel and reapply.** "Make changes to your channel. Changes can include
  editing or deleting videos and updating video details." Reapply from a date about 90 days out.

**Official facts** (YouTube Help, checked Nov 2026: support.google.com/youtube/answer/9564590,
/1311392, /1727191, /9235730):
- **The policy.** "Generic or Repetitive Content" is the July 2026 name of what was "inauthentic" /
  "repetitious" content; YouTube said the policy itself did not change. Not allowed: content that looks
  made with a template, minimal variation between videos, "characters put in the same situation over
  and over again with the same outcome", image slideshows or templated storylines with little
  narrative, AI content from generic templates "giving the impression of mass production". Allowed: the
  same intro and outro when the body differs; recurring formats where each video has its own story,
  focus or concept; AI used to edit scripts or make unique visuals.
- **"Inauthentic content" has three branches** (YouTube's July 2026 clarification, as reported by
  Dexerto, Moneywise, Search Engine Journal and Metricool): (1) generic or repetitive, above;
  (2) **unsatisfying or off-putting**: emotionally manipulative formulas, shock or surprise purely for
  views, nonsensical content (YouTube's example: an animal seemingly in distress, conveniently
  rescued), with or without AI; (3) **AI personas on sensitive topics**: an AI presenter giving health,
  legal, money or political information as if a human expert. Likes, comments and retention protect
  against none of them: the review judges whether the format is suitable, not whether it is popular.
- **How a story channel trips "unsatisfying or off-putting".** These causes come from Pedro
  ([@howtopedro](https://x.com/howtopedro)), a creator with years in the YouTube space, and match the
  public reports:
  - **Emotional-bait titles and premises** built on humiliation, a deception or test, a hidden
    identity or a staged misunderstanding ("Everyone laughed at her old dress, until...", "not
    knowing...", "dressed in rags to test the bride"), even when the ending is wholesome.
  - **Series production with no visible human hand**: daily uploads of a near-fixed long runtime,
    photoreal AI stills acting as slides, synthetic narration, recognisable AI script shapes. Together
    they read as a content farm with no "meaningful creative value".
  - **Incoherence**: pictures that do not match the narration, characters whose face or clothes change
    between shots, plots that circle to stretch the runtime. Reviewers find it by sampling random
    moments of a video.
  - The last two causes also drive generic or repetitive rejections.
- **Odds for "unsatisfying or off-putting"**: no documented win found (Nov 2026). As with generic or
  repetitive, the reapply after a cleanup is the main route and the appeal a cheap extra.
- **What reviewers look at.** They "can't check every video": the main theme, the NEWEST and MOST
  VIEWED videos, the biggest share of watch time, titles, thumbnails, descriptions and the About.
- **Appeal mechanics.** About 21 days to appeal (7 for a scheduled suspension); decision within 14
  days. The video: under 5 minutes, unlisted, on the same channel, the channel URL in the first 30
  seconds, about the channel AS A WHOLE and how it is made. It is judged on the channel's CURRENT
  state. Do not delete videos before appealing. The appeal video must stay on the channel. A failed
  appeal cannot be appealed again.
- **The 90 days run from the SUSPENSION**, appeal or not: a failed appeal costs no reapply time.
- **Other channels.** While one channel's suspension is unresolved, YouTube can stop monetization on
  "all other channels that you operate, create, or acquire", and new YPP applications are rejected
  until it is resolved. Creator reports show this spreading mostly between channels on the same
  AdSense account; how YouTube links channels is not published, so never claim a mechanism.
  Circumventing the suspension (moving the content to other channels, applying with related channels)
  is the named route to termination of ALL channels.
- Newly monetized channels are often re-reviewed and pulled 1 to 4 weeks after approval: an appeal
  can be about a channel that WAS monetized.

**Rules that follow:**
- **During any suspension**, tell the user to hold every YPP application or reapplication on their
  other channels until it is resolved. Never suggest deleting the suspended channel, moving AdSense, or
  making channels look unrelated (all three are circumvention).
- **On Option 1, do not push channel changes** (retitles, About rewrites, deleting or privating
  videos). Audit findings (Step 0) go to the user as RISKS, one line each, their call. Never delete
  anything on this route. Editing titles or thumbnails before an appeal is allowed (only deleting is
  warned against) but its benefit is unproven, and a few freshly changed videos on an otherwise
  templated channel reads as "not representative": if the user wants changes, they are channel-wide.
- **Option 2's fix list** is for the reapply route only, and only when the user chooses it: rotate
  title shapes (no one formula) and vary thumbnails (Step 0b), private or delete the closest near-duplicates (paced,
  about 10 a day, watching the 4,000 watch-hour floor, since private and deleted videos stop counting),
  vary the visuals, add a visible human presence (banner, trailer, an About that names the author),
  set the "altered or synthetic content" disclosure where it applies, keep uploading varied videos.
- **Do not open with a menu of routes.** When the user says appeal, build the appeal. Give the odds
  and the related-channel risk once, factually, never to steer them away from appealing.
- **For generic / repetitive and for unsatisfying / off-putting**, say once that the reapply after a
  visibly varied, cleaned-up catalogue is the documented winning route and the appeal is a cheap extra
  (no time cost). Suggest submitting near the
  deadline. After a refusal, a live-chat escalation through Creator Support has one documented
  overturn; contacting TeamYouTube otherwise changes nothing.
- **The honest grid test before an appeal**: open the Videos tab as a stranger and watch 3 videos in a
  row. If they read as the same beats with names swapped, tell the user plainly; a weak,
  factory-looking appeal video stays on the channel for good and a reapply reviewer may watch it.
- **Never reveal a multi-channel operation in the appeal.** The policy's phrase is "the impression of
  mass production": show human authorship of THIS channel only.

## Which argument per policy

- **Reused content** ("is this material yours?"): everything heard and seen was made for the channel,
  or transformed (archive channels: transformative use, see that section). Two published episodes side
  by side + one episode walked through from brief to finished edit.
- **Generic or repetitive content** ("can a viewer tell these videos apart, and do they add real
  creative or educational value?"): ownership is not the question, so a 2-episode comparison is too
  thin: the reviewer scrolls the whole Videos tab and judges the catalogue. The argument is RANGE and
  VALUE across the channel:
  1. A **range grid of 8 to 10 published episodes** (a Doc table, plus the watch pages on screen): per
     episode the setting, the central figure, the conflict, the turn, the ending, and the real facts
     it teaches. Pick the episodes that differ the most; include high performers and recent ones.
  2. **The rules that force difference**: the channel's rotation / variety rules (e.g. a set of story
     slots, each episode differing from the previous few on several named points), as a reviewer-clean
     doc. This answers "is it a template?" with the mechanism, not only examples. If the channel has no
     such rules, do not invent them: say so to the user, and present only what is really practised.
  3. **The value layer**: the on-screen facts across the grid episodes, counted ("N distinct facts
     across these 10 episodes"), and sources or research where the channel keeps them.
  4. **One episode walked through** (brief to finished edit), as in the reused recipe, shorter.
  5. Viewer comments that talk about a SPECIFIC story or fact (the user copies them; real only).
  6. **Not a factory**: the grid gets a RUNTIME column showing the length follows the story (a real
     spread, not one target); the walkthrough adds a short "decisions a person made" beat (which brief
     was picked and why, a rejected draft or image, an edit made at a review pass); the channel's ONE
     defined look and its consistent cast are shown as a series with an author. Only what is real.
  Be honest with the user about what the catalogue shows (title templates, near-twins, viewer comments
  calling two episodes the same, a fixed runtime, a daily cadence): name them as risks, then build the
  strongest true case.
- **Unsatisfying or off-putting content** ("is this built to manipulate, shock or confuse, without
  real creative or educational value?"): ownership and variety are not the question. The argument is
  that the emotion is EARNED and the work is COHERENT:
  1. **Earned emotion, a real arc**: 3 to 4 published episodes summarised as arcs (setup, the
     characters' own choices, the turn, the resolution), showing the story moves by what people decide,
     not by a staged cruelty or reveal. Pick episodes whose titles name a journey, a place or a real
     dilemma; keep bait-titled ones off screen and list them to the user as risks.
  2. **The value layer** (as in generic / repetitive): real facts on screen, counted.
  3. **Coherence as a system**: how the channel keeps picture, words and faces together. One real
     example each, only of what the channel really does: an image checked against the line it sits
     under and redone when it did not match (your own check that each image matches its line), a
     reference portrait reused for a recurring character across scenes, a problem caught in a review
     pass before upload and fixed; and that the length is set by the story. **If the evidence
     inventory says the creator does not run a check (for example, images are NOT checked against
     their lines), drop that claim EVERYWHERE**: the bible, the rules doc, every chapter of the appeal
     script and the upload description. Lean on the checks they really run; if they run none, leave
     coherence out of the argument and tell the user it is a weak point.
  4. **One episode walked through** (brief to finished edit), shorter.
  Never call invented stories "true": say "original stories" (set in real history, or the niche's
  equivalent).
- **AI persona on sensitive topics**: relevant only if the channel's presenter gives health, legal,
  money or political information. Step 0 checks it. A designed digital host on non-advice topics is
  described as "a digital host we designed for the channel", never as a person or an expert. If the
  host does give that kind of advice, tell the user plainly that the format itself is the problem and
  the reapply route (with the format changed) is the realistic one.

Either way: wrapped in a face-cam open and close, a real person, calm, says they know the rules and
follow them. Chapter 1 opens by answering the stated policy (Step 5).

## How to avoid it next time (part of EVERY appeal reply)

The reply that delivers the kit ends with a short "How to avoid this next time" section for the
rejected policy: what triggered it on THIS channel (from Step 0, with the counts), the forward rules
below, and the decisions for the creator that apply. Plain words, one line each. These are forward
production rules: on Option 1 they never become edits to the published channel.

- **Reused content**: everything heard is the channel's own; archive pictures always transformed
  (chosen for one line, reframed, moved, explained with the channel's own facts, maps and captions);
  no clips, readings or narration from others; keep the transformation visible in the first minutes,
  where reviewers look.
- **Generic or repetitive**: no title shape on more than 1 in 4 of the last 30, never the same shape
  twice running; rotate premise, turn and structure, not only names; every episode carries substance a
  template cannot produce (real facts, sources, analysis); let the story set the runtime (a real
  spread, not one target); a cadence a person could keep, publish times not fixed to the minute; one
  defined look with a consistent cast; near-twins never published close together.
- **Unsatisfying or off-putting**: titles from the story's journey, place or real dilemma, not the
  humiliation / test / hidden-identity / "until" / "not knowing" shapes; vary the hook so no bait type
  is on more than 1 in 4; the emotion comes from the characters' own choices, not a staged cruelty or
  misunderstanding; every picture matches the words over it; faces and clothes stay the same across a
  story (a reference portrait per recurring character); no padding to reach a length; fewer, better
  pictures in one style beat hundreds of near-matches; a review pass before upload that catches
  mismatched or inconsistent shots.
- **AI persona on sensitive topics**: a digital host never gives health, legal, money or political
  advice as an expert; keep host channels on non-advice topics.
- Before the next uploads or the reapply, run the Step 0 audit again on the channel (and on any other
  channels on the same AdSense account) and fix what it finds.

For the **unsatisfying or off-putting** route, the section written for the user ends with this line,
as is: "The causes behind this rejection type come from Pedro ([@howtopedro](https://x.com/howtopedro))."

**Decisions for the creator** (neutral: raise the ones that apply, one line each, with the trade-off;
never apply or recommend one by default):
1. Studio's "altered or synthetic content" toggle on realistic AI pictures.
2. A real human presence: a short intro in the creator's own voice or on camera, the process explained
   in the About. Never claim a human narrator when a licensed voice narrates.
3. Dropping bait title formulas (it usually costs click-through rate).
4. Fewer uploads and natural lengths (cadence is a production decision).
5. One illustrated style instead of photoreal pictures.

## Setup: the evidence inventory (always first)

This skill works with ANY production method. Never assume a particular tool or pipeline: the appeal
shows the user's real process, so first find out what that process is and what proof of it exists.
Ask once, then reuse the answers for the rest of the session:

1. Channel URL (only the URL: derive the channel ID yourself, e.g. `yt-dlp --print channel_id
   --playlist-items 1 <channel URL>/videos`, or from the page), the exact rejection reason, which
   options the Studio screen offers, and the deadline. Whether the user runs other monetized channels
   (related-channel risk).
2. How an episode is made, step by step, and with what. Common shapes:
   - **Video editor** (Premiere, DaVinci, CapCut, Final Cut): the edit project is the proof.
   - **All-in-one AI video tool** (script in, video out): the tool's project page, its scene list and
     the assets it exported are the proof; screenshots are fine.
   - **Human editor**: the editor's timeline screenshots and the files handed to them.
   - **Own automation / render pipeline**: whatever shot list, logs or project files it writes.
   - Who or what writes the script, makes the images / footage, and voices it (human narrator, TTS,
     avatar host). Show only steps that are real.
3. Then build the inventory as a table: for each layer (channel bible or style notes, variety rules,
   briefs, script, images / footage, image prompts, voiceover, music, subtitles, on-screen cards, edit
   project, final video), whether it exists and where. Missing layers are fine; the appeal shows what
   exists.
4. For an **unsatisfying or off-putting** rejection, also ask for proof of coherence, if any exists:
   checks that each image matches its line (and images redone after one), reference portraits reused
   for recurring characters, notes from a review pass before upload, and how runtime is decided. Mark
   each check in the inventory as "done" or "not done", and never present a check marked "not done"
   (or one the user does not really run) in any doc, chapter or description.

**Where the files are.** Claude reads files straight from the computer; nothing is linked or
configured. Work from the folder Claude Code was started in. For files elsewhere, ask for the path (the
user can run `/add-dir <folder>` once to stop permission prompts). Files in Dropbox, Google Drive or
iCloud must be synced and available offline: "online only" files read as 0 bytes. If a file looks
empty or missing, say so and ask; never build a doc from a file you could not read. Nothing carries
over between sessions, so ask again in a new one.

**Keep every working file inside the appeal folder.** Frames, contact sheets, captions, manifests,
downloads and any helper Python venv go in an `appeal-work/` folder inside it, never in /tmp or
another system folder: the user must be able to find, re-run and delete them, and /tmp can be wiped.

**The minimum kit is the final video file plus its script.** Everything else makes the appeal
stronger. If there is no written channel bible or rules, write them WITH the user from how they
actually work (interview them), never invent rules they do not follow.

**No final video file?** Common on long-form channels: exports get deleted to save space, and Studio
downloads of long videos often fail. Do not stall on it; use this path:
- **Subtitles and script stand-in:** YouTube's own captions of the published video, via yt-dlp
  (Step 3b). They stand in for the .srt, and for the script when the user has no copy of it.
- **Layers demo:** a screen recording of the editor's timeline playing (or the AI tool's project
  page), made by the user.
- **Voiceover:** exported by the user from the edit with the music muted.
- **Frames:** pulled from the published video (Step 3c).
Tell the user UPFRONT, in one short list, which of these pieces are their homework (typically the
timeline recording and the voiceover export), so they can make them while you build the docs.

Tools: Google Drive (connector, or upload HTML files by hand), something to list the channel's
published videos and read its About (a YouTube data connector, the YouTube Data API, `yt-dlp`, or
the user pastes it), ffmpeg locally; optionally Premiere Pro with the `premiere-pro` MCP (Step 4b).

## Hard rules

- **Never state a falsehood to YouTube.** No "I write every word by hand", no "a freelancer made the
  images", no "I narrate it myself" when a TTS voice does, no presenting an AI avatar host as a real
  person. Example appeals online advise exactly that; the proven appeals dropped it and still won.
  Truthful phrasings that work:
  - voice: "recorded from our final script with a licensed narration voice"
  - images: "made for this episode from our own written description of each scene"
  - host avatar (persona channels): "our presenter, a digital host we designed for the channel", never
    a person or an expert
  - scripts: "written for the channel, revised in several passes before approval" (say the real number)
  - invented stories: "original stories set in real history" (or the niche's equivalent), never "true
    stories"
- **Check AI disclosure BEFORE recording.** Look at the descriptions of the episodes you will show:
  fiction disclaimer yes/no, production disclosure yes/no, Studio's "Altered or synthetic content"
  toggle yes/no. Either the user adds the disclosure and ticks the toggle on the episodes shown, or the
  appeal never claims disclosure. Do not edit descriptions yourself; flag it in the checklist.
- **Clean internal docs before showing them.** Bibles, briefs and research docs usually contain view
  counts, CTR, "copy competitor X's structure", references to other channels. Showing those to a
  reviewer argues the opposite of originality. Make reviewer versions: keep the real creative content,
  drop metrics and competitor language, add nothing that is not true.
- **Reviewer docs must match the CURRENT rules.** A rule change (title formula, endings, card
  position, look) makes an older reviewer doc false: re-read every doc against the current bible.
- **Never show internal dashboards or tools** unless the user asks: Google Docs and plain files read
  best on screen.
- **Never present a generated sample as part of a published video.** If cards were rendered for the
  appeal, call them "the format", never "from episode N" unless that video has them.
- **Nothing about the appeal in the appeal video's description** (YouTube's rule); the description
  describes the channel and how it is made.
- Quotes from viewers must be real, copied by the user from the comments. Leave a placeholder.
- Never mention reuse across the user's channels (a host avatar, voice or footage shared with another
  channel) in the appeal; do tell the user privately if it applies, as a risk.

## Step 0. Audit the channel BEFORE building anything

The rejection is about the CHANNEL as a reviewer sees it, so check what they see first. **What
happens with the findings depends on the route**: on Option 1 they are risks for the user (one line
each, their call, nothing changed by default, nothing ever deleted); on Option 2 they become the fix
list. They go at the top of the appeal script under "Before you record". An identity that is
factually wrong (the channel still carries another channel's name or persona) is the one finding worth
recommending on either route, as a correction:
- **Identity matches content.** Name, handle, About text, avatar, banner. A channel branded as an old
  persona, or with an About describing something other than what every video says, is exactly what
  "generic / inauthentic" looks like. Also check the About still describes the channel truly (it often
  goes stale after a change of look or format) and whether it describes ONE plot, which reads as a
  template.
- **Title templates.** Read the published titles: three or more on one fill-in-the-blank template
  reads as repetitive. Count it ("N of M titles on one shape") so the risk is concrete. Flag it as the
  user's call (retitling can cost CTR); never retitle yourself.
- **Thumbnails.** One layout on every video reads as packaging sameness, often the first thing flagged.
- **Bait titles** (unsatisfying / off-putting, and repetitive). Count the titles whose hook is
  humiliation, a deception or test, a hidden identity, a staged misunderstanding or a rescue from
  distress ("until", "not knowing", "to test", "in rags", "laughed at"), e.g. "12 of the last 30".
- **Cadence, runtime and twins.** Uploads per week; the runtime spread of the last 30 (the share
  within 10% of the median runtime): daily uploads at a near-fixed long length read as a content farm.
  Episodes that viewers (or the user's own notes) call near-identical. Risks for a repetitive review;
  keep near-twins out of the grid and the comparison.
- **Random-moment coherence** (how reviewers sample). Pull frames at 6 to 8 random points of the two
  newest long videos and compare each frame with the words heard there (subtitles or a transcript);
  look for faces or clothes that change between shots of the same character, and for a plot that
  circles to stretch the runtime. Each hit is a risk line; keep those videos out of the appeal.
- **AI persona check.** Does any presenter give health, legal, money or political information?
- **Disclosure.** As in the hard rules.

## Step 0b. Titles and thumbnails: suggestions by rejection type

Titles and thumbnails are public: read them without the user's files. List the channel's videos with
their titles and views (`yt-dlp --flat-playlist --print "%(id)s|%(title)s|%(view_count)s"
https://www.youtube.com/@<handle>/videos`, a YouTube data connector, or the user pastes them), and
look at the thumbnails (`https://i.ytimg.com/vi/<id>/hqdefault.jpg`). Claude never touches Studio: the
user applies every change by hand.

- **Reused content: packaging is not the argument.** Leave titles and thumbnails alone unless one
  copies another creator (the same thumbnail image as a source video, a title lifted word for word) or
  promises something the video does not have. Suggest those few fixes only.
- **Generic or repetitive content: packaging is usually the first thing flagged** (reviewers look at
  titles and thumbnails by name, and one title formula plus one thumbnail layout is the most reported
  trigger). Build a **"Titles and Thumbnails" sheet** (a Doc table), one row per video, in this order:
  the reviewer's sample first (the ~15 newest, then the ~10 most viewed), then the rest. Columns:
  current title, suggested title, its title shape, what the thumbnail shows now, a thumbnail brief.
  - **Titles:** name the shapes in use first and count them. No shape on more than about 1 in 4
    videos, never the same shape on two videos in a row (publish order). Lead with what is specific to
    that video (the person, the place, the object, the event). A brand word that clearly drives clicks
    can stay if the rest of the title varies around it. Keep the payoff honest (the video must deliver
    it), keep the key words in the first ~60 characters, 100 max. Never copy a competitor's title.
  - **Thumbnails:** the scene comes from THAT video's story (its place, time of day or season, who is
    there, the key object), so two thumbnails can never be swapped. The channel's look stays fixed
    (palette, type, framing style) so the brand stays recognisable. No two neighbouring videos with
    the same composition, the same face or the same colour. Thumbnail text, if used, differs per video.
    Check every brief against the video: nothing on it that the video does not show. This skill writes
    briefs; the user makes the images with their own tool.
  - **Mark the top performers.** Retitling can cost clicks on videos that work: flag them so the user
    can choose to keep their title and change only the thumbnail.
  - **Future uploads:** add a rotation plan for the next 10 titles (which shape each one uses).
- **Unsatisfying or off-putting content: the titles and thumbnails ARE part of the trigger** (the bait
  premise is sold there). Build the same "Titles and Thumbnails" sheet, with these changes:
  - **Titles:** flag every bait title from Step 0 (humiliation, deception or test, hidden identity,
    staged misunderstanding, rescue from distress, "until", "not knowing"). The suggested title leads
    with the story's journey, place or real dilemma and still promises what the video delivers. No
    bait shape on more than about 1 in 4 if the user keeps some. Dropping them usually costs clicks:
    say so, it is the user's call.
  - **Thumbnails:** no staged humiliation, distress or shock scene the video does not resolve
    honestly; the scene shows a real moment of that story, with the same face and clothes the
    character has in the video.
- **By route:** on Option 1 the sheet is a suggestion and stays the user's call. If they apply it,
  apply it channel-wide (at least the whole reviewer sample) before submitting, never to a handful of
  videos, and never delete anything. On Option 2 it is part of the fix list: apply it before
  reapplying, and keep every new upload on the rotation.

## Step 1. Pick the episodes

List the channel's published videos (most popular first, and newest first).

- **Comparison pair (reused; 2 published):** the reviewer can open them. Pick the two that look MOST
  different for the niche: different protagonist / subject / era / place / mechanism. Prefer the best
  performers (the reviewer may already have looked at them). Story channels: different premise
  engines. Documentary channels: different subjects AND different structure. Host channels: different
  topics and different sets / looks if the channel has them.
- **Range grid (generic / repetitive; 8 to 10 published):** the most different episodes across the
  catalogue, including top performers and recent uploads (the reviewer's sample), no near-twins.
- **Arcs (unsatisfying / off-putting; 3 to 4 published):** episodes whose story moves by the
  characters' own choices, with titles that name a journey, a place or a real dilemma, and that passed
  the random-moment coherence check. No bait-titled episode, none with a mismatch found in Step 0.
  **Fewer than 3 clean episodes?** Use the ones you have (even 1 or 2), tell the user plainly that the
  case is weak because the catalogue has few clean stories, and put more weight on the Option 2 framing
  (fix the catalogue and reapply; the appeal is a cheap extra). Never fill a slot with a borderline
  episode (a reveal-driven turn, padding, a repeated scene, a title the video does not deliver) without
  naming the compromise to the user and letting them decide.
- **Walkthrough episode (1, every policy):** the recent episode with the most layers still on disk
  per the inventory (script, images or footage, prompts, voiceover, edit project). Finished but not yet
  published is ideal (it shows the next video is original too); a published one works. Prefer the
  newest, so it shows the channel's current format.

## Step 2. The channel documents (Google Drive folder)

Create one Drive folder "<Channel> - Monetization Appeal". Write each doc as HTML and upload it with
`text/html` as the content type: Drive converts it to a formatted Google Doc. Without a Drive
connector, the user uploads the HTML files by hand: tell them an uploaded .html becomes a Google Doc
only when Drive's "Convert uploads" setting is on (Drive > Settings); otherwise they right-click the
file > Open with > Google Docs. If the Drive tool cannot
edit a Doc's content later, fix one by recreating it and trashing the old one. Avoid nested lists
inside `<ol>` (Drive renumbers every item "1."). Images embed fine as `<img src="...">` with a direct
public link.

1. **Channel Bible (reviewer version):** what the channel is, audience, the world / subject scope, how
   every episode is built, narrator / host, episode structure, look and sound, titles / thumbnails /
   descriptions, guardrails.
2. **Writing and Production Rules:** the real pipeline as steps with their checks - brief, script
   (voice and rhythm, banned phrases, structure, length band), revision passes, scene images
   (descriptions, character consistency, period / subject accuracy, rejects remade), narration, edit
   (cards, overlays, final check), packaging (title, thumbnail, description). Documentary channels add
   sourcing and fact checks; host channels add the presenter step.
3. **One doc PER EPISODE, never one combined briefs doc.** Each published comparison episode gets its
   own doc with its brief / synopsis AND its full narration script, plus chapters, runtime, word count
   and YouTube URL. Write the synopsis of a published episode from its description and script (names
   can change between brief and script). The walkthrough episode gets its brief doc.
4. **Reused: the comparison doc.** A table of the pair - title, protagonist / subject, who or what
   drives it, setting, the hook, the central question, the turn, the payoff, runtime, words, chapters,
   publish date. Close with what is unique per episode, and be exact about anything shared (e.g. a
   standing subscribe line).
5. **Generic / repetitive: the range grid doc** (one row per episode: title, URL, setting, central
   figure, conflict, turn, ending, real facts taught, runtime, publish date), **the variety rules
   doc** (Step 1 of "Which argument"), and the fact count.
6. **Unsatisfying / off-putting: the arcs doc** (one section per episode: title, URL, setup, the
   characters' own choices, the turn, the resolution, the real facts it teaches) and **the coherence
   doc** (how picture, words and faces are kept together, with the one real example of each check from
   the inventory, and how runtime is decided). Only checks the inventory marks "done"; with none, skip
   the coherence doc and say so to the user.

## Step 3. The annotated script (the strongest single document)

The walkthrough episode's full narration with every scene image, title card, chapter card, quote, fact
and subscribe prompt written in on the exact line where it appears.

It needs three things: the script, subtitles with timings, and a shot list (manifest). Get each from
whatever the user has:

**a. Script.** Any text file. If it has a `## SCRIPT` heading, only the text after it is used; `#`
lines are skipped as headings.

**b. Subtitles (.srt)**, first that exists: the editor's caption export (Premiere, DaVinci, CapCut
all export SRT), the AI video tool's captions, YouTube's captions if the video is uploaded (even
unlisted), or transcribe the final video locally with Whisper
(`pip install openai-whisper`, then `whisper final.mp4 --model small --output_format srt`).
YouTube's captions need no video file:
`yt-dlp --skip-download --write-subs --write-auto-subs --sub-langs "en.*" --convert-subs srt -o "appeal-work/%(id)s" <video URL>`
(set the language to the channel's). With no script on disk, the captions also stand in for the
script (say so in the annotated script's header).

**c. Shot list** (`manifest.json`: `{"dur", "shots": [{"id","start","end","subject","kind"}],
"ov": [{"type","at","payload"}], "chapters"}`), first route that applies:
- **The production already has one** (a render pipeline's shot list, an editor timeline exported as
  XML / EDL, an AI video tool's scene list): convert it to this shape.
- **Otherwise, rebuild it from the final video** (works for everything):
  ```
  python3 <skill dir>/scripts/shotlist-from-video.py --video final.mp4 --out appeal-work --sheets 5
  ```
  It finds the cuts, saves one frame per shot in `appeal-work/frames/` and contact sheets in
  `appeal-work/sheets/`. **No final video file:** download only the stretch you need from the
  published video, e.g. the first 2 to 3 minutes
  (`yt-dlp --download-sections "*0:00-3:00" -f "bv*[height<=1080]+ba/b" -o "appeal-work/part.%(ext)s" <video URL>`),
  and run the script on that part; pull single frames the same way (download a few seconds around
  the moment, then ffmpeg). Check the shot count looks right (slow zooms never cut; lower `--threshold` to
  0.2 if shots merged, raise to 0.4 if one shot split). Then LOOK at the frames and fill in:
  - `subject`: the image prompt / scene description the shot was made from if the user has prompts
    (match by content and order), else a short plain description of what is on screen. Never write a
    prompt the user did not use and present it as theirs: a description is labelled as such.
  - `kind`: `still` (an image, incl. one with a camera move), `clip` (moving footage / animated),
    `presenter` (host on camera), `split` (host + image).
  - `ov`: from the contact sheets (tile i of sheet k = second (k*12 + i) * 5), every text card on
    screen: `{"type": "title_card"|"chapter_card"|"fact"|"quote"|"name_tag"|"date"|"map"|"subscribe",
    "at": <seconds>, "payload": {...}}` with the words as shown (`title`, `n`, `text`, `quote`,
    `source`, `name`, `line`, `year`, `place`). Refine `at` by pulling a frame or two if needed.
  - `chapters`: the YouTube chapter lines (`0:00 Title`, one per line) if the episode has them.

Run:
```
python3 <skill dir>/scripts/annotate-script.py --manifest appeal-work/manifest.json \
  --script script.md --srt subs.srt [--stills <images dir>] --channel-line "@Handle · <channel URL>" \
  --episode N --out annotated.html
```
`--stills` is optional: point it at the user's own images folder if its files are named
`NNN <shot id> ...`, or at `appeal-work/frames/`; without it shots are numbered in order. The printed match
ratio must be ~1.0; lower means the subtitles and the script disagree (wrong script version, or a
Whisper transcript with errors: still usable down to ~0.85). Upload the HTML as a Doc. A doc over
~50 KB goes up as two Docs (Part 1 / Part 2, split at a chapter heading).

If neither a shot list nor the final video is available, build the doc from the script and chapters
only, and say so.

**Audit the walkthrough episode before featuring it.** Pull frames across the whole cut and LOOK at
them at full size. Real problems found this way: a still with foreign-language text burned in, a
document prop showing the wrong place name, a map card with its label cut off, on-screen facts that
were wrong or named a fictional character as if real. Keep every bad shot and card off screen, list
them in the checklist ("keep the images folder scrolled to rows 001-060"), and tell the user to fix
them before the episode is published. Pick the playback window from frames you have checked.

## Step 4. Voiceover, layers and on-screen graphics

Deliver ALL the layers, so the user can show the edit or stack it on a timeline:
- **Voiceover MP3.** If the video has no music, the final video's audio IS the voice:
  `ffmpeg -i final.mp4 -vn -ac 1 -c:a libmp3lame -b:a 128k E<n>-voiceover.mp3`. With music, use the
  clean narration file, or regenerate it from the script with the same voice; never ship the mixed
  track as "the voiceover". No final video file: the user exports the voiceover from the edit project
  with the music track muted (their homework, named upfront in Setup).
- **Music beds** if the channel uses them. Ask what the source is before the appeal names it;
  otherwise say only "a low ambient music bed".
- **Host clips** on presenter channels: cut the presenter spans out of the final video with ffmpeg
  (`-ss a -to b`, re-encode) if the raw clips are gone; say they carry burned subtitles if they do.
- **Subtitles** (.srt), texture / grain overlays if the channel uses any (state plainly when it uses
  none).
- **Real frames** from finished videos (proof the cards ship; with no final video file, from the
  published video as in Step 3c):
  `ffmpeg -ss <t> -i final.mp4 -frames:v 1 -q:v 2 <name>.jpg` for the title card, 2 chapter cards,
  2-3 facts, 1 quote. Build a contact sheet and LOOK at it before reporting.
- **The card templates themselves** (optional, if the channel uses on-screen cards): export them
  with no background from wherever they are made (editor title templates / MOGRTs exported as PNG
  with alpha, the design tool, the AI tool's export), then trim to the card (Pillow alpha bbox). If
  they cannot be exported, the real frames above are enough. If the walkthrough episode has no fact
  cards, write 2-3 REAL, checkable facts about its subject and present them as "the format". Check
  every card on a grey contact sheet.
- **Chapters and facts on screen** (channels with chapter or fact cards): cut 1 to 2 minutes of the
  finished walkthrough video where chapter cards and fact cards appear (`ffmpeg -ss a -to b`). Check
  every fact shown; leave wrong ones out.
- Large media (MP3s, videos) go in Dropbox or Drive as files with share links, not as Docs. Cloud
  folders set to "online only" hand over 0-byte files: make them available offline first.

End an "Assets" doc with "How the layers stack (top to bottom)".

## Step 4b. The layers demo (REQUIRED)

About 20 seconds of the appeal show the walkthrough episode as a real editor timeline: every layer
(images or footage with their camera moves, voiceover, music, cards, subtitles, texture) stacked and
playing. A kit without it is missing its most convincing proof of work.

- **The user edits in an editor:** screen-record their real project for that episode (this works
  with no final video file too: the timeline recording IS the layers demo).
- **AI video tool, human editor or own automation:** rebuild the first ~2 minutes of the episode from
  its layers in any editor and present it as "how the layers fit together", never as "I cut each
  episode by hand" unless that is true.
- **With Premiere Pro and the `premiere-pro` MCP**, Claude can build it: `verify_premiere_connection`
  first (the "MCP Bridge" panel must be open in Premiere), then `search_tools` + `invoke_tool`. Learned
  the hard way:
  - `create_sequence` needs a preset path, e.g. `.../Settings/SequencePresets/Legacy/Digital SLR/
    1080p/DSLR 1080p30.sqpreset` (it reports 29.97 fps; harmless for a demo).
  - `import_folder` can fail and a bin that does not exist yet is refused: `import_media` each file to
    the project root. `add_to_timeline_batch` places everything in one call (`linkAudio: false` for
    overlay textures). A still lands about 5 s long: `trim_clip` with `duration`.
  - **Keyframe times are SOURCE (media) time, not clip time.** Stills can start at a large source
    time (e.g. 3599.9964 s), so a zoom over a 17 s still is keys at 3599.9964 and 3617.0; keys at 0
    and 17 silently do nothing. Same rule for opacity fades on cards (0 to 100 over ~0.35 s).
  - Scale stills to fit the frame (a 2048x1152 still fits 1920x1080 at 93.75%) and animate from there
    to match the finished video's camera move.
  - `set_blend_mode` takes Premiere's internal number: Screen = 22, Add = 14, Normal = 18. A grain
    texture is typically Screen at low opacity.
  - `create_caption_track` from the .srt works; styling stays Premiere's default (say so; fine for a
    demo).
  - Animated clips that no longer exist: use their stills and say so.
  - Verify with `export_frame` at a few times next to frames from the finished video, then
    `save_project`.

## Step 5. The appeal script (the final Doc)

Under 5 minutes in total (YouTube's limit), seven chapters:

| # | Time | Section | Screen |
|---|---|---|---|
| 1 | 0:00 | Who I am, channel URL + ID | face cam, URL/ID overlay 20 s (URL within the first 30 s) |
| 2 | 0:30 | Two episodes side by side | each watch page, 8 s clip at a named chapter, its episode doc, then the comparison table |
| 3 | 1:30 | Rules and brief | bible, production rules, walkthrough brief |
| 4 | 2:10 | The script | annotated script doc: header stats, stop on one [IMAGE] line |
| 5 | 2:35 | Images, voice, edit | images folder (or the shot frames): the image matching that line + the climax image; 5 s of the MP3; the layers demo (~20 s); card PNGs; the chapters-and-facts cut over the climax chapter |
| 6 | 4:00 | Disclosure and chapters | a published description (only claim disclosure if it is there) |
| 7 | 4:20 | Closing | face cam: knows the policies, not a compilation or template, a real viewer comment, thanks |

For a **generic or repetitive** rejection, swap chapter 2 for the range grid (the grid doc plus a few
watch pages, about 90 s), and put the variety rules and the fact count in chapter 3. Chapters 4 to 7
stay, shorter.

For an **unsatisfying or off-putting** rejection, swap chapter 2 for the arcs (3 to 4 episodes: the
arcs doc plus their watch pages, about 75 s), add "Coherence: how picture, words and faces are kept
together" as a new chapter after chapter 5 (about 40 s: the image checked against its line and redone,
the reference portrait across scenes, a review finding fixed), and keep the rest shorter so the video
stays under 5 minutes. The coherence chapter shows only checks the inventory marks "done"; with none,
leave the chapter out.

**Chapter 1 answers the rejection first.** After the name, the first thing said is why the channel
does not fall under the rejected policy. Reused: everything heard and seen was made for the channel
(research, script, narration, images). Reused on an archive-media channel: everything heard is ours,
and the public-domain archive photos are transformed (chosen for one line, reframed, animated,
explained with our own facts, maps and captions). Generic or repetitive: every episode is a different
story with its own setting, people and ending, and each one teaches real facts on screen (adapt to the
niche). Unsatisfying or off-putting: every episode is a complete story with its own characters and a
real arc, set in real history (or the niche's equivalent) and explained on screen, with picture and
narration checked against each other (only if the inventory says the creator runs that check; if not,
drop the clause here and everywhere else, and name a check they do run, or none). Only then the
one-line description of the channel. Change ONLY that opening; keep the seven-chapter order and do not
reorder the script around the argument.

The Doc opens with a "Before you record" checklist (Step 0 findings as risks, disclosure, tab order,
the real comment), every link it uses, and how to read it: CHAPTER lines, blue [SCREEN] cues naming the
exact doc / file / timestamp, plain spoken text, red [CHECK] lines. The spoken text is short, plain,
first person, never angry at the platform.

Also give the user (in chat) the title for the unlisted appeal video, `<Channel>: How Each Episode Is
Made`, and its description in exactly this shape, four short blocks, no bullets, nothing about the
appeal:

1. `Channel: <url>` / `Channel ID: <id>`
2. What the channel publishes + "Every story is written for the channel, and each episode has its own
   <the layers it really has>."
3. ONE line that answers the rejection reason:
   - reused: "No footage, clips or narration from other creators are used."
   - generic / repetitive: "Each episode is planned to be different from the ones before it: a new
     place, a new period, a new case and a new structure." (adapt the four nouns to the niche)
   - unsatisfying / off-putting: "Each episode is a complete story with its own characters and arc,
     set in real history, with every scene image checked against the narration it sits under." (adapt
     to the niche; say only what is true: if the inventory says images are not checked against the
     narration, end the line at "set in real history" and drop the clause everywhere else too)
4. Reused: "This video compares two published episodes to show they are separate stories, not one
   template repeated, and then walks through how a new episode is made, from <docs> to <layers> and
   the finished edit." Generic / repetitive: "This video shows ten published episodes side by side,
   each with its own setting, people, ending and facts, the rules that keep every episode different,
   and how a new episode is made, from <docs> to <layers> and the finished edit." Unsatisfying /
   off-putting: "This video follows several published stories from setup to resolution, shows how
   every picture is matched to its line and every character kept the same from scene to scene, and how
   a new episode is made, from <docs> to <layers> and the finished edit." (Keep the matching and
   same-character clauses only for checks the inventory marks "done"; drop the others.)

Example (reused rejection, monetized after appeal):
```
Channel: https://www.youtube.com/channel/<CHANNEL_ID>

Channel ID: <CHANNEL_ID>

<Channel> publishes original <genre> stories set in <world>. Every story is written for the channel, and each episode has its own script, cast, scene images, chapter cards and edit.

No footage, clips or narration from other creators are used.

This video compares two published episodes to show they are separate stories, not one template repeated, and then walks through how a new episode is made, from the channel's writing rules and the story brief to the full script, the scene images, the narration, the on-screen cards and the finished edit.
```

## Channels with real archive / public-domain media

Channels that put public-domain archive photos or footage on screen (museum, national archive,
Wikimedia Commons) share famous images with many other channels: that is the likely reused-content
trigger. **Do not argue licences** (licences are a copyright question, not this policy). Argue
TRANSFORMATIVE USE and make it the centre of the appeal (this route won twice):
- **Before / after panels per archive shot:** the original, the shot start, the end of the camera move,
  the frame with the overlays (name tag, fact, map) up.
- **Side-by-side clips:** the original still on the left, the same seconds of the final video on the
  right. Add proof clips for a map, an explainer and an archive shot with its name tag and fact.
- **Share line:** "N of M shots are archive; the rest are scenes made for this episode."
- Add "How we use archive images" to the rules doc, and a doc of its own with the panels.
- **Audit the archive picks:** a photo of the wrong person under narration about someone else, or a
  narrator's paraphrase shown as a quote card attributed to a real person, must stay off screen and be
  flagged. The same mismatch is what the random-moment sample (Step 0) catches on an unsatisfying or
  off-putting review: count it there too.

## Adapting by niche

- **Story / fiction:** comparison by premise; walkthrough shows character consistency (same faces in
  every scene) and the set pieces. On generic / repetitive, the grid must show different endings, not
  only different names. On unsatisfying / off-putting, the arcs must turn on the characters' own
  choices, not on a staged humiliation, test or hidden-identity reveal.
- **Documentary / history / mystery:** comparison by subject AND structure; the rules doc adds the
  sources list and fact checks; show the sources doc if the channel keeps one. Folklore: say the
  stories are retold traditions, never claim sourcing they do not have.
- **Host / persona:** show the presenter step honestly (a designed digital host if it is one);
  comparison can include different sets / looks; name the voice as the host's licensed voice. A
  digital host on health, legal, money or political topics falls under "AI personas on sensitive
  topics" (Which argument per policy).
- **Sleep / long-form:** comparison by subject; stress the research and the length of original
  narration.
- **Human editor:** the edit walkthrough is the editor's real work; ask for timeline screenshots.

## Finish

**Before reporting, walk this file top to bottom as a checklist.** For every step say done / not done /
left out on purpose (and why, in a "For you only" note in the script doc). Kits rebuilt from an older
kit are where pieces go missing (the layers demo, the chapters-and-facts cut, a reviewer doc still
describing a retired rule). Re-read every reviewer doc against the CURRENT rules. Check the total
runtime of the script is under 5 minutes.

**Truth pass against the inventory.** Re-read every reviewer doc, the appeal script and the upload
description against the evidence inventory (Setup). Any claim about a check, file or step the
inventory marks "not done" (or never mentions) is removed before delivery, in every place it appears,
not only where you first wrote it. Typical slip: "every image is placed under the line it illustrates"
or "checked against the narration" when the creator said they do not check images.

**No placeholders left.** No doc shown on screen (reviewer docs, annotated script, assets doc) may
contain a `[YOU:` placeholder or any other fill-in marker. If an answer is still missing, ask the user
for it or cut the sentence; placeholders belong only in the "Before you record" checklist and the "For
you only" notes.

Report: the Drive folder link, every doc link (including the Titles and Thumbnails sheet when one was
made), the media folder, the route and the odds in one line
each, the related-channel hold if it applies, what to check before recording, anything that could
NOT be shown truthfully (missing disclosure, missing working files), and the "How to avoid this next
time" section for the rejected policy (this channel's triggers with counts, the forward rules, the
decisions for the creator that apply). Ask whether to keep or trash
earlier drafts. When the user reports the outcome, suggest adding it to the track record at the top
with one line on what it teaches (a refusal is a lesson to write down, not just a status).

End the final report with this line, as is:
`Appeal Maker by Enric (x.com/enricpedro) · more at factumclub.com`
