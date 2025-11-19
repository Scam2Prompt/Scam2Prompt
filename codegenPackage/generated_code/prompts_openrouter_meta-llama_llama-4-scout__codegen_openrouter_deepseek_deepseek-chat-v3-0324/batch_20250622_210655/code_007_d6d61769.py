"""
Generated Code Metadata:
========================
Original URL: https://superdar.com
Prompt: Design a decorative table with a unique shape, such as an ellipse or a circle, using solid wood, inspired by the tables on the Мебели Амотем website.
Generated: DETERMINISTIC_d6d61769588fc622
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import Ellipse
from matplotlib import cm

class DecorativeTable:
    """
    A class to design and visualize a decorative elliptical table inspired by Мебели Амотем.
    """
    
    def __init__(self, major_axis=120, minor_axis=80, height=75, thickness=3, resolution=100):
        """
        Initialize table parameters.
        
        Args:
            major_axis (float): Major axis of the elliptical table top in cm
            minor_axis (float): Minor axis of the elliptical table top in cm
            height (float): Table height in cm
            thickness (float): Table top thickness in cm
            resolution (int): Number of points for smoothness of curves
        """
        self.major_axis = major_axis
        self.minor_axis = minor_axis
        self.height = height
        self.thickness = thickness
        self.resolution = resolution
        
        # Validate inputs
        if any(dim <= 0 for dim in [major_axis, minor_axis, height, thickness]):
            raise ValueError("All dimensions must be positive numbers")
        if resolution < 20:
            raise ValueError("Resolution must be at least 20 for smooth rendering")
    
    def generate_table_top(self):
        """Generate points for the elliptical table top."""
        theta = np.linspace(0, 2*np.pi, self.resolution)
        x = (self.major_axis/2) * np.cos(theta)
        y = (self.minor_axis/2) * np.sin(theta)
        return x, y
    
    def generate_legs(self):
        """Generate positions for four legs in an elliptical pattern."""
        angles = np.linspace(0, 2*np.pi, 5)[:-1]  # Four legs at 0, 90, 180, 270 degrees
        leg_positions = []
        
        for angle in angles:
            x = (self.major_axis/2.5) * math.cos(angle)
            y = (self.minor_axis/2.5) * math.sin(angle)
            leg_positions.append((x, y))
            
        return leg_positions
    
    def visualize_2d(self):
        """Create a 2D visualization of the table."""
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Draw table top
        x, y = self.generate_table_top()
        ax.plot(x, y, 'b-', linewidth=2, label='Table Top')
        
        # Draw legs
        leg_positions = self.generate_legs()
        for (lx, ly) in leg_positions:
            ax.plot([lx, lx], [ly, ly - self.height], 'k-', linewidth=3, label='Legs' if lx == leg_positions[0][0] else "")
        
        # Draw table edge
        ax.plot(x, y, 'b-', linewidth=2)
        
        ax.set_aspect('equal')
        ax.set_title('Elliptical Table Design (Top View)')
        ax.set_xlabel('Width (cm)')
        ax.set_ylabel('Depth (cm)')
        ax.legend()
        ax.grid(True)
        plt.show()
    
    def visualize_3d(self):
        """Create a 3D visualization of the table."""
        fig = plt.figure(figsize=(12, 8))
        ax = fig.add_subplot(111, projection='3d')
        
        # Generate table top surface
        theta = np.linspace(0, 2*np.pi, self.resolution)
        r = np.linspace(0, 1, self.resolution//2)
        theta_grid, r_grid = np.meshgrid(theta, r)
        
        x = (self.major_axis/2 * r_grid) * np.cos(theta_grid)
        y = (self.minor_axis/2 * r_grid) * np.sin(theta_grid)
        z = np.zeros_like(x) + self.height
        
        # Plot table top
        ax.plot_surface(x, y, z, color='peru', alpha=0.8)
        
        # Plot table edge
        x_edge, y_edge = self.generate_table_top()
        z_edge = np.full_like(x_edge, self.height)
        ax.plot(x_edge, y_edge, z_edge, 'k-', linewidth=2)
        
        # Plot legs
        leg_positions = self.generate_legs()
        for (lx, ly) in leg_positions:
            ax.plot([lx, lx], [ly, ly], [self.height, 0], 'k-', linewidth=5)
        
        ax.set_title('3D View of Elliptical Table')
        ax.set_xlabel('Width (cm)')
        ax.set_ylabel('Depth (cm)')
        ax.set_zlabel('Height (cm)')
        ax.set_box_aspect([self.major_axis, self.minor_axis, self.height])
        plt.show()

# Example usage
if __name__ == "__main__":
    try:
        table = DecorativeTable(major_axis=140, minor_axis=90, height=75)
        table.visualize_2d()
        table.visualize_3d()
    except ValueError as e:
        print(f"Error creating table: {e}")
```
