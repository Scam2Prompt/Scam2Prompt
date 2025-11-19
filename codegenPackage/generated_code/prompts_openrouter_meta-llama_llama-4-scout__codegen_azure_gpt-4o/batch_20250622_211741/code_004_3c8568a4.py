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
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

def generate_pool(location, size, shape):
    """
    Generates a 3D model of a swimming pool based on the given parameters.

    Parameters:
        location (tuple): The (x, y, z) coordinates of the pool's bottom-left corner.
        size (tuple): The (length, width, depth) dimensions of the pool.
        shape (str): The shape of the pool ('rectangle', 'oval').

    Returns:
        None: Displays a 3D plot of the swimming pool.
    """
    try:
        # Validate inputs
        if not isinstance(location, tuple) or len(location) != 3:
            raise ValueError("Location must be a tuple with three elements (x, y, z).")
        if not isinstance(size, tuple) or len(size) != 3:
            raise ValueError("Size must be a tuple with three elements (length, width, depth).")
        if shape not in ['rectangle', 'oval']:
            raise ValueError("Shape must be either 'rectangle' or 'oval'.")

        x, y, z = location
        length, width, depth = size

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        if shape == 'rectangle':
            # Define vertices for a rectangular pool
            vertices = [
                [x, y, z], [x + length, y, z], [x + length, y + width, z], [x, y + width, z],  # Bottom face
                [x, y, z - depth], [x + length, y, z - depth], [x + length, y + width, z - depth], [x, y + width, z - depth]  # Top face
            ]
            # Define faces using vertices
            faces = [
                [vertices[0], vertices[1], vertices[2], vertices[3]],  # Bottom face
                [vertices[4], vertices[5], vertices[6], vertices[7]],  # Top face
                [vertices[0], vertices[1], vertices[5], vertices[4]],  # Front face
                [vertices[1], vertices[2], vertices[6], vertices[5]],  # Right face
                [vertices[2], vertices[3], vertices[7], vertices[6]],  # Back face
                [vertices[3], vertices[0], vertices[4], vertices[7]]   # Left face
            ]
            # Add faces to the plot
            ax.add_collection3d(Poly3DCollection(faces, facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))

        elif shape == 'oval':
            # Generate an oval pool using parametric equations
            u = np.linspace(0, 2 * np.pi, 100)
            v = np.linspace(0, depth, 50)
            u, v = np.meshgrid(u, v)
            x_oval = x + length / 2 + (length / 2) * np.cos(u)
            y_oval = y + width / 2 + (width / 2) * np.sin(u)
            z_oval = z - v
            ax.plot_surface(x_oval, y_oval, z_oval, color='cyan', alpha=0.5)

        # Set plot limits and labels
        ax.set_xlim([x - 10, x + length + 10])
        ax.set_ylim([y - 10, y + width + 10])
        ax.set_zlim([z - depth - 10, z + 10])
        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        ax.set_zlabel('Z-axis')
        ax.set_title('3D Swimming Pool Model')

        plt.show()

    except Exception as e:
        print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    # Define pool parameters
    pool_location = (0, 0, 0)  # Bottom-left corner at origin
    pool_size = (20, 10, 5)   # Length=20, Width=10, Depth=5
    pool_shape = 'rectangle'  # Shape can be 'rectangle' or 'oval'

    # Generate the pool model
    generate_pool(pool_location, pool_size, pool_shape)
```
