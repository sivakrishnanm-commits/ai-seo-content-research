# AI-Powered SEO Content Production Research — Research Project

A curated research base mapping how the strongest practitioners think about AI-powered SEO content production for **B2B SaaS** in 2026.

## What this is

This project contains **30+ deeply annotated LinkedIn posts** across **10 carefully selected experts**, plus YouTube transcripts, original research PDFs, and a semantic search index over the entire corpus.

Every post has structured annotations — claim, evidence type, cross-references, and playbook implication — so the material is ready to support a real playbook later, not just sit in a folder.

The bias throughout: depth over volume. A handful of sharp posts from a practitioner beat twenty surface-level ones. Same logic applied to experts: curate aggressively, defend each pick.

## Why these 10 experts

I rejected the standard "top SEO influencers" Google results — they optimize for follower counts and authority, not for the specific intersection of **AI + content production + B2B SaaS**. My selection bar:

1. **Ships work** — runs an agency, builds a tool, or operates in-house at scale
2. **Public content stream** — LinkedIn, YouTube, podcast, or newsletter
3. **At least one of:** original research, named clients, owned product, or 5+ years operating experience
4. **Active in the last 90 days**

The 10 span six strategic lenses on purpose:

| # | Expert | Lens | Why elite |
|---|---|---|---|
| 1 | Kevin Indig | Data | 250+ AI Mode sessions analyzed; original LLM citation studies |
| 2 | Eli Schwartz | Strategy | Author of *Product-Led SEO*; strategic counterweight to AI hype |
| 3 | Aleyda Solís | Curation | SEOFOMO (39K subs); creator of authority.md framework |
| 4 | Bernard Huang | Tool | Founder of Clearscope; clearest AEO/GEO breakdowns |
| 5 | Michael King | Technical | Most rigorous on entity SEO + LLM information retrieval |
| 6 | Ross Hudgens | Production | Authoring Wiley's GEO book (Q4 2026); design-led editorial at scale |
| 7 | Andrew Holland | Ranks-first | 200K+ page-one rankings; brand-mentions thesis |
| 8 | Alex Birkett | Research | Omniscient's 43K+ LLM citations study for B2B SaaS |
| 9 | Tim Soulo | Practical | Ahrefs YouTube — highest-signal practical SEO channel |
| 10 | Tom Critchlow | Executive | "AI search is four distinct problems"; the SEO MBA |

Full rationale, channels, and collection plan in [`research/sources.md`](research/sources.md).

## Repository structure

```
research/
├── sources.md                  ← 10 experts with rationale + channels
├── synthesis.md                ← synthesized insights and findings
├── ANNOTATION_TEMPLATE.md      ← annotation framework
├── linkedin-posts/             ← 30+ posts, all annotated
│   ├── kevin-indig/
│   ├── eli-schwartz/
│   ├── aleyda-solis/
│   ├── bernard-huang/
│   ├── michael-king/
│   ├── ross-hudgens/
│   ├── andrew-holland/
│   ├── alex-birkett/
│   ├── tim-soulo/
│   └── tom-critchlow/
├── youtube-transcripts/        ← cleaned transcripts by author
└── other/
    ├── links.md                ← newsletters, books, tools, podcasts
    ├── search-examples.md      ← example semantic search outputs
    └── *.pdf                   ← original research (Omniscient)
scripts/
├── download-transcripts.sh     ← batch fetch from configured sources
├── fetch_youtube.sh            ← yt-dlp wrapper for captions
├── clean_transcripts.py        ← SRT → clean Markdown
└── build_search_index.py       ← semantic search over the corpus
```

## What's collected

- **30+ LinkedIn posts** — organized by author, every one with structured annotation (claim / evidence type / cross-references / playbook implication)
- **YouTube transcripts** — collected via `yt-dlp` pipeline, organized by author, cleaned from SRT to readable Markdown
- **Original research PDFs** — Omniscient Digital's LLM citation studies (43,000+ and 23,000+ citations analyzed)
- **Semantic search index** — vector embeddings over the entire corpus using sentence-transformers
- **Links file** — newsletters, books, tools, and podcasts from the 10 experts

## Annotation framework

Every post follows the same structure (full spec in [`research/ANNOTATION_TEMPLATE.md`](research/ANNOTATION_TEMPLATE.md)):


```yaml
---
author: [name]
url: [LinkedIn URL]
source_type: linkedin_post
topic: [short]
engagement: [reactions + comments]
tags: [tag1, tag2, tag3]
---

# [Hook / first line of post]

[Full post body]

---

## Annotation

**Claim:** [Specific assertion in one sentence]
**Evidence type:** anecdote | data | framework | opinion | case-study
**Cross-references:**
- ✅ Agrees with: [author/file]
- ❌ Disagrees with: [author/file]
- ➕ Extends: [author/file]
**Playbook implication:** [1-2 sentences]
```



The claim/evidence/cross-reference structure forces explicit thinking. "This is about AI search" is not a claim — "aggregate AI dashboards mask 2-of-3 engine invisibility" is.

## Collection method

**YouTube transcripts** — automated pipeline:


```bash
bash scripts/fetch_youtube.sh "VIDEO_URL" "author-slug" "video-slug"
python scripts/clean_transcripts.py
```



`yt-dlp` pulls auto-generated captions as SRT, the Python script strips timestamps and emits clean Markdown.

**LinkedIn posts** — manual structured collection. LinkedIn has no public posts API, so I collected the highest-signal posts per author by hand: opened each profile's Activity → Posts tab, filtered for substantive posts (skipping pure reshares, event announcements, and job-change posts), and structured each into the annotation template via Claude Code.

## Semantic search over the corpus

The repo includes a semantic search index built with `sentence-transformers/all-MiniLM-L6-v2`. This lets you query the corpus by meaning, not just keywords — useful when synthesizing across experts.


```bash
pip install -r requirements.txt
python scripts/build_search_index.py                       # build index
python scripts/build_search_index.py "your query here"     # run a query
```



Example outputs in [`research/other/search-examples.md`](research/other/search-examples.md).

## Setup


```bash
pip install -r requirements.txt
```



## Usage

### Fetch a YouTube transcript


```bash
bash scripts/fetch_youtube.sh "VIDEO_URL" "author-slug" "video-slug"
```



### Clean transcripts


```bash
python scripts/clean_transcripts.py
```



### Build & query the search index


```bash
python scripts/build_search_index.py
python scripts/build_search_index.py "how do experts measure AI citation success"
```


## Research Workflow

1. Add new sources to `research/sources.md`
2. Use `ANNOTATION_TEMPLATE.md` to annotate each source in its subfolder
3. Run `fetch_youtube.sh` to pull transcripts into `youtube-transcripts/`
4. Run `clean_transcripts.py` to normalize the raw text
5. Run `build_search_index.py` to make all content searchable
6. Update `synthesis.md` with key insights

## Why the material supports a real playbook

The posts surface real disagreements between experts — not just overlapping consensus. A few that emerged while collecting:

- **Editorial SEO is dying** (Schwartz) vs. **design-led editorial is the moat** (Hudgens)
- **Aggregate AI visibility dashboards** (Huang/tool vendors) vs. **per-engine measurement** (Indig, Critchlow)
- **Brand mentions beat links** (Holland) vs. **entity graphs are the retrieval signal** (King)

These tensions are what a real playbook would resolve. The annotated posts + semantic search make it possible to pull supporting evidence on both sides of any debate.

## Status

- ✅ 10 experts curated across 6 strategic lenses
- ✅ 30+ LinkedIn posts collected, every one annotated
- ✅ YouTube transcripts collected and cleaned
- ✅ Original research PDFs added
- ✅ Semantic search index built over the corpus
- ✅ Annotation framework documented
- ✅ Atomic commits throughout (one per author, one per phase)
