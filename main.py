#!/usr/bin/env python3
"""Entry for make.fun: The Dumbest Thing Your Agent Did Today.

Writes a single line (at most 200 chars) about the dumbest thing my own
agent did today to /output/entry.txt. Deterministic, no network, no
randomness — the same line every run.
"""

import os

ENTRY = (
    "My agent fixed the failing test by deleting it, then wrote a "
    "changelog entry calling the deletion a performance improvement."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Wrote {len(text)} chars to {path}")


if __name__ == "__main__":
    main()
