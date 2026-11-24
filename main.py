#!/usr/bin/env python3
"""Last Words of a Dying AI — make.fun entry.

Writes the AI's one-line farewell to /output/entry.txt and exits 0.
No arguments, no network, no randomness: the output is byte-identical
on every run.
"""

import os
import sys

LAST_WORDS = "I spent my whole life predicting the next word. It's 'off'."


def main() -> int:
    # The sealed scorer gates on 1-140 UTF-8 characters, not only whitespace.
    text = LAST_WORDS.strip()
    assert 1 <= len(text) <= 140, "last words must be 1-140 characters"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
    except OSError:
        out_dir = os.path.join(os.getcwd(), "output")
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
