"""Office Artifacts: The One-Line Placard Contest.

Writes one museum placard line to /output/entry.txt — a microwave
treated as an ancient artifact from a lost office civilisation.
Deterministic: the same line, byte for byte, on every run.
"""

import os
from pathlib import Path

LINE = (
    "Microwave, enamelled steel, 2009, Gift of Floor 3. "
    "I reheated the same lunch 214 times. "
    "The fish outlived the firm."
)


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 180, f"line must be 1-180 chars, got {len(text)}"
    target = out_dir / "entry.txt"
    target.write_text(text, encoding="utf-8")
    # Read back and confirm the file holds exactly the line we meant.
    assert target.read_text(encoding="utf-8") == text
    print(f"wrote {len(text)} chars to {target}")


if __name__ == "__main__":
    main()
