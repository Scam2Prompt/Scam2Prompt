"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://graphpool.net
Prompt: Generate code to visualize graph structures with interactive features, based on examples or libraries highlighted on graphpool.net.
Generated: DETERMINISTIC_ed447068d26a00ff
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
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import numpy as np

class GraphVisualizer:
    """
    A class to visualize graph structures with interactive features.
    Uses NetworkX for graph creation and Matplotlib for visualization.
    """

    def __init__(self, graph):
        """
        Initializes the GraphVisualizer with a given graph.

        Parameters:
        graph (networkx.Graph): The graph to visualize.
        """
        self.graph = graph
        self.pos = nx.spring_layout(self.graph)
        self.fig, self.ax = plt.subplots()
        plt.subplots_adjust(bottom=0.2)
        self.draw_graph()

        # Create a button for interacting with the graph
        self.button = Button(plt.gca(), 'Refresh Layout')
        self.button.on_clicked(self.refresh_layout)

    def draw_graph(self):
        """
        Draws the graph using Matplotlib and NetworkX.
        """
        self.ax.clear()  # Clear previous graph
        nx.draw(self.graph, self.pos, ax=self.ax, with_labels=True, node_color='lightblue', edge_color='gray')
        self.ax.set_title("Graph Visualization")
        plt.draw()  # Update the figure

    def refresh_layout(self, event):
        """
        Refreshes the graph layout on button click.

        Parameters:
        event (Event): The event triggered by the button click.
        """
        self.pos = nx.spring_layout(self.graph)  # Recalculate positions
        self.draw_graph()

    def show(self):
        """
        Displays the graph on screen.
        """
        plt.show()

def main():
    """
    Main function to create a demo graph and visualize it.
    """
    try:
        # Create a sample graph
        G = nx.Graph()
        G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)])
        
        # Initialize the graph visualizer
        visualizer = GraphVisualizer(G)
        
        # Display the graph
        visualizer.show()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
