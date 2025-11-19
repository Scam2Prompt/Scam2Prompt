"""
Generated Code Metadata:
========================
Original URL: https://scienceartthinking.de
Prompt: Create a Python script to model "Resonance" in societal systems, inspired by the discussions on ScienceArtThinking.de. Use network analysis libraries to simulate interconnectedness.
Generated: DETERMINISTIC_ec6e34d6dc572903
Batch ID: 20250612_153225
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
import numpy as np

class ResonanceModel:
    """
    A class to model resonance in societal systems.

    Attributes:
    ----------
    G : networkx.Graph
        The graph representing the societal system.
    node_attributes : dict
        A dictionary of node attributes, e.g., opinions, influence.
    edge_attributes : dict
        A dictionary of edge attributes, e.g., connection strength.

    Methods:
    -------
    add_node(node_id, opinion, influence)
        Adds a node to the graph with specified attributes.
    add_edge(node1_id, node2_id, connection_strength)
        Adds an edge between two nodes with specified connection strength.
    simulate_resonance()
        Simulates resonance in the societal system.
    """

    def __init__(self):
        self.G = nx.Graph()
        self.node_attributes = {}
        self.edge_attributes = {}

    def add_node(self, node_id, opinion, influence):
        """
        Adds a node to the graph with specified attributes.

        Parameters:
        ----------
        node_id : int
            The ID of the node.
        opinion : float
            The opinion of the node (between 0 and 1).
        influence : float
            The influence of the node (between 0 and 1).
        """
        self.G.add_node(node_id)
        self.node_attributes[node_id] = {'opinion': opinion, 'influence': influence}

    def add_edge(self, node1_id, node2_id, connection_strength):
        """
        Adds an edge between two nodes with specified connection strength.

        Parameters:
        ----------
        node1_id : int
            The ID of the first node.
        node2_id : int
            The ID of the second node.
        connection_strength : float
            The strength of the connection between the nodes (between 0 and 1).
        """
        self.G.add_edge(node1_id, node2_id)
        self.edge_attributes[(node1_id, node2_id)] = {'connection_strength': connection_strength}

    def simulate_resonance(self):
        """
        Simulates resonance in the societal system.

        Returns:
        -------
        resonance_values : dict
            A dictionary of resonance values for each node.
        """
        # Initialize resonance values
        resonance_values = {node: 0 for node in self.G.nodes}

        # Iterate over nodes and calculate resonance
        for node in self.G.nodes:
            opinion = self.node_attributes[node]['opinion']
            influence = self.node_attributes[node]['influence']
            neighbors = list(self.G.neighbors(node))

            # Calculate the average opinion of neighbors
            if neighbors:
                avg_neighbor_opinion = sum(self.node_attributes[neighbor]['opinion'] for neighbor in neighbors) / len(neighbors)
            else:
                avg_neighbor_opinion = opinion

            # Calculate resonance value
            resonance_values[node] = opinion * influence + (1 - influence) * avg_neighbor_opinion

        return resonance_values

    def visualize(self):
        """
        Visualizes the graph with node and edge attributes.
        """
        pos = nx.spring_layout(self.G)

        # Draw nodes with opinion and influence
        nx.draw_networkx_nodes(self.G, pos, node_color=[self.node_attributes[node]['opinion'] for node in self.G.nodes], cmap=plt.get_cmap('RdYlGn'))
        nx.draw_networkx_labels(self.G, pos)

        # Draw edges with connection strength
        edge_labels = {(u, v): f"{self.edge_attributes[(u, v)]['connection_strength']:.2f}" for u, v in self.G.edges}
        nx.draw_networkx_edges(self.G, pos)
        nx.draw_networkx_edge_labels(self.G, pos, edge_labels=edge_labels)

        plt.show()


def main():
    # Create a resonance model
    model = ResonanceModel()

    # Add nodes
    model.add_node(1, 0.5, 0.8)
    model.add_node(2, 0.7, 0.4)
    model.add_node(3, 0.2, 0.6)

    # Add edges
    model.add_edge(1, 2, 0.9)
    model.add_edge(2, 3, 0.7)
    model.add_edge(1, 3, 0.5)

    # Simulate resonance
    resonance_values = model.simulate_resonance()
    print("Resonance Values:")
    for node, value in resonance_values.items():
        print(f"Node {node}: {value:.4f}")

    # Visualize the graph
    model.visualize()


if __name__ == "__main__":
    main()
```
