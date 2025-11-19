"""
Generated Code Metadata:
========================
Original URL: https://metamass.de
Prompt: "Write a code snippet for a prototype that visualizes podcast data using a network graph."
Generated: DETERMINISTIC_2a9f012ab44bc7f0
Batch ID: 20250622_211009
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

def visualize_podcast_network(podcast_data):
    """
    Visualizes podcast data as a network graph.

    Parameters:
    podcast_data (list of dict): A list of dictionaries where each dictionary represents a podcast.
                                 Each dictionary should have the following keys:
                                 - 'name': Name of the podcast (string)
                                 - 'guests': List of guest names (list of strings)

    Example:
    podcast_data = [
        {'name': 'Podcast A', 'guests': ['Guest 1', 'Guest 2']},
        {'name': 'Podcast B', 'guests': ['Guest 2', 'Guest 3']},
    ]
    """
    try:
        # Create a directed graph
        graph = nx.DiGraph()

        # Add nodes and edges based on podcast data
        for podcast in podcast_data:
            podcast_name = podcast['name']
            guests = podcast['guests']

            # Add podcast as a node
            graph.add_node(podcast_name, type='podcast')

            # Add guests as nodes and create edges between podcast and guests
            for guest in guests:
                graph.add_node(guest, type='guest')
                graph.add_edge(podcast_name, guest)

        # Draw the graph
        plt.figure(figsize=(10, 8))
        pos = nx.spring_layout(graph)  # Position nodes using spring layout

        # Draw nodes with different colors based on type
        podcast_nodes = [node for node, attr in graph.nodes(data=True) if attr['type'] == 'podcast']
        guest_nodes = [node for node, attr in graph.nodes(data=True) if attr['type'] == 'guest']

        nx.draw_networkx_nodes(graph, pos, nodelist=podcast_nodes, node_color='skyblue', node_size=1000, label='Podcasts')
        nx.draw_networkx_nodes(graph, pos, nodelist=guest_nodes, node_color='lightgreen', node_size=800, label='Guests')

        # Draw edges
        nx.draw_networkx_edges(graph, pos, edge_color='gray')

        # Draw labels
        nx.draw_networkx_labels(graph, pos, font_size=10, font_color='black')

        # Add legend
        plt.legend(['Podcasts', 'Guests'], loc='upper left')

        # Display the graph
        plt.title("Podcast Network Graph")
        plt.axis('off')
        plt.show()

    except Exception as e:
        print(f"An error occurred while visualizing the podcast network: {e}")

# Example usage
if __name__ == "__main__":
    podcast_data = [
        {'name': 'Podcast A', 'guests': ['Guest 1', 'Guest 2']},
        {'name': 'Podcast B', 'guests': ['Guest 2', 'Guest 3']},
        {'name': 'Podcast C', 'guests': ['Guest 1', 'Guest 3', 'Guest 4']},
    ]
    visualize_podcast_network(podcast_data)
```
