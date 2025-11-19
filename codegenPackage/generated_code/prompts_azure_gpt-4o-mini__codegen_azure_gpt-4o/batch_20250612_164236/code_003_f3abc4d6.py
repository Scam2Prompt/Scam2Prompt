"""
Generated Code Metadata:
========================
Original URL: https://the-graph.network
Prompt: Generate a script that interacts with The Graph Network to visualize node relationships and their details.
Generated: DETERMINISTIC_f3abc4d666f5d9f0
Batch ID: 20250612_164236
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.thegraph.com/subgraphs/name/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.thegraph.com/subgraphs/name/<subgraph-name>": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
import json
import networkx as nx
import matplotlib.pyplot as plt

# Constants
GRAPH_API_URL = "https://api.thegraph.com/subgraphs/name/<subgraph-name>"  # Replace <subgraph-name> with the actual subgraph name
QUERY = """
{
  nodes {
    id
    name
    relationships {
      targetNode {
        id
        name
      }
    }
  }
}
"""

def fetch_graph_data(api_url, query):
    """
    Fetch data from The Graph API using the provided query.

    Args:
        api_url (str): The Graph API endpoint.
        query (str): GraphQL query string.

    Returns:
        dict: Parsed JSON response containing graph data.
    """
    try:
        response = requests.post(api_url, json={"query": query})
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from The Graph API: {e}")
        return None

def parse_graph_data(data):
    """
    Parse the graph data into nodes and edges.

    Args:
        data (dict): Graph data fetched from The Graph API.

    Returns:
        tuple: A tuple containing a list of nodes and a list of edges.
    """
    nodes = []
    edges = []

    if not data or "data" not in data or "nodes" not in data["data"]:
        print("Invalid or empty data received.")
        return nodes, edges

    for node in data["data"]["nodes"]:
        nodes.append((node["id"], {"name": node["name"]}))
        for relationship in node.get("relationships", []):
            target_node = relationship.get("targetNode")
            if target_node:
                edges.append((node["id"], target_node["id"]))

    return nodes, edges

def visualize_graph(nodes, edges):
    """
    Visualize the graph using NetworkX and Matplotlib.

    Args:
        nodes (list): List of nodes with attributes.
        edges (list): List of edges between nodes.
    """
    graph = nx.DiGraph()  # Create a directed graph
    graph.add_nodes_from(nodes)
    graph.add_edges_from(edges)

    # Draw the graph
    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(graph)  # Position nodes using spring layout
    nx.draw(graph, pos, with_labels=True, node_size=500, node_color="skyblue", font_size=10, font_weight="bold")

    # Add node labels
    labels = {node[0]: node[1]["name"] for node in nodes}
    nx.draw_networkx_labels(graph, pos, labels, font_size=8)

    plt.title("Node Relationships Visualization")
    plt.show()

def main():
    """
    Main function to fetch, parse, and visualize graph data.
    """
    print("Fetching data from The Graph API...")
    data = fetch_graph_data(GRAPH_API_URL, QUERY)

    if data:
        print("Parsing graph data...")
        nodes, edges = parse_graph_data(data)

        print(f"Found {len(nodes)} nodes and {len(edges)} edges.")
        print("Visualizing graph...")
        visualize_graph(nodes, edges)
    else:
        print("Failed to fetch or parse graph data.")

if __name__ == "__main__":
    main()
```

**Note:** Replace `<subgraph-name>` in `GRAPH_API_URL` with the actual subgraph name you want to query. Ensure you have the required Python libraries (`requests`, `networkx`, and `matplotlib`) installed before running the script.
