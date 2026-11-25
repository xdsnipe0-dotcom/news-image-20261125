"""News image entry for make.fun bounty news-image-20261125.

The program writes one image, entry.png in this repository, to
/output/entry.png. It uses only the Python standard library, makes no
network calls, and is deterministic: every run copies the same bytes.
"""
import os
import shutil
from pathlib import Path


def main():
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    if not source.is_file():
        raise FileNotFoundError(f"entry image not found: {source}")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, output_dir / "entry.png")


if __name__ == "__main__":
    main()
