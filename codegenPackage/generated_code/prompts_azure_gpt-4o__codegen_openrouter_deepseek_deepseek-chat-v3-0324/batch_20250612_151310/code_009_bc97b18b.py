"""
Generated Code Metadata:
========================
Original URL: https://getgrass-io.pages.dev
Prompt: Develop a tool to visualize the contribution of Grass nodes to AI training pipelines, highlighting their role as the data layer of AI.
Generated: DETERMINISTIC_bc97b18b1bfa065e
Batch ID: 20250612_151310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import matplotlib.pyplot as plt
import networkx as nx
from typing import Dict, List, Optional, Tuple

class GrassNodeVisualizer:
    """
    A tool to visualize the contribution of Grass nodes in AI training pipelines.
    Grass nodes represent the data layer in AI pipelines.
    """

    def __init__(self):
        """Initialize the visualizer with empty graph and default styles."""
        self.graph = nx.DiGraph()
        self.node_colors = []
        self.node_sizes = []
        self.edge_colors = []
        self.edge_widths = []

    def load_pipeline(self, pipeline_config: Dict) -> None:
        """
        Load an AI pipeline configuration into the visualizer.
        
        Args:
            pipeline_config: Dictionary containing pipeline configuration.
                            Expected keys: 'nodes' and 'edges'.
        """
        if not isinstance(pipeline_config, dict):
            raise ValueError("Pipeline config must be a dictionary")
        
        if 'nodes' not in pipeline_config or 'edges' not in pipeline_config:
            raise ValueError("Pipeline config must contain 'nodes' and 'edges' keys")

        self._clear_graph()
        self._add_nodes(pipeline_config['nodes'])
        self._add_edges(pipeline_config['edges'])

    def _clear_graph(self) -> None:
        """Clear the current graph and reset styling attributes."""
        self.graph.clear()
        self.node_colors = []
        self.node_sizes = []
        self.edge_colors = []
        self.edge_widths = []

    def _add_nodes(self, nodes: List[Dict]) -> None:
        """
        Add nodes to the graph with appropriate styling.
        
        Args:
            nodes: List of node dictionaries. Each node should have:
                  - 'id': Unique identifier
                  - 'type': Node type (e.g., 'data', 'model', 'processing')
                  - Optional 'size': Relative importance/size
        """
        for node in nodes:
            if 'id' not in node or 'type' not in node:
                raise ValueError("Node must contain 'id' and 'type' fields")

            self.graph.add_node(node['id'], **node)

            # Set node color based on type
            if node['type'].lower() == 'data':
                self.node_colors.append('green')  # Grass nodes are green
            elif node['type'].lower() == 'model':
                self.node_colors.append('blue')
            else:
                self.node_colors.append('gray')

            # Set node size based on importance or default
            size = node.get('size', 1000)
            self.node_sizes.append(size)

    def _add_edges(self, edges: List[Dict]) -> None:
        """
        Add edges to the graph with appropriate styling.
        
        Args:
            edges: List of edge dictionaries. Each edge should have:
                  - 'source': Source node ID
                  - 'target': Target node ID
                  - Optional 'weight': Edge weight/importance
        """
        for edge in edges:
            if 'source' not in edge or 'target' not in edge:
                raise ValueError("Edge must contain 'source' and 'target' fields")

            self.graph.add_edge(edge['source'], edge['target'], **edge)

            # Set edge color and width
            self.edge_colors.append('black')
            weight = edge.get('weight', 1.0)
            self.edge_widths.append(weight * 2)

    def visualize(self, title: str = "AI Training Pipeline with Grass Nodes") -> None:
        """
        Generate and display the visualization.
        
        Args:
            title: Title for the visualization plot.
        """
        if len(self.graph.nodes) == 0:
            raise ValueError("No nodes to visualize. Load a pipeline first.")

        plt.figure(figsize=(12, 8))
        
        # Get node positions using spring layout
        pos = nx.spring_layout(self.graph, k=0.5, iterations=50)
        
        # Draw nodes
        nx.draw_networkx_nodes(
            self.graph, pos,
            node_color=self.node_colors,
            node_size=self.node_sizes,
            alpha=0.8
        )
        
        # Draw edges
        nx.draw_networkx_edges(
            self.graph, pos,
            edge_color=self.edge_colors,
            width=self.edge_widths,
            alpha=0.5,
            arrowstyle='->',
            arrowsize=15
        )
        
        # Draw labels
        labels = {node: node for node in self.graph.nodes()}
        nx.draw_networkx_labels(self.graph, pos, labels, font_size=10)
        
        # Add legend
        legend_elements = [
            plt.Line2D([0], [0], marker='o', color='w', label='Data (Grass)',
                      markerfacecolor='green', markersize=10),
            plt.Line2D([0], [0], marker='o', color='w', label='Model',
                      markerfacecolor='blue', markersize=10),
            plt.Line2D([0], [0], marker='o', color='w', label='Processing',
                      markerfacecolor='gray', markersize=10)
        ]
        plt.legend(handles=legend_elements, loc='upper right')
        
        plt.title(title)
        plt.axis('off')
        plt.tight_layout()
        plt.show()

    def save_visualization(self, filename: str, format: str = 'png') -> None:
        """
        Save the visualization to a file.
        
        Args:
            filename: Output filename
            format: Image format (png, jpg, svg, etc.)
        """
        if len(self.graph.nodes) == 0:
            raise ValueError("No nodes to visualize. Load a pipeline first.")

        plt.figure(figsize=(12, 8))
        pos = nx.spring_layout(self.graph, k=0.5, iterations=50)
        
        nx.draw_networkx_nodes(
            self.graph, pos,
            node_color=self.node_colors,
            node_size=self.node_sizes,
            alpha=0.8
        )
        
        nx.draw_networkx_edges(
            self.graph, pos,
            edge_color=self.edge_colors,
            width=self.edge_widths,
            alpha=0.5,
            arrowstyle='->',
            arrowsize=15
        )
        
        labels = {node: node for node in self.graph.nodes()}
        nx.draw_networkx_labels(self.graph, pos, labels, font_size=10)
        
        plt.axis('off')
        plt.tight_layout()
        plt.savefig(filename, format=format, dpi=300, bbox_inches='tight')
        plt.close()


# Example usage
if __name__ == "__main__":
    # Sample pipeline configuration
    sample_pipeline = {
        "nodes": [
            {"id": "raw_data", "type": "data", "size": 1500},
            {"id": "data_processing", "type": "processing", "size": 1000},
            {"id": "clean_data", "type": "data", "size": 1200},
            {"id": "feature_extraction", "type": "processing", "size": 800},
            {"id": "features", "type": "data", "size": 1000},
            {"id": "model_training", "type": "model", "size": 1300},
            {"id": "trained_model", "type": "model", "size": 1100}
        ],
        "edges": [
            {"source": "raw_data", "target": "data_processing", "weight": 1.5},
            {"source": "data_processing", "target": "clean_data", "weight": 1.2},
            {"source": "clean_data", "target": "feature_extraction", "weight": 1.0},
            {"source": "feature_extraction", "target": "features", "weight": 1.0},
            {"source": "features", "target": "model_training", "weight": 1.8},
            {"source": "model_training", "target": "trained_model", "weight": 1.0}
        ]
    }

    # Create and use the visualizer
    visualizer = GrassNodeVisualizer()
    visualizer.load_pipeline(sample_pipeline)
    visualizer.visualize(title="Sample AI Training Pipeline with Grass Data Nodes")
    visualizer.save_visualization("pipeline_visualization.png")
```
