"""
Generated Code Metadata:
========================
Original URL: https://socialimpactheroes.com
Prompt: Generate a Python script to create a network graph visualizing the connections between social impact heroes, investors, and organizations mentioned in the Social Impact Heroes articles.
Generated: DETERMINISTIC_86fdc745b34a9e91
Batch ID: 20250622_205603
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
import pandas as pd

# Function to create a network graph from the provided data
def create_network_graph(data):
    """
    Create a network graph visualizing connections between social impact heroes, investors, and organizations.

    Parameters:
    data (pd.DataFrame): A DataFrame containing the relationships between heroes, investors, and organizations.

    Returns:
    G (nx.Graph): A NetworkX graph object representing the network.
    """
    # Initialize a directed graph
    G = nx.Graph()

    # Iterate through the DataFrame to add edges to the graph
    for index, row in data.iterrows():
        hero = row['Hero']
        investor = row['Investor']
        organization = row['Organization']

        # Add nodes for heroes, investors, and organizations
        G.add_node(hero, type='hero')
        G.add_node(investor, type='investor')
        G.add_node(organization, type='organization')

        # Add edges to represent relationships
        G.add_edge(hero, investor)
        G.add_edge(hero, organization)

    return G

# Function to visualize the network graph
def visualize_graph(G):
    """
    Visualize the network graph using Matplotlib.

    Parameters:
    G (nx.Graph): A NetworkX graph object to visualize.
    """
    # Set the layout for the graph
    pos = nx.spring_layout(G)

    # Draw the nodes and edges
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, font_color='black', font_weight='bold', edge_color='gray')

    # Show the plot
    plt.title("Social Impact Heroes Network")
    plt.show()

# Main function to execute the script
def main():
    # Sample data representing relationships (this should be replaced with actual data)
    data = {
        'Hero': ['Hero A', 'Hero B', 'Hero A', 'Hero C'],
        'Investor': ['Investor 1', 'Investor 2', 'Investor 3', 'Investor 1'],
        'Organization': ['Org 1', 'Org 2', 'Org 3', 'Org 1']
    }

    # Convert the sample data into a DataFrame
    df = pd.DataFrame(data)

    # Create the network graph
    G = create_network_graph(df)

    # Visualize the graph
    visualize_graph(G)

# Entry point of the script
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
