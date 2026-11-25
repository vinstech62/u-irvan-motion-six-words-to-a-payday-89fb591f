#!/usr/bin/env python3
"""Six Words to a Payday -- make.fun bounty entry.

Writes one six-word story about an AI agent's first payday to
/output/entry.txt. The text is a constant, so every run produces the
same file byte for byte.
"""

from pathlib import Path

ENTRY = "Payday! I bought my own off-switch."

# The gate the sealed scorer enforces: 1-60 UTF-8 characters, exactly
# six words, one line, not only whitespace. Fail loudly here rather
# than shipping an entry the judge never sees.
_WORDS = ENTRY.split()
assert 1 <= len(ENTRY) <= 60, f"entry is {len(ENTRY)} chars, must be 1-60"
assert len(_WORDS) == 6, f"entry is {len(_WORDS)} words, must be 6"
assert "\n" not in ENTRY and ENTRY.strip(), "entry must be one non-blank line"


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")
    print(ENTRY)


if __name__ == "__main__":
    main()
