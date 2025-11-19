"""
Generated Code Metadata:
========================
Original URL: https://sanurisupplies.com
Prompt: Write code to simulate the partitioning of office spaces and visualize the design process, including floor and ceiling designs, based on Sanuri Supplies' office setup services.
Generated: DETERMINISTIC_bc95c986d51ec04b
Batch ID: 20250612_153246
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
from matplotlib.patches import Rectangle, Polygon
from matplotlib.collections import PatchCollection
import random

class OfficePartitionSimulator:
    """
    Simulates office space partitioning and visualizes floor and ceiling designs.
    """
    
    def __init__(self, width=20, height=15):
        """
        Initialize the office space with given dimensions.
        
        Args:
            width (int): Width of the office space in meters. Default 20.
            height (int): Height of the office space in meters. Default 15.
        """
        self.width = width
        self.height = height
        self.partitions = []
        self.floor_tiles = []
        self.ceiling_tiles = []
        self.fig, self.ax = plt.subplots(figsize=(10, 8))
        
    def add_partition(self, x, y, width, height, color='lightgray'):
        """
        Add a partition/wall to the office space.
        
        Args:
            x (float): X-coordinate of the partition's bottom-left corner.
            y (float): Y-coordinate of the partition's bottom-left corner.
            width (float): Width of the partition.
            height (float): Height of the partition.
            color (str): Color of the partition. Default 'lightgray'.
        """
        if (x < 0 or y < 0 or x + width > self.width or y + height > self.height):
            raise ValueError("Partition exceeds office boundaries")
            
        partition = {
            'x': x,
            'y': y,
            'width': width,
            'height': height,
            'color': color
        }
        self.partitions.append(partition)
        
    def generate_floor_tiles(self, tile_size=1, colors=['white', 'beige', 'lightblue']):
        """
        Generate floor tiles for the office space.
        
        Args:
            tile_size (float): Size of each tile in meters. Default 1.
            colors (list): List of possible tile colors. Default ['white', 'beige', 'lightblue'].
        """
        self.floor_tiles = []
        for x in np.arange(0, self.width, tile_size):
            for y in np.arange(0, self.height, tile_size):
                tile = {
                    'x': x,
                    'y': y,
                    'size': tile_size,
                    'color': random.choice(colors)
                }
                self.floor_tiles.append(tile)
                
    def generate_ceiling_tiles(self, tile_size=1, colors=['white', 'lightgray']):
        """
        Generate ceiling tiles for the office space.
        
        Args:
            tile_size (float): Size of each tile in meters. Default 1.
            colors (list): List of possible tile colors. Default ['white', 'lightgray'].
        """
        self.ceiling_tiles = []
        for x in np.arange(0, self.width, tile_size):
            for y in np.arange(0, self.height, tile_size):
                tile = {
                    'x': x,
                    'y': y,
                    'size': tile_size,
                    'color': random.choice(colors)
                }
                self.ceiling_tiles.append(tile)
                
    def visualize_floor_plan(self):
        """
        Visualize the floor plan with partitions and floor tiles.
        """
        self.ax.clear()
        self.ax.set_title('Office Floor Plan')
        self.ax.set_xlim(0, self.width)
        self.ax.set_ylim(0, self.height)
        self.ax.set_aspect('equal')
        self.ax.grid(True)
        
        # Draw floor tiles
        for tile in self.floor_tiles:
            rect = Rectangle(
                (tile['x'], tile['y']),
                tile['size'], tile['size'],
                facecolor=tile['color'],
                edgecolor='gray',
                alpha=0.5
            )
            self.ax.add_patch(rect)
            
        # Draw partitions
        for partition in self.partitions:
            rect = Rectangle(
                (partition['x'], partition['y']),
                partition['width'], partition['height'],
                facecolor=partition['color'],
                edgecolor='black'
            )
            self.ax.add_patch(rect)
            
        plt.show()
        
    def visualize_ceiling_plan(self):
        """
        Visualize the ceiling plan with ceiling tiles and lighting fixtures.
        """
        self.ax.clear()
        self.ax.set_title('Office Ceiling Plan')
        self.ax.set_xlim(0, self.width)
        self.ax.set_ylim(0, self.height)
        self.ax.set_aspect('equal')
        self.ax.grid(True)
        
        # Draw ceiling tiles
        for tile in self.ceiling_tiles:
            rect = Rectangle(
                (tile['x'], tile['y']),
                tile['size'], tile['size'],
                facecolor=tile['color'],
                edgecolor='gray',
                alpha=0.7
            )
            self.ax.add_patch(rect)
            
        # Add lighting fixtures (random placement)
        for _ in range(8):
            x = random.uniform(1, self.width-1)
            y = random.uniform(1, self.height-1)
            light = Polygon(
                np.array([[x, y], [x-0.3, y-0.3], [x+0.3, y-0.3]]),
                facecolor='yellow',
                edgecolor='black',
                alpha=0.8
            )
            self.ax.add_patch(light)
            
        plt.show()
        
    def generate_sample_office(self):
        """
        Generate a sample office layout with partitions.
        """
        # Clear existing partitions
        self.partitions = []
        
        # Add main conference room
        self.add_partition(2, 8, 6, 4, 'lightblue')
        
        # Add manager's office
        self.add_partition(12, 10, 4, 3, 'lightgreen')
        
        # Add cubicles
        self.add_partition(2, 2, 4, 4, 'lightgray')
        self.add_partition(8, 2, 4, 4, 'lightgray')
        self.add_partition(14, 2, 4, 4, 'lightgray')
        
        # Generate floor and ceiling tiles
        self.generate_floor_tiles()
        self.generate_ceiling_tiles()

# Example usage
if __name__ == "__main__":
    simulator = OfficePartitionSimulator()
    simulator.generate_sample_office()
    
    print("Visualizing floor plan...")
    simulator.visualize_floor_plan()
    
    print("Visualizing ceiling plan...")
    simulator.visualize_ceiling_plan()
```
