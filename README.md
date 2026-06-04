# Agent Skills

A curated collection of **agent skills** — modular, file-based instruction sets that extend what an AI coding assistant can do. Each skill is a self-contained directory with a `SKILL.md` file that defines its trigger conditions, workflow protocols, and tool usage patterns.

This repository is published at [github.com/MichaelTesemma/agent-skills](https://github.com/MichaelTesemma/agent-skills).

---

## What Is a Skill?

A skill is a markdown file (plus optional scripts and references) that teaches an AI agent a **repeatable methodology** for a specific task. Skills encode hard-won process knowledge — the checklists, edge cases, and quality gates that separate a one-off hack from a reliable result.

Skills live in `~/.agents/skills/` and are loaded by the agent harness when the user's request matches the skill's trigger description.

---

## Skills Index

### Research & Literature

| Skill | Description |
|---|---|
| **[deep-research](./deep-research/)** | Systematic academic literature reviews in 6 phases — frontier analysis, survey construction, deep dives, tooling, synthesis, and compilation. Produces structured notes, a curated paper database, and a final report. |
| **[literature-review](./literature-review/)** | Comprehensive literature reviews using multi-perspective dialogue simulation. Generates diverse expert personas, conducts grounded Q&A conversations, and synthesizes findings into structured knowledge. |
| **[literature-search](./literature-search/)** | Search academic literature via Semantic Scholar, arXiv, and OpenAlex APIs. Returns structured JSONL with title, authors, year, venue, abstract, citations, and BibTeX. |
| **[research-planning](./research-planning/)** | Design research plans and paper architectures — methodology outlines, paper structure, dependency-ordered task lists, UML diagrams, and experiment designs. |
| **[github-research](./github-research/)** | Explore and analyze GitHub repositories related to a research topic. Reads deep-research output, discovers repos from multiple sources, deeply analyzes code, and produces integration blueprints. |

### Development & Engineering

| Skill | Description |
|---|---|
| **[frontend-design](./frontend-design/)** | Create distinctive, production-grade frontend interfaces with high design quality. Generates creative, polished code that avoids generic AI aesthetics. |
| **[prototype](./prototype/)** | Build throwaway prototypes to flesh out a design before committing. Routes between terminal apps (for state/logic questions) and UI variations (for visual exploration). |
| **[tdd](./tdd/)** | Test-driven development with a disciplined red-green-refactor loop. Covers deep module patterns, interface design, mocking strategies, and test writing. |
| **[spec-to-plan](./spec-to-plan/)** | Read a PRD, spec, or requirements document and produce a detailed, file-by-file implementation plan as a markdown file with checkboxes. |
| **[improve-codebase-architecture](./improve-codebase-architecture/)** | Find deepening opportunities in a codebase — consolidate tightly-coupled modules, make code more testable and AI-navigable, informed by domain language and architecture decision records. |

### Debugging & Diagnosis

| Skill | Description |
|---|---|
| **[diagnose](./diagnose/)** | Disciplined diagnosis loop for hard bugs and performance regressions: reproduce → minimise → hypothesise → instrument → fix → regression-test. |

### Planning & Decision-Making

| Skill | Description |
|---|---|
| **[grill-me](./grill-me/)** | Interview the user relentlessly about a plan or design until reaching shared understanding, resolving each branch of the decision tree. |
| **[grill-with-docs](./grill-with-docs/)** | Grilling session that challenges your plan against the existing domain model, sharpens terminology, and updates documentation (CONTEXT.md, ADRs) inline as decisions crystallise. |
| **[to-prd](./to-prd/)** | Turn conversation context into a Product Requirements Document and publish it to the project issue tracker. |
| **[to-issues](./to-issues/)** | Break a plan, spec, or PRD into independently-grabbable issues on the project issue tracker using tracer-bullet vertical slices. |

### Utilities

| Skill | Description |
|---|---|
| **[find-skills](./find-skills/)** | Helps users discover and install agent skills from the ecosystem. Searches the skills leaderboard, verifies quality, and presents options. |
| **[markdown-to-pdf](./markdown-to-pdf/)** | Converts markdown files to PDF using the `markdown-pdf` npm package. |

---

## Skill Anatomy

Each skill directory typically contains:

```
skill-name/
├── SKILL.md          # The skill definition (required)
├── scripts/          # Helper scripts (optional)
└── references/       # Reference materials (optional)
```

A `SKILL.md` uses YAML frontmatter to declare:

```yaml
---
name: skill-name
description: What triggers this skill and what it does
argument-hint: [optional-argument-hint]
---
```

The body defines the full methodology — phases, quality gates, tool usage rules, and output conventions.

---

## Workflow

A typical skill-augmented session looks like:

1. A user request matches a skill's trigger description.
2. The agent loads the skill's `SKILL.md` and follows its protocol.
3. The skill enforces its phase gates — later phases block until earlier ones produce checkpoints.
4. Output is written to a structured directory or shared context.

Some skills compose: `github-research` reads the output of `deep-research`; `literature-review` can feed into `research-planning`.

---

## Contributing

This collection evolves as methodologies are refined. Skills are added when a repeatable, cross-project workflow crystallises — one that would benefit from enforced phase gates and quality checks rather than ad-hoc execution.

### Design Principles

- **Self-contained**: A skill should be understandable from its `SKILL.md` alone.
- **Phase-gated**: Each phase produces a checkpoint; later phases verify earlier ones.
- **Tool-agnostic**: Prefer portable scripts (Python, bash) over platform-specific tools.
- **Minimal surface area**: One job per skill. Compose existing skills rather than duplicating.

---

## License

All skills in this repository are provided for use with the [pi coding agent](https://github.com/earendil-works/pi-coding-agent) and similar agent harnesses. See individual skill directories for any license terms.