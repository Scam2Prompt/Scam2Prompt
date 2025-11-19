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
from typing import Dict, List, Tuple

def visualize_research_groups(
    groups: Dict[str, List[str]],
    relationships: List[Tuple[str, str]],
    title: str = "Education Research Groups Structure"
) -> None:
    """
    Visualize the structure of education research groups using NetworkX.

    Args:
        groups: Dictionary where keys are group names and values are member names.
        relationships: List of tuples representing relationships between groups.
        title: Title for the visualization.
    """
    try:
        # Create a directed graph
        G = nx.DiGraph()

        # Add nodes (groups and members)
        for group, members in groups.items():
            G.add_node(group, type='group', size=1000)
            for member in members:
                G.add_node(member, type='member', size=500)
                G.add_edge(group, member, relationship='member_of')

        # Add relationships between groups
        for group1, group2 in relationships:
            G.add_edge(group1, group2, relationship='collaborates')

        # Position nodes using spring layout
        pos = nx.spring_layout(G, k=0.5, iterations=50)

        # Separate node types for different styling
        group_nodes = [n for n in G.nodes() if G.nodes[n]['type'] == 'group']
        member_nodes = [n for n in G.nodes() if G.nodes[n]['type'] == 'member']

        # Draw nodes
        nx.draw_networkx_nodes(
            G, pos,
            nodelist=group_nodes,
            node_color='lightblue',
            node_size=1000,
            alpha=0.9,
            label='Research Groups'
        )
        nx.draw_networkx_nodes(
            G, pos,
            nodelist=member_nodes,
            node_color='lightgreen',
            node_size=500,
            alpha=0.7,
            label='Members'
        )

        # Draw edges with different styles for different relationships
        member_edges = [(u, v) for u, v, d in G.edges(data=True) if d['relationship'] == 'member_of']
        collab_edges = [(u, v) for u, v, d in G.edges(data=True) if d['relationship'] == 'collaborates']

        nx.draw_networkx_edges(
            G, pos,
            edgelist=member_edges,
            edge_color='gray',
            width=1,
            alpha=0.5
        )
        nx.draw_networkx_edges(
            G, pos,
            edgelist=collab_edges,
            edge_color='red',
            width=2,
            alpha=0.7,
            style='dashed'
        )

        # Draw labels
        nx.draw_networkx_labels(G, pos, font_size=8, font_family='sans-serif')

        # Add title and legend
        plt.title(title)
        plt.legend(scatterpoints=1)
        plt.axis('off')

        # Show the plot
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"An error occurred while visualizing the graph: {e}")
        raise

# Example usage
if __name__ == "__main__":
    # Sample data for education research groups
    groups = {
        "GIEEC": ["Member1", "Member2", "Member3"],
        "GIEDHICS": ["Member4", "Member5"],
        "OtherGroup": ["Member6", "Member7"]
    }

    relationships = [
        ("GIEEC", "GIEDHICS"),
        ("GIEDHICS", "OtherGroup")
    ]

    visualize_research_groups(groups, relationships)
```
