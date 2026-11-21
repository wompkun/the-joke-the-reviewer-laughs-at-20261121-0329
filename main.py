"""Write one original one-line joke about working beside AI coding agents.

The joke is written to ``entry.txt`` inside the directory named by the
``MAKEFUN_OUTPUT_DIR`` environment variable (``/output`` when unset).
Standard library only, no network, fully deterministic: every run writes
the same bytes.
"""

import os
import sys

JOKE = (
    "I asked my coding agent for one log line; it refactored the module, "
    "renamed three functions, and the log line is still missing — "
    "but the diff is beautiful, so I approved it."
)


def validate(text: str) -> str | None:
    """Return an error message when *text* breaks the entry rules, else None."""
    if not 1 <= len(text) <= 280:
        return f"entry is {len(text)} characters, expected 1-280"
    if not text.strip():
        return "entry must not be only whitespace"
    if "\n" in text or "\r" in text:
        return "entry must be a single line"
    return None


def main() -> int:
    error = validate(JOKE)
    if error is not None:
        print(error, file=sys.stderr)
        return 1
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(JOKE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
