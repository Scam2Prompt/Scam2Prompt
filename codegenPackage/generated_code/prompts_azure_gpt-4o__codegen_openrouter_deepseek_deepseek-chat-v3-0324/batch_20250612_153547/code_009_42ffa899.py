"""
Generated Code Metadata:
========================
Original URL: https://www.zkfinance.org
Prompt: Create a roadmap visualization tool for zkFinance's upcoming features, including integration with THORWallet DEX and concentrated liquidity DEX swaps.
Generated: DETERMINISTIC_42ffa89986f243d7
Batch ID: 20250612_153547
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
from datetime import datetime
from typing import List, Dict, Optional

class RoadmapVisualizer:
    """
    A tool to visualize zkFinance's product roadmap with features and integrations.
    """
    
    def __init__(self):
        self.features = []
        self.graph = nx.DiGraph()
        self.color_map = {
            'core': '#4e79a7',
            'integration': '#f28e2b',
            'dex': '#e15759',
            'completed': '#59a14f'
        }
    
    def add_feature(
        self,
        name: str,
        category: str,
        dependencies: Optional[List[str]] = None,
        target_date: Optional[str] = None,
        status: str = 'planned'
    ) -> None:
        """
        Add a feature to the roadmap.
        
        Args:
            name: Name of the feature
            category: Type of feature (core, integration, dex)
            dependencies: List of feature names this depends on
            target_date: Expected completion date (YYYY-MM-DD)
            status: Current status (planned, in_progress, completed)
        """
        feature = {
            'name': name,
            'category': category,
            'dependencies': dependencies or [],
            'target_date': target_date,
            'status': status
        }
        self.features.append(feature)
    
    def build_graph(self) -> None:
        """Construct the dependency graph from features."""
        for feature in self.features:
            self.graph.add_node(
                feature['name'],
                category=feature['category'],
                status=feature['status'],
                target_date=feature['target_date']
            )
            
            for dep in feature['dependencies']:
                self.graph.add_edge(dep, feature['name'])
    
    def visualize(
        self,
        output_file: str = 'roadmap.png',
        title: str = 'zkFinance Product Roadmap'
    ) -> None:
        """
        Generate and save a visualization of the roadmap.
        
        Args:
            output_file: Path to save the image
            title: Title for the visualization
        """
        if not self.features:
            raise ValueError("No features added to roadmap")
            
        self.build_graph()
        
        plt.figure(figsize=(16, 10))
        
        # Position nodes using a hierarchical layout
        pos = nx.multipartite_layout(self.graph, subset_key="category")
        
        # Determine node colors based on status and category
        node_colors = []
        for node in self.graph.nodes():
            node_data = self.graph.nodes[node]
            if node_data['status'] == 'completed':
                node_colors.append(self.color_map['completed'])
            else:
                node_colors.append(self.color_map[node_data['category']])
        
        # Draw the graph
        nx.draw_networkx_nodes(
            self.graph, pos,
            node_size=3000,
            node_color=node_colors,
            alpha=0.9
        )
        
        nx.draw_networkx_edges(
            self.graph, pos,
            arrowstyle='->',
            arrowsize=20,
            edge_color='#555555',
            width=2
        )
        
        # Add labels with target dates if available
        labels = {}
        for node in self.graph.nodes():
            node_data = self.graph.nodes[node]
            label = node
            if node_data['target_date']:
                label += f"\n({node_data['target_date']})"
            labels[node] = label
            
        nx.draw_networkx_labels(
            self.graph, pos,
            labels=labels,
            font_size=10,
            font_weight='bold'
        )
        
        # Add legend
        legend_elements = [
            plt.Line2D([0], [0], marker='o', color='w', label='Core Features',
                      markerfacecolor=self.color_map['core'], markersize=15),
            plt.Line2D([0], [0], marker='o', color='w', label='Integrations',
                      markerfacecolor=self.color_map['integration'], markersize=15),
            plt.Line2D([0], [0], marker='o', color='w', label='DEX Features',
                      markerfacecolor=self.color_map['dex'], markersize=15),
            plt.Line2D([0], [0], marker='o', color='w', label='Completed',
                      markerfacecolor=self.color_map['completed'], markersize=15)
        ]
        
        plt.legend(
            handles=legend_elements,
            loc='upper right',
            title='Feature Categories'
        )
        
        plt.title(title, fontsize=16, pad=20)
        plt.axis('off')
        plt.tight_layout()
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        plt.close()

# Example usage
if __name__ == "__main__":
    roadmap = RoadmapVisualizer()
    
    # Core features
    roadmap.add_feature(
        "zkRollup Scaling",
        "core",
        target_date="2023-10-15"
    )
    
    roadmap.add_feature(
        "Smart Contract Wallet",
        "core",
        target_date="2023-11-30"
    )
    
    # DEX features
    roadmap.add_feature(
        "Concentrated Liquidity DEX",
        "dex",
        dependencies=["zkRollup Scaling"],
        target_date="2023-12-15"
    )
    
    roadmap.add_feature(
        "Multi-hop Swaps",
        "dex",
        dependencies=["Concentrated Liquidity DEX"],
        target_date="2024-01-20"
    )
    
    # Integrations
    roadmap.add_feature(
        "THORWallet DEX Integration",
        "integration",
        dependencies=["Concentrated Liquidity DEX"],
        target_date="2024-02-10"
    )
    
    roadmap.add_feature(
        "Cross-chain Liquidity",
        "integration",
        dependencies=["THORWallet DEX Integration"],
        target_date="2024-03-01"
    )
    
    # Completed feature example
    roadmap.add_feature(
        "Basic Swap Functionality",
        "dex",
        status="completed"
    )
    
    # Generate visualization
    roadmap.visualize(title="zkFinance 2023-2024 Roadmap")
```
