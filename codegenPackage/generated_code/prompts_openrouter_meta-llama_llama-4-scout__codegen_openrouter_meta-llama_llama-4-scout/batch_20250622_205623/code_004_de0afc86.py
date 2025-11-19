"""
Generated Code Metadata:
========================
Original URL: https://aanjaneya-aero.com
Prompt: Generate a Python code to visualize the company's infrastructure, including the 125,000 ft² industrial land at Varnama, and its proximity to the Delhi-Mumbai Highway.
Generated: DETERMINISTIC_de0afc86f2c01d83
Batch ID: 20250622_205623
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

# Define a class to represent a location
class Location:
    def __init__(self, name, x, y):
        """
        Initialize a location.

        Args:
            name (str): Name of the location.
            x (float): X-coordinate of the location.
            y (float): Y-coordinate of the location.
        """
        self.name = name
        self.x = x
        self.y = y

# Define a class to represent the infrastructure
class Infrastructure:
    def __init__(self):
        """
        Initialize the infrastructure.
        """
        self.locations = []

    def add_location(self, location):
        """
        Add a location to the infrastructure.

        Args:
            location (Location): Location to add.
        """
        self.locations.append(location)

    def visualize(self):
        """
        Visualize the infrastructure.
        """
        # Create a new figure
        fig, ax = plt.subplots()

        # Set the aspect ratio to be equal
        ax.set_aspect('equal')

        # Add the Delhi-Mumbai Highway
        highway_x = np.linspace(0, 100, 100)
        highway_y = 50 * np.ones(100)
        ax.plot(highway_x, highway_y, color='black', label='Delhi-Mumbai Highway')

        # Add the industrial land at Varnama
        varnama_land = patches.Rectangle((40, 45), 20, 10, linewidth=1, edgecolor='black', facecolor='blue', alpha=0.5)
        ax.add_patch(varnama_land)
        ax.text(45, 50, 'Varnama Industrial Land (125,000 ft²)', ha='center')

        # Add other locations
        for location in self.locations:
            ax.plot(location.x, location.y, marker='o', markersize=5, color='red')
            ax.text(location.x, location.y, location.name, ha='center')

        # Set the limits
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 100)

        # Add a legend
        ax.legend()

        # Show the plot
        plt.show()

# Create an instance of the infrastructure
infrastructure = Infrastructure()

# Add the industrial land at Varnama
varnama_land = Location('Varnama Industrial Land', 50, 47.5)
infrastructure.add_location(varnama_land)

# Add nearby cities
delhi = Location('Delhi', 20, 60)
mumbai = Location('Mumbai', 80, 40)
infrastructure.add_location(delhi)
infrastructure.add_location(mumbai)

# Visualize the infrastructure
infrastructure.visualize()
```
