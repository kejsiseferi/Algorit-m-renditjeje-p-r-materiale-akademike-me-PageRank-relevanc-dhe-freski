import json
import networkx as nx


def load_documents(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def build_graph(documents):
    G = nx.DiGraph()

    for doc in documents:
        G.add_node(doc["id"], title=doc["title"])

    for doc in documents:
        for link in doc["links"]:
            G.add_edge(doc["id"], link)

    return G
