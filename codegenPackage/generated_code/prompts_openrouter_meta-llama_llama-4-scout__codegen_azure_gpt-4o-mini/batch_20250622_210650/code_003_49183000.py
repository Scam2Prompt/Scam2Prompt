"""
Generated Code Metadata:
========================
Original URL: https://fernandez3d.com
Prompt: "Create a library for generating 3D exterior models with intricate details, inspired by the services offered on fernandez3d.com."
Generated: DETERMINISTIC_49183000524738ef
Batch ID: 20250622_210650
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

class ExteriorModelGenerator:
    """
    A class to generate 3D exterior models with intricate details.
    """

    def __init__(self):
        """
        Initializes the ExteriorModelGenerator.
        """
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')

    def generate_cube(self, size=1, position=(0, 0, 0)):
        """
        Generates a cube model.

        Parameters:
        size (float): The size of the cube.
        position (tuple): The (x, y, z) position of the cube's center.
        """
        try:
            r = size / 2
            x = [position[0] - r, position[0] + r, position[0] + r, position[0] - r, position[0] - r, position[0] - r, position[0] + r, position[0] + r]
            y = [position[1] - r, position[1] - r, position[1] + r, position[1] + r, position[1] - r, position[1] - r, position[1] + r, position[1] + r]
            z = [position[2] - r, position[2] - r, position[2] - r, position[2] - r, position[2] + r, position[2] + r, position[2] + r, position[2] + r]
            self.ax.scatter(x, y, z)
        except Exception as e:
            print(f"Error generating cube: {e}")

    def generate_sphere(self, radius=1, position=(0, 0, 0), resolution=20):
        """
        Generates a sphere model.

        Parameters:
        radius (float): The radius of the sphere.
        position (tuple): The (x, y, z) position of the sphere's center.
        resolution (int): The resolution of the sphere.
        """
        try:
            u = np.linspace(0, 2 * np.pi, resolution)
            v = np.linspace(0, np.pi, resolution)
            x = radius * np.outer(np.cos(u), np.sin(v)) + position[0]
            y = radius * np.outer(np.sin(u), np.sin(v)) + position[1]
            z = radius * np.outer(np.ones(np.size(u)), np.cos(v)) + position[2]
            self.ax.plot_surface(x, y, z, color='b', alpha=0.5)
        except Exception as e:
            print(f"Error generating sphere: {e}")

    def show_model(self):
        """
        Displays the generated 3D model.
        """
        try:
            self.ax.set_xlabel('X axis')
            self.ax.set_ylabel('Y axis')
            self.ax.set_zlabel('Z axis')
            plt.show()
        except Exception as e:
            print(f"Error displaying model: {e}")

# Example usage
if __name__ == "__main__":
    model_generator = ExteriorModelGenerator()
    model_generator.generate_cube(size=2, position=(0, 0, 0))
    model_generator.generate_sphere(radius=1, position=(3, 3, 0), resolution=30)
    model_generator.show_model()
```
