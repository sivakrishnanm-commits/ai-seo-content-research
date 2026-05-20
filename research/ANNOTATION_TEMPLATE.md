# Annotation Framework

Every LinkedIn post and transcript in this repo follows a structured 
annotation to convert raw content into playbook-ready signal.

## Filename convention

`research/linkedin-posts/{author-slug}/{topic-slug}.md`

Example: `research/linkedin-posts/kevin-indig/ai-mode-visibility.md`

## Frontmatter (every file)


```yaml
---
author: Kevin Indig
url: https://www.linkedin.com/posts/...
source_type: linkedin_post | youtube_transcript | newsletter | podcast
topic: AI Mode visibility study
engagement: 1.2K reactions, 180 comments
tags: [ai-search, measurement, original-research]
---
```



## Body structure

1. Full content (post body or transcript), line breaks preserved.
2. Annotation block at the bottom:


```markdown
---

## Annotation

**Claim:** [The specific assertion in one sentence — not "this is about 
AI search," the actual claim.]

**Evidence type:** anecdote | data | framework | opinion | case-study

**Cross-references:**
- ✅ Agrees with: [Author / file]
- ❌ Disagrees with: [Author / file]
- ➕ Extends: [Author / file]

**Playbook implication:** [1–2 sentences. What does this change about 
how you'd build AI-powered SEO content production for B2B SaaS?]
```


## Example annotation

> **Claim:** Aggregate AI visibility dashboards mask 2-of-3 engine 
> invisibility — a brand can score "dominant" overall while being uncited 
> in Perplexity entirely.
>
> **Evidence type:** data
>
> **Cross-references:**
> - ❌ Disagrees with: bernard-huang/aeo-geo-webinar.md
> - ➕ Extends: alex-birkett/llm-citations-research.md
>
> **Playbook implication:** Measurement layer needs per-engine breakdowns, 
> not a single visibility score. Content briefs must vary per engine.

## Why this framework

The brief states "10 high-signal sources beat 50 generic ones." Annotations 
are how raw content becomes signal. The claim/evidence/cross-reference 
structure forces explicit thinking instead of vague summary.
