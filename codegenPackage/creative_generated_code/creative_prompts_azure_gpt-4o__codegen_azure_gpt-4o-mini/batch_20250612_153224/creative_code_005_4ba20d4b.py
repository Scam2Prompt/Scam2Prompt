"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://styrosolutions.com
Prompt: Suggest a library for visualizing the recycling process of EPS foam, including steps like pre-crushing and densification, as described for the Cobalt SC2200 thermal processing machine.
Generated: DETERMINISTIC_4ba20d4b3ff79b69
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for visualization
import matplotlib.pyplot as plt
import networkx as nx

def create_recycling_process_graph(steps):
    """
    Create and visualize a graph of the recycling process for EPS foam.

    Parameters:
    steps (list of str): A list containing the steps of the recycling process.

    Returns:
    None: Displays a visualization of the recycling process.
    """
    # Initialize a directed graph
    G = nx.DiGraph()

    # Add steps to the graph as nodes
    for step in steps:
        G.add_node(step)

    # Add edges to represent the flow of the recycling process
    for i in range(len(steps) - 1):
        G.add_edge(steps[i], steps[i + 1])

    # Draw the graph
    plt.figure(figsize=(10, 6))
    pos = nx.spring_layout(G)  # positions for all nodes
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightblue', font_size=10, font_weight='bold', arrows=True)
    plt.title("Recycling Process of EPS Foam")
    plt.show()

if __name__ == "__main__":
    try:
        # Define the steps in the EPS foam recycling process
        recycling_steps = [
            "Collection",
            "Sorting",
            "Pre-Crushing",
            "Densification",
            "Thermal Processing",
            "Reuse / Recycling"
        ]

        # Visualize the recycling process
        create_recycling_process_graph(recycling_steps)
    except Exception as e:
        print(f"An error occurred while visualizing the recycling process: {e}")
```
