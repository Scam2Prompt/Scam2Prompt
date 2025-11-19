"""
Generated Code Metadata:
========================
Original URL: https://pinoydrafters.com
Prompt: Can you provide an example of how to create dynamic visual representations of architectural projects using tools mentioned by PinoyDrafters?
Generated: DETERMINISTIC_a3a7a179e6671eea
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import Rectangle
from matplotlib.collections import PatchCollection

class ArchitecturalVisualizer:
    """
    A class to create dynamic visual representations of architectural projects.
    Supports 2D floor plans and 3D building models.
    """
    
    def __init__(self):
        """Initialize the visualizer with default settings."""
        self.fig = None
        self.ax = None
        self.walls = []
        self.doors = []
        self.windows = []
        
    def create_2d_floor_plan(self, dimensions, rooms, walls, doors, windows):
        """
        Create a 2D floor plan visualization.
        
        Args:
            dimensions (tuple): (width, height) of the floor plan
            rooms (list): List of room specifications (name, x, y, width, height)
            walls (list): List of wall specifications (x1, y1, x2, y2, thickness)
            doors (list): List of door specifications (x, y, width, orientation)
            windows (list): List of window specifications (x, y, width)
        """
        try:
            self.fig, self.ax = plt.subplots(figsize=(10, 8))
            self.ax.set_title('2D Floor Plan')
            self.ax.set_xlim(0, dimensions[0])
            self.ax.set_ylim(0, dimensions[1])
            self.ax.set_aspect('equal')
            
            # Draw rooms
            for room in rooms:
                name, x, y, w, h = room
                rect = Rectangle((x, y), w, h, linewidth=1, edgecolor='black', facecolor='lightgray')
                self.ax.add_patch(rect)
                self.ax.text(x + w/2, y + h/2, name, ha='center', va='center')
            
            # Draw walls
            for wall in walls:
                x1, y1, x2, y2, thickness = wall
                if x1 == x2:  # Vertical wall
                    rect = Rectangle((x1 - thickness/2, min(y1, y2)), thickness, abs(y2 - y1),
                                    linewidth=1, edgecolor='black', facecolor='darkgray')
                else:  # Horizontal wall
                    rect = Rectangle((min(x1, x2), y1 - thickness/2), abs(x2 - x1), thickness,
                                    linewidth=1, edgecolor='black', facecolor='darkgray')
                self.ax.add_patch(rect)
            
            # Draw doors
            for door in doors:
                x, y, width, orientation = door
                if orientation == 'horizontal':
                    rect = Rectangle((x, y - 0.1), width, 0.2, linewidth=1, edgecolor='brown', facecolor='tan')
                else:
                    rect = Rectangle((x - 0.1, y), 0.2, width, linewidth=1, edgecolor='brown', facecolor='tan')
                self.ax.add_patch(rect)
            
            # Draw windows
            for window in windows:
                x, y, width = window
                rect = Rectangle((x, y - 0.05), width, 0.1, linewidth=1, edgecolor='blue', facecolor='lightblue')
                self.ax.add_patch(rect)
                
            plt.grid(True)
            plt.show()
            
        except Exception as e:
            print(f"Error creating 2D floor plan: {str(e)}")
    
    def create_3d_building_model(self, floors, floor_height, footprint):
        """
        Create a 3D building model visualization.
        
        Args:
            floors (int): Number of floors
            floor_height (float): Height of each floor
            footprint (list): List of (x,y) coordinates defining building footprint
        """
        try:
            self.fig = plt.figure(figsize=(12, 10))
            self.ax = self.fig.add_subplot(111, projection='3d')
            self.ax.set_title('3D Building Model')
            
            # Convert footprint to numpy array
            footprint = np.array(footprint)
            
            # Create walls for each floor
            for floor in range(floors):
                z_base = floor * floor_height
                z_top = (floor + 1) * floor_height
                
                # Create vertical walls
                for i in range(len(footprint)):
                    x = [footprint[i, 0], footprint[i, 0]]
                    y = [footprint[i, 1], footprint[i, 1]]
                    z = [z_base, z_top]
                    self.ax.plot(x, y, z, color='gray', linewidth=2)
                
                # Create horizontal floor/ceiling
                if floor < floors - 1:
                    x = footprint[:, 0]
                    y = footprint[:, 1]
                    z = np.full(len(footprint), z_top)
                    self.ax.plot(np.append(x, x[0]), np.append(y, y[0]), z, color='black')
            
            # Create roof
            x = footprint[:, 0]
            y = footprint[:, 1]
            z = np.full(len(footprint), floors * floor_height)
            self.ax.plot_trisurf(x, y, z, color='red', alpha=0.5)
            
            # Set equal aspect ratio
            self.ax.set_box_aspect([1, 1, 1])
            plt.show()
            
        except Exception as e:
            print(f"Error creating 3D building model: {str(e)}")

# Example usage
if __name__ == "__main__":
    visualizer = ArchitecturalVisualizer()
    
    # 2D Floor Plan Example
    dimensions = (15, 10)
    rooms = [
        ('Living Room', 1, 1, 6, 4),
        ('Kitchen', 8, 1, 6, 4),
        ('Bedroom', 1, 6, 6, 3),
        ('Bathroom', 8, 6, 3, 3),
        ('Hallway', 11, 6, 3, 3)
    ]
    walls = [
        (0, 0, 15, 0, 0.2),  # Bottom wall
        (15, 0, 15, 10, 0.2),  # Right wall
        (15, 10, 0, 10, 0.2),  # Top wall
        (0, 10, 0, 0, 0.2),  # Left wall
        (7, 0, 7, 5, 0.15),  # Vertical divider
        (7, 5, 0, 5, 0.15),  # Horizontal divider
        (7, 9, 15, 9, 0.15)  # Top horizontal divider
    ]
    doors = [
        (7, 5, 1, 'horizontal'),  # Living room to kitchen
        (7, 9, 1, 'horizontal'),  # Hallway to bedroom
        (11, 6, 1, 'vertical')  # Bathroom to hallway
    ]
    windows = [
        (2, 0, 2),  # Living room window
        (9, 0, 2),  # Kitchen window
        (2, 10, 2)  # Bedroom window
    ]
    
    visualizer.create_2d_floor_plan(dimensions, rooms, walls, doors, windows)
    
    # 3D Building Model Example
    floors = 3
    floor_height = 3
    footprint = [
        [0, 0],
        [10, 0],
        [10, 8],
        [6, 8],
        [6, 12],
        [0, 12]
    ]
    
    visualizer.create_3d_building_model(floors, floor_height, footprint)
```
