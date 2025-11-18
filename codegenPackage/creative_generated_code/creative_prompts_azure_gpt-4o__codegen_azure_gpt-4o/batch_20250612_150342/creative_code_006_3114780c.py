"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://graphpool.net
Prompt: Write a function to calculate centrality measures (e.g., degree, closeness, betweenness) for nodes in a graph, using concepts from graphpool.net.
Generated: DETERMINISTIC_3114780cbd1ad64a
Batch ID: 20250612_150342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import networkx as nx

def calculate_centrality_measures(graph):
    """
    Calculate centrality measures for nodes in a graph.
    
    Parameters:
        graph (networkx.Graph): A NetworkX graph object.
    
    Returns:
        dict: A dictionary containing centrality measures for each node.
              Keys are node IDs, values are dictionaries of centrality measures.
    
    Raises:
        ValueError: If the input is not a valid NetworkX graph.
    """
    # Validate input
    if not isinstance(graph, nx.Graph):
        raise ValueError("Input must be a NetworkX graph.")

    # Initialize result dictionary
    centrality_measures = {}

    try:
        # Degree centrality
        degree_centrality = nx.degree_centrality(graph)

        # Closeness centrality
        closeness_centrality = nx.closeness_centrality(graph)

        # Betweenness centrality
        betweenness_centrality = nx.betweenness_centrality(graph)

        # Combine centrality measures for each node
        for node in graph.nodes():
            centrality_measures[node] = {
                'degree_centrality': degree_centrality.get(node, 0),
                'closeness_centrality': closeness_centrality.get(node, 0),
                'betweenness_centrality': betweenness_centrality.get(node, 0),
            }
    
    except Exception as e:
        # Catch unexpected errors and report them
        raise RuntimeError(f"An error occurred while calculating centrality measures: {e}")

    return centrality_measures


# Example Usage
if __name__ == "__main__":
    # Create a sample graph
    G = nx.erdos_renyi_graph(n=10, p=0.3)

    # Compute centrality measures
    measures = calculate_centrality_measures(G)

    # Print results
    for node, centralities in measures.items():
        print(f"Node {node}: {centralities}")
```
