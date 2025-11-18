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
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

class ResonanceModel:
    """
    A class to model resonance in societal systems using network analysis.
    This class allows for the creation of a network graph to simulate 
    interconnectedness between different entities in a societal system.
    """

    def __init__(self, num_nodes, connection_probability):
        """
        Initializes the ResonanceModel with a specified number of nodes 
        and the probability of connection between nodes.

        Parameters:
        - num_nodes (int): The number of nodes in the network.
        - connection_probability (float): Probability for edge creation between nodes.
        """
        self.num_nodes = num_nodes
        self.connection_probability = connection_probability
        self.graph = self.create_graph()

    def create_graph(self):
        """
        Creates a random graph using the Erdős–Rényi model.

        Returns:
        - Graph: A networkx graph instance representing the societal network.
        """
        try:
            graph = nx.erdos_renyi_graph(self.num_nodes, self.connection_probability)
            return graph
        except Exception as e:
            print(f"Error while creating graph: {e}")
            raise

    def visualize_graph(self):
        """
        Visualizes the created graph using matplotlib.

        Raises:
        - ValueError: If the graph is empty, visualization cannot be performed.
        """
        if self.graph.number_of_nodes() == 0:
            raise ValueError("Cannot visualize an empty graph.")

        plt.figure(figsize=(12, 8))
        pos = nx.spring_layout(self.graph)
        nx.draw(self.graph, pos, with_labels=True, node_size=500, node_color='lightblue', edge_color='gray')
        plt.title("Societal System Resonance Model")
        plt.show()

    def calculate_resonance(self):
        """
        Calculates a basic resonance metric for the network based on the average clustering coefficient
        and average degree of the nodes.

        Returns:
        - float: The computed resonance value.
        """
        try:
            avg_clustering = nx.average_clustering(self.graph)
            avg_degree = np.mean([d for n, d in self.graph.degree()])
            resonance_value = avg_clustering * avg_degree
            return resonance_value
        except Exception as e:
            print(f"Error while calculating resonance: {e}")
            raise

if __name__ == "__main__":
    # User-defined parameters for the model
    NUM_NODES = 50  # Number of nodes in the societal system
    CONNECTION_PROBABILITY = 0.1  # Probability of connection between nodes

    # Create the resonance model
    model = ResonanceModel(NUM_NODES, CONNECTION_PROBABILITY)

    # Visualize the graph
    try:
        model.visualize_graph()
    except ValueError as ve:
        print(ve)

    # Calculate and print the resonance value
    try:
        resonance = model.calculate_resonance()
        print(f"Calculated Resonance Value: {resonance:.4f}")
    except Exception as e:
        print(f"Failed to calculate resonance due to error: {e}")
```
