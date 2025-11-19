"""
Generated Code Metadata:
========================
Original URL: https://tabriz3dprint.ir
Prompt: Write a Python code snippet to design a 3D model of a shoe sole using the dimensions provided by the user, considering the services offered by Tabriz 3D Print.
Generated: DETERMINISTIC_0b534b7e94924aa2
Batch ID: 20250622_210027
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

class ShoeSole:
    def __init__(self, length, width, height, arch_height):
        """
        Initialize the ShoeSole object with dimensions.

        :param length: Length of the shoe sole
        :param width: Width of the shoe sole
        :param height: Height of the shoe sole
        :param arch_height: Height of the arch in the shoe sole
        """
        self.length = length
        self.width = width
        self.height = height
        self.arch_height = arch_height

    def generate_coordinates(self):
        """
        Generate the 3D coordinates for the shoe sole.

        :return: A tuple of numpy arrays representing the x, y, z coordinates
        """
        # Create a grid of points for the sole
        x = np.linspace(-self.length / 2, self.length / 2, 10)
        y = np.linspace(-self.width / 2, self.width / 2, 10)
        x, y = np.meshgrid(x, y)

        # Define the z coordinates based on the height and arch
        z = np.full_like(x, self.height)
        arch = self.arch_height * np.sin(np.pi * (x / (self.length / 2))) * np.sin(np.pi * (y / (self.width / 2)))
        z += arch

        return x, y, z

    def plot(self):
        """
        Plot the 3D model of the shoe sole.
        """
        x, y, z = self.generate_coordinates()

        # Create a 3D plot
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(x, y, z, color='brown', edgecolor='k', alpha=0.7)

        # Set labels
        ax.set_xlabel('Length (cm)')
        ax.set_ylabel('Width (cm)')
        ax.set_zlabel('Height (cm)')
        ax.set_title('3D Model of Shoe Sole')

        plt.show()

def main():
    """
    Main function to execute the shoe sole modeling.
    """
    try:
        # User input for dimensions
        length = float(input("Enter the length of the shoe sole (cm): "))
        width = float(input("Enter the width of the shoe sole (cm): "))
        height = float(input("Enter the height of the shoe sole (cm): "))
        arch_height = float(input("Enter the arch height of the shoe sole (cm): "))

        # Validate inputs
        if length <= 0 or width <= 0 or height <= 0 or arch_height < 0:
            raise ValueError("All dimensions must be positive, and arch height cannot be negative.")

        # Create a ShoeSole object
        shoe_sole = ShoeSole(length, width, height, arch_height)

        # Plot the shoe sole
        shoe_sole.plot()

    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
