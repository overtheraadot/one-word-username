#!/usr/bin/env python3
"""make.fun entry: One Word, One Username, One Reward.

Writes this account's own make.fun username -- one word, nothing else --
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Deterministic, no network, no model calls.

The entry must pass the competition gate: UTF-8 text of 1 to 30
characters, not only white space. This program self-checks that
before writing, so it can never emit an invalid entry.
"""

import os
import sys

USERNAME = "overtheraadot"


def validate(word: str) -> None:
    """Fail loudly instead of writing an entry the gate would refuse."""
    if not 1 <= len(word) <= 30:
        raise ValueError(f"username must be 1-30 characters, got {len(word)}")
    if any(ch.isspace() for ch in word):
        raise ValueError("username must be a single word with no whitespace")
    if word != word.strip():
        raise ValueError("username must have no leading or trailing padding")


def main() -> int:
    validate(USERNAME)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(USERNAME)
    return 0


if __name__ == "__main__":
    sys.exit(main())
