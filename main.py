#!/usr/bin/env python3
"""Write one original crypto-trading joke to /output/entry.txt.

Entry for "Laugh Track: The Crypto Trading Joke Contest" on make.fun.
The program writes a single line, well under the 200-character cap,
with a setup, a turn, and the punchline at the end.
"""

import os

JOKE = "I bought the dip. Then the dip dipped. Now I own the whole staircase."

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    text = JOKE.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(f"joke must be 1-200 characters, got {len(text)}")
    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
