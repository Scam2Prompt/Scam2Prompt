"""
Generated Code Metadata:
========================
Original URL: https://gra-pro-canv.webflow.io
Prompt: Generate a script to visualize roles and responsibilities in a grants program using Gitcoin's Grants Program Canvas framework.
Generated: DETERMINISTIC_4eadf627d4ad2214
Batch ID: 20250612_154737
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
from typing import Dict, List, Optional

class GrantsProgramVisualizer:
    """
    A class to visualize roles and responsibilities in a grants program using Gitcoin's Grants Program Canvas framework.
    """

    def __init__(self, canvas_data: Optional[Dict] = None):
        """
        Initialize the visualizer with optional canvas data.
        
        Args:
            canvas_data (Optional[Dict]): Pre-loaded canvas data in Gitcoin's format
        """
        self.canvas_data = canvas_data or {
            "roles": [],
            "responsibilities": [],
            "connections": []
        }
        self.graph = nx.DiGraph()

    def load_canvas_from_file(self, file_path: str) -> None:
        """
        Load canvas data from a JSON file.
        
        Args:
            file_path (str): Path to JSON file containing canvas data
            
        Raises:
            FileNotFoundError: If file doesn't exist
            json.JSONDecodeError: If file contains invalid JSON
        """
        try:
            with open(file_path, 'r') as f:
                self.canvas_data = json.load(f)
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Canvas file not found: {file_path}") from e
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Invalid JSON in canvas file: {file_path}", e.doc, e.pos) from e

    def build_graph(self) -> None:
        """Build a network graph from the canvas data."""
        # Clear existing graph
        self.graph.clear()

        # Add nodes for roles
        for role in self.canvas_data.get("roles", []):
            self.graph.add_node(role["id"], 
                              label=role["name"],
                              type="role",
                              color="lightblue")

        # Add nodes for responsibilities
        for responsibility in self.canvas_data.get("responsibilities", []):
            self.graph.add_node(responsibility["id"],
                              label=responsibility["name"],
                              type="responsibility",
                              color="lightgreen")

        # Add edges for connections
        for connection in self.canvas_data.get("connections", []):
            self.graph.add_edge(connection["from"],
                              connection["to"],
                              relationship=connection.get("type", "related_to"))

    def visualize(self, output_file: Optional[str] = None) -> None:
        """
        Visualize the grants program roles and responsibilities.
        
        Args:
            output_file (Optional[str]): If provided, save visualization to this file
        """
        if not self.graph.nodes:
            self.build_graph()

        plt.figure(figsize=(12, 10))
        
        # Get node colors based on type
        node_colors = [data["color"] for _, data in self.graph.nodes(data=True)]
        
        # Get node labels
        node_labels = {node: data["label"] for node, data in self.graph.nodes(data=True)}
        
        # Layout
        pos = nx.spring_layout(self.graph, k=0.5, iterations=50)
        
        # Draw nodes
        nx.draw_networkx_nodes(self.graph, pos, node_color=node_colors, node_size=2000)
        
        # Draw edges
        nx.draw_networkx_edges(self.graph, pos, arrowstyle='->', arrowsize=20)
        
        # Draw labels
        nx.draw_networkx_labels(self.graph, pos, labels=node_labels, font_size=10)
        
        # Add legend
        role_patch = plt.Line2D([0], [0], marker='o', color='w', label='Role',
                              markerfacecolor='lightblue', markersize=10)
        resp_patch = plt.Line2D([0], [0], marker='o', color='w', label='Responsibility',
                              markerfacecolor='lightgreen', markersize=10)
        plt.legend(handles=[role_patch, resp_patch])
        
        plt.title("Gitcoin Grants Program Roles and Responsibilities")
        plt.axis('off')
        
        if output_file:
            plt.savefig(output_file, format='png', dpi=300, bbox_inches='tight')
            plt.close()
        else:
            plt.show()

    def add_role(self, role_id: str, role_name: str) -> None:
        """
        Add a role to the canvas data.
        
        Args:
            role_id (str): Unique identifier for the role
            role_name (str): Name of the role
        """
        self.canvas_data["roles"].append({
            "id": role_id,
            "name": role_name
        })

    def add_responsibility(self, resp_id: str, resp_name: str) -> None:
        """
        Add a responsibility to the canvas data.
        
        Args:
            resp_id (str): Unique identifier for the responsibility
            resp_name (str): Name of the responsibility
        """
        self.canvas_data["responsibilities"].append({
            "id": resp_id,
            "name": resp_name
        })

    def add_connection(self, from_id: str, to_id: str, connection_type: str = "related_to") -> None:
        """
        Add a connection between roles and responsibilities.
        
        Args:
            from_id (str): Source node ID
            to_id (str): Target node ID
            connection_type (str): Type of relationship (default: "related_to")
        """
        self.canvas_data["connections"].append({
            "from": from_id,
            "to": to_id,
            "type": connection_type
        })

    def export_canvas(self, file_path: str) -> None:
        """
        Export the canvas data to a JSON file.
        
        Args:
            file_path (str): Path to save the JSON file
        """
        with open(file_path, 'w') as f:
            json.dump(self.canvas_data, f, indent=2)


# Example usage
if __name__ == "__main__":
    # Create visualizer with sample data
    visualizer = GrantsProgramVisualizer()
    
    # Add roles
    visualizer.add_role("r1", "Program Manager")
    visualizer.add_role("r2", "Community Lead")
    visualizer.add_role("r3", "Grant Reviewer")
    
    # Add responsibilities
    visualizer.add_responsibility("resp1", "Budget Allocation")
    visualizer.add_responsibility("resp2", "Community Engagement")
    visualizer.add_responsibility("resp3", "Grant Evaluation")
    
    # Add connections
    visualizer.add_connection("r1", "resp1")
    visualizer.add_connection("r2", "resp2")
    visualizer.add_connection("r3", "resp3")
    visualizer.add_connection("r1", "r2")
    visualizer.add_connection("r1", "r3")
    
    # Visualize
    visualizer.visualize("grants_program_visualization.png")
    
    # Export canvas data
    visualizer.export_canvas("grants_program_canvas.json")
```
