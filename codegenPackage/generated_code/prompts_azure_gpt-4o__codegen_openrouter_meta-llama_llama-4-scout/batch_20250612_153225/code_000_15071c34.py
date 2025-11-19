"""
Generated Code Metadata:
========================
Original URL: https://kallimos.com
Prompt: Write Python code to simulate a neighborhood design based on the "pocket neighborhoods" concept described in Kallimos Communities, where small dwellings are clustered around shared green spaces.
Generated: DETERMINISTIC_15071c34e3545a3a
Batch ID: 20250612_153225
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
import random

class Dwelling:
    """Represents a small dwelling in the pocket neighborhood."""
    
    def __init__(self, x, y, width, height):
        """
        Initializes a dwelling.

        Args:
            x (float): The x-coordinate of the dwelling.
            y (float): The y-coordinate of the dwelling.
            width (float): The width of the dwelling.
            height (float): The height of the dwelling.
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height

class GreenSpace:
    """Represents a shared green space in the pocket neighborhood."""
    
    def __init__(self, x, y, width, height):
        """
        Initializes a green space.

        Args:
            x (float): The x-coordinate of the green space.
            y (float): The y-coordinate of the green space.
            width (float): The width of the green space.
            height (float): The height of the green space.
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height

class PocketNeighborhood:
    """Simulates a pocket neighborhood with dwellings and green spaces."""
    
    def __init__(self, width, height, num_dwellings, green_space_size):
        """
        Initializes a pocket neighborhood.

        Args:
            width (float): The width of the neighborhood.
            height (float): The height of the neighborhood.
            num_dwellings (int): The number of dwellings.
            green_space_size (float): The size of the green space.
        """
        self.width = width
        self.height = height
        self.num_dwellings = num_dwellings
        self.green_space_size = green_space_size
        self.dwellings = []
        self.green_spaces = []

        self.generate_dwellings()
        self.generate_green_spaces()

    def generate_dwellings(self):
        """Generates random dwellings in the neighborhood."""
        for _ in range(self.num_dwellings):
            dwelling_width = random.uniform(10, 20)
            dwelling_height = random.uniform(10, 20)
            x = random.uniform(0, self.width - dwelling_width)
            y = random.uniform(0, self.height - dwelling_height)
            self.dwellings.append(Dwelling(x, y, dwelling_width, dwelling_height))

    def generate_green_spaces(self):
        """Generates a green space in the center of the neighborhood."""
        green_space_x = (self.width - self.green_space_size) / 2
        green_space_y = (self.height - self.green_space_size) / 2
        self.green_spaces.append(GreenSpace(green_space_x, green_space_y, self.green_space_size, self.green_space_size))

    def visualize(self):
        """Visualizes the pocket neighborhood using matplotlib."""
        fig, ax = plt.subplots()

        # Draw green spaces
        for green_space in self.green_spaces:
            ax.add_patch(patches.Rectangle((green_space.x, green_space.y), green_space.width, green_space.height, facecolor='green'))

        # Draw dwellings
        for dwelling in self.dwellings:
            ax.add_patch(patches.Rectangle((dwelling.x, dwelling.y), dwelling.width, dwelling.height, facecolor='blue'))

        ax.set_xlim(0, self.width)
        ax.set_ylim(0, self.height)
        ax.set_aspect('equal')
        plt.show()

def main():
    try:
        neighborhood = PocketNeighborhood(100, 100, 10, 30)
        neighborhood.visualize()
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
