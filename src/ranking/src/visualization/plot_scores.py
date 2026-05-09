import matplotlib.pyplot as plt


def plot_scores(titles, scores):

    plt.figure(figsize=(10, 5))

    plt.bar(titles, scores)

    plt.xticks(rotation=45)

    plt.ylabel("Final Score")

    plt.title("Document Ranking Scores")

    plt.tight_layout()

    plt.show()
