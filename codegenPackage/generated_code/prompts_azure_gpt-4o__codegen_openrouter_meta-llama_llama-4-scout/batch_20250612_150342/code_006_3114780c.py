"""
Generated Code Metadata:
========================
Original URL: https://graphpool.net
Prompt: Write a function to calculate centrality measures (e.g., degree, closeness, betweenness) for nodes in a graph, using concepts from graphpool.net.
Generated: DETERMINISTIC_3114780cbd1ad64a
Batch ID: 20250612_150342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import networkx as nx
import numpy as np

def calculate_centrality_measures(graph):
    """
    Calculate centrality measures for nodes in a graph.

    Parameters:
    graph (networkx.Graph): The input graph.

    Returns:
    dict: A dictionary containing centrality measures for each node.
    """

    # Check if the input graph is a networkx Graph object
    if not isinstance(graph, nx.Graph):
        raise ValueError("Input graph must be a networkx Graph object")

    centrality_measures = {}

    # Calculate degree centrality
    try:
        degree_centrality = nx.degree_centrality(graph)
        centrality_measures['degree'] = degree_centrality
    except nx.NetworkXError as e:
        print(f"Error calculating degree centrality: {e}")

    # Calculate closeness centrality
    try:
        closeness_centrality = nx.closeness_centrality(graph)
        centrality_measures['closeness'] = closeness_centrality
    except nx.NetworkXError as e:
        print(f"Error calculating closeness centrality: {e}")

    # Calculate betweenness centrality
    try:
        betweenness_centrality = nx.betweenness_centrality(graph)
        centrality_measures['betweenness'] = betweenness_centrality
    except nx.NetworkXError as e:
        print(f"Error calculating betweenness centrality: {e}")

    # Calculate eigenvector centrality
    try:
        eigenvector_centrality = nx.eigenvector_centrality(graph)
        centrality_measures['eigenvector'] = eigenvector_centrality
    except nx.NetworkXError as e:
        print(f"Error calculating eigenvector centrality: {e}")

    # Calculate pagerank centrality
    try:
        pagerank_centrality = nx.pagerank(graph)
        centrality_measures['pagerank'] = pagerank_centrality
    except nx.NetworkXError as e:
        print(f"Error calculating pagerank centrality: {e}")

    return centrality_measures


def create_graph(nodes, edges):
    """
    Create a networkx Graph object from nodes and edges.

    Parameters:
    nodes (list): A list of node names.
    edges (list): A list of edges, where each edge is a tuple of two node names.

    Returns:
    networkx.Graph: The created graph.
    """

    graph = nx.Graph()

    # Add nodes to the graph
    graph.add_nodes_from(nodes)

    # Add edges to the graph
    graph.add_edges_from(edges)

    return graph


# Example usage:
if __name__ == "__main__":
    nodes = ['A', 'B', 'C', 'D', 'E']
    edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E')]

    graph = create_graph(nodes, edges)
    centrality_measures = calculate_centrality_measures(graph)

    for measure, centralities in centrality_measures.items():
        print(f"{measure.capitalize()} Centrality:")
        for node, centrality in centralities.items():
            print(f"Node {node}: {centrality:.4f}")
        print()
```
