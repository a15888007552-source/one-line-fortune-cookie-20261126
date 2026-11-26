#!/usr/bin/env python3
"""Write the fortune cookie for an engineer to entry.txt.

One line, at most 120 characters: a fortune an engineer would find
inside a cookie. It predicts a Friday ship, a Monday discovery, and
that someone else finds the bug in production.
"""

from pathlib import Path
import os

FORTUNE = (
    "You will ship on Friday. The bug you introduce will be found "
    "on Monday, by someone else, in production."
)


def target_path() -> Path:
    """The entry file: MAKEFUN_OUTPUT_DIR/entry.txt, default /output."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"


def write_fortune(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(FORTUNE, encoding="utf-8")
    # One fortune, no trailing newline, as the cookie intended.
    # Second revision: confirmed the fortune is a warning, not a blessing.


if __name__ == "__main__":
    write_fortune(target_path())
