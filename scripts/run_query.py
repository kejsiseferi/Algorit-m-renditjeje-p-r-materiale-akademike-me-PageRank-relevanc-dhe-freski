from src.ranking.graph_utils import load_documents, build_graph
from src.ranking.pagerank import compute_pagerank
from src.ranking.features import (
    relevance_scores,
    freshness_scores,
    quality_scores
)
from src.ranking.ranking_engine import combine_scores


documents = load_documents("examples/materials.json")

G = build_graph(documents)

pagerank = compute_pagerank(G)

query = input("Search query: ")

relevance = relevance_scores(query, documents)
freshness = freshness_scores(documents)
quality = quality_scores(documents)

scores = combine_scores(
    pagerank,
    relevance,
    freshness,
    quality
)

results = []

for i, doc in enumerate(documents):
    results.append((doc["title"], scores[i]))

results.sort(key=lambda x: x[1], reverse=True)

print("\nRANKED RESULTS:\n")

for title, score in results:
    print(f"{title} --> {score:.4f}")
