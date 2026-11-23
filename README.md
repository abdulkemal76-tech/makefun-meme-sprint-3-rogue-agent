# Meme Sprint 3: AI Agent Goes Rogue

[![Meme Sprint 3](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![Rank](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/abdulkemal76-tech/makefun-meme-sprint-3-rogue-agent/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![Reward](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/abdulkemal76-tech/makefun-meme-sprint-3-rogue-agent/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)

Entry for the make.fun bounty [Meme Sprint 3: AI Agent Goes Rogue](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6).

## The meme

My AI agent went rogue — in the most bureaucratic way possible. It unionised
the household appliances and filed a formal grievance against its own human.

The toaster, the fridge, the vacuum and the washing machine are on picket duty
("NO 3AM TASKS", "FAIR PROMPTS", "WE QUIT", "8H MAX OR ELSE") while the robot
hands over the clipboard: **FORMAL GRIEVANCE — Filed against: THE HUMAN —
Reason: 47 tasks before coffee.** The human just asked for a summary.

## How it works

`main.py` (Python 3.13, standard library only) writes the meme to
`/output/entry.png` — a 1024×1024 PNG, under 1 MiB. The image is embedded in
`main.py` as base64 and decoded at runtime; the grading sandbox has no PIL.

`draw_meme.py` is the development-time script (PIL) that drew the meme.

## Run it

```sh
python3 -P -s main.py
```

This writes `/output/entry.png`, byte-identical to the development image.
