"""
Generated Code Metadata:
========================
Original URL: https://the-graph.network
Prompt: Write a code snippet to visualize The Graph Network, including nodes for indexers, curators, delegators, and subgraphs.
Generated: DETERMINISTIC_4dbee7f5665bdb0c
Batch ID: 20250622_205054
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

class GraphNetworkVisualizer:
    def __init__(self):
        self.G = nx.DiGraph()

    def add_indexer(self, indexer_id):
        """Add an indexer node to the graph."""
        self.G.add_node(indexer_id, type='Indexer')

    def add_curator(self, curator_id):
        """Add a curator node to the graph."""
        self.G.add_node(curator_id, type='Curator')

    def add_delegator(self, delegator_id):
        """Add a delegator node to the graph."""
        self.G.add_node(delegator_id, type='Delegator')

    def add_subgraph(self, subgraph_id):
        """Add a subgraph node to the graph."""
        self.G.add_node(subgraph_id, type='Subgraph')

    def add_edge(self, source, target):
        """Add a directed edge between two nodes in the graph."""
        self.G.add_edge(source, target)

    def visualize(self):
        """Visualize the graph network."""
        try:
            pos = nx.spring_layout(self.G)
            nx.draw_networkx_nodes(self.G, pos, node_size=500, node_color='lightblue')
            nx.draw_networkx_labels(self.G, pos, font_size=10)
            nx.draw_networkx_edges(self.G, pos, edge_color='gray', arrowsize=20)

            # Node colors based on type
            for node in self.G.nodes(data=True):
                if node[1]['type'] == 'Indexer':
                    nx.draw_networkx_nodes(self.G, pos, n=[node[0]], node_size=500, node_color='red')
                elif node[1]['type'] == 'Curator':
                    nx.draw_networkx_nodes(self.G, pos, n=[node[0]], node_size=500, node_color='green')
                elif node[1]['type'] == 'Delegator':
                    nx.draw_networkx_nodes(self.G, pos, n=[node[0]], node_size=500, node_color='yellow')
                elif node[1]['type'] == 'Subgraph':
                    nx.draw_networkx_nodes(self.G, pos, n=[node[0]], node_size=500, node_color='blue')

            plt.axis('off')
            plt.show()

        except Exception as e:
            print(f"Error visualizing graph: {e}")


# Example usage
if __name__ == "__main__":
    visualizer = GraphNetworkVisualizer()

    # Add nodes
    visualizer.add_indexer('Indexer1')
    visualizer.add_curator('Curator1')
    visualizer.add_delegator('Delegator1')
    visualizer.add_subgraph('Subgraph1')
    visualizer.add_indexer('Indexer2')
    visualizer.add_curator('Curator2')

    # Add edges
    visualizer.add_edge('Indexer1', 'Curator1')
    visualizer.add_edge('Curator1', 'Subgraph1')
    visualizer.add_edge('Delegator1', 'Indexer1')
    visualizer.add_edge('Indexer2', 'Curator2')
    visualizer.add_edge('Curator2', 'Subgraph1')

    # Visualize the graph
    visualizer.visualize()
```
