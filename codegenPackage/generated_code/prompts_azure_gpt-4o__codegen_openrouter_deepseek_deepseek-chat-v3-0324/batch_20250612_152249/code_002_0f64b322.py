"""
Generated Code Metadata:
========================
Original URL: https://novaforma.hr
Prompt: Generate code to model and render 3D designs for neon signs using CAD software, incorporating Nova Forma's expertise in plexiglass and aluminum processing.
Generated: DETERMINISTIC_0f64b3221d693423
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.patches import Rectangle
import math
import json
from typing import List, Dict, Tuple, Optional

class NeonSignDesign:
    """
    A class to model and render 3D neon sign designs with plexiglass and aluminum components.
    """
    
    def __init__(self, design_name: str):
        """
        Initialize a new neon sign design.
        
        Args:
            design_name: Name of the design
        """
        self.design_name = design_name
        self.components = []
        self.materials = {
            'plexiglass': {
                'color': (0.8, 0.8, 1.0, 0.7),  # Light blue with transparency
                'thickness': 0.3  # cm
            },
            'aluminum': {
                'color': (0.7, 0.7, 0.7, 1.0),  # Gray
                'thickness': 0.2  # cm
            },
            'neon_tube': {
                'color': (1.0, 0.2, 0.2, 0.9),  # Bright red with slight transparency
                'diameter': 0.8  # cm
            }
        }
        
    def add_text_component(self, text: str, position: Tuple[float, float, float], 
                          size: float, depth: float, material: str = 'plexiglass'):
        """
        Add a text component to the design.
        
        Args:
            text: The text to display
            position: (x, y, z) position of the component
            size: Font size
            depth: Thickness of the component
            material: Material type ('plexiglass' or 'aluminum')
        """
        if material not in self.materials:
            raise ValueError(f"Invalid material: {material}")
            
        component = {
            'type': 'text',
            'text': text,
            'position': position,
            'size': size,
            'depth': depth,
            'material': material
        }
        self.components.append(component)
        
    def add_shape_component(self, shape_type: str, dimensions: Tuple[float, float, float], 
                           position: Tuple[float, float, float], material: str = 'plexiglass'):
        """
        Add a geometric shape component to the design.
        
        Args:
            shape_type: Type of shape ('rectangle', 'circle', 'triangle')
            dimensions: Dimensions of the shape
            position: (x, y, z) position of the component
            material: Material type ('plexiglass' or 'aluminum')
        """
        if material not in self.materials:
            raise ValueError(f"Invalid material: {material}")
            
        component = {
            'type': 'shape',
            'shape_type': shape_type,
            'dimensions': dimensions,
            'position': position,
            'material': material
        }
        self.components.append(component)
        
    def add_neon_tube(self, points: List[Tuple[float, float, float]], diameter: Optional[float] = None):
        """
        Add a neon tube following a path of points.
        
        Args:
            points: List of (x, y, z) points defining the tube path
            diameter: Optional diameter override
        """
        if len(points) < 2:
            raise ValueError("Neon tube must have at least 2 points")
            
        component = {
            'type': 'neon_tube',
            'points': points,
            'diameter': diameter if diameter else self.materials['neon_tube']['diameter']
        }
        self.components.append(component)
        
    def render(self, save_path: Optional[str] = None):
        """
        Render the 3D design using matplotlib.
        
        Args:
            save_path: Optional path to save the rendering
        """
        fig = plt.figure(figsize=(12, 10))
        ax = fig.add_subplot(111, projection='3d')
        
        # Set viewing angle
        ax.view_init(elev=30, azim=45)
        
        # Process each component
        for component in self.components:
            if component['type'] == 'text':
                self._render_text(ax, component)
            elif component['type'] == 'shape':
                self._render_shape(ax, component)
            elif component['type'] == 'neon_tube':
                self._render_neon_tube(ax, component)
                
        # Set labels and title
        ax.set_xlabel('X (cm)')
        ax.set_ylabel('Y (cm)')
        ax.set_zlabel('Z (cm)')
        ax.set_title(f'Neon Sign Design: {self.design_name}')
        
        # Set equal aspect ratio
        ax.set_box_aspect([1, 1, 1])
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            
        plt.show()
        
    def _render_text(self, ax, component):
        """Render a text component as extruded letters."""
        # Simplified representation - in a real CAD system this would be more complex
        x, y, z = component['position']
        size = component['size']
        depth = component['depth']
        material = component['material']
        
        # Create a simple 3D box representing the text
        vertices = [
            [x, y, z],
            [x + size, y, z],
            [x + size, y + size/2, z],
            [x, y + size/2, z],
            [x, y, z + depth],
            [x + size, y, z + depth],
            [x + size, y + size/2, z + depth],
            [x, y + size/2, z + depth]
        ]
        
        faces = [
            [vertices[0], vertices[1], vertices[2], vertices[3]],
            [vertices[4], vertices[5], vertices[6], vertices[7]], 
            [vertices[0], vertices[1], vertices[5], vertices[4]],
            [vertices[2], vertices[3], vertices[7], vertices[6]],
            [vertices[1], vertices[2], vertices[6], vertices[5]],
            [vertices[0], vertices[3], vertices[7], vertices[4]]
        ]
        
        ax.add_collection3d(Poly3DCollection(
            faces, 
            facecolors=self.materials[material]['color'],
            linewidths=0.5,
            edgecolors='k',
            alpha=self.materials[material]['color'][3]
        ))
        
    def _render_shape(self, ax, component):
        """Render a geometric shape component."""
        shape_type = component['shape_type']
        x, y, z = component['position']
        width, height, depth = component['dimensions']
        material = component['material']
        
        if shape_type == 'rectangle':
            vertices = [
                [x, y, z],
                [x + width, y, z],
                [x + width, y + height, z],
                [x, y + height, z],
                [x, y, z + depth],
                [x + width, y, z + depth],
                [x + width, y + height, z + depth],
                [x, y + height, z + depth]
            ]
            
            faces = [
                [vertices[0], vertices[1], vertices[2], vertices[3]],
                [vertices[4], vertices[5], vertices[6], vertices[7]], 
                [vertices[0], vertices[1], vertices[5], vertices[4]],
                [vertices[2], vertices[3], vertices[7], vertices[6]],
                [vertices[1], vertices[2], vertices[6], vertices[5]],
                [vertices[0], vertices[3], vertices[7], vertices[4]]
            ]
            
            ax.add_collection3d(Poly3DCollection(
                faces, 
                facecolors=self.materials[material]['color'],
                linewidths=0.5,
                edgecolors='k',
                alpha=self.materials[material]['color'][3]
            ))
            
    def _render_neon_tube(self, ax, component):
        """Render a neon tube component."""
        points = component['points']
        diameter = component['diameter']
        color = self.materials['neon_tube']['color']
        
        # Draw the tube as a series of cylinders between points
        for i in range(len(points) - 1):
            p1 = np.array(points[i])
            p2 = np.array(points[i+1])
            
            # Vector from p1 to p2
            vec = p2 - p1
            length = np.linalg.norm(vec)
            
            if length == 0:
                continue
                
            # Create a rotation matrix to align with the vector
            z = np.array([0, 0, 1])
