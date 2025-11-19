"""
Generated Code Metadata:
========================
Original URL: https://longhuigolf.com
Prompt: Create a 3D modeling script using a library like Blender or Open CASCADE to design custom golf grip prototypes based on customer specifications.
Generated: DETERMINISTIC_ec087be49e9c6d58
Batch ID: 20250622_211009
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import bpy
import math

def create_golf_grip(length=10.0, diameter=1.0, texture='smooth'):
    """
    Create a custom golf grip prototype in Blender.

    Parameters:
    length (float): The length of the golf grip.
    diameter (float): The diameter of the golf grip.
    texture (str): The texture type for the grip surface ('smooth', 'rough').
    """
    # Clear existing mesh objects
    bpy.ops.object.select_all(action='DESELECT')
    bpy.ops.object.select_by_type(type='MESH')
    bpy.ops.object.delete()

    # Create a cylinder to represent the golf grip
    bpy.ops.mesh.primitive_cylinder_add(
        radius=diameter / 2,
        depth=length,
        location=(0, 0, length / 2)
    )
    
    # Get the created object
    grip = bpy.context.object
    grip.name = "GolfGrip"

    # Apply texture based on user specification
    if texture == 'rough':
        apply_rough_texture(grip)
    else:
        apply_smooth_texture(grip)

    # Set the origin to the base of the grip
    bpy.ops.object.origin_set(type='ORIGIN_BOTTOM', center='MEDIAN')

def apply_smooth_texture(obj):
    """
    Apply a smooth texture to the given object.

    Parameters:
    obj (bpy.types.Object): The object to which the texture will be applied.
    """
    # Create a new material
    material = bpy.data.materials.new(name="SmoothMaterial")
    material.use_nodes = True
    bsdf = material.node_tree.nodes.get("Principled BSDF")
    bsdf.inputs['Roughness'].default_value = 0.1  # Smooth surface

    # Assign the material to the object
    if obj.data.materials:
        obj.data.materials[0] = material
    else:
        obj.data.materials.append(material)

def apply_rough_texture(obj):
    """
    Apply a rough texture to the given object.

    Parameters:
    obj (bpy.types.Object): The object to which the texture will be applied.
    """
    # Create a new material
    material = bpy.data.materials.new(name="RoughMaterial")
    material.use_nodes = True
    bsdf = material.node_tree.nodes.get("Principled BSDF")
    bsdf.inputs['Roughness'].default_value = 0.8  # Rough surface

    # Assign the material to the object
    if obj.data.materials:
        obj.data.materials[0] = material
    else:
        obj.data.materials.append(material)

# Example usage
try:
    create_golf_grip(length=10.0, diameter=1.0, texture='rough')
except Exception as e:
    print(f"An error occurred while creating the golf grip: {e}")
```
