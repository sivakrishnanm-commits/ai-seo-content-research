---
author: Kevin Indig
url: https://www.linkedin.com/posts/kevinindig_almost-no-cited-sources-are-visible-across-activity-7459946771713060864-fuYy?utm_source=share&utm_medium=member_desktop&rcm=ACoAACRImngBzYt5MemdmK04bMCCxmAPBWNe2XU
source_type: linkedin_post
topic: Citation overlap stays flat across query intent types
engagement: 33 reactions, 15 comments
tags: [ai-visibility, citation-analysis, query-intent, cross-llm, aeo]
---

# Almost no cited sources are visible across several LLMs for the same prompt.

I checked whether user intent might make a difference. It doesn't.

The instinct says it should. "Best CRM," "best running shoes," "best project management software" feel like queries with a narrower pool of acceptable sources than broad informational prompts. Engines should agree more often.

Across 2.6 million URLs split between commercial, informational, and other intent, they really don't. The universal overlap rate stays roughly flat.

Each LLM picks different sources most of the time, even where the query should constrain the answer set. The retrieval logic, what each engine trusts and what format it favors, does more work than the query type.

That mutes a common AEO assumption: that bottom-of-funnel visibility converges across engines. Commercial visibility has the same fragmentation problem as informational visibility.

The best-of guide that wins in Perplexity probably isn't the same guide winning in ChatGPT or Google AI Overviews. Optimizing for one LLM and treating that as universal coverage is a planning error.

---

## Annotation

**Claim:** Cross-LLM citation overlap stays flat regardless of query intent — commercial queries fragment just as much as informational ones, falsifying the assumption that bottom-of-funnel visibility converges across engines.

**Evidence type:** data

**Cross-references:**
- ✅ Agrees with: kevin-indig/ai-visibility-fragmentation.md
- ❌ Disagrees with: [TBD — AEO practitioners who treat commercial content as engine-agnostic]
- ➕ Extends: alex-birkett/llm-citations-research.md

**Playbook implication:** B2B SaaS "best-of" and comparison content cannot be written once and treated as covering all LLM surfaces. Each engine's citation logic differs enough that a piece ranking in Perplexity for "best [category] software" may be invisible in ChatGPT — requiring engine-specific content or distribution strategies for high-intent queries.
