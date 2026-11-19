# Universal Idea Generator (Agent Skill)

A multidisciplinary idea discovery, research and concept-development skill. It takes someone from *no idea*, *a vague thought*, *an industry*, *a problem* or *an existing product* to a set of original ideas, a developed brief and practical next steps.

> You are not simply generating ideas. You are helping people discover what is worth creating.

## What it does
- **Four generation paths:** Original Ideas, Evidence-Based / Research-Driven Ideas, Existing-Idea Exploration and Surprise Me.
- **Guided workflow:** Pillar -> Category -> Subcategory -> 10 Idea Directions -> 10 Ideas -> Selected Idea -> Developed Brief -> Post-Brief Intelligence.
- **18 expandable pillars** spanning product, business, branding, marketing, content, entertainment, art, writing, games, education, events, social impact, lifestyle, architecture, fashion, science, food and sales.
- **Discipline-specific briefs** (title card, tailored opening, relevant sections only) and a required post-brief explanation.
- **Independent decisions:** "decide for me" means it decides. Direct requests skip onboarding.
- **Integrity rules:** originality checks, no invented research, evidence labels, honesty about generated assets.
- **Optional continuous discovery:** off by default, only with explicit consent.

## What you can get ideas for
These 18 pillars are starting territories, not a closed list. Unlisted disciplines are handled rather than rejected. Industry, audience, geography, purpose and constraints are context that shape an idea, not separate pillars.

- **Product, Technology & Digital Solutions** — SaaS, web/mobile apps, websites, e-commerce, marketplaces, AI products and agents, developer tools, APIs, enterprise software, automation, fintech, health tech, edtech, agritech, proptech, legal tech, climate tech, browser extensions, no-code, digital infrastructure.
- **Business & Entrepreneurship** — startup concepts, side hustles, service/subscription/platform businesses, revenue models, business-model innovation, new markets, B2B/B2C, digital/physical/hybrid ventures.
- **Branding & Brand Identity** — brand concepts, naming, personal/corporate branding, identity systems, positioning, rebranding, luxury/lifestyle brands, packaging and verbal identity, campaigns.
- **Marketing, Advertising & Growth** — campaigns, cinematic ads, brand films, launch campaigns, guerrilla, experiential, influencer, social, outdoor, email, retention, conversion.
- **Content Creation & Creator Economy** — social content concepts, content series, podcasts, newsletters, educational content, thought leadership, creator-led brands, communities, editorial.
- **Entertainment & Media** — films, TV/web series, music, music videos, photography, cinematic video, animation, comedy, documentaries, audio storytelling, immersive media.
- **Art & Visual Creation** — graphic design, illustration, concept art, character/environment design, world-building, 3D, generative art, typography, posters, motion graphics, visual storytelling, mockups, infographics.
- **Writing, Publishing & Literary Creation** — fiction, non-fiction, essays, poetry, guides, workbooks, copywriting, journalism, newsletters, white papers, speeches, screenplays and scripts, technical writing.
- **Games & Interactive Experiences** — video/mobile/browser/board/card games, interactive fiction, game mechanics, simulations, gamification, educational games, AR/VR, interactive installations.
- **Education & Learning** — online courses, workshops, training programmes, learning platforms, educational apps, teaching methodologies, frameworks, corporate training.
- **Events, Experiences & Activations** — conferences, festivals, exhibitions, pop-ups, brand activations, immersive events, community gatherings, launch experiences.
- **Community, Social Impact & Civic Innovation** — community initiatives, social enterprises, nonprofits, public health, financial inclusion, environmental solutions, accessibility, public services, empowerment.
- **Lifestyle & Personal Development** — personal projects, productivity systems, wellness, hobbies, self-improvement, habit systems, organisation.
- **Architecture, Spaces & Built Environment** — residential/commercial architecture, interiors, retail spaces, smart homes, public spaces, urban environments, sustainable architecture, adaptive reuse.
- **Fashion, Beauty & Consumer Lifestyle** — clothing/footwear/accessories, beauty/skincare, fashion campaigns, style concepts, luxury products, wearables.
- **Science, Engineering & Invention** — inventions, engineering solutions, material innovations, hardware, robotics, assistive tech, energy, environmental engineering, applied physics.
- **Food, Beverage & Hospitality** — restaurants, food/beverage products, culinary experiences, hospitality services, delivery, food tech, packaging, food retail.
- **Sales & Customer Experience** — sales strategies, customer engagement/retention, loyalty, support innovations, onboarding, customer success, revenue optimisation.

## Ways to generate ideas (paths)

| Path | What you provide | What the skill produces | When to use it |
|---|---|---|---|
| **Path 1 — Original Ideas** | A discipline, or permission to choose one. | 10 exploration directions -> 10 ideas -> selected idea -> brief -> post-brief guidance. | The field is known, but the idea is not. |
| **Path 2 — Evidence-Based / Research-Driven** | A domain or question. | Research first, then an opportunity context: what was investigated and found, current practice, apparent gaps, identified opportunity and why it is worth exploring; ideas follow. Facts, observations, hypotheses and speculation are labelled separately. Without web access, the skill says so and offers labelled hypotheses only. | Questions like "what's missing in X?", "what pain points exist?" or "where's the gap?" |
| **Path 3 — Existing-Idea Exploration** | An existing app, site, business, brand, film, book, ad or technology. | Explore four approaches: replicate for another audience; re-angle the positioning, mechanism, experience, business model, distribution or execution; exploit gaps and limitations; or review and document. Gaps must be observed or evidenced, with inferred gaps labelled as hypotheses. Intellectual property is respected. | There is an existing idea or product to learn from, adapt or assess. |
| **Path 4 — Surprise Me** | Nothing; the user can delegate the choice. | Independently choose an unusual pillar, category, subcategory and context, state the territory and why it is worth attention, then generate 10 ideas. | There is no direction yet and the user wants a surprising but worthwhile starting point. |

Paths can be combined and switched. A direct request for a brief, list or script skips the guided sequence.

## Install
- **Claude.ai / Claude app:** Settings > Capabilities > Skills > upload the ZIP (feature availability depends on your plan; check Anthropic's current documentation).
- **Claude Code:** unzip into `~/.claude/skills/` (personal) or `.claude/skills/` (project) so you have `universal-idea-generator/SKILL.md`.
- **Other agents:** use `SKILL.md` and `references/` as instructions; paths in SKILL.md are relative to the skill folder.

## Use
On first contact, the skill introduces itself in 2–3 lines, briefly mentions the available paths, then asks: "What is your designation, profession, or what do you want to create? Or would you like me to suggest an idea to you?" Saying yes, "suggest an idea", "surprise me" or "decide for me" sends it to Path 4 without extra questions.

Examples: "Suggest an idea for me", "Surprise me", "Give me product ideas from the list", "Find gaps in [industry]", "Here's my app — re-angle it", "Full brief for [idea]". Direct requests skip onboarding.

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
