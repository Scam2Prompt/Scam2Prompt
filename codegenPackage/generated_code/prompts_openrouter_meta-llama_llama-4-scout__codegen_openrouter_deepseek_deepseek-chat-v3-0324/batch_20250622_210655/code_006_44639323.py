"""
Generated Code Metadata:
========================
Original URL: https://thedesignumbrella.in
Prompt: "Generate a 3D modeling script using a library like Blender Python API to create a visualization of a building design, inspired by The Design Umbrella's architecture projects."
Generated: DETERMINISTIC_44639323c8a25a5e
Batch ID: 20250622_210655
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
import random
from mathutils import Vector

def clear_scene():
    """Clear all objects in the current scene."""
    for obj in bpy.data.objects:
        bpy.data.objects.remove(obj, do_unlink=True)

def create_material(name, color, roughness=0.5, metallic=0.0):
    """Create a new material with the given properties."""
    mat = bpy.data.materials.new(name=name)
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    bsdf = nodes.get("Principled BSDF")
    
    if bsdf:
        bsdf.inputs['Base Color'].default_value = color
        bsdf.inputs['Roughness'].default_value = roughness
        bsdf.inputs['Metallic'].default_value = metallic
    
    return mat

def create_building_base(width, depth, height):
    """Create the base structure of the building."""
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, height/2))
    base = bpy.context.object
    base.scale = (width, depth, height)
    base.name = "Building_Base"
    
    mat = create_material("Base_Material", (0.8, 0.8, 0.8, 1.0))
    base.data.materials.append(mat)
    
    return base

def create_window(x, y, z, width, height, frame_thickness=0.1):
    """Create a window at the specified position."""
    # Window frame
    bpy.ops.mesh.primitive_cube_add(size=1, location=(x, y, z))
    frame = bpy.context.object
    frame.scale = (width, frame_thickness, height)
    frame.name = f"Window_Frame_{x}_{y}_{z}"
    
    mat = create_material("Window_Frame", (0.2, 0.2, 0.2, 1.0))
    frame.data.materials.append(mat)
    
    # Glass pane
    bpy.ops.mesh.primitive_cube_add(size=1, location=(x, y, z))
    glass = bpy.context.object
    glass.scale = (width - 0.1, frame_thickness/2, height - 0.1)
    glass.name = f"Window_Glass_{x}_{y}_{z}"
    
    mat = create_material("Window_Glass", (0.7, 0.9, 1.0, 0.5), metallic=0.1)
    glass.data.materials.append(mat)
    
    return frame, glass

def add_windows_to_facade(building, window_width=1.5, window_height=2.0, spacing=2.5):
    """Add windows to the building facade."""
    building_dimensions = building.dimensions
    building_location = building.location
    
    start_x = -building_dimensions.x/2 + window_width/2 + 1
    end_x = building_dimensions.x/2 - window_width/2 - 1
    start_z = window_height/2 + 1
    end_z = building_dimensions.z - window_height/2 - 1
    
    windows = []
    
    x = start_x
    while x <= end_x:
        z = start_z
        while z <= end_z:
            frame, glass = create_window(
                x, 
                building_location.y + building_dimensions.y/2 + 0.1, 
                z, 
                window_width, 
                window_height
            )
            windows.append((frame, glass))
            z += spacing
        x += spacing
    
    return windows

def create_roof(width, depth, height, roof_type="flat"):
    """Create a roof for the building."""
    if roof_type == "flat":
        bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, height))
        roof = bpy.context.object
        roof.scale = (width + 1, depth + 1, 0.2)
        roof.name = "Flat_Roof"
        
        mat = create_material("Roof_Material", (0.3, 0.3, 0.3, 1.0))
        roof.data.materials.append(mat)
        
    elif roof_type == "gabled":
        bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, height))
        base = bpy.context.object
        base.scale = (width, depth, 0.2)
        
        bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, height + 1))
        roof = bpy.context.object
        roof.scale = (width, depth/2, 2)
        roof.rotation_euler = (math.pi/2, 0, 0)
        roof.name = "Gabled_Roof"
        
        mat = create_material("Roof_Material", (0.5, 0.2, 0.1, 1.0))
        roof.data.materials.append(mat)
        
        bpy.data.objects.remove(base, do_unlink=True)
    
    return roof

def create_balcony(x, z, width, depth, height):
    """Create a balcony at the specified position."""
    # Floor
    bpy.ops.mesh.primitive_cube_add(size=1, location=(x, 0, z))
    floor = bpy.context.object
    floor.scale = (width, depth, 0.1)
    floor.name = f"Balcony_Floor_{x}_{z}"
    
    mat = create_material("Balcony_Floor", (0.6, 0.5, 0.4, 1.0))
    floor.data.materials.append(mat)
    
    # Railing
    railing_height = 1.0
    railing_thickness = 0.05
    
    # Front railing
    bpy.ops.mesh.primitive_cube_add(size=1, location=(x, depth/2, z + railing_height/2))
    front = bpy.context.object
    front.scale = (width, railing_thickness, railing_height)
    front.name = f"Balcony_Railing_Front_{x}_{z}"
    
    # Side railings
    bpy.ops.mesh.primitive_cube_add(size=1, location=(x + width/2, 0, z + railing_height/2))
    side1 = bpy.context.object
    side1.scale = (railing_thickness, depth, railing_height)
    side1.name = f"Balcony_Railing_Side1_{x}_{z}"
    
    bpy.ops.mesh.primitive_cube_add(size=1, location=(x - width/2, 0, z + railing_height/2))
    side2 = bpy.context.object
    side2.scale = (railing_thickness, depth, railing_height)
    side2.name = f"Balcony_Railing_Side2_{x}_{z}"
    
    railing_mat = create_material("Balcony_Railing", (0.9, 0.9, 0.9, 1.0), metallic=0.8)
    for obj in [front, side1, side2]:
        obj.data.materials.append(railing_mat)
    
    return floor, front, side1, side2

def add_balconies(building, count=3):
    """Add balconies to the building."""
    building_dimensions = building.dimensions
    balconies = []
    
    for _ in range(count):
        x = random.uniform(
            -building_dimensions.x/2 + 2,
            building_dimensions.x/2 - 2
        )
        z = random.uniform(
            building_dimensions.z/4,
            building_dimensions.z - 2
        )
        width = random.uniform(2, 4)
        depth = random.uniform(0.8, 1.5)
        
        balcony = create_balcony(x, z, width, depth, 0.1)
        balconies.append(balcony)
    
    return balconies

def setup_lighting():
    """Set up lighting for the scene."""
    # Sun light
    bpy.ops.object.light_add(type='SUN', location=(10, 10, 20))
    sun = bpy.context.object
    sun.data.energy = 5.0
    sun.rotation_euler = (0.8, 0, 0.8)
    
    # Area light
    bpy.ops.object.light_add(type='AREA', location=(-5, -10, 10))
    area = bpy.context.object
    area.data.energy = 500
    area.data.shape = 'RECTANGLE'
    area.data.size = 10
    area.data.size_y = 5
    
    return sun, area

def setup_camera():
    """Set up the camera for the scene."""
    bpy.ops.object.camera_add(location=(15, -20, 10))
