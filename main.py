#!/usr/bin/env python3
"""Round 3 entry program for the Wednesday 18 November 2026 news-image bounty.

The broadsheet is drawn beforehand and shipped in this repo as entry.png;
this program only places that file where the harness reads it. It uses
nothing but the standard library, touches no network, and writes the
same bytes on every run. Round 3 rebuilt the broadsheet from scratch in
clean serif type after round 2's pixel type cost it readability; the
program itself is unchanged in behaviour, only reworded.

Run: python3 main.py   (or: MAKEFUN_OUTPUT_DIR=out python3 main.py)
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)


if __name__ == "__main__":
    main()
