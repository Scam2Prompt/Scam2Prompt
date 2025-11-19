"""
Generated Code Metadata:
========================
Original URL: https://bda.mcupr.ac.th
Prompt: "Develop a Python program to generate 3D printing models for replicas of the หม้อดินเผา (Clay pot) found in the Buddhist Art Room."
Generated: DETERMINISTIC_b38d830ed2076823
Batch ID: 20250622_210655
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

class ClayPotModel:
    def __init__(self, height=10, radius=5, resolution=100):
        """
        Initialize the ClayPotModel with specified dimensions and resolution.

        :param height: Height of the clay pot
        :param radius: Radius of the clay pot
        :param resolution: Number of points to generate for the pot's surface
        """
        self.height = height
        self.radius = radius
        self.resolution = resolution

    def generate_pot(self):
        """
        Generate the 3D coordinates for the clay pot model.

        :return: Tuple of X, Y, Z coordinates for the pot's surface
        """
        try:
            # Create a grid of angles and heights
            theta = np.linspace(0, 2 * np.pi, self.resolution)
            z = np.linspace(0, self.height, self.resolution)

            # Create a meshgrid for the pot's surface
            theta_grid, z_grid = np.meshgrid(theta, z)

            # Define the radius as a function of height to create a pot shape
            r = self.radius * (1 - z_grid / self.height)

            # Convert polar coordinates to Cartesian coordinates
            x = r * np.cos(theta_grid)
            y = r * np.sin(theta_grid)

            return x, y, z_grid
        except Exception as e:
            print(f"Error generating pot model: {e}")
            return None, None, None

    def plot_pot(self):
        """
        Plot the generated clay pot model in 3D.

        :return: None
        """
        x, y, z = self.generate_pot()
        if x is None or y is None or z is None:
            print("Failed to generate pot model for plotting.")
            return

        # Create a 3D plot
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(x, y, z, color='saddlebrown', edgecolor='none')

        # Set plot labels
        ax.set_xlabel('X axis')
        ax.set_ylabel('Y axis')
        ax.set_zlabel('Z axis')
        ax.set_title('3D Model of Clay Pot')

        # Show the plot
        plt.show()

if __name__ == "__main__":
    # Create a clay pot model instance
    clay_pot = ClayPotModel(height=10, radius=5, resolution=100)

    # Plot the clay pot model
    clay_pot.plot_pot()
```
