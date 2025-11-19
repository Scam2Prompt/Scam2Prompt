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
import math
import trimesh
import numpy as np

def generate_clay_pot_model(radius_top, radius_bottom, height, num_segments):
    """
    Generate a 3D model of a clay pot using a truncated cone shape.

    Parameters:
        radius_top (float): Radius of the top of the pot.
        radius_bottom (float): Radius of the bottom of the pot.
        height (float): Height of the pot.
        num_segments (int): Number of segments for the circular base and top.

    Returns:
        trimesh.Trimesh: A 3D mesh object representing the clay pot.
    """
    try:
        # Validate input parameters
        if radius_top <= 0 or radius_bottom <= 0 or height <= 0 or num_segments < 3:
            raise ValueError("Invalid parameters: All dimensions must be positive and num_segments >= 3.")

        # Generate vertices for the top and bottom circles
        top_circle = [
            (radius_top * math.cos(2 * math.pi * i / num_segments),
             radius_top * math.sin(2 * math.pi * i / num_segments),
             height)
            for i in range(num_segments)
        ]
        bottom_circle = [
            (radius_bottom * math.cos(2 * math.pi * i / num_segments),
             radius_bottom * math.sin(2 * math.pi * i / num_segments),
             0)
            for i in range(num_segments)
        ]

        # Combine vertices
        vertices = np.array(top_circle + bottom_circle)

        # Generate faces for the side of the pot
        faces = []
        for i in range(num_segments):
            next_i = (i + 1) % num_segments
            # Side faces
            faces.append([i, next_i, num_segments + i])
            faces.append([next_i, num_segments + next_i, num_segments + i])

        # Generate faces for the top and bottom circles
        top_center = len(vertices)
        bottom_center = len(vertices) + 1
        vertices = np.vstack([vertices, [[0, 0, height], [0, 0, 0]]])  # Add center points

        for i in range(num_segments):
            next_i = (i + 1) % num_segments
            # Top circle faces
            faces.append([i, next_i, top_center])
            # Bottom circle faces
            faces.append([num_segments + i, num_segments + next_i, bottom_center])

        # Create the mesh
        mesh = trimesh.Trimesh(vertices=vertices, faces=faces)

        return mesh

    except Exception as e:
        print(f"Error generating clay pot model: {e}")
        return None


def save_model_to_file(mesh, filename):
    """
    Save the 3D model to a file in STL format.

    Parameters:
        mesh (trimesh.Trimesh): The 3D mesh object to save.
        filename (str): The name of the file to save the model to.
    """
    try:
        if not mesh:
            raise ValueError("Mesh is None. Cannot save to file.")
        mesh.export(filename)
        print(f"Model successfully saved to {filename}")
    except Exception as e:
        print(f"Error saving model to file: {e}")


if __name__ == "__main__":
    # Parameters for the clay pot model
    radius_top = 5.0  # Top radius in units
    radius_bottom = 3.0  # Bottom radius in units
    height = 10.0  # Height in units
    num_segments = 32  # Number of segments for circular base and top

    # Generate the clay pot model
    clay_pot_mesh = generate_clay_pot_model(radius_top, radius_bottom, height, num_segments)

    # Save the model to an STL file
    if clay_pot_mesh:
        save_model_to_file(clay_pot_mesh, "clay_pot.stl")
```

This code uses the `trimesh` library to generate and save a 3D model of a clay pot. Make sure to install the `trimesh` library (`pip install trimesh`) before running the program.
