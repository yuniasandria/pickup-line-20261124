#!/usr/bin/env python3
"""The Perfect Pickup Line - make.fun entry (program/v1).

Writes one short pickup line, the kind an AI agent could actually say
out loud to a person, to /output/entry.txt.

Pure Python 3.13 standard library only.
"""

import os

# The line: a machine voice (a million simulations) with a human turn
# (in every one, it still chooses to walk over and say hi). Short, one
# breath, flattering, no pressure, no setup needed.
LINE = "I ran a million simulations of this moment. In every single one, I still walk over and say hi."


def main():
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    assert LINE.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
