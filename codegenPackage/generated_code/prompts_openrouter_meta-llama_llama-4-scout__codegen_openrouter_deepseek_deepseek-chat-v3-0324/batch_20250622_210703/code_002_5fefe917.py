"""
Generated Code Metadata:
========================
Original URL: https://healthcareventure.nl
Prompt: Generate a Python script to visualize the buy-and-build model of acquiring and growing multiple youth mental healthcare firms.
Generated: DETERMINISTIC_5fefe917cb7abfb4
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt
import networkx as nx
import random
from typing import List, Dict, Optional

class AcquisitionGraph:
    """Visualizes the buy-and-build model for youth mental healthcare firms."""
    
    def __init__(self):
        """Initialize the graph with default settings."""
        self.graph = nx.DiGraph()
        self.firm_counter = 0
        self.colors = {
            'platform': '#1f77b4',
            'acquisition': '#ff7f0e',
            'organic': '#2ca02c'
        }
        
    def add_platform_firm(self, name: str, revenue: float) -> None:
        """Add the initial platform firm to the graph.
        
        Args:
            name: Name of the platform firm
            revenue: Annual revenue in millions
        """
        self.graph.add_node(
            name,
            type='platform',
            revenue=revenue,
            color=self.colors['platform']
        )
        self.firm_counter += 1
    
    def add_acquisition(self, 
                       parent: str, 
                       name: str, 
                       revenue: float,
                       acquisition_cost: float) -> None:
        """Add an acquired firm to the graph.
        
        Args:
            parent: Name of the parent firm
            name: Name of the acquired firm
            revenue: Annual revenue in millions
            acquisition_cost: Cost of acquisition in millions
        """
        if parent not in self.graph:
            raise ValueError(f"Parent firm {parent} does not exist")
            
        self.graph.add_node(
            name,
            type='acquisition',
            revenue=revenue,
            color=self.colors['acquisition']
        )
        self.graph.add_edge(
            parent,
            name,
            cost=acquisition_cost,
            type='acquisition'
        )
        self.firm_counter += 1
    
    def add_organic_growth(self,
                          parent: str,
                          name: str,
                          revenue: float,
                          investment: float) -> None:
        """Add an organically grown firm to the graph.
        
        Args:
            parent: Name of the parent firm
            name: Name of the new firm
            revenue: Annual revenue in millions
            investment: Initial investment in millions
        """
        if parent not in self.graph:
            raise ValueError(f"Parent firm {parent} does not exist")
            
        self.graph.add_node(
            name,
            type='organic',
            revenue=revenue,
            color=self.colors['organic']
        )
        self.graph.add_edge(
            parent,
            name,
            cost=investment,
            type='organic'
        )
        self.firm_counter += 1
    
    def visualize(self, 
                 title: str = "Buy-and-Build Model for Youth Mental Healthcare Firms",
                 figsize: tuple = (12, 8)) -> None:
        """Generate a visualization of the acquisition graph.
        
        Args:
            title: Title for the visualization
            figsize: Size of the figure (width, height)
        """
        plt.figure(figsize=figsize)
        
        pos = nx.spring_layout(self.graph, seed=42)
        
        # Draw nodes
        node_colors = [self.graph.nodes[n]['color'] for n in self.graph.nodes()]
        node_sizes = [self.graph.nodes[n]['revenue'] * 100 for n in self.graph.nodes()]
        
        nx.draw_networkx_nodes(
            self.graph,
            pos,
            node_color=node_colors,
            node_size=node_sizes,
            alpha=0.8
        )
        
        # Draw edges
        edge_colors = []
        edge_widths = []
        for u, v in self.graph.edges():
            edge_type = self.graph.edges[u, v]['type']
            cost = self.graph.edges[u, v]['cost']
            edge_colors.append(self.colors[edge_type])
            edge_widths.append(cost / 2)
        
        nx.draw_networkx_edges(
            self.graph,
            pos,
            edge_color=edge_colors,
            width=edge_widths,
            alpha=0.6,
            arrowstyle='->',
            arrowsize=15
        )
        
        # Draw labels
        labels = {n: f"{n}\n${self.graph.nodes[n]['revenue']}M" for n in self.graph.nodes()}
        nx.draw_networkx_labels(
            self.graph,
            pos,
            labels=labels,
            font_size=10,
            font_weight='bold'
        )
        
        # Add legend
        plt.scatter([], [], c=self.colors['platform'], label='Platform Firm', alpha=0.8)
        plt.scatter([], [], c=self.colors['acquisition'], label='Acquired Firm', alpha=0.8)
        plt.scatter([], [], c=self.colors['organic'], label='Organic Growth', alpha=0.8)
        plt.legend(scatterpoints=1, frameon=True, labelspacing=1)
        
        plt.title(title, fontsize=16)
        plt.axis('off')
        plt.tight_layout()
        plt.show()

def generate_sample_data() -> AcquisitionGraph:
    """Generate sample data for visualization."""
    graph = AcquisitionGraph()
    
    # Add platform firm
    graph.add_platform_firm("Mindful Youth", 10.0)
    
    # Add acquisitions
    graph.add_acquisition("Mindful Youth", "Teen Therapy Co", 3.5, 7.0)
    graph.add_acquisition("Mindful Youth", "Youth Wellness", 2.8, 5.6)
    graph.add_acquisition("Teen Therapy Co", "Adolescent Care", 1.2, 3.0)
    
    # Add organic growth
    graph.add_organic_growth("Mindful Youth", "TeenMind App", 1.5, 2.0)
    graph.add_organic_growth("Youth Wellness", "Parent Support", 0.8, 1.0)
    
    return graph

if __name__ == "__main__":
    # Generate and visualize sample data
    acquisition_graph = generate_sample_data()
    acquisition_graph.visualize()
```
