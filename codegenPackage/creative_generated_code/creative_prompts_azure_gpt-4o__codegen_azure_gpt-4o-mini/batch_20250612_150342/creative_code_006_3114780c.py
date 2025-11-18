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
import numpy as np

def calculate_centrality_measures(graph):
    """
    Calculate centrality measures for each node in the given graph.
    
    Parameters:
    graph (networkx.Graph): A NetworkX graph object.

    Returns:
    dict: A dictionary containing the degree, closeness, and betweenness centrality 
          for each node in the graph.
    
    Raises:
    ValueError: If the input graph is empty or not a NetworkX graph.
    """
    
    # Validate input
    if not isinstance(graph, nx.Graph):
        raise ValueError("Input must be a NetworkX graph.")
    
    if len(graph) == 0:
        raise ValueError("Input graph is empty.")
    
    # Initialize a dictionary to hold centrality measures
    centrality_measures = {}
    
    try:
        # Calculate degree centrality
        degree_centrality = nx.degree_centrality(graph)
        
        # Calculate closeness centrality
        closeness_centrality = nx.closeness_centrality(graph)
        
        # Calculate betweenness centrality
        betweenness_centrality = nx.betweenness_centrality(graph)
        
        # Combine results into the centrality_measures dictionary
        for node in graph.nodes():
            centrality_measures[node] = {
                'degree': degree_centrality[node],
                'closeness': closeness_centrality[node],
                'betweenness': betweenness_centrality[node]
            }
    
    except Exception as e:
        raise RuntimeError(f"An error occurred while calculating centrality measures: {e}")

    return centrality_measures

# Example usage
if __name__ == "__main__":
    # Create a sample graph
    G = nx.Graph()
    G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)])
    
    # Calculate centrality measures
    try:
        centrality = calculate_centrality_measures(G)
        print(centrality)
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except RuntimeError as re:
        print(f"RuntimeError: {re}")
```
