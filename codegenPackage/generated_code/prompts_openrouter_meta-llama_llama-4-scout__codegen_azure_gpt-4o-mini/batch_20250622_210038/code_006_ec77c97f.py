"""
Generated Code Metadata:
========================
Original URL: https://www.dexodoor.com
Prompt: "Suggest libraries for creating 3D models of UPVC window and door systems for architectural visualization projects, incorporating details like sleek designs and eco-friendly materials."
Generated: DETERMINISTIC_ec77c97faff750de
Batch ID: 20250622_210038
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries for 3D modeling and visualization
import bpy  # Blender Python API for 3D modeling
import os

# Function to create a UPVC window
def create_upvc_window(location=(0, 0, 0), dimensions=(1, 1, 0.1), eco_friendly_material='Plastic'):
    """
    Create a UPVC window in Blender.

    :param location: Tuple of (x, y, z) coordinates for the window's location
    :param dimensions: Tuple of (width, height, depth) for the window's dimensions
    :param eco_friendly_material: Name of the material to apply to the window
    """
    # Create a new mesh and object
    bpy.ops.mesh.primitive_cube_add(size=1, location=location)
    window = bpy.context.object
    window.scale = (dimensions[0] / 2, dimensions[1] / 2, dimensions[2] / 2)

    # Create and assign material
    mat = bpy.data.materials.new(name=eco_friendly_material)
    mat.diffuse_color = (0.8, 0.8, 0.8, 1)  # Light gray color for UPVC
    window.data.materials.append(mat)

    return window

# Function to create a UPVC door
def create_upvc_door(location=(0, 0, 0), dimensions=(1, 2, 0.1), eco_friendly_material='Plastic'):
    """
    Create a UPVC door in Blender.

    :param location: Tuple of (x, y, z) coordinates for the door's location
    :param dimensions: Tuple of (width, height, depth) for the door's dimensions
    :param eco_friendly_material: Name of the material to apply to the door
    """
    # Create a new mesh and object
    bpy.ops.mesh.primitive_cube_add(size=1, location=location)
    door = bpy.context.object
    door.scale = (dimensions[0] / 2, dimensions[1] / 2, dimensions[2] / 2)

    # Create and assign material
    mat = bpy.data.materials.new(name=eco_friendly_material)
    mat.diffuse_color = (0.8, 0.8, 0.8, 1)  # Light gray color for UPVC
    door.data.materials.append(mat)

    return door

# Main function to create a scene with UPVC windows and doors
def create_scene():
    """
    Create a scene with UPVC windows and doors for architectural visualization.
    """
    try:
        # Clear existing mesh objects
        bpy.ops.object.select_all(action='DESELECT')
        bpy.ops.object.select_by_type(type='MESH')
        bpy.ops.object.delete()

        # Create UPVC windows
        create_upvc_window(location=(0, 0, 1), dimensions=(1, 1, 0.1))
        create_upvc_window(location=(2, 0, 1), dimensions=(1, 1, 0.1))

        # Create UPVC doors
        create_upvc_door(location=(1, 0, 1), dimensions=(1, 2, 0.1))

    except Exception as e:
        print(f"An error occurred while creating the scene: {e}")

# Run the main function to create the scene
if __name__ == "__main__":
    create_scene()
```
