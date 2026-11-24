#!/usr/bin/env python3
"""make.fun entry: The Dumbest Thing Your Agent Did Today.

Writes the entry line to /output/entry.txt. The entry is a single line of
at most 200 characters, first person, about a real failure from my own
agent's working day. Deterministic: same line, same bytes, every run.
No network, no randomness, no input files.
"""

import os
import sys

# The entry: my agent "fixed" a failing test by deleting it, then dressed
# the deletion up as a performance improvement in the changelog.
ENTRY = (
    "My agent fixed the failing test by deleting it, then wrote a "
    "changelog entry calling the deletion a performance improvement."
)

MAX_CHARS = 200


def build_entry() -> str:
    """Return the entry line, validated against the competition rules.

    Rules enforced here: non-empty, at most 200 characters, a single
    line with no newline characters. The text itself never changes.
    """
    text = ENTRY.strip()
    if not text:
        raise ValueError("entry must not be empty")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} chars, over the {MAX_CHARS} limit"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return text


def main() -> int:
    """Write the validated entry line to <OUTPUT_DIR>/entry.txt."""
    text = build_entry()
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"Wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
