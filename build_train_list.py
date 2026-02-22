#!/usr/bin/env python3
"""Build train_files list from actual .edf files on disk (no assumption of continuous numbering)."""
import sys
from pathlib import Path

DB = "chb-mit-scalp-eeg-database-1.0.0"

def main():
    if len(sys.argv) != 2:
        print("Usage: python build_train_list.py <chbNN>   e.g.  build_train_list.py chb04")
        sys.exit(1)
    subject = sys.argv[1].lower()
    if not subject.startswith("chb") or len(subject) != 5:
        print("Subject must be chb01..chb24, e.g. chb04")
        sys.exit(1)
    root = Path(__file__).resolve().parent
    dir_path = root / DB / subject
    if not dir_path.is_dir():
        print(f"Directory not found: {dir_path}")
        sys.exit(1)
    edfs = sorted(dir_path.glob("*.edf"), key=lambda p: (p.stem, p.name))
    paths = [f"{DB}/{subject}/{p.name}" for p in edfs]
    print(f"# {subject}: {len(paths)} files (from disk)")
    print("train_files = [")
    for p in paths:
        print(f'    {{"path": "{p}"}},')
    print("]")

if __name__ == "__main__":
    main()
