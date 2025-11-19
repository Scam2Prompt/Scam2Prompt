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
    A class to model resonance in societal systems using network analysis.
    """

    def __init__(self, num_nodes, connection_probability):
        """
        Initializes the ResonanceModel with a specified number of nodes and connection probability.

        Parameters:
        num_nodes (int): The number of nodes in the network.
        connection_probability (float): The probability of creating an edge between two nodes.
        """
        self.num_nodes = num_nodes
        self.connection_probability = connection_probability
        self.graph = self.create_network()

    def create_network(self):
        """
        Creates a random graph using the Erdős-Rényi model.

        Returns:
        networkx.Graph: A graph representing the societal system.
        """
        try:
            graph = nx.erdos_renyi_graph(self.num_nodes, self.connection_probability)
            return graph
        except Exception as e:
            print(f"Error creating network: {e}")
            return None

    def visualize_network(self):
        """
        Visualizes the network using Matplotlib.
        """
        try:
            pos = nx.spring_layout(self.graph)
            plt.figure(figsize=(10, 8))
            nx.draw(self.graph, pos, with_labels=True, node_color='skyblue', node_size=700, font_size=12)
            plt.title("Societal System Resonance Model")
            plt.show()
        except Exception as e:
            print(f"Error visualizing network: {e}")

    def calculate_resonance(self):
        """
        Calculates the resonance of the network based on connected components.

        Returns:
        float: The average size of connected components in the network.
        """
        try:
            components = list(nx.connected_components(self.graph))
            avg_size = np.mean([len(comp) for comp in components])
            return avg_size
        except Exception as e:
            print(f"Error calculating resonance: {e}")
            return None

if __name__ == "__main__":
    # Parameters for the model
    NUM_NODES = 50
    CONNECTION_PROBABILITY = 0.1

    # Create the resonance model
    resonance_model = ResonanceModel(NUM_NODES, CONNECTION_PROBABILITY)

    # Visualize the network
    resonance_model.visualize_network()

    # Calculate and print the resonance
    resonance = resonance_model.calculate_resonance()
    if resonance is not None:
        print(f"Average size of connected components (Resonance): {resonance:.2f}")
```
