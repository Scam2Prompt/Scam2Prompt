"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scienceartthinking.de
Prompt: Create a Python script to model "Resonance" in societal systems, inspired by the discussions on ScienceArtThinking.de. Use network analysis libraries to simulate interconnectedness.
Generated: DETERMINISTIC_ec6e34d6dc572903
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Python script to model "Resonance" in societal systems using network analysis.

This script simulates interconnectedness in societal systems inspired by discussions
on ScienceArtThinking.de. It uses the `networkx` library to build and analyze the network graph.
"""

import networkx as nx
import matplotlib.pyplot as plt

def generate_societal_network(num_nodes=10, connectivity=0.3):
    """
    Generate a random societal network graph.
    
    Parameters:
        num_nodes (int): The number of nodes in the graph representing entities in the society.
        connectivity (float): Probability of edge creation between any two nodes (0-1).
    
    Returns:
        networkx.Graph: A graph representing the societal network.
    """
    # Create a random graph with given probabilities for edge creation
    graph = nx.erdos_renyi_graph(num_nodes, connectivity)
    
    # Add weights to edges to represent "resonance strength"
    for u, v in graph.edges:
        graph[u][v]['weight'] = round(nx.random.uniform(0.1, 1.0), 2)  # Random weight between 0.1 and 1.0
    
    return graph

def calculate_resonance(graph):
    """
    Calculate resonance as a measure of interconnectedness in the graph.
    
    Resonance is defined here as the sum of weights of all edges in the graph.
    
    Parameters:
        graph (networkx.Graph): The societal network graph.
    
    Returns:
        float: The total resonance value of the graph.
    """
    total_resonance = sum(data['weight'] for _, _, data in graph.edges(data=True))
    return total_resonance

def display_graph(graph):
    """
    Display the societal network graph visually using matplotlib.
    
    Parameters:
        graph (networkx.Graph): The societal network graph.
    """
    pos = nx.spring_layout(graph)  # Position nodes in a visually pleasing layout
    edge_weights = nx.get_edge_attributes(graph, 'weight')
    
    plt.figure(figsize=(8, 6))
    nx.draw(
        graph, pos, with_labels=True, node_color='lightblue',
        edge_color='gray', node_size=500, font_size=10
    )
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_weights)
    plt.title("Societal Network Graph with Resonance Weights")
    plt.show()

def main():
    """
    Main function to execute the societal network resonance simulation.
    """
    try:
        # Generate a societal network graph
        print("Generating a societal network...")
        num_nodes = int(input("Enter the number of nodes in the network (e.g., 10): "))
        connectivity = float(input("Enter the connectivity probability between nodes (0-1, e.g., 0.3): "))
        
        graph = generate_societal_network(num_nodes, connectivity)
        
        # Calculate resonance
        resonance = calculate_resonance(graph)
        print(f"Total Resonance in the Network: {resonance:.2f}")
        
        # Display the graph
        display_graph(graph)
    
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
