import numpy as np


def combine_scores(
    pagerank,
    relevance,
    freshness,
    quality,
    wP=0.4,
    wR=0.3,
    wF=0.2,
    wQ=0.1
):

    final_scores = []

    pagerank_values = np.array(
        list(pagerank.values())
    )

    for i in range(len(relevance)):

        score = (
            wP * pagerank_values[i]
            + wR * relevance[i]
            + wF * freshness[i]
            + wQ * quality[i]
        )

        final_scores.append(score)

    return np.array(final_scores)
