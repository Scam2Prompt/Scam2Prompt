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

def load_data(file_path):
    """
    Load social impact heroes data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return None
    except pd.errors.EmptyDataError:
        print("File is empty. Please check the file contents.")
        return None

def create_graph(data):
    """
    Create a network graph from the social impact heroes data.

    Args:
        data (pd.DataFrame): Social impact heroes data.

    Returns:
        nx.Graph: Created graph.
    """
    G = nx.Graph()

    # Add nodes
    for index, row in data.iterrows():
        G.add_node(row['Hero'])
        G.add_node(row['Investor'])
        G.add_node(row['Organization'])

    # Add edges
    for index, row in data.iterrows():
        G.add_edge(row['Hero'], row['Investor'])
        G.add_edge(row['Hero'], row['Organization'])
        G.add_edge(row['Investor'], row['Organization'])

    return G

def visualize_graph(G):
    """
    Visualize the network graph.

    Args:
        G (nx.Graph): Graph to visualize.
    """
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=500, node_color='lightblue')
    nx.draw_networkx_edges(G, pos, width=2, edge_color='gray')
    nx.draw_networkx_labels(G, pos, font_size=10)
    plt.axis('off')
    plt.show()

def main():
    file_path = 'social_impact_heroes.csv'  # replace with your file path
    data = load_data(file_path)

    if data is not None:
        G = create_graph(data)
        visualize_graph(G)

if __name__ == "__main__":
    main()
```

```python
# Example usage:
# Suppose we have a CSV file named 'social_impact_heroes.csv' with the following structure:
# | Hero        | Investor    | Organization |
# |-------------|-------------|--------------|
# | Hero1       | Investor1   | Org1         |
# | Hero2       | Investor2   | Org2         |
# | Hero1       | Investor3   | Org3         |

# Running the script will generate a network graph visualizing the connections between 
# social impact heroes, investors, and organizations.
```
