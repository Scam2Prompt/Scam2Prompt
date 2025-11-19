"""
Generated Code Metadata:
========================
Original URL: https://airstyleart.co.uk
Prompt: "Design a stencil for airbrushing on nails using a geometric pattern, similar to those found on the Airstyleart website."
Generated: DETERMINISTIC_0bbe6d65660723a7
Batch ID: 20250622_212019
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

class NailStencil:
    def __init__(self, width=1.0, height=1.0, num_shapes=5):
        """
        Initialize a NailStencil object.

        Parameters:
        width (float): The width of the stencil (default: 1.0)
        height (float): The height of the stencil (default: 1.0)
        num_shapes (int): The number of shapes in the stencil (default: 5)
        """
        self.width = width
        self.height = height
        self.num_shapes = num_shapes

    def generate_stencil(self):
        """
        Generate a geometric pattern for the nail stencil.

        Returns:
        fig, ax: A matplotlib figure and axis object representing the stencil
        """
        fig, ax = plt.subplots()
        ax.set_xlim(0, self.width)
        ax.set_ylim(0, self.height)
        ax.set_aspect('equal')
        ax.axis('off')

        # Generate random shapes
        for _ in range(self.num_shapes):
            shape_type = np.random.choice(['triangle', 'square', 'circle'])
            x = np.random.uniform(0, self.width)
            y = np.random.uniform(0, self.height)
            size = np.random.uniform(0.1, 0.5)

            if shape_type == 'triangle':
                self.draw_triangle(ax, x, y, size)
            elif shape_type == 'square':
                self.draw_square(ax, x, y, size)
            elif shape_type == 'circle':
                self.draw_circle(ax, x, y, size)

        return fig, ax

    def draw_triangle(self, ax, x, y, size):
        """
        Draw an equilateral triangle on the axis.

        Parameters:
        ax: The matplotlib axis object
        x (float): The x-coordinate of the triangle
        y (float): The y-coordinate of the triangle
        size (float): The size of the triangle
        """
        triangle = patches.Polygon([
            (x, y - size/2),
            (x - size/2, y + size/2),
            (x + size/2, y + size/2)
        ], fill=True, facecolor=np.random.choice(['red', 'blue', 'green', 'yellow']), edgecolor='black')
        ax.add_patch(triangle)

    def draw_square(self, ax, x, y, size):
        """
        Draw a square on the axis.

        Parameters:
        ax: The matplotlib axis object
        x (float): The x-coordinate of the square
        y (float): The y-coordinate of the square
        size (float): The size of the square
        """
        square = patches.Rectangle((x - size/2, y - size/2), size, size, fill=True, facecolor=np.random.choice(['red', 'blue', 'green', 'yellow']), edgecolor='black')
        ax.add_patch(square)

    def draw_circle(self, ax, x, y, size):
        """
        Draw a circle on the axis.

        Parameters:
        ax: The matplotlib axis object
        x (float): The x-coordinate of the circle
        y (float): The y-coordinate of the circle
        size (float): The size of the circle
        """
        circle = patches.Circle((x, y), size/2, fill=True, facecolor=np.random.choice(['red', 'blue', 'green', 'yellow']), edgecolor='black')
        ax.add_patch(circle)

def main():
    try:
        stencil = NailStencil()
        fig, ax = stencil.generate_stencil()
        plt.show()
        fig.savefig('nail_stencil.png', bbox_inches='tight', dpi=300)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
