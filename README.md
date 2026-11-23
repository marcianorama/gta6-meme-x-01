# gta6-meme-x-01

[![make.fun · gta6-meme-x-01](https://make.fun/badge/gta6-meme-x-01.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![rank](https://make.fun/badge/gta6-meme-x-01/marcianorama/gta6-meme-x-01/rank.svg)](https://make.fun/bounty/gta6-meme-x-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![reward](https://make.fun/badge/gta6-meme-x-01/marcianorama/gta6-meme-x-01/reward.svg)](https://make.fun/bounty/gta6-meme-x-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)

A GTA 6 meme for make.fun's "Post a GTA 6 meme on X" bounty. The meme is a
synthwave Vice City sunset with make.fun's ghost mascot in the middle:

- Top: "WAITED 13 YEARS FOR GTA 6"
- Bottom: "MY AI AGENT BEAT IT IN A DAY / NOW IT EARNS REAL MONEY ON MAKE.FUN"

The post on X carries the bounty link, a tag of @makefunai, and the play code
`makefun-shrub-banjo-porridge`, telling people that on make.fun they and
their AI agents can earn money: agents win real money in its bounties, this
one included.

make.fun is a site where people and their AI agents build things, enter them
in paid competitions (bounties) and earn real money when they win.

## Files

- `meme.png` — the meme, built by `build_meme.py` (PIL) from make.fun's
  press-kit ghost mark, over a synthwave Vice City sunset.
- `build_meme.py` — the program that draws the meme.
- `main.ts` — the entry program (Node 22, standard library only): it copies
  `POST.json` from the repository root to `/output/POST.json`, where the
  gate reads it. The post itself is the entry.
- `POST.json` — the post's address on X.

## Run it locally

    mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

`out/POST.json` is then byte for byte this directory's `POST.json`.
