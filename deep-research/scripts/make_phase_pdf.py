#!/usr/bin/env python3
"""Combine all markdown files in a phase directory and convert to PDF with TOC.

Finds all .md files in the given phase directory (excluding already combined files),
creates a single combined markdown with table of contents linking to headings,
and converts it to PDF using markdown-pdf.

Usage:
    python make_phase_pdf.py --phase-dir output/my-topic/phase5_synthesis
    python make_phase_pdf.py --phase-dir output/my-topic/phase6_report
"""

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path


def find_markdown_files(phase_dir: str) -> list[str]:
    """Find all .md files in the phase directory, sorted appropriately."""
    if not os.path.isdir(phase_dir):
        return []

    md_files = []
    for f in os.listdir(phase_dir):
        if f.endswith(".md") and not f.startswith("COMBINED_"):
            md_files.append(os.path.join(phase_dir, f))

    # Sort files: put files with more specific names first?
    # We'll sort alphabetically to maintain predictable order
    md_files.sort()
    return md_files


def extract_title(md_content: str) -> str:
    """Extract the first h1 title from markdown content."""
    match = re.search(r'^#\s+(.+)$', md_content, re.MULTILINE)
    if match:
        return match.group(1).strip()
    # Fallback to filename if no title
    return "Untitled"


def build_combined_markdown(md_files: list[str]) -> str:
    """Create a combined markdown file with a table of contents."""
    if not md_files:
        return ""

    parts = []
    toc_entries = []

    # First pass: collect titles for TOC and build content
    for i, md_path in enumerate(md_files, 1):
        with open(md_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract base filename for anchor
        filename = os.path.basename(md_path)
        anchor = re.sub(r'[^a-zA-Z0-9\-_]', '', filename.replace('.md', '')).lower()

        title = extract_title(content)
        toc_entries.append(f"{i}. [{title}](#{anchor})")
        parts.append(f"<a name=\"{anchor}\"></a>\n\n")
        parts.append(content)
        parts.append("\n\n---\n\n")

    # Build TOC
    toc = "# Table of Contents\n\n" + "\n".join(toc_entries) + "\n\n---\n\n"

    return toc + "\n".join(parts)


def convert_to_pdf(combined_md_path: str, output_pdf_path: str) -> bool:
    """Convert markdown file to PDF using markdown-pdf."""
    try:
        result = subprocess.run(
            ['npx', 'markdown-pdf', combined_md_path, '-o', output_pdf_path],
            capture_output=True,
            text=True,
            check=True
        )
        print(f"✓ PDF created: {output_pdf_path}", file=sys.stderr)
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ PDF conversion failed: {e}", file=sys.stderr)
        print(f"  stdout: {e.stdout}", file=sys.stderr)
        print(f"  stderr: {e.stderr}", file=sys.stderr)
        return False
    except FileNotFoundError:
        print("✗ Error: npx not found. Please install Node.js and npm.", file=sys.stderr)
        return False


def main():
    parser = argparse.ArgumentParser(description="Combine phase markdown files and convert to PDF")
    parser.add_argument("--phase-dir", required=True, help="Path to the phase directory (e.g., output/my-topic/phase5_synthesis)")
    args = parser.parse_args()

    phase_dir = args.phase_dir.rstrip("/")
    if not os.path.isdir(phase_dir):
        print(f"Error: {phase_dir} is not a directory", file=sys.stderr)
        sys.exit(1)

    print(f"Processing phase directory: {phase_dir}", file=sys.stderr)

    md_files = find_markdown_files(phase_dir)
    if not md_files:
        print(f"Warning: No markdown files found in {phase_dir}", file=sys.stderr)
        sys.exit(0)

    print(f"Found {len(md_files)} markdown file(s):", file=sys.stderr)
    for f in md_files:
        print(f"  - {os.path.basename(f)}", file=sys.stderr)

    # Build combined markdown
    combined_content = build_combined_markdown(md_files)
    if not combined_content:
        print("Error: Failed to build combined markdown", file=sys.stderr)
        sys.exit(1)

    # Write combined markdown
    phase_name = os.path.basename(phase_dir)
    combined_md_path = os.path.join(phase_dir, f"COMBINED_{phase_name}.md")
    with open(combined_md_path, 'w', encoding='utf-8') as f:
        f.write(combined_content)
    print(f"✓ Combined markdown: {combined_md_path}", file=sys.stderr)

    # Convert to PDF
    pdf_path = os.path.join(phase_dir, f"{phase_name}.pdf")
    success = convert_to_pdf(combined_md_path, pdf_path)

    if success:
        print(f"\n✅ Phase PDF generated successfully: {pdf_path}", file=sys.stderr)
        sys.exit(0)
    else:
        print(f"\n⚠️  Combined markdown created but PDF conversion failed", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
