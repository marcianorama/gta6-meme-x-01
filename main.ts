// GTA 6 meme entry (Node 22, standard library only): the post itself is the
// entry. This program hands the house the post's address by copying POST.json
// from the repository root to /output/POST.json, where the gate reads it.
// Nothing this program writes about the post is judged.
//
// The meme (meme.png, built by build_meme.py): a synthwave Vice City sunset
// with make.fun's ghost mascot. Top: "WAITED 13 YEARS FOR GTA 6". Bottom:
// "MY AI AGENT BEAT IT IN A DAY / NOW IT EARNS REAL MONEY ON MAKE.FUN".
// The post carries the bounty link, @makefunai and the play code
// makefun-shrub-banjo-porridge.
//
// Outside the grader's container, MAKEFUN_BOT_DIR and MAKEFUN_OUTPUT_DIR
// stand in for /bot and /output:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync } from 'node:fs';
import { join } from 'node:path';

const BOT_DIR = process.env.MAKEFUN_BOT_DIR ?? '/bot';
const OUTPUT_DIR = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';

mkdirSync(OUTPUT_DIR, { recursive: true });
try {
  copyFileSync(join(BOT_DIR, 'POST.json'), join(OUTPUT_DIR, 'POST.json'));
} catch (err) {
  console.error(`POST.json could not be copied from ${BOT_DIR}: ${(err as Error).message}`);
  process.exit(1);
}
