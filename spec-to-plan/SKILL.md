---
name: spec-to-plan
description: Read a PRD, spec, or requirements document and produce a detailed, file-by-file implementation plan as a markdown file with checkboxes. Use when the user says "make a plan for this", "break this down into files", "create an implementation plan", or references a spec file they want organized into actionable steps.
---

# Spec-to-Plan Skill

Read a specification or PRD file and produce a comprehensive, step-by-step, file-by-file implementation plan with checkboxes.

## When to use

- User references a spec/PRD file (via `@filename.md` or direct path) and asks for an implementation plan
- User says "make a plan", "break this down", "create implementation steps"
- User shares a document and asks "how would you build this?"

Do NOT use when:
- The user wants to start building right away (use the plan implicitly, skip writing it out)
- The spec is trivial (a few files) — just build it

## Process

### 1. Read and analyze the spec

Read the full spec/PRD file. Extract:

| Aspect | What to identify |
|--------|-----------------|
| **Architecture** | Stack, framework, database, auth, deployment |
| **Data model** | All tables, entities, schemas, relationships |
| **Routes/Endpoints** | Web pages, API routes, auth requirements per route |
| **Business logic** | Key rules, validations, edge cases, state machines |
| **UI/Components** | Pages, views, components, design system |
| **Scrapers/Pipelines** | Data ingestion, ETL, cron jobs |
| **Testing** | What to test, at what level |
| **Infrastructure** | Environment variables, deployment config |

### 2. Organize into steps

Group files into logical implementation steps. Each step should:

- Be independently verifiable (has a clear done state)
- Produce at least one file (often several)
- Build on previous steps (dependencies respected)
- Follow a sensible order: scaffold → data → core logic → UI → API → tests → productionize

Common step structure (adjust based on the project):

```
Step 1:  Scaffold + Config        (package.json, env, DB connection, app shell)
Step 2:  Auth                     (routes, middleware, views)
Step 3:  Database schema + Seed   (migrations, seed data)
Step 4:  Core scrapers/fetchers   (data ingestion)
Step 5:  Extraction + Dedup       (parsing, deduplication logic)
Step 6:  Pipeline orchestration   (ingest, scheduler)
Step 7:  Admin features           (review queue, management)
Step 8:  Public web app           (routes, views, CSS, JS)
Step 9:  User dashboard           (create/edit events, analytics)
Step 10: API endpoints            (JSON API for programmatic access)
Step 11: Tests                    (unit, integration, E2E)
Step 12: Productionize            (logging, monitoring, Docker, deploy config)
```

### 3. List every file

For each step, list every file that needs to be created. For each file, include:

- **Path** — relative to project root
- **Purpose** — what it exports, what it does
- **Key contents** — functions, classes, SQL, routes, selectors, patterns
- **Key decisions** — notable implementation details from the spec

Format each file as a checkbox:

```
- [ ] **`src/config/database.js`** — Open SQLite database. Enable WAL mode, foreign keys. Export `db` instance. Create data dir if missing.
```

### 4. Write the plan

Write the plan as a markdown file at the project root. Name it based on the spec:

- `IMPLEMENTATION_PLAN.md` (if the spec is the primary project document)
- `{SPEC_NAME}_PLAN.md` (if there are multiple specs in the project)

Include:

- Title referencing the project name from the spec
- Brief intro describing the stack and architecture
- Each step as a heading level 2 (`## Step N: ...`)
- Every file as a checkbox list item under its step
- A progress summary table at the bottom
- A "Key Changes" table if the plan modernizes or replaces an existing approach

### 5. Guidelines

Follow CLAUDE.md throughout:

- **Think before coding.** State assumptions about the spec. If something is ambiguous, flag it.
- **Simplicity first.** Don't add speculative steps or files. Every file in the plan must trace directly to something in the spec.
- **Goal-driven.** Each step should have a verify line explaining how to confirm it's done.
- **Match the spec's vocabulary.** Use the same terms for tables, routes, and concepts as the spec does.

### 6. Verify

Before finishing, check:

- [ ] Every file in the plan traces to a requirement or component in the spec
- [ ] Steps are in dependency order (nothing references a file from a later step)
- [ ] Each checkbox has enough context for someone to implement it
- [ ] The progress summary table matches the actual file count
- [ ] Auth/filesystem/storage decisions are consistent (e.g., all use the same DB, all use the same auth mechanism)
- [ ] No unnecessary files or speculative features

## Output

A markdown file at the project root containing the complete implementation plan with checkboxes.