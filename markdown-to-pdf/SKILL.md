---
name: markdown-to-pdf
description: Converts markdown files to PDF using markdown-pdf npm package
argument-hint: '*.md'
---

# Markdown to PDF Skill

## Trigger

Activate this skill when the user wants to:
- "Convert markdown to PDF"
- "Create PDF from markdown files"
- "Generate PDF documentation"
- Use `/markdown-to-pdf [glob-pattern]` slash command

## Overview

This skill converts markdown files to PDF format using the markdown-pdf npm package. It's useful for creating printable documentation, sharing formatted documents, or archiving markdown content.

**Installation**: `~/.claude/skills/markdown-to-pdf/` — scripts and skill definition.
**Output**: PDF files with the same base name as the source markdown files, placed in the same directory.

## Usage

### Basic Usage
```
/markdown-to-pdf
```
Converts all `.md` files in the current directory to PDF.

### With Specific Pattern
```
/markdown-to-pdf technical*.md
```
Converts only files matching the pattern.

### With Specific Files
```
/markdown-to-pdf file1.md file2.md
```
Converts specific files (space-separated list).

## How It Works

1. Finds markdown files matching the provided pattern (defaults to `*.md`)
2. For each markdown file, runs `npx markdown-pdf input.md -o input.pdf`
3. Creates PDF files with the same name as source files but with `.pdf` extension
4. Reports success/failure for each conversion

## Example

```
$ /markdown-to-pdf technical*.md
Found 4 file(s) to convert:
  - technical_prd_job_searching_app_ethiopia.md
  - technical_prd_legal_chatbot_app_ethiopia.md
  - technical_prd_local_events_tracker_app_etiopia.md
  - technical_prd_unbiased_news_aggregator_ethiopia.md
Converting technical_prd_job_searching_app_ethiopia.md -> technical_prd_job_searching_app_ethiopia.pdf...
✓ Successfully converted to technical_prd_job_searching_app_ethiopia.pdf
Converting technical_prd_legal_chatbot_app_ethiopia.md -> technical_prd_legal_chatbot_app_ethiopia.pdf...
✓ Successfully converted to technical_prd_legal_chatbot_app_ethiopia.pdf
Converting technical_prd_local_events_tracker_app_etiopia.md -> technical_prd_local_events_tracker_app_etiopia.pdf...
✓ Successfully converted to technical_prd_local_events_tracker_app_etiopia.pdf
Converting technical_prd_unbiased_news_aggregator_ethiopia.md -> technical_prd_unbiased_news_aggregator_ethiopia.pdf...
✓ Successfully converted to technical_prd_unbiased_news_aggregator_ethiopia.pdf

All 4 file(s) converted successfully!
```

## Requirements

- Node.js and npm must be installed
- The skill will automatically install `markdown-pdf` via npx if not present