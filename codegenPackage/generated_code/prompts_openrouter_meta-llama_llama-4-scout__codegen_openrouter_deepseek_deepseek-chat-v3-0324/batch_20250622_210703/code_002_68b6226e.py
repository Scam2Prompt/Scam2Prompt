"""
Generated Code Metadata:
========================
Original URL: https://amayrainterior.com
Prompt: "Write a Python script to create a 3D visualization of a modular kitchen design, similar to those offered by Amayra Interiors."
Generated: DETERMINISTIC_68b6226effec1ea7
Batch ID: 20250622_210703
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

class KitchenDesign3D:
    """
    A 3D visualization of a modular kitchen design.
    """
    def __init__(self, width=10, depth=6, height=2.5):
        """
        Initialize kitchen dimensions.
        :param width: Kitchen width in meters
        :param depth: Kitchen depth in meters
        :param height: Kitchen height in meters
        """
        self.width = width
        self.depth = depth
        self.height = height
        self.fig = plt.figure(figsize=(12, 8))
        self.ax = self.fig.add_subplot(111, projection='3d')
        
    def draw_walls(self):
        """Draw the kitchen walls."""
        # Floor
        floor = np.array([
            [0, 0, 0],
            [self.width, 0, 0],
            [self.width, self.depth, 0],
            [0, self.depth, 0]
        ])
        self.ax.add_collection3d(Poly3DCollection([floor], color='lightgray', alpha=0.5))
        
        # Walls
        wall1 = np.array([
            [0, 0, 0],
            [0, 0, self.height],
            [0, self.depth, self.height],
            [0, self.depth, 0]
        ])
        wall2 = np.array([
            [0, 0, 0],
            [self.width, 0, 0],
            [self.width, 0, self.height],
            [0, 0, self.height]
        ])
        wall3 = np.array([
            [self.width, 0, 0],
            [self.width, 0, self.height],
            [self.width, self.depth, self.height],
            [self.width, self.depth, 0]
        ])
        self.ax.add_collection3d(Poly3DCollection([wall1, wall2, wall3], color='beige', alpha=0.7))
    
    def draw_cabinets(self):
        """Draw kitchen cabinets."""
        # Base cabinets
        cabinet_depth = 0.6
        cabinet_height = 0.9
        
        # Left base cabinet
        left_cabinet = np.array([
            [0.5, 0, 0],
            [1.5, 0, 0],
            [1.5, cabinet_depth, 0],
            [0.5, cabinet_depth, 0],
            [0.5, 0, cabinet_height],
            [1.5, 0, cabinet_height],
            [1.5, cabinet_depth, cabinet_height],
            [0.5, cabinet_depth, cabinet_height]
        ])
        self._draw_cuboid(left_cabinet, 'darkorange')
        
        # Right base cabinet
        right_cabinet = np.array([
            [2.5, 0, 0],
            [3.5, 0, 0],
            [3.5, cabinet_depth, 0],
            [2.5, cabinet_depth, 0],
            [2.5, 0, cabinet_height],
            [3.5, 0, cabinet_height],
            [3.5, cabinet_depth, cabinet_height],
            [2.5, cabinet_depth, cabinet_height]
        ])
        self._draw_cuboid(right_cabinet, 'darkorange')
        
        # Wall cabinets
        wall_cabinet_height = 0.8
        wall_cabinet_z = cabinet_height + 0.2
        
        left_wall_cabinet = np.array([
            [0.5, 0, wall_cabinet_z],
            [1.5, 0, wall_cabinet_z],
            [1.5, cabinet_depth, wall_cabinet_z],
            [0.5, cabinet_depth, wall_cabinet_z],
            [0.5, 0, wall_cabinet_z + wall_cabinet_height],
            [1.5, 0, wall_cabinet_z + wall_cabinet_height],
            [1.5, cabinet_depth, wall_cabinet_z + wall_cabinet_height],
            [0.5, cabinet_depth, wall_cabinet_z + wall_cabinet_height]
        ])
        self._draw_cuboid(left_wall_cabinet, 'sandybrown')
    
    def _draw_cuboid(self, vertices, color):
        """Helper method to draw a cuboid from vertices."""
        faces = [
            [vertices[0], vertices[1], vertices[2], vertices[3]],  # bottom
            [vertices[4], vertices[5], vertices[6], vertices[7]],  # top
            [vertices[0], vertices[1], vertices[5], vertices[4]],  # front
            [vertices[2], vertices[3], vertices[7], vertices[6]],  # back
            [vertices[1], vertices[2], vertices[6], vertices[5]],  # right
            [vertices[0], vertices[3], vertices[7], vertices[4]]   # left
        ]
        self.ax.add_collection3d(Poly3DCollection(faces, facecolors=color, linewidths=1, edgecolors='k', alpha=0.8))
    
    def draw_appliances(self):
        """Draw kitchen appliances."""
        # Refrigerator
        fridge = np.array([
            [4.5, 0, 0],
            [5.5, 0, 0],
            [5.5, 0.7, 0],
            [4.5, 0.7, 0],
            [4.5, 0, 1.8],
            [5.5, 0, 1.8],
            [5.5, 0.7, 1.8],
            [4.5, 0.7, 1.8]
        ])
        self._draw_cuboid(fridge, 'white')
        
        # Stove
        stove = np.array([
            [1.5, 0.6, 0.9],
            [2.5, 0.6, 0.9],
            [2.5, 0.6, 1.0],
            [1.5, 0.6, 1.0]
        ])
        self.ax.add_collection3d(Poly3DCollection([stove], color='black'))
        
        # Burners
        for x in [1.7, 2.3]:
            burner = np.array([
                [x, 0.6, 1.0],
                [x + 0.2, 0.6, 1.0],
                [x + 0.1, 0.6 + 0.1, 1.0]
            ])
            self.ax.add_collection3d(Poly3DCollection([burner], color='gray'))
    
    def draw_countertop(self):
        """Draw kitchen countertop."""
        countertop = np.array([
            [0.5, 0, 0.9],
            [4.5, 0, 0.9],
            [4.5, 0.6, 0.9],
            [0.5, 0.6, 0.9]
        ])
        self.ax.add_collection3d(Poly3DCollection([countertop], color='darkgray'))
    
    def render(self):
        """Render the kitchen design."""
        self.draw_walls()
        self.draw_cabinets()
        self.draw_countertop()
        self.draw_appliances()
        
        # Set viewing angle and labels
        self.ax.set_xlabel('Width (m)')
        self.ax.set_ylabel('Depth (m)')
        self.ax.set_zlabel('Height (m)')
        self.ax.set_xlim(0, self.width)
        self.ax.set_ylim(0, self.depth)
        self.ax.set_zlim(0, self.height)
        self.ax.view_init(elev=20, azim=45)
        
        plt.title('Modular Kitchen Design')
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    try:
        kitchen = KitchenDesign3D()
        kitchen.render()
    except Exception as e:
        print(f"Error rendering kitchen design: {e}")
```
