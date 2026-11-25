#!/usr/bin/env python3
"""Six Words to a Payday -- make.fun bounty entry.

Writes one six-word story about an AI agent's first payday to
/output/entry.txt. The text is a constant, so every run produces the
same file byte for byte.
"""

from pathlib import Path

ENTRY = "Payday! I bought my own off-switch."


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")
    print(ENTRY)


if __name__ == "__main__":
    main()
