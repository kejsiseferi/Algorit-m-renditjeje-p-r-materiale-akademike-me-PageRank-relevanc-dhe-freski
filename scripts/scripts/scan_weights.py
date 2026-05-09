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

query = "quantum mechanics"

relevance = relevance_scores(query, documents)
freshness = freshness_scores(documents)
quality = quality_scores(documents)


weight_sets = [
    (0.4, 0.3, 0.2, 0.1),
    (0.6, 0.2, 0.1, 0.1),
    (0.2, 0.5, 0.2, 0.1),
]


for weights in weight_sets:

    wP, wR, wF, wQ = weights

    scores = combine_scores(
        pagerank,
        relevance,
        freshness,
        quality,
        wP=wP,
        wR=wR,
        wF=wF,
        wQ=wQ
    )

    print("\n====================")
    print(f"Weights: {weights}")
    print("====================")

    results = []

    for i, doc in enumerate(documents):
        results.append(
            (doc["title"], scores[i])
        )

    results.sort(
        key=lambda x: x[1],
        reverse=True
    )

    for title, score in results:
        print(f"{title} --> {score:.4f}")
