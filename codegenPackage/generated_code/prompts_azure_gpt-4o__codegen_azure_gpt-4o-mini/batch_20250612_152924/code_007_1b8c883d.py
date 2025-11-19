"""
Generated Code Metadata:
========================
Original URL: https://cristalesgraf.com
Prompt: Write a function to generate 3D visualizations of glass and aluminum installations, incorporating features similar to those described on CristalesGraf's website.
Generated: DETERMINISTIC_1b8c883de9d4adcc
Batch ID: 20250612_152924
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

def generate_3d_visualization(material='glass', dimensions=(1, 1, 1), position=(0, 0, 0)):
    """
    Generate a 3D visualization of a material installation (glass or aluminum).
    
    Parameters:
    - material (str): The type of material ('glass' or 'aluminum').
    - dimensions (tuple): A tuple representing the width, height, and depth of the installation.
    - position (tuple): A tuple representing the x, y, and z coordinates of the installation's position.
    
    Raises:
    - ValueError: If the material is not 'glass' or 'aluminum'.
    - TypeError: If dimensions or position are not tuples of length 3.
    """
    
    # Validate input parameters
    if material not in ['glass', 'aluminum']:
        raise ValueError("Material must be either 'glass' or 'aluminum'.")
    
    if not (isinstance(dimensions, tuple) and len(dimensions) == 3):
        raise TypeError("Dimensions must be a tuple of length 3.")
    
    if not (isinstance(position, tuple) and len(position) == 3):
        raise TypeError("Position must be a tuple of length 3.")
    
    # Create a 3D figure
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Define the vertices of the cuboid
    x = [0, dimensions[0], dimensions[0], 0, 0, dimensions[0], dimensions[0], 0]
    y = [0, 0, dimensions[1], dimensions[1], 0, 0, dimensions[1], dimensions[1]]
    z = [0, 0, 0, 0, dimensions[2], dimensions[2], dimensions[2], dimensions[2]]
    
    # Translate the cuboid to the specified position
    x = np.array(x) + position[0]
    y = np.array(y) + position[1]
    z = np.array(z) + position[2]
    
    # Define the faces of the cuboid
    faces = [[x[j] for j in [0, 1, 2, 3]],
             [x[j] for j in [4, 5, 6, 7]],
             [x[j] for j in [0, 1, 5, 4]],
             [x[j] for j in [2, 3, 7, 6]],
             [x[j] for j in [1, 2, 6, 5]],
             [x[j] for j in [4, 7, 3, 0]]]
    
    # Set colors based on material
    color = 'lightblue' if material == 'glass' else 'gray'
    
    # Plot each face of the cuboid
    for face in faces:
        ax.add_collection3d(plt.Polygon(np.array([face, y]), color=color, alpha=0.5))
    
    # Set labels and limits
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    ax.set_title(f'3D Visualization of {material.capitalize()} Installation')
    
    # Set the aspect ratio
    ax.set_box_aspect([1,1,1])  # Equal aspect ratio
    
    # Show the plot
    plt.show()

# Example usage
if __name__ == "__main__":
    try:
        generate_3d_visualization(material='glass', dimensions=(2, 1, 1), position=(0, 0, 0))
    except Exception as e:
        print(f"An error occurred: {e}")
```
