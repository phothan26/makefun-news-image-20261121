"""make.fun entry: Sum up 21 November's world news in one image.

The simplest deterministic program: copy the image held in this
repository (entry.png) to /output/entry.png. No network, no randomness,
no timestamps -- both runs write the same bytes.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST = os.path.join(os.environ.get("OUTPUT_DIR", "/output"), "entry.png")


def main() -> None:
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    shutil.copyfile(SRC, DST)


if __name__ == "__main__":
    main()
    sys.exit(0)
