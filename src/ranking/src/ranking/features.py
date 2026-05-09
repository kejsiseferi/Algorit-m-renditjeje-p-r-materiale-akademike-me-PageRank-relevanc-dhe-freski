from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from datetime import datetime


def relevance_scores(query, documents):

    texts = [doc["content"] for doc in documents]

    vectorizer = TfidfVectorizer()

    tfidf = vectorizer.fit_transform(texts + [query])

    similarities = cosine_similarity(
        tfidf[-1],
        tfidf[:-1]
    )[0]

    return similarities


def freshness_scores(documents):

    current_year = datetime.now().year

    scores = []

    for doc in documents:
        age = current_year - doc["year"]
        scores.append(1 / (1 + age))

    return np.array(scores)


def quality_scores(documents):

    return np.array([
        doc["quality"] for doc in documents
    ])
