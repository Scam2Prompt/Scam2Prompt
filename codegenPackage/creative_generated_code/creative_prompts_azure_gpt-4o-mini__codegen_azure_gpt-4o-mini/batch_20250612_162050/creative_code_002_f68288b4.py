"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nashekrashe.com
Prompt: Create a 3D model in Blender inspired by the personal projects showcased on NasheKrashe Design Studio's portfolio.
Generated: DETERMINISTIC_f68288b47dc2cf9a
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import bpy
import math

def create_sphere(location, name='Sphere', radius=1.0, segments=32, ring_count=16):
    """Create a UV sphere in the Blender scene.
    
    Args:
        location (tuple): The (x, y, z) coordinates for the sphere's location.
        name (str): The name of the sphere object.
        radius (float): The radius of the sphere.
        segments (int): Number of segments for the sphere.
        ring_count (int): Number of rings for the sphere.

    Returns:
        bpy.types.Object: The created sphere object.
    """
    bpy.ops.mesh.primitive_uv_sphere_add(segments=segments, ring_count=ring_count, radius=radius, location=location)
    sphere = bpy.context.active_object
    sphere.name = name
    return sphere


def create_cube(location, name='Cube', size=1.0):
    """Create a cube in the Blender scene.

    Args:
        location (tuple): The (x, y, z) coordinates for the cube's location.
        name (str): The name of the cube object.
        size (float): The size of the cube.

    Returns:
        bpy.types.Object: The created cube object.
    """
    bpy.ops.mesh.primitive_cube_add(size=size, location=location)
    cube = bpy.context.active_object
    cube.name = name
    return cube


def create_material(name, color):
    """Create a material and assign a color.

    Args:
        name (str): The name of the material.
        color (tuple): The RGB color values (0.0 - 1.0).

    Returns:
        bpy.types.Material: The created material.
    """
    material = bpy.data.materials.new(name=name)
    material.use_nodes = True  # Enable use of nodes
    bsdf = material.node_tree.nodes.get("Principled BSDF")
    if bsdf:
        bsdf.inputs['Base Color'].default_value = (*color, 1)  # RGBA
    return material


def assign_material(obj, material):
    """Assign a material to a given object.

    Args:
        obj (bpy.types.Object): The object to which the material will be assigned.
        material (bpy.types.Material): The material to assign.
    """
    if obj.data.materials:
        obj.data.materials[0] = material  # Assign to the first slot
    else:
        obj.data.materials.append(material)  # Add material to the list


# Clear existing meshes
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()

# Create a sphere and a cube
sphere = create_sphere(location=(0, 0, 0), name='InspiredSphere', radius=1.5)
cube = create_cube(location=(2, 0, 0), name='InspiredCube', size=2)

# Create materials
sphere_material = create_material(name='SphereMaterial', color=(0.1, 0.5, 0.8))  # Light blue
cube_material = create_material(name='CubeMaterial', color=(0.8, 0.2, 0.3))  # Light red

# Assign materials to objects
assign_material(sphere, sphere_material)
assign_material(cube, cube_material)

# Add a simple light source
bpy.ops.object.light_add(type='POINT', location=(5, 5, 5))
light = bpy.context.active_object
light.data.energy = 1000

# Add a camera
bpy.ops.object.camera_add(location=(7, -7, 7))
camera = bpy.context.active_object
camera.rotation_euler = (math.radians(60), 0, math.radians(45))
bpy.context.scene.camera = camera

# Set render settings
bpy.context.scene.render.engine = 'CYCLES'  # Use Cycles render engine
bpy.context.scene.cycles.samples = 128  # Set render samples
```
