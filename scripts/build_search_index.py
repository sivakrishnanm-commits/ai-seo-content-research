"""Build a semantic search index over all collected content.

Usage:
    python scripts/build_search_index.py        # build/refresh index
    python scripts/build_search_index.py "your query here"
"""
import sys
import pickle
from pathlib import Path
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

INDEX_DIR = Path(".embeddings")
INDEX_DIR.mkdir(exist_ok=True)
INDEX_PATH = INDEX_DIR / "corpus.pkl"

def load_corpus():
    docs = []
    for p in Path("research").rglob("*.md"):
        if p.name in ("ANNOTATION_TEMPLATE.md", "sources.md", "synthesis.md"):
            continue
        text = p.read_text(encoding="utf-8")
        words = text.split()
        if len(words) > 500:
            for i in range(0, len(words), 400):
                chunk = " ".join(words[i:i+500])
                docs.append({"path": str(p), "chunk": i // 400, "text": chunk})
        else:
            docs.append({"path": str(p), "chunk": 0, "text": text})
    return docs

def build_index():
    print("Fitting TF-IDF vectorizer...")
    docs = load_corpus()
    texts = [d["text"] for d in docs]
    vectorizer = TfidfVectorizer(
        sublinear_tf=True,
        max_df=0.85,
        min_df=1,
        ngram_range=(1, 2),
        max_features=50000,
    )
    embeddings = vectorizer.fit_transform(texts).toarray().astype(np.float32)
    print(f"Embedding {len(docs)} chunks...")
    with open(INDEX_PATH, "wb") as f:
        pickle.dump({"docs": docs, "embeddings": embeddings, "vectorizer": vectorizer}, f)
    print(f"✅ Index built: {len(docs)} chunks → {INDEX_PATH}")

def search(query: str, k: int = 5):
    if not INDEX_PATH.exists():
        print("No index yet. Run without query first.")
        return
    with open(INDEX_PATH, "rb") as f:
        data = pickle.load(f)
    vectorizer = data["vectorizer"]
    q_emb = vectorizer.transform([query]).toarray().astype(np.float32)
    sims = cosine_similarity(q_emb, data["embeddings"])[0]
    top = np.argsort(-sims)[:k]
    print(f"\n🔎 Top {k} matches for: {query!r}\n")
    for rank, idx in enumerate(top, 1):
        d = data["docs"][idx]
        preview = d["text"][:300].replace("\n", " ")
        print(f"[{rank}] {sims[idx]:.3f}  {d['path']} (chunk {d['chunk']})")
        print(f"     {preview}...\n")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        search(" ".join(sys.argv[1:]))
    else:
        build_index()
