"""
Generated Code Metadata:
========================
Original URL: https://evlworld.com
Prompt: Generate a Python script that utilizes the principles of 3D graffiti art as described on Erni Vales' website to create a digital representation of a street art piece.
Generated: DETERMINISTIC_37db7533ff802548
Batch ID: 20250612_161035
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
from matplotlib.patches import Rectangle
from matplotlib.collections import PatchCollection
import random
import colorsys

class Graffiti3DArt:
    """
    A class to generate 3D graffiti art inspired by Erni Vales' style.
    """
    
    def __init__(self, num_layers=5, canvas_size=10):
        """
        Initialize the graffiti art parameters.
        
        Args:
            num_layers (int): Number of 3D layers in the artwork
            canvas_size (int): Size of the canvas (square)
        """
        self.num_layers = num_layers
        self.canvas_size = canvas_size
        self.fig = plt.figure(figsize=(10, 10))
        self.ax = self.fig.add_subplot(111, projection='3d')
        
    def generate_colors(self, n):
        """Generate vibrant colors for the graffiti."""
        colors = []
        for i in range(n):
            hue = i / float(n)
            saturation = 0.7 + random.random() * 0.3
            value = 0.5 + random.random() * 0.5
            rgb = colorsys.hsv_to_rgb(hue, saturation, value)
            colors.append(rgb)
        return colors
    
    def create_letter(self, position, size, angle, layer, color):
        """
        Create a stylized 3D letter for the graffiti.
        
        Args:
            position (tuple): (x,y) position of the letter
            size (float): Size of the letter
            angle (float): Rotation angle in degrees
            layer (int): Layer depth
            color (tuple): RGB color
        """
        x, y = position
        z = layer * 0.5
        
        # Create letter shape (simplified as rectangles)
        patches = []
        
        # Main vertical stroke
        patches.append(Rectangle((x, y), size*0.2, size, angle=angle))
        
        # Horizontal strokes
        patches.append(Rectangle((x, y), size*0.8, size*0.2, angle=angle))
        patches.append(Rectangle((x, y+size*0.8), size*0.8, size*0.2, angle=angle))
        
        # Diagonal stroke
        patches.append(Rectangle((x+size*0.6, y), size*0.2, size*0.6, angle=angle+45))
        
        # Convert to 3D
        collection = PatchCollection(patches, alpha=0.8, color=color)
        self.ax.add_collection3d(collection, zs=z, zdir='z')
        
    def create_tag(self, position, size, layer, colors):
        """
        Create a graffiti tag with multiple letters.
        
        Args:
            position (tuple): Starting (x,y) position
            size (float): Base size of letters
            layer (int): Layer depth
            colors (list): List of RGB colors
        """
        x, y = position
        letters = ['G', 'R', 'A', 'F', 'F', 'I', 'T', 'I']
        
        for i, letter in enumerate(letters):
            self.create_letter(
                position=(x + i * size * 0.8, y),
                size=size * (0.9 + random.random() * 0.2),
                angle=random.uniform(-15, 15),
                layer=layer,
                color=colors[i % len(colors)]
            )
    
    def add_spray_effect(self, num_dots=500):
        """Add spray paint effect around the artwork."""
        for _ in range(num_dots):
            x = random.uniform(0, self.canvas_size)
            y = random.uniform(0, self.canvas_size)
            z = random.uniform(0, self.num_layers * 0.5)
            size = random.uniform(0.05, 0.2)
            color = (random.random(), random.random(), random.random(), 0.3)
            self.ax.scatter(x, y, z, s=size*100, c=[color], marker='o')
    
    def generate_artwork(self):
        """Generate the complete 3D graffiti artwork."""
        colors = self.generate_colors(8)
        
        # Create multiple layers of tags
        for layer in range(self.num_layers):
            # Main tag
            self.create_tag(
                position=(2 + random.random(), 2 + random.random()),
                size=1.5 - layer * 0.1,
                layer=layer,
                colors=colors
            )
            
            # Additional smaller tags
            for _ in range(2):
                self.create_tag(
                    position=(
                        random.uniform(0, self.canvas_size - 3),
                        random.uniform(0, self.canvas_size - 3)
                    ),
                    size=0.8 - layer * 0.05,
                    layer=layer,
                    colors=colors
                )
        
        # Add spray effects
        self.add_spray_effect()
        
        # Set view and style
        self.ax.set_xlim(0, self.canvas_size)
        self.ax.set_ylim(0, self.canvas_size)
        self.ax.set_zlim(0, self.num_layers * 0.5)
        self.ax.set_axis_off()
        self.ax.view_init(elev=20, azim=-60)
        
        # Add title
        plt.title("3D Graffiti Art", pad=20, fontsize=16, fontweight='bold')
        
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    try:
        art = Graffiti3DArt(num_layers=5, canvas_size=10)
        art.generate_artwork()
    except Exception as e:
        print(f"Error generating artwork: {e}")
```
