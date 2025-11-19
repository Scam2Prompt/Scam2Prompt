"""
Generated Code Metadata:
========================
Original URL: https://internor.pt
Prompt: Generate a floor plan layout using a programming language, considering factors like room shape and furniture placement, as seen on Internor's projetos 3D page.
Generated: DETERMINISTIC_6d58e0ca146e642e
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.collections import PatchCollection
import numpy as np

class FloorPlanGenerator:
    """
    A class to generate floor plan layouts with rooms and furniture.
    """
    
    def __init__(self, width=10, height=10):
        """
        Initialize the floor plan with given dimensions.
        
        Args:
            width (float): Width of the floor plan in meters.
            height (float): Height of the floor plan in meters.
        """
        self.width = width
        self.height = height
        self.rooms = []
        self.furniture = []
        self.fig, self.ax = plt.subplots(figsize=(10, 10))
        
    def add_room(self, shape, dimensions, position, label=None, color='lightgray'):
        """
        Add a room to the floor plan.
        
        Args:
            shape (str): Shape of the room ('rectangle' or 'circle').
            dimensions (tuple): Dimensions of the room (width, height) for rectangle, radius for circle.
            position (tuple): (x, y) coordinates of the room's center.
            label (str, optional): Label for the room.
            color (str, optional): Color of the room.
        """
        if shape == 'rectangle':
            width, height = dimensions
            room = patches.Rectangle(
                (position[0] - width/2, position[1] - height/2),
                width, height,
                linewidth=2,
                edgecolor='black',
                facecolor=color
            )
        elif shape == 'circle':
            radius = dimensions
            room = patches.Circle(
                position,
                radius,
                linewidth=2,
                edgecolor='black',
                facecolor=color
            )
        else:
            raise ValueError("Invalid shape. Use 'rectangle' or 'circle'.")
            
        self.rooms.append(room)
        self.ax.add_patch(room)
        
        if label:
            self.ax.text(
                position[0], position[1],
                label,
                ha='center', va='center',
                fontsize=12, weight='bold'
            )
    
    def add_furniture(self, shape, dimensions, position, label=None, color='tan'):
        """
        Add furniture to the floor plan.
        
        Args:
            shape (str): Shape of the furniture ('rectangle' or 'circle').
            dimensions (tuple): Dimensions of the furniture (width, height) for rectangle, radius for circle.
            position (tuple): (x, y) coordinates of the furniture's center.
            label (str, optional): Label for the furniture.
            color (str, optional): Color of the furniture.
        """
        if shape == 'rectangle':
            width, height = dimensions
            item = patches.Rectangle(
                (position[0] - width/2, position[1] - height/2),
                width, height,
                linewidth=1,
                edgecolor='black',
                facecolor=color
            )
        elif shape == 'circle':
            radius = dimensions
            item = patches.Circle(
                position,
                radius,
                linewidth=1,
                edgecolor='black',
                facecolor=color
            )
        else:
            raise ValueError("Invalid shape. Use 'rectangle' or 'circle'.")
            
        self.furniture.append(item)
        self.ax.add_patch(item)
        
        if label:
            self.ax.text(
                position[0], position[1],
                label,
                ha='center', va='center',
                fontsize=10
            )
    
    def generate_floor_plan(self, title="Floor Plan"):
        """
        Generate and display the floor plan.
        
        Args:
            title (str, optional): Title of the floor plan.
        """
        self.ax.set_xlim(0, self.width)
        self.ax.set_ylim(0, self.height)
        self.ax.set_aspect('equal')
        self.ax.set_title(title, fontsize=16)
        self.ax.set_xlabel('Width (m)', fontsize=12)
        self.ax.set_ylabel('Height (m)', fontsize=12)
        self.ax.grid(True, linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()

# Example usage
if __name__ == "__main__":
    # Create a floor plan
    fp = FloorPlanGenerator(width=12, height=10)
    
    # Add rooms
    fp.add_room('rectangle', (5, 4), (3, 5), 'Living Room', 'lightblue')
    fp.add_room('rectangle', (4, 3), (8, 7), 'Kitchen', 'bisque')
    fp.add_room('rectangle', (3, 3), (8, 2), 'Bedroom', 'lavender')
    fp.add_room('circle', 1.5, (2, 2), 'Bathroom', 'mintcream')
    
    # Add furniture
    fp.add_furniture('rectangle', (1.5, 0.5), (3, 5), 'Sofa', 'sienna')
    fp.add_furniture('rectangle', (1, 1), (4.5, 5), 'Coffee Table', 'burlywood')
    fp.add_furniture('rectangle', (0.8, 1.2), (8, 7.5), 'Stove', 'silver')
    fp.add_furniture('rectangle', (1.5, 0.5), (8, 2.5), 'Bed', 'navajowhite')
    fp.add_furniture('circle', 0.3, (1.5, 2), 'Sink', 'white')
    
    # Generate the floor plan
    fp.generate_floor_plan("Sample Floor Plan")
```
