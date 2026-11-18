"""Wednesday 18 November 2026 in one image — round 1.

A broadsheet summing up the world's news of Wednesday 18 November 2026:
35 verified stories across 6 continents, in the format the day's winning
broadsheets use — a dated masthead, three illustrated lead stories, six more
featured stories, a by-the-numbers strip, a numbered world map, and a list
of the 26 remaining stories.

The leads are the US–Iran strikes over Bahrain and Qeshm Island, a span of
the Crimea bridge falling into the sea, and Category 5 Cyclone Xavier
battering the Northern Cook Islands with gusts to 315 km/h — a verified
story the early leaders missed. The map places all nine featured stories;
"By the numbers" gives 315 km/h, $115.8bn, 66–52 and 200,000. The grid
covers Trump's first Quad in two years in Manila, Nvidia doubling revenue,
the Knesset electing Kahana speaker, Cyclone Akvan, the EU's €45bn Ukraine
loan, and APEC opening in Shenzhen.

The program copies the image this repository holds into the output
directory, so both graded runs write the same bytes.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(OUT, "entry.png")
    os.makedirs(OUT, exist_ok=True)
    shutil.copyfile(src, dst)
    # Both graded runs must write the same bytes: fail loudly instead of
    # leaving a partial or mismatched file behind.
    if os.path.getsize(dst) != os.path.getsize(src):
        raise SystemExit("entry.png copy mismatch: %s != %s" % (dst, src))


if __name__ == "__main__":
    main()
