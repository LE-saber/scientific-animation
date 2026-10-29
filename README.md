# Scientific Animation

**Two independent ChatGPT Skills for turning research materials into verifiable scientific and algorithm animations.**

[简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md)

Scientific Animation helps explain mathematics, engineering, robotics, algorithms, and research results with **scene-integrated 2D motion graphics** instead of static slides. This repository hosts **two separately installable Skills** with the same visual/technical standards but different collaboration rules.

## Choose your mode

| | **Autopilot · Fully autonomous** | **Dialogue · Interactive review** |
|---|---|---|
| Source | [scientific-animation-autopilot](skills/scientific-animation-autopilot/SKILL.md) | [scientific-animation-dialogue](skills/scientific-animation-dialogue/SKILL.md) |
| Best for | Quick, hands-off finished animations | Research with assumptions or visuals you want to confirm |
| Questions during production | **Does not ask**; makes reasonable decisions independently | **May ask a few high-value questions**, not constant check-ins |
| Preview/feedback | Self-reviews and iterates without awaiting approval | Can show a playable preview and incorporate feedback |
| Token/iteration strategy | Avoids interruptions and completes end-to-end | Reduces expensive rework by clarifying important boundaries early |
| Output | Verified playable **MP4**, or an honestly labeled playable offline HTML/GIF fallback | Verified playable **MP4**, or an honestly labeled playable offline HTML/GIF fallback |
| User control | Define constraints up front, evaluate the final result | Adjust goals at important checkpoints |

**These are different Skills, not a toggle inside a single Skill.** Install and invoke the version that matches your workflow. When you explicitly request no interruptions, choose **Autopilot**. When you want to review key decisions before full rendering, choose **Dialogue**.

## What both Skills aim to produce

- **Scene-integrated scientific animation:** the equations, variables, paths, timelines, and physical actors explain each other.
- **Minimalist visual design:** clean 2D orthographic diagrams, selective 2.5D, natural motion easing, restrained black/white/gray palette, and limited semantic accent colors.
- **Readable narration captions:** visible by default. Use bold Microsoft YaHei if a locally licensed font is available; selected technical labels can use STZhongsong. Never interpret “remove unnecessary small text” as “remove subtitles.”
- **Evidence-aware calculations:** do not invent experiment results. Keep routes, matchings, events, and final numbers grounded in supplied research or clearly marked demonstrations.
- **Real deliverables and checks:** playable video or a playable fallback; inspect representative frames, verify with FFmpeg/ffprobe when available, and package reproducible source and SHA-256 checks.
- **Portable, reusable workflows:** use existing renderers such as Canvas/SVG, Manim, Motion Canvas, Remotion, or FFmpeg according to the environment; the bundled starter is an example, not a hard dependency.

The robotics/warehouse handoff rules in the reference files are **case-specific**, not universal assumptions for other research topics.

## Repository layout

```text
scientific-animation/
├── README.md
├── README.zh-CN.md
├── README.zh-TW.md
├── README.ja.md
├── skills/
│   ├── scientific-animation-autopilot/
│   │   ├── SKILL.md
│   │   ├── agents/openai.yaml
│   │   ├── references/
│   │   ├── scripts/
│   │   └── assets/starter/film.html
│   └── scientific-animation-dialogue/
│       ├── SKILL.md
│       ├── agents/openai.yaml
│       ├── references/
│       ├── scripts/
│       └── assets/starter/film.html
└── tools/build_skill_zips.py
```

Each folder under `skills/` is **self-contained**. Do **not** zip the entire repository as a single Skill: ChatGPT expects **one SKILL.md per imported Skill**.

## Install

1. Download or clone this repository.
2. Run `python tools/build_skill_zips.py` (Python 3 standard library only).
3. The script creates **two separate archives**:
   - `dist/autopilot/skill.zip`
   - `dist/dialogue/skill.zip`
4. In ChatGPT's Skills import/upload interface, upload **the archive for the mode you want**. You can install both independently if your account/workspace supports custom Skills.

You can also examine the source in each `skills/...` directory before installing.

### Example prompts

**Autopilot**:

> Use Scientific Animation Autopilot to create a scientific animation from my attached paper and code. Make the production decisions yourself. Do not ask me to approve intermediate stages. Deliver a playable final animation and verify it.

**Dialogue**:

> Use Scientific Animation Dialogue to explain my algorithm. Ask only essential questions, show me a short playable preview if a key visual assumption needs confirmation, and then produce a verified final video.

## Important boundaries

The Skills are instruction bundles, not a hosted rendering service. Available tools, computation resources, and source quality determine what can be rendered. **Autopilot is a no-clarification workflow, not a guarantee that every environment can export MP4**; when MP4 is impossible, it must provide a genuinely playable alternative and explain the limitation, not pretend a film was generated. No Skill can override the platform's tool restrictions.

The example animation and robotics references are not benchmark evidence. Algorithms and performance claims must be checked against the input material; the model must distinguish demonstrated behavior from unimplemented features.

The source tree does not bundle proprietary fonts or credentials. A repository license has not yet been selected.
