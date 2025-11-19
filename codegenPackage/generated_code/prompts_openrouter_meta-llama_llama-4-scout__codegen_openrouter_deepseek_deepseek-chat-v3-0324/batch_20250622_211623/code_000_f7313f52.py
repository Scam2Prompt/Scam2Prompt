"""
Generated Code Metadata:
========================
Original URL: https://linea-7.webflow.io
Prompt: "Design a modern minimalist home in the style of Bauhaus Brutalist, incorporating natural and earthy tones, using materials like concrete and metal frames."
Generated: DETERMINISTIC_f7313f52ed315e84
Batch ID: 20250622_211623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Modern Minimalist Home Design - Bauhaus Brutalist Style

This script generates a 3D model of a minimalist home in Bauhaus Brutalist style
using earthy tones and materials like concrete and metal frames.
"""

import math
from typing import List, Tuple
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

class BauhausBrutalistHome:
    """
    A class to represent and visualize a Bauhaus Brutalist style home.
    """
    
    def __init__(self):
        """Initialize the home with default parameters."""
        self.materials = {
            'concrete': {'color': '#8B8B8B', 'alpha': 0.9},
            'metal': {'color': '#5A5A5A', 'alpha': 0.7},
            'wood': {'color': '#8B4513', 'alpha': 0.8},
            'glass': {'color': '#ADD8E6', 'alpha': 0.3}
        }
        self.dimensions = {
            'width': 20,
            'depth': 15,
            'height': 8
        }
        self.window_size = 2
        self.door_size = (2.5, 1)
        
    def create_cube(self, origin: Tuple[float, float, float], 
                   size: Tuple[float, float, float]) -> List[Tuple]:
        """
        Generate vertices for a cube given origin and size.
        
        Args:
            origin: (x, y, z) coordinates of the cube's bottom-front-left corner
            size: (width, depth, height) dimensions of the cube
            
        Returns:
            List of vertices forming the cube's faces
        """
        x, y, z = origin
        w, d, h = size
        
        vertices = [
            # Front face
            [(x, y, z), (x+w, y, z), (x+w, y, z+h), (x, y, z+h)],
            # Back face
            [(x, y+d, z), (x+w, y+d, z), (x+w, y+d, z+h), (x, y+d, z+h)],
            # Left face
            [(x, y, z), (x, y+d, z), (x, y+d, z+h), (x, y, z+h)],
            # Right face
            [(x+w, y, z), (x+w, y+d, z), (x+w, y+d, z+h), (x+w, y, z+h)],
            # Bottom face
            [(x, y, z), (x+w, y, z), (x+w, y+d, z), (x, y+d, z)],
            # Top face
            [(x, y, z+h), (x+w, y, z+h), (x+w, y+d, z+h), (x, y+d, z+h)]
        ]
        
        return vertices
    
    def add_window(self, wall_vertices: List[Tuple], 
                  position: Tuple[float, float], 
                  size: float = 2) -> Tuple[List[Tuple], List[Tuple]]:
        """
        Create a window opening in a wall.
        
        Args:
            wall_vertices: Vertices of the wall face
            position: (x_offset, z_offset) from bottom-left corner of wall
            size: Window size (square)
            
        Returns:
            Tuple of (wall_with_opening, window_frame)
        """
        x, y, z = wall_vertices[0][0]  # Bottom-left corner of wall
        x_offset, z_offset = position
        
        # Create window opening
        window_vertices = [
            (x + x_offset, y, z + z_offset),
            (x + x_offset + size, y, z + z_offset),
            (x + x_offset + size, y, z + z_offset + size),
            (x + x_offset, y, z + z_offset + size)
        ]
        
        # Create window frame (metal)
        frame_thickness = 0.1
        frame_vertices = [
            # Outer frame
            self.create_cube(
                (x + x_offset - frame_thickness, y - frame_thickness, z + z_offset - frame_thickness),
                (size + 2*frame_thickness, 2*frame_thickness, size + 2*frame_thickness)
            ),
            # Inner frame (glass)
            self.create_cube(
                (x + x_offset, y, z + z_offset),
                (size, 0.01, size)
            )
        ]
        
        return window_vertices, frame_vertices
    
    def visualize(self):
        """Create and display the 3D visualization of the home."""
        fig = plt.figure(figsize=(12, 8))
        ax = fig.add_subplot(111, projection='3d')
        
        # Main structure (concrete)
        main_structure = self.create_cube(
            (0, 0, 0), 
            (self.dimensions['width'], self.dimensions['depth'], self.dimensions['height'])
        )
        ax.add_collection3d(Poly3DCollection(
            main_structure, 
            facecolors=self.materials['concrete']['color'], 
            alpha=self.materials['concrete']['alpha']
        ))
        
        # Add windows
        window_positions = [
            (3, 2), (8, 2), (13, 2),  # Front wall
            (3, 10, 2), (8, 10, 2), (13, 10, 2)  # Back wall (y offset by depth)
        ]
        
        for pos in window_positions:
            wall_face = self.create_cube(
                (pos[0], 0 if len(pos) == 2 else pos[1], 0), 
                (self.window_size, 0.1, self.window_size)
            )[0]  # Get front or back face
            _, frame = self.add_window(wall_face, (0, 0) if len(pos) == 2 else (pos[0], pos[2]))
            
            # Add frame to plot
            for part in frame:
                ax.add_collection3d(Poly3DCollection(
                    part, 
                    facecolors=self.materials['metal']['color'], 
                    alpha=self.materials['metal']['alpha']
                ))
        
        # Add door
        door_vertices = self.create_cube(
            (self.dimensions['width']/2 - self.door_size[0]/2, 0, 0),
            (self.door_size[0], 0.1, self.door_size[1])
        )[0]  # Front face
        ax.add_collection3d(Poly3DCollection(
            [door_vertices], 
            facecolors=self.materials['wood']['color'], 
            alpha=self.materials['wood']['alpha']
        ))
        
        # Flat roof (concrete slab)
        roof_vertices = self.create_cube(
            (-1, -1, self.dimensions['height']),
            (self.dimensions['width']+2, self.dimensions['depth']+2, 0.5)
        )
        ax.add_collection3d(Poly3DCollection(
            roof_vertices, 
            facecolors=self.materials['concrete']['color'], 
            alpha=self.materials['concrete']['alpha']*0.8
        ))
        
        # Set plot limits and labels
        ax.set_xlim([-2, self.dimensions['width']+2])
        ax.set_ylim([-2, self.dimensions['depth']+2])
        ax.set_zlim([0, self.dimensions['height']+2])
        ax.set_xlabel('Width (m)')
        ax.set_ylabel('Depth (m)')
        ax.set_zlabel('Height (m)')
        ax.set_title('Bauhaus Brutalist Home Design')
        
        plt.tight_layout()
        plt.show()

# Example usage
if __name__ == "__main__":
    try:
        home = BauhausBrutalistHome()
        home.visualize()
    except Exception as e:
        print(f"Error generating home design: {e}")
```
