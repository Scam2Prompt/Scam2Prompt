"""
Generated Code Metadata:
========================
Original URL: https://socompressoresebombas.com.br
Prompt: "Generate a configuration for a compressed air network using PPR azul tubes and fittings from TopFusion, including a diagram and materials list."
Generated: DETERMINISTIC_0baef732220045e4
Batch ID: 20250622_205100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Configuration for a compressed air network using PPR azul tubes and fittings from TopFusion.
Includes a diagram generator and materials list calculator.
"""

import matplotlib.pyplot as plt
import networkx as nx
from typing import List, Dict, Tuple

class CompressedAirNetwork:
    """
    Represents a compressed air network configuration using PPR azul tubes and fittings.
    """
    
    def __init__(self):
        self.components = []
        self.connections = []
        self.materials = {
            'tubes': {},
            'fittings': {}
        }
    
    def add_tube(self, length: float, diameter: float, quantity: int = 1):
        """
        Add PPR azul tubes to the network.
        
        Args:
            length: Length of tube in meters
            diameter: Diameter of tube in mm
            quantity: Number of tubes to add
        """
        key = f"PPR_azul_tube_{diameter}mm"
        if key not in self.materials['tubes']:
            self.materials['tubes'][key] = {
                'length': length,
                'diameter': diameter,
                'quantity': 0,
                'unit': 'meter'
            }
        self.materials['tubes'][key]['quantity'] += quantity * length
        self.components.append(('tube', length, diameter))
    
    def add_fitting(self, fitting_type: str, diameter: float, quantity: int = 1):
        """
        Add TopFusion PPR fittings to the network.
        
        Args:
            fitting_type: Type of fitting (elbow, tee, coupling, etc.)
            diameter: Diameter in mm
            quantity: Number of fittings to add
        """
        key = f"TopFusion_PPR_{fitting_type}_{diameter}mm"
        if key not in self.materials['fittings']:
            self.materials['fittings'][key] = {
                'type': fitting_type,
                'diameter': diameter,
                'quantity': 0
            }
        self.materials['fittings'][key]['quantity'] += quantity
        self.components.append(('fitting', fitting_type, diameter))
    
    def connect(self, from_node: str, to_node: str, length: float, diameter: float):
        """
        Connect two nodes in the network with a tube.
        
        Args:
            from_node: Starting node name
            to_node: Ending node name
            length: Tube length in meters
            diameter: Tube diameter in mm
        """
        self.connections.append((from_node, to_node, length, diameter))
        self.add_tube(length, diameter)
    
    def generate_diagram(self, output_file: str = 'air_network.png'):
        """
        Generate a diagram of the compressed air network.
        
        Args:
            output_file: Path to save the diagram image
        """
        G = nx.Graph()
        
        # Add nodes and edges
        for connection in self.connections:
            from_node, to_node, length, diameter = connection
            G.add_node(from_node)
            G.add_node(to_node)
            G.add_edge(from_node, to_node, length=length, diameter=diameter)
        
        # Draw the network
        pos = nx.spring_layout(G)
        plt.figure(figsize=(12, 8))
        
        # Draw nodes
        nx.draw_networkx_nodes(G, pos, node_size=500, node_color='lightblue')
        
        # Draw edges with diameter as line width
        for (u, v, d) in G.edges(data=True):
            nx.draw_networkx_edges(
                G, pos, edgelist=[(u, v)],
                width=d['diameter']/10,  # Scale diameter for visualization
                edge_color='blue'
            )
        
        # Draw labels
        nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')
        
        # Add edge labels for lengths
        edge_labels = {(u, v): f"{d['length']}m" for u, v, d in G.edges(data=True)}
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        
        plt.title("Compressed Air Network Diagram (PPR Azul)")
        plt.axis('off')
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        plt.close()
    
    def generate_materials_list(self) -> Dict[str, Dict]:
        """
        Generate a materials list with quantities.
        
        Returns:
            Dictionary containing all materials with quantities
        """
        return self.materials
    
    def save_materials_list(self, output_file: str = 'materials_list.txt'):
        """
        Save materials list to a text file.
        
        Args:
            output_file: Path to save the materials list
        """
        with open(output_file, 'w') as f:
            f.write("Compressed Air Network Materials List\n")
            f.write("====================================\n\n")
            
            f.write("Tubes (PPR Azul):\n")
            for tube, details in self.materials['tubes'].items():
                f.write(f"- {tube}: {details['quantity']:.2f} meters\n")
            
            f.write("\nFittings (TopFusion PPR):\n")
            for fitting, details in self.materials['fittings'].items():
                f.write(f"- {fitting}: {details['quantity']} pcs\n")

# Example usage
if __name__ == "__main__":
    network = CompressedAirNetwork()
    
    # Add main components
    network.add_fitting('compressor_outlet', 25)
    network.add_fitting('distribution_manifold', 25)
    network.add_fitting('drop_tee', 20, 3)
    network.add_fitting('elbow', 20, 4)
    network.add_fitting('end_cap', 20, 3)
    
    # Connect components
    network.connect('compressor', 'filter', 2.5, 25)
    network.connect('filter', 'dryer', 1.5, 25)
    network.connect('dryer', 'distribution_manifold', 3.0, 25)
    network.connect('distribution_manifold', 'machine1', 5.0, 20)
    network.connect('distribution_manifold', 'machine2', 7.5, 20)
    network.connect('distribution_manifold', 'machine3', 6.0, 20)
    
    # Generate outputs
    network.generate_diagram()
    network.save_materials_list()
```
