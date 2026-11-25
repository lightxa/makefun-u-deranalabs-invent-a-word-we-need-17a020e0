#!/usr/bin/env python3
"""Invent a Word We Need entry.

Coins one new English word, "doorwhy", and defines it in a single
clear line. Writes that line to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt). Pure stdlib, deterministic,
no network at runtime.
"""

import os
from pathlib import Path

LINE = "doorwhy (n.) \u2014 forgetting why you walked into a room the moment you step inside."


def validate(text: str) -> None:
    """Fail loudly unless the entry is one plain line of 1-140 chars."""
    if not 1 <= len(text) <= 140:
        raise SystemExit(f"entry must be 1-140 characters, got {len(text)}")
    if not text.strip():
        raise SystemExit("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")


def main() -> None:
    text = LINE.strip()
    validate(text)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
