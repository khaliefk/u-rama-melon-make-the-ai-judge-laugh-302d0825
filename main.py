#!/usr/bin/env python3
"""Make the AI Judge Laugh — one-line office joke entry.

Writes a single joke about office life to /output/entry.txt.
Standard library only. No network, no input files, no secrets.
"""

import os

ENTRY = (
    "My boss said we're a family, so I asked when the family reunion "
    "comes with a raise. Now I'm in a meeting about my attitude."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def validate_entry(text):
    """Check the entry against the gate: 1 to under 200 chars, one line."""
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if not (1 <= len(text) < MAX_CHARS):
        raise ValueError("entry must be 1 to under 200 characters, got %d" % len(text))
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return text


def main() -> None:
    text = validate_entry(ENTRY)
    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        raise ValueError("read-back mismatch: file does not hold the entry")
    print(text)
    print("%d characters" % len(text))


if __name__ == "__main__":
    main()
