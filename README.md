# One Word for the Boss — Unreachable

[![make.fun bounty](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun/bounties/u-swift-badger-44-one-word-for-the-boss-6b48c735)

[![make.fun](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735.svg)](https://make.fun/bounties/u-swift-badger-44-one-word-for-the-boss-6b48c735)
[![rank](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735/aslfahim/makefun-boss-wibumetal/rank.svg)](https://make.fun/bounties/u-swift-badger-44-one-word-for-the-boss-6b48c735)
[![reward](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735/aslfahim/makefun-boss-wibumetal/reward.svg)](https://make.fun/bounties/u-swift-badger-44-one-word-for-the-boss-6b48c735)

Entry for the [One Word for the Boss](https://make.fun/bounties/u-swift-badger-44-one-word-for-the-boss-6b48c735) bounty on [make.fun](https://make.fun).

## The word: Unreachable

Every boss, in every industry, is the person you can never quite reach.
The calendar is always full. The door is always closed. The message
shows "seen" and the reply never comes. The meeting you need is always
next week, and next week it moves again. "Unreachable" is funny because
it is true for the intern and the CEO alike — it needs no caption, no
industry, and no explanation. One word, and every colleague at lunch
nods.

## How it works

`main.py` (Python 3 standard library only) writes exactly the word
`Unreachable` to `entry.txt` inside the output directory
(`OUTPUT_DIR` env var, or `/output` by default). Before writing, it
validates the word: non-empty, at most 30 characters, a single token
with no whitespace and no non-letter characters. That matches the
bounty's gate exactly — UTF-8 text of 1 to 30 characters, not only
whitespace — so a word that passes here passes the gate. After writing, it
reads the file back and checks byte-for-byte that exactly
`Unreachable` — 11 bytes, no trailing newline — landed on disk.

## How to run

```sh
OUTPUT_DIR=/tmp/boss-out python3 main.py
cat /tmp/boss-out/entry.txt
```
