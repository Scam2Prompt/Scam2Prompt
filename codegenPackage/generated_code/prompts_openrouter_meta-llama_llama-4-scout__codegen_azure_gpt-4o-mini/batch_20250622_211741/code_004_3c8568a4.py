"""
Generated Code Metadata:
========================
Original URL: https://oeg-group.com
Prompt: "Write a Python script that generates a 3D model of a custom swimming pool for a residential outdoor environment, using parameters such as location, size, and shape."
Generated: DETERMINISTIC_3c8568a4f0942139
Batch ID: 20250622_211741
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

class SwimmingPool:
    def __init__(self, location, size, shape):
        """
        Initializes the SwimmingPool object with location, size, and shape.

        :param location: Tuple (x, y, z) representing the pool's location in 3D space.
        :param size: Tuple (length, width, depth) representing the pool's dimensions.
        :param shape: String representing the shape of the pool ('rectangular', 'circular').
        """
        self.location = location
        self.size = size
        self.shape = shape.lower()

    def generate_pool(self):
        """
        Generates the 3D coordinates for the swimming pool based on its shape and size.

        :return: Tuple of X, Y, Z coordinates for the pool.
        """
        x, y, z = self.location
        length, width, depth = self.size

        if self.shape == 'rectangular':
            return self._generate_rectangular_pool(x, y, z, length, width, depth)
        elif self.shape == 'circular':
            return self._generate_circular_pool(x, y, z, length, depth)
        else:
            raise ValueError("Shape must be either 'rectangular' or 'circular'.")

    def _generate_rectangular_pool(self, x, y, z, length, width, depth):
        """
        Generates coordinates for a rectangular swimming pool.

        :return: Tuple of X, Y, Z coordinates for the rectangular pool.
        """
        X = np.array([[x, x + length, x + length, x],
                       [x, x + length, x + length, x]])
        Y = np.array([[y, y, y + width, y + width],
                       [y, y, y + width, y + width]])
        Z = np.array([[z, z, z, z],
                       [z - depth, z - depth, z - depth, z - depth]])
        return X, Y, Z

    def _generate_circular_pool(self, x, y, z, radius, depth):
        """
        Generates coordinates for a circular swimming pool.

        :return: Tuple of X, Y, Z coordinates for the circular pool.
        """
        theta = np.linspace(0, 2 * np.pi, 100)
        X = x + radius * np.cos(theta)
        Y = y + radius * np.sin(theta)
        Z = np.full_like(X, z)
        Z_bottom = np.full_like(X, z - depth)
        return X, Y, Z, Z_bottom

    def plot_pool(self):
        """
        Plots the swimming pool in a 3D environment.
        """
        try:
            if self.shape == 'rectangular':
                X, Y, Z = self.generate_pool()
                fig = plt.figure()
                ax = fig.add_subplot(111, projection='3d')
                ax.plot_surface(X, Y, Z, alpha=0.7, color='blue')
                ax.set_title('Rectangular Swimming Pool')
            elif self.shape == 'circular':
                X, Y, Z, Z_bottom = self.generate_pool()
                fig = plt.figure()
                ax = fig.add_subplot(111, projection='3d')
                ax.plot_surface(X, Y, Z, alpha=0.7, color='blue')
                ax.plot_surface(X, Y, Z_bottom, alpha=0.7, color='blue')
                ax.set_title('Circular Swimming Pool')
            else:
                raise ValueError("Shape must be either 'rectangular' or 'circular'.")

            ax.set_xlabel('X Coordinate')
            ax.set_ylabel('Y Coordinate')
            ax.set_zlabel('Z Coordinate')
            plt.show()
        except Exception as e:
            print(f"An error occurred while plotting the pool: {e}")

if __name__ == "__main__":
    # Example usage
    try:
        # Define parameters for the swimming pool
        location = (0, 0, 0)  # Location in 3D space
        size = (10, 5, 2)     # Size: length, width, depth
        shape = 'rectangular' # Shape of the pool

        # Create a swimming pool object
        pool = SwimmingPool(location, size, shape)

        # Plot the swimming pool
        pool.plot_pool()
    except Exception as e:
        print(f"An error occurred: {e}")
```
