"""
Generated Code Metadata:
========================
Original URL: https://cimedweb.org
Prompt: "Create a code snippet to visualize the structure of education research groups, such as CIMEd's GIEEC and GIEDHICS, using a graph library like NetworkX."
Generated: DETERMINISTIC_f78ba3fb4688ee8b
Batch ID: 20250622_211652
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

def visualize_research_groups():
    """
    Visualizes the structure of education research groups using NetworkX.
    Groups and subgroups are represented as nodes, and their relationships as edges.
    """
    try:
        # Initialize a directed graph
        graph = nx.DiGraph()

        # Define research groups and their subgroups
        research_groups = {
            "CIMEd": ["GIEEC", "GIEDHICS"],
            "GIEEC": ["Subgroup1", "Subgroup2"],
            "GIEDHICS": ["Subgroup3", "Subgroup4"]
        }

        # Add nodes and edges to the graph
        for group, subgroups in research_groups.items():
            graph.add_node(group)  # Add main group as a node
            for subgroup in subgroups:
                graph.add_node(subgroup)  # Add subgroup as a node
                graph.add_edge(group, subgroup)  # Connect main group to its subgroups

        # Draw the graph
        plt.figure(figsize=(8, 6))
        pos = nx.spring_layout(graph)  # Position nodes using spring layout
        nx.draw(
            graph, pos, with_labels=True, node_size=3000, node_color="lightblue",
            font_size=10, font_weight="bold", edge_color="gray"
        )
        plt.title("Education Research Groups Structure", fontsize=14)
        plt.show()

    except Exception as e:
        print(f"An error occurred while visualizing the research groups: {e}")

# Run the visualization function
if __name__ == "__main__":
    visualize_research_groups()
```
