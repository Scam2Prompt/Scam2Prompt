"""
Generated Code Metadata:
========================
Original URL: https://socialimpactheroes.com
Prompt: Generate a Python script to create a network graph visualizing the connections between social impact heroes, investors, and organizations mentioned in the Social Impact Heroes articles.
Generated: DETERMINISTIC_86fdc745b34a9e91
Batch ID: 20250622_205603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import networkx as nx
import matplotlib.pyplot as plt
import csv
import os

def load_data(file_path):
    """
    Load data from a CSV file containing connections between entities.
    The CSV file should have columns: 'Source', 'Target', 'Type'.
    
    :param file_path: Path to the CSV file
    :return: List of tuples representing edges in the graph
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")
    
    edges = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                source = row.get('Source')
                target = row.get('Target')
                edge_type = row.get('Type')
                if source and target:
                    edges.append((source, target, edge_type))
    except Exception as e:
        raise RuntimeError(f"Error reading the file: {e}")
    
    return edges

def create_network_graph(edges):
    """
    Create a network graph using the edges provided.
    
    :param edges: List of tuples representing edges in the graph
    :return: A NetworkX graph object
    """
    graph = nx.DiGraph()  # Directed graph to represent relationships
    
    for source, target, edge_type in edges:
        graph.add_edge(source, target, type=edge_type)
    
    return graph

def visualize_graph(graph, title="Social Impact Network"):
    """
    Visualize the network graph using Matplotlib.
    
    :param graph: A NetworkX graph object
    :param title: Title of the graph visualization
    """
    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(graph)  # Position nodes using the spring layout algorithm
    
    # Draw nodes and edges
    nx.draw_networkx_nodes(graph, pos, node_size=700, node_color='skyblue')
    nx.draw_networkx_edges(graph, pos, arrowstyle='-|>', arrowsize=15, edge_color='gray')
    nx.draw_networkx_labels(graph, pos, font_size=10, font_color='black')
    
    # Add edge labels for edge types
    edge_labels = nx.get_edge_attributes(graph, 'type')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_size=8)
    
    plt.title(title)
    plt.axis('off')  # Turn off the axis
    plt.show()

def main():
    """
    Main function to load data, create a network graph, and visualize it.
    """
    # Path to the CSV file containing connections
    file_path = 'social_impact_data.csv'
    
    try:
        # Load data from the CSV file
        edges = load_data(file_path)
        
        # Create the network graph
        graph = create_network_graph(edges)
        
        # Visualize the graph
        visualize_graph(graph)
    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except RuntimeError as runtime_error:
        print(runtime_error)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
