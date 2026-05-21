# Semantic Search Index — Example Query Outputs

Index built with TF-IDF + cosine similarity (sklearn) over all markdown files in `research/`.  
Model: TF-IDF (1–2 gram, sublinear TF, max 50k features) — offline fallback; HuggingFace blocked in this environment.  
Corpus: 43 chunks from research markdown files.  
Index path: `.embeddings/corpus.pkl`

---

## Query 1: "how do experts measure AI citation success"

```
🔎 Top 5 matches for: 'how do experts measure AI citation success'

[1] 0.062  research/linkedin-posts/tim-soulo/ai-referral-traffic-misleading-metric.md (chunk 0)
     --- author: Tim Soulo url: https://www.linkedin.com/posts/timsoulo_ai-search-traffic-to-75k-websites-dropped-activity-7462189011965620226-7cmv?utm_source=share&utm_medium=member_desktop&rcm=ACoAACRImngBzYt5MemdmK04bMCCxmAPBWNe2XU source_type: linkedin_post topic: AI search referral traffic is declin...

[2] 0.058  research/linkedin-posts/aleyda-solis/ecommerce-ai-citation-patterns.md (chunk 0)
     --- author: Aleyda Solís url: https://www.linkedin.com/posts/aleyda_ecommerce-ai-search-optimization-what-activity-7459978678416871424-1A3Z?utm_source=share&utm_medium=member_desktop&rcm=ACoAACRImngBzYt5MemdmK04bMCCxmAPBWNe2XU source_type: linkedin_post topic: Ecommerce AI citation patterns extend b...

[3] 0.024  research/linkedin-posts/bernard-huang/aeo-prompt-tracking-fundamentals.md (chunk 0)
     --- author: Bernard Huang url: https://www.linkedin.com/posts/bernardjhuang_if-seo-tracking-keywords-then-aeo-tracking-activity-7424551520656039936-Lhe1?utm_source=share&utm_medium=member_desktop&rcm=ACoAACRImngBzYt5MemdmK04bMCCxmAPBWNe2XU source_type: linkedin_post topic: AEO = tracking prompts, bu...

[4] 0.022  research/linkedin-posts/eli-schwartz/ai-content-farms-penalized.md (chunk 0)
     --- author: Eli Schwartz url: https://www.linkedin.com/posts/schwartze_some-seo-teams-genuinely-thought-theyd-cracked-activity-7452695263019921408-zrUT?utm_source=share&utm_medium=member_desktop&rcm=ACoAACRImngBzYt5MemdmK04bMCCxmAPBWNe2XU source_type: linkedin_post topic: AI content farms penalized ...

[5] 0.022  research/linkedin-posts/bernard-huang/aeo-experiment-prompt-intent.md (chunk 0)
     --- author: Bernard Huang url: https://www.linkedin.com/posts/bernardjhuang_for-those-of-you-following-along-we-started-activity-7456035794974302208-fnZR?utm_source=share&utm_medium=member_desktop&rcm=ACoAACRImngBzYt5MemdmK04bMCCxmAPBWNe2XU source_type: linkedin_post topic: AEO experiment — prompt i...
```

---

## Query 2: "editorial SEO is dying versus design-led editorial"

```
🔎 Top 5 matches for: 'editorial SEO is dying versus design-led editorial'

[1] 0.085  research/linkedin-posts/kevin-indig/organic-search-still-drives-answers.md (chunk 0)
     --- author: Kevin Indig url: https://www.linkedin.com/posts/kevinindig_even-though-clicks-drop-like-flies-when-google-share-7327710402555850752-O1EJ?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAACRImngBzYt5MemdmK04bMCCxmAPBWNe2XU source_type: linkedin_post topic: UX study — org...

[2] 0.031  research/linkedin-posts/kevin-indig/ai-skills-salary-premium.md (chunk 0)
     --- author: Kevin Indig url: https://www.linkedin.com/posts/kevinindig_the-seo-job-market-has-quietly-repriced-itself-activity-7454488282047913985-qZg7?utm_source=share&utm_medium=member_desktop&rcm=ACoAACRImngBzYt5MemdmK04bMCCxmAPBWNe2XU source_type: linkedin_post topic: AI skills command a 27% sal...

[3] 0.022  research/linkedin-posts/ross-hudgens/category-leader-llm-visibility-risk.md (chunk 1)
     affiliates, incentivized by higher competitor commissions, produce counter-narrative content ("X is dead," "Y isn't worth using") that compounds into measurable sentiment drag in AI-generated recommendations. **Evidence type:** opinion **Cross-references:** - ✅ Agrees with: eli-schwartz/llm-optimiza...

[4] 0.022  research/other/links.md (chunk 0)
     # Additional Resources  Additional sources referenced or relevant to this research project, organized  by category. Not all are collected as files in this repo — these serve as  pointers for deeper investigation beyond the curated material.  ## Newsletters  - Kevin Indig — Growth Memo: https://www.k...

[5] 0.021  research/linkedin-posts/eli-schwartz/ai-content-farms-penalized.md (chunk 0)
     --- author: Eli Schwartz url: https://www.linkedin.com/posts/schwartze_some-seo-teams-genuinely-thought-theyd-cracked-activity-7452695263019921408-zrUT?utm_source=share&utm_medium=member_desktop&rcm=ACoAACRImngBzYt5MemdmK04bMCCxmAPBWNe2XU source_type: linkedin_post topic: AI content farms penalized ...
```

---

## Query 3: "brand mentions versus entity graphs in AI search"

```
🔎 Top 5 matches for: 'brand mentions versus entity graphs in AI search'

[1] 0.108  research/linkedin-posts/ross-hudgens/category-leader-llm-visibility-risk.md (chunk 1)
     affiliates, incentivized by higher competitor commissions, produce counter-narrative content ("X is dead," "Y isn't worth using") that compounds into measurable sentiment drag in AI-generated recommendations. **Evidence type:** opinion **Cross-references:** - ✅ Agrees with: eli-schwartz/llm-optimiza...

[2] 0.077  research/linkedin-posts/andrew-holland/geo-is-not-seo.md (chunk 1)
     are prepared, or are quickly getting prepared, for the changes. I know because people message me on this. However, 90% of what's being written on AI search is nonsense. It's SEO consultants who spend most of their time repeating "It's just SEO" At the same time, being strategically ambiguous and say...

[3] 0.064  research/linkedin-posts/kevin-indig/brand-mentions-vs-citations.md (chunk 0)
     --- author: Kevin Indig url: https://www.linkedin.com/posts/kevinindig_you-might-have-noticed-that-ai-models-do-activity-7453027466018869249-RULD?utm_source=share&utm_medium=member_desktop&rcm=ACoAACRImngBzYt5MemdmK04bMCCxmAPBWNe2XU source_type: linkedin_post topic: Recognized brands get named in AI...

[4] 0.062  research/linkedin-posts/tim-soulo/ai-referral-traffic-misleading-metric.md (chunk 0)
     --- author: Tim Soulo url: https://www.linkedin.com/posts/timsoulo_ai-search-traffic-to-75k-websites-dropped-activity-7462189011965620226-7cmv?utm_source=share&utm_medium=member_desktop&rcm=ACoAACRImngBzYt5MemdmK04bMCCxmAPBWNe2XU source_type: linkedin_post topic: AI search referral traffic is declin...

[5] 0.056  research/linkedin-posts/andrew-holland/geo-is-not-seo.md (chunk 0)
     --- author: Andrew Holland url: https://www.linkedin.com/posts/andrew-holland-seo_the-seo-industry-just-changed-overnight-with-activity-7462771951510597633-TAYm?utm_source=share&utm_medium=member_desktop&rcm=ACoAACRImngBzYt5MemdmK04bMCCxmAPBWNe2XU source_type: linkedin_post topic: Google I/O made AI...
```
