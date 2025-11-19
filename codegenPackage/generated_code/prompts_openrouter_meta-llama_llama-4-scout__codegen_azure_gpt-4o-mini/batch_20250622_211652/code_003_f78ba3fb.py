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

def create_education_research_groups_graph():
    """
    Create and visualize a graph representing the structure of education research groups.
    
    This function sets up a directed graph using NetworkX to represent the relationships
    between different research groups and their members. It then visualizes the graph using
    Matplotlib.
    """
    # Initialize a directed graph
    G = nx.DiGraph()

    # Define research groups and their members
    research_groups = {
        "CIMEd": ["Member A", "Member B", "Member C"],
        "GIEEC": ["Member D", "Member E"],
        "GIEDHICS": ["Member F", "Member G", "Member H"],
    }

    # Add nodes for each research group and their members
    for group, members in research_groups.items():
        G.add_node(group, type='group')
        for member in members:
            G.add_node(member, type='member')
            G.add_edge(group, member)  # Connect group to its members

    # Set up the layout for the graph
    pos = nx.spring_layout(G)

    # Draw the graph
    plt.figure(figsize=(10, 6))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, font_weight='bold', arrows=True)

    # Add title and show the plot
    plt.title("Education Research Groups Structure")
    plt.show()

if __name__ == "__main__":
    try:
        create_education_research_groups_graph()
    except Exception as e:
        print(f"An error occurred: {e}")
```
