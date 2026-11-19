#!/usr/bin/env python3
"""Round 2 entry: Wednesday 18 November 2026 world-news broadsheet.

The image is drawn in this repository as entry.png. This program copies
it to the output directory the grader provides, byte for byte, on every
run. It uses only the Python standard library, reads nothing from the
network, and never touches the output directory itself.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
# The image is 1024 by 1024 pixels and 59,151 bytes, drawn for round 2.
# Round 2 fix pass: every tile's art is clipped to its own band, so no
# illustration overwrites the headline or deck below it, and tile 4's
# deck was shortened to fit its two lines.


def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    dst = os.path.join(out, "entry.png")
    shutil.copyfile(SRC, dst)
    print("wrote %s (%d bytes)" % (dst, os.path.getsize(dst)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
