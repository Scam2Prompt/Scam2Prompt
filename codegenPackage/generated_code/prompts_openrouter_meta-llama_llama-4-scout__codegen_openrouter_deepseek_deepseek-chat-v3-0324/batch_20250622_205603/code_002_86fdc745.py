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
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from typing import List, Dict, Optional, Tuple

class SocialImpactGraph:
    """
    A class to create and visualize a network graph of social impact heroes, investors, and organizations.
    """
    
    def __init__(self):
        """
        Initialize the graph with empty data structures.
        """
        self.graph = nx.Graph()
        self.node_colors = []
        self.node_sizes = []
        self.labels = {}
        
    def load_data(self, heroes_data: List[Dict], investors_data: List[Dict], orgs_data: List[Dict]) -> None:
        """
        Load data into the graph from provided lists of dictionaries.
        
        Args:
            heroes_data: List of dictionaries containing hero information
            investors_data: List of dictionaries containing investor information
            orgs_data: List of dictionaries containing organization information
        """
        try:
            # Add nodes with attributes
            self._add_nodes(heroes_data, 'hero')
            self._add_nodes(investors_data, 'investor')
            self._add_nodes(orgs_data, 'organization')
            
            # Add edges based on connections
            self._add_edges(heroes_data, investors_data, orgs_data)
            
        except Exception as e:
            raise ValueError(f"Error loading data: {str(e)}")
    
    def _add_nodes(self, data: List[Dict], node_type: str) -> None:
        """
        Add nodes to the graph from a data list.
        
        Args:
            data: List of node data dictionaries
            node_type: Type of node ('hero', 'investor', 'organization')
        """
        for item in data:
            if 'id' not in item or 'name' not in item:
                raise ValueError(f"Missing required fields in {node_type} data")
                
            node_id = item['id']
            self.graph.add_node(node_id, **item, type=node_type)
            
            # Store visualization properties
            self.labels[node_id] = item['name']
            
            if node_type == 'hero':
                self.node_colors.append('lightgreen')
                self.node_sizes.append(800)
            elif node_type == 'investor':
                self.node_colors.append('lightblue')
                self.node_sizes.append(600)
            else:  # organization
                self.node_colors.append('pink')
                self.node_sizes.append(1000)
    
    def _add_edges(self, heroes: List[Dict], investors: List[Dict], orgs: List[Dict]) -> None:
        """
        Add edges between nodes based on their connections.
        
        Args:
            heroes: List of hero data dictionaries
            investors: List of investor data dictionaries
            orgs: List of organization data dictionaries
        """
        # Connect heroes to their organizations
        for hero in heroes:
            if 'organizations' in hero:
                for org_id in hero['organizations']:
                    if self.graph.has_node(hero['id']) and self.graph.has_node(org_id):
                        self.graph.add_edge(hero['id'], org_id, relationship='affiliated_with')
        
        # Connect investors to organizations they fund
        for investor in investors:
            if 'investments' in investor:
                for org_id in investor['investments']:
                    if self.graph.has_node(investor['id']) and self.graph.has_node(org_id):
                        self.graph.add_edge(investor['id'], org_id, relationship='funds')
    
    def visualize(self, output_file: Optional[str] = None) -> None:
        """
        Visualize the graph and optionally save to file.
        
        Args:
            output_file: Path to save the visualization (optional)
        """
        try:
            plt.figure(figsize=(12, 10))
            
            # Compute layout
            pos = nx.spring_layout(self.graph, k=0.15, iterations=50)
            
            # Draw nodes
            nx.draw_networkx_nodes(
                self.graph, 
                pos, 
                node_color=self.node_colors,
                node_size=self.node_sizes,
                alpha=0.9
            )
            
            # Draw edges
            nx.draw_networkx_edges(
                self.graph, 
                pos, 
                width=1.0, 
                alpha=0.5
            )
            
            # Draw labels
            nx.draw_networkx_labels(
                self.graph, 
                pos, 
                self.labels, 
                font_size=10,
                font_family='sans-serif'
            )
            
            # Add legend
            legend_elements = [
                plt.Line2D([0], [0], marker='o', color='w', label='Hero', markerfacecolor='lightgreen', markersize=10),
                plt.Line2D([0], [0], marker='o', color='w', label='Investor', markerfacecolor='lightblue', markersize=10),
                plt.Line2D([0], [0], marker='o', color='w', label='Organization', markerfacecolor='pink', markersize=10)
            ]
            plt.legend(handles=legend_elements, loc='upper right')
            
            plt.title("Social Impact Network Graph")
            plt.axis('off')
            
            if output_file:
                plt.savefig(output_file, format='png', dpi=300, bbox_inches='tight')
                print(f"Graph saved to {output_file}")
            else:
                plt.show()
                
        except Exception as e:
            raise RuntimeError(f"Error visualizing graph: {str(e)}")
    
    def export_graphml(self, output_file: str) -> None:
        """
        Export the graph to GraphML format.
        
        Args:
            output_file: Path to save the GraphML file
        """
        try:
            nx.write_graphml(self.graph, output_file)
            print(f"Graph exported to {output_file}")
        except Exception as e:
            raise RuntimeError(f"Error exporting graph: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Sample data (in a real scenario, this would come from a database or API)
    heroes = [
        {"id": "h1", "name": "Jane Doe", "organizations": ["o1", "o2"]},
        {"id": "h2", "name": "John Smith", "organizations": ["o2"]}
    ]
    
    investors = [
        {"id": "i1", "name": "Impact Fund", "investments": ["o1", "o3"]},
        {"id": "i2", "name": "Green Capital", "investments": ["o2"]}
    ]
    
    organizations = [
        {"id": "o1", "name": "Eco Solutions"},
        {"id": "o2", "name": "Clean Water Initiative"},
        {"id": "o3", "name": "Renewable Energy Foundation"}
    ]
    
    try:
        # Create and visualize the graph
        graph = SocialImpactGraph()
        graph.load_data(heroes, investors, organizations)
        graph.visualize("social_impact_network.png")
        graph.export_graphml("social_impact_network.graphml")
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
