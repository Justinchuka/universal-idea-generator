#!/usr/bin/env python3
"""Mechanical checks for a skill folder. Usage: python scripts/validate_skill.py <skill-folder>"""
import re, sys
from pathlib import Path

def main(folder):
    root = Path(folder).resolve()
    errs = []
    skill = root / "SKILL.md"
    if not skill.exists():
        print("FAIL: SKILL.md missing"); return 1
    text = skill.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        errs.append("frontmatter missing or malformed")
    else:
        fm = m.group(1)
        name = re.search(r"^name:\s*(.+)$", fm, re.M)
        desc = re.search(r"^description:\s*(.+)$", fm, re.M)
        if not name: errs.append("name missing")
        elif name.group(1).strip() != root.name: errs.append(f"name '{name.group(1).strip()}' != folder '{root.name}'")
        if not desc: errs.append("description missing")
        elif len(desc.group(1)) > 1024: errs.append(f"description too long ({len(desc.group(1))} chars, max 1024)")
    lines = text.count("\n") + 1
    if lines > 500: errs.append(f"SKILL.md has {lines} lines (>500)")
    for ref in set(re.findall(r"`((?:references|examples|evals|scripts)/[^`\s]+)`", text)):
        if not (root / ref).exists(): errs.append(f"referenced path missing: {ref}")
    for f in root.rglob("*"):
        if f.is_file() and f.stat().st_size == 0: errs.append(f"empty file: {f.relative_to(root)}")
        if f.is_file() and f.suffix == ".md":
            for ref in set(re.findall(r"`((?:references|examples|evals|scripts)/[^`\s]+)`", f.read_text(encoding='utf-8'))):
                if not (root / ref).exists(): errs.append(f"{f.relative_to(root)} references missing path: {ref}")
    nested = [p for p in root.rglob("SKILL.md") if p != skill]
    if nested: errs.append(f"nested SKILL.md: {nested}")
    for d in root.iterdir():
        if d.is_dir() and not any(d.iterdir()): errs.append(f"empty folder: {d.name}")
    for pat in ("TODO", "TBD", "lorem ipsum", "PLACEHOLDER"):
        for f in root.rglob("*.md"):
            if pat.lower() in f.read_text(encoding="utf-8").lower(): errs.append(f"placeholder '{pat}' in {f.relative_to(root)}")
    if errs:
        print("FAIL"); [print(" -", e) for e in errs]; return 1
    print(f"PASS: {root.name} ({lines} lines in SKILL.md)"); return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "."))
