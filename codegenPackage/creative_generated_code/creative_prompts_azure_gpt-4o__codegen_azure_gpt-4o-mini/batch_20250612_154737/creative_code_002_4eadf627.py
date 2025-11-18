"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gra-pro-canv.webflow.io
Prompt: Generate a script to visualize roles and responsibilities in a grants program using Gitcoin's Grants Program Canvas framework.
Generated: DETERMINISTIC_4eadf627d4ad2214
Batch ID: 20250612_154737
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt
import networkx as nx

# Define roles and responsibilities in a grants program
roles = {
    'Program Manager': ['Oversee grants program', 'Coordinate stakeholders'],
    'Grant Writer': ['Prepare grant proposals', 'Research funding opportunities'],
    'Finance Officer': ['Manage budget', 'Track expenditures'],
    'Evaluation Specialist': ['Assess grant impact', 'Collect data'],
    'Communication Officer': ['Promote grants program', 'Manage outreach'],
}

def create_graph(roles):
    """
    Create a directed graph from the roles and their responsibilities.

    Args:
        roles (dict): A dictionary where keys are roles and values are lists of responsibilities.

    Returns:
        G (networkx.DiGraph): A directed graph representing roles and responsibilities.
    """
    G = nx.DiGraph()

    # Add roles and their responsibilities to the graph
    for role, responsibilities in roles.items():
        G.add_node(role)  # Add role as a node
        for responsibility in responsibilities:
            G.add_node(responsibility)  # Add responsibility as a node
            G.add_edge(role, responsibility)  # Create a directed edge

    return G

def visualize_graph(G):
    """
    Visualize the directed graph using Matplotlib.

    Args:
        G (networkx.DiGraph): The directed graph to visualize.
    """
    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(G)  # Define layout for better visualization
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightblue', font_size=10, font_color='black', font_weight='bold', arrows=True)
    plt.title("Roles and Responsibilities in Grants Program", fontsize=15)
    plt.tight_layout()
    plt.show()

def main():
    """
    Main function to execute the roles visualization.
    """
    try:
        # Create the graph from roles and responsibilities
        G = create_graph(roles)

        # Visualize the graph
        visualize_graph(G)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
