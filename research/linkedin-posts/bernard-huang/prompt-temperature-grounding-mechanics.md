---
author: Bernard Huang
url: https://www.linkedin.com/posts/bernardjhuang_weve-been-doing-extensive-research-into-activity-7426678788962410496-Yric?utm_source=share&utm_medium=member_desktop&rcm=ACoAACRImngBzYt5MemdmK04bMCCxmAPBWNe2XU
source_type: linkedin_post
topic: Temperature, sample size, and grounding mechanics determine AI brand mention reliability
engagement: 19 reactions, 0 comments
tags: [prompt-tracking, temperature, gemini, grounding, brand-mentions, measurement]
---

# We've been doing extensive research into prompting at Clearscope.

We've been doing extensive research into prompting at Clearscope. The main problem with prompting is variance — how do I know what a user gets back from an AI response is the same as what I get back from my prompt?

To dig deep into this, we've explored looking at sample size and temperature.

tl;dr — 
* prompting AI models with temperature 0 gives you the most precise response from an AI,
* responses are then influenced by grounding with search + memory/context/personalization. 
* by default, Gemini tries to prevent bias by ignoring a brand as a source if the brand is mentioned in the response,
* but grounding with search allows a brand's webpage some influence over a response

# Larger sample size provide more accurate %s of brand mentions, citations, sources. 
Prompt tracking data is better consumed by understanding frequencies. Especially when considering the query fan out — you are way more likely to have influence over an AI when targeting a high probability query fan out

# Temperature 0 expresses the closest to the absolute response
Most AI models are default set to temperature 1. This gives the AI flexibility in deviating away from the "absolute response".

So what happens when we look at large sample size frequencies and compare it to temperature 0 responses?

Prompt: [commercial: what are the most affordable SEO tools?]

At temperature 0, you can see that all brands get mentioned by Gemini. They want to give a comprehensive list. The variance at temperatures 0.5 and 1 are likely influenced by memory/context/personalization considerations.

When looking at Gemini sources, we notice that Gemini does not want to use content from any brand that was recommended by default. Ahrefs and Semrush only show up 20%-37% in frequency when the model is allowed to have more freedom. IMO, this indicates how much "grounding" influence Gemini is allowing for this kind of prompt.

Lastly, inspecting the query fan out gives an indication of "reasoning weight". Again, at temperature 0, you get the fullest idea of highest frequency weights. The long long tail of queries present an interesting set of queries to potentially pursue IF your brand intersects well with the subtopic.

---

## Annotation

**Claim:** Reliable AEO measurement requires large sample sizes read as frequency percentages rather than single-prompt snapshots, because temperature variance and Gemini's grounding bias against self-recommending brands make individual responses unrepresentative of actual user exposure.

**Evidence type:** data

**Cross-references:**
- ✅ Agrees with: kevin-indig/ai-visibility-fragmentation.md
- ❌ Disagrees with: [TBD — tools reporting single-prompt AI visibility scores as definitive]
- ➕ Extends: bernard-huang/aeo-experiment-prompt-intent.md

**Playbook implication:** B2B SaaS teams must treat AEO brand mention data as statistical frequencies across many prompt runs, not as pass/fail snapshots — a single-prompt check that returns no brand mention is meaningless; only frequency data across temperature variation reveals true visibility.
