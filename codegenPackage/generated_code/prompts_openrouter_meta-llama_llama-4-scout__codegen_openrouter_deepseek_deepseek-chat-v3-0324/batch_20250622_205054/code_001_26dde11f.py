"""
Generated Code Metadata:
========================
Original URL: https://the-graph.network
Prompt: Recommend a library or API for creating interactive network visualizations like the one on https://the-graph.network, specifically for a project involving indexer, curator, and delegator nodes.
Generated: DETERMINISTIC_26dde11f8e39ae93
Batch ID: 20250622_205054
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network
import json

def create_network_visualization(nodes_data, edges_data, output_file="network.html"):
    """
    Creates an interactive network visualization using Pyvis.
    
    Args:
        nodes_data (list): List of dictionaries containing node information.
                          Example: [{"id": 1, "label": "Indexer", "title": "Indexer Node 1"}, ...]
        edges_data (list): List of dictionaries containing edge information.
                          Example: [{"from": 1, "to": 2, "label": "delegates"}, ...]
        output_file (str): Output HTML file name for the visualization.
    
    Returns:
        None (writes to HTML file)
    """
    try:
        # Create a Pyvis network
        net = Network(height="750px", width="100%", bgcolor="#222222", font_color="white")
        
        # Add nodes and edges
        for node in nodes_data:
            net.add_node(node["id"], 
                        label=node["label"],
                        title=node.get("title", ""),
                        group=node.get("group", ""))
        
        for edge in edges_data:
            net.add_edge(edge["from"], 
                         edge["to"],
                         title=edge.get("title", ""),
                         label=edge.get("label", ""))
        
        # Configure physics for better layout
        net.set_options("""
        {
            "physics": {
                "barnesHut": {
                    "gravitationalConstant": -80000,
                    "centralGravity": 0.3,
                    "springLength": 250,
                    "springConstant": 0.04,
                    "damping": 0.09,
                    "avoidOverlap": 0.1
                },
                "minVelocity": 0.75
            }
        }
        """)
        
        # Save and show the network
        net.show(output_file)
        print(f"Network visualization saved to {output_file}")
        
    except Exception as e:
        print(f"Error creating network visualization: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Sample data for The Graph network
    nodes = [
        {"id": 1, "label": "Indexer 1", "title": "Indexer Node", "group": "indexer"},
        {"id": 2, "label": "Indexer 2", "title": "Indexer Node", "group": "indexer"},
        {"id": 3, "label": "Curator 1", "title": "Curator Node", "group": "curator"},
        {"id": 4, "label": "Delegator 1", "title": "Delegator Node", "group": "delegator"},
        {"id": 5, "label": "Delegator 2", "title": "Delegator Node", "group": "delegator"}
    ]
    
    edges = [
        {"from": 3, "to": 1, "label": "curates", "title": "Curates subgraph"},
        {"from": 4, "to": 1, "label": "delegates", "title": "Delegates GRT"},
        {"from": 5, "to": 2, "label": "delegates", "title": "Delegates GRT"}
    ]
    
    create_network_visualization(nodes, edges)
```
