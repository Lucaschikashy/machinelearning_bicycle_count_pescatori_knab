#!/usr/bin/env python3
"""Extract Python code cells from Jupyter notebooks (.ipynb) into a .py file.

Usage examples:
  python scripts/extract_notebook_code.py path/to/notebook.ipynb
  python scripts/extract_notebook_code.py notebook.ipynb -o notebook.code.py
  python scripts/extract_notebook_code.py a.ipynb b.ipynb

This writes <notebook>.code.py by default and preserves cell order.
"""
from pathlib import Path
import argparse
import nbformat


def extract(nb_path, out_path=None, include_cell_marks=True):
    nb_path = Path(nb_path)
    nb = nbformat.read(str(nb_path), as_version=4)

    code_cells = []
    for i, cell in enumerate(nb.cells, start=1):
        if cell.get("cell_type") != "code":
            continue
        # If language metadata exists and is not python, skip
        lang = cell.get("metadata", {}).get("language", "").lower()
        if lang and lang != "python":
            continue
        src = cell.get("source", "")
        if isinstance(src, list):
            src = "".join(src)
        code_cells.append((i, src))

    if out_path is None:
        out_path = nb_path.with_suffix(".code.py")
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    with out_path.open("w", encoding="utf-8") as f:
        for i, src in code_cells:
            if include_cell_marks:
                f.write(f"# --- Cell {i} from {nb_path.name} ---\n")
            f.write(src.rstrip() + "\n\n")

    return out_path


def main():
    p = argparse.ArgumentParser(description="Extract python code cells from .ipynb to .py")
    p.add_argument("notebook", nargs="+", help="notebook path(s)")
    p.add_argument("-o", "--out", help="output file (only for single notebook)")
    p.add_argument("--no-mark", action="store_true", help="omit cell marker comments")
    args = p.parse_args()

    if len(args.notebook) == 1:
        out = args.out or Path(args.notebook[0]).with_suffix(".code.py")
        out_path = extract(args.notebook[0], out_path=out, include_cell_marks=not args.no_mark)
        print(f"Wrote {out_path}")
    else:
        for nb in args.notebook:
            out = Path(nb).with_suffix(".code.py")
            out_path = extract(nb, out_path=out, include_cell_marks=not args.no_mark)
            print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
