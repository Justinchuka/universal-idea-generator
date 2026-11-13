# Universal Idea Generator (Agent Skill)

A multidisciplinary idea discovery, research and concept-development skill. It takes someone from *no idea*, *a vague thought*, *an industry*, *a problem* or *an existing product* to a set of original directions, ten developed ideas, and a discipline-specific brief with post-brief guidance.

> You are not simply generating ideas. You are helping people discover what is worth creating.

## What it does
- **Four generation paths:** Original Ideas, Evidence-Based / Research-Driven Ideas, Existing-Idea Exploration (replicate for another audience / different angle / exploit gaps / review and document), and Surprise Me.
- **Guided workflow:** Pillar -> Category -> Subcategory -> 10 Idea Directions -> 10 Ideas -> Selected Idea -> Developed Brief -> Post-Brief Intelligence.
- **18 expandable pillars** (digital products, business, branding, marketing, content, entertainment and media, art, writing and publishing, games, education, events, social impact, lifestyle, architecture, fashion, invention, food, sales). Unlisted disciplines are handled, not rejected.
- **Discipline-specific briefs** (title card, tailored opening, relevant sections only) and a required post-brief explanation.
- **Independent decisions:** "decide for me" means it decides. Direct requests skip onboarding.
- **Integrity rules:** originality checks, no invented research, evidence labels, honesty about generated assets.
- **Optional continuous discovery:** off by default, only with explicit consent.

## Install
- **Claude.ai / Claude app:** Settings > Capabilities > Skills > upload the ZIP (feature availability depends on your plan; check Anthropic's current documentation).
- **Claude Code:** unzip into `~/.claude/skills/` (personal) or `.claude/skills/` (project) so you have `universal-idea-generator/SKILL.md`.
- **Other agents:** use `SKILL.md` and `references/` as instructions; paths in SKILL.md are relative to the skill folder.

## Use
Just ask, for example: "Ten ideas for a cinematic ad for a new smartphone", "Surprise me", "Find gaps in [industry]", "Here's an app, what can I do with it?", or "Give me the full brief for [idea]".

## Structure
```
universal-idea-generator/
  SKILL.md                 routing, workflow, non-negotiables
  references/              taxonomy, paths, research, originality, briefs, post-brief, refinement, interaction, media, continuous discovery
  examples/                illustrative (fictional) examples
  evals/evals.json         14 test prompts with pass criteria
  scripts/validate_skill.py mechanical checks
  LICENSE                  MIT
```

## Limitations
- Research quality depends on the environment having web search. Without it, the skill says so and offers labelled hypotheses only.
- Recurring discovery needs a scheduling tool; the skill cannot run in the background by itself.
- It generates ideas and briefs. Producing actual images, audio or video requires separate tools.
- The eval prompts have not been run against a live model by the author of this package; see `evals/evals.json`.

## Validate
`python scripts/validate_skill.py .`

## License
MIT. See `LICENSE`.
