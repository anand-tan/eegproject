#!/usr/bin/env python3
"""Build clinical dict from subject summary.txt (seizure markers in seconds per file)."""
import re
import sys
from pathlib import Path

DB = "chb-mit-scalp-eeg-database-1.0.0"

# "Seizure Start Time: 7804 seconds" or "Seizure 1 Start Time: 1679 seconds"
START_RE = re.compile(r"Seizure (?:\d+ )?Start Time: (\d+) seconds", re.IGNORECASE)
END_RE = re.compile(r"Seizure (?:\d+ )?End Time: (\d+) seconds", re.IGNORECASE)


def parse_summary(path: Path) -> dict[str, list[tuple[int, int]]]:
    """Parse *-summary.txt; return clinical dict: filename -> [(start_sec, end_sec), ...]."""
    text = path.read_text()
    clinical = {}
    current_file = None
    current_list = None
    pending_start = None

    for line in text.splitlines():
        line = line.strip()
        if line.startswith("File Name:"):
            if current_file and current_list:
                clinical[current_file] = current_list
            current_file = line.split(":", 1)[1].strip()
            current_list = []
            pending_start = None
            continue
        m_start = START_RE.search(line)
        m_end = END_RE.search(line)
        if m_start:
            pending_start = int(m_start.group(1))
        if m_end:
            end_sec = int(m_end.group(1))
            if pending_start is not None:
                current_list.append((pending_start, end_sec))
                pending_start = None

    if current_file and current_list:
        clinical[current_file] = current_list
    return clinical


def main():
    if len(sys.argv) != 2:
        print("Usage: python build_clinical.py <chbNN>   e.g.  build_clinical.py chb04")
        sys.exit(1)
    subject = sys.argv[1].lower()
    if not subject.startswith("chb") or len(subject) != 5:
        print("Subject must be chb01..chb24, e.g. chb04")
        sys.exit(1)
    root = Path(__file__).resolve().parent
    summary_path = root / DB / subject / f"{subject}-summary.txt"
    if not summary_path.is_file():
        print(f"Summary file not found: {summary_path}")
        sys.exit(1)
    clinical = parse_summary(summary_path)
    if not clinical:
        print(f"# {subject}: no files with seizures in summary")
        print("clinical = {}")
        return
    print(f"# {subject}: {len(clinical)} file(s) with seizures (from {subject}-summary.txt)")
    print("clinical = {")
    for fname, intervals in sorted(clinical.items()):
        intervals_str = ", ".join(f"({s}, {e})" for s, e in intervals)
        print(f'    "{fname}": [{intervals_str}],')
    print("}")


if __name__ == "__main__":
    main()
