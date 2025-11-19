"""
Generated Code Metadata:
========================
Original URL: https://greystoneinfra.in
Prompt: Write code using Blender's Python API to design a virtual 3D model of a hospitality space, incorporating high-end furnishing and efficient themes as emphasized by Greystone Infra.
Generated: DETERMINISTIC_9509b9d2900f765d
Batch ID: 20250612_153246
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
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()

def setup_scene():
    """Set up the scene with proper lighting and camera."""
    # Set render engine to Cycles for high-quality rendering
    bpy.context.scene.render.engine = 'CYCLES'
    
    # Add a camera
    bpy.ops.object.camera_add(location=(10, -10, 5))
    camera = bpy.context.active_object
    camera.rotation_euler = (math.radians(60), 0, math.radians(45))
    bpy.context.scene.camera = camera
    
    # Add area lights for even illumination
    light_locations = [
        (5, -5, 8),
        (-5, 5, 8),
        (0, 0, 10)
    ]
    
    for loc in light_locations:
        bpy.ops.object.light_add(type='AREA', location=loc)
        light = bpy.context.active_object
        light.data.energy = 1000
        light.data.shape = 'RECTANGLE'
        light.data.size = 5
        light.data.size_y = 5

def create_floor(width=20, length=20):
    """Create a floor plane."""
    bpy.ops.mesh.primitive_plane_add(size=1, location=(0, 0, 0))
    floor = bpy.context.active_object
    floor.scale = (width, length, 1)
    floor.name = "Floor"
    
    # Add material
    mat = bpy.data.materials.new(name="FloorMaterial")
    floor.data.materials.append(mat)
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    nodes.clear()
    
    # Create shader nodes
    bsdf = nodes.new('ShaderNodeBsdfPrincipled')
    bsdf.inputs['Base Color'].default_value = (0.8, 0.75, 0.7, 1)
    bsdf.inputs['Roughness'].default_value = 0.2
    
    output = nodes.new('ShaderNodeOutputMaterial')
    mat.node_tree.links.new(bsdf.outputs['BSDF'], output.inputs['Surface'])
    
    return floor

def create_walls(width=20, length=20, height=3):
    """Create walls around the perimeter."""
    wall_thickness = 0.2
    walls = []
    
    # Front wall
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, length/2, height/2))
    wall = bpy.context.active_object
    wall.scale = (width, wall_thickness, height)
    wall.name = "FrontWall"
    walls.append(wall)
    
    # Back wall
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, -length/2, height/2))
    wall = bpy.context.active_object
    wall.scale = (width, wall_thickness, height)
    wall.name = "BackWall"
    walls.append(wall)
    
    # Left wall
    bpy.ops.mesh.primitive_cube_add(size=1, location=(-width/2, 0, height/2))
    wall = bpy.context.active_object
    wall.scale = (wall_thickness, length, height)
    wall.name = "LeftWall"
    walls.append(wall)
    
    # Right wall
    bpy.ops.mesh.primitive_cube_add(size=1, location=(width/2, 0, height/2))
    wall = bpy.context.active_object
    wall.scale = (wall_thickness, length, height)
    wall.name = "RightWall"
    walls.append(wall)
    
    # Add material to walls
    mat = bpy.data.materials.new(name="WallMaterial")
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    nodes.clear()
    
    bsdf = nodes.new('ShaderNodeBsdfPrincipled')
    bsdf.inputs['Base Color'].default_value = (0.95, 0.95, 0.95, 1)
    bsdf.inputs['Roughness'].default_value = 0.1
    
    output = nodes.new('ShaderNodeOutputMaterial')
    mat.node_tree.links.new(bsdf.outputs['BSDF'], output.inputs['Surface'])
    
    for wall in walls:
        wall.data.materials.append(mat)
    
    return walls

def create_luxury_sofa(location=(0, 0, 0)):
    """Create a high-end sofa model."""
    # Base
    bpy.ops.mesh.primitive_cube_add(size=1, location=location)
    sofa = bpy.context.active_object
    sofa.scale = (2, 0.8, 0.4)
    sofa.name = "SofaBase"
    
    # Backrest
    bpy.ops.mesh.primitive_cube_add(size=1, location=(location[0], location[1], location[2] + 0.6))
    backrest = bpy.context.active_object
    backrest.scale = (2, 0.8, 0.8)
    backrest.name = "SofaBackrest"
    
    # Armrests
    armrest_locations = [
        (location[0] - 1, location[1], location[2] + 0.3),
        (location[0] + 1, location[1], location[2] + 0.3)
    ]
    
    for loc in armrest_locations:
        bpy.ops.mesh.primitive_cube_add(size=1, location=loc)
        armrest = bpy.context.active_object
        armrest.scale = (0.2, 0.8, 0.6)
        armrest.name = "SofaArmrest"
    
    # Create sofa group
    sofa_group = bpy.data.collections.new("LuxurySofa")
    bpy.context.scene.collection.children.link(sofa_group)
    
    for obj in [sofa, backrest] + [obj for obj in bpy.context.selected_objects if "Armrest" in obj.name]:
        bpy.context.scene.collection.objects.unlink(obj)
        sofa_group.objects.link(obj)
    
    # Add material
    mat = bpy.data.materials.new(name="SofaMaterial")
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    nodes.clear()
    
    bsdf = nodes.new('ShaderNodeBsdfPrincipled')
    bsdf.inputs['Base Color'].default_value = (0.1, 0.05, 0.02, 1)
    bsdf.inputs['Roughness'].default_value = 0.7
    bsdf.inputs['Sheen'].default_value = 0.2
    
    output = nodes.new('ShaderNodeOutputMaterial')
    mat.node_tree.links.new(bsdf.outputs['BSDF'], output.inputs['Surface'])
    
    for obj in sofa_group.objects:
        obj.data.materials.append(mat)
    
    return sofa_group

def create_dining_table(location=(0, 0, 0)):
    """Create a high-end dining table."""
    # Table top
    bpy.ops.mesh.primitive_cylinder_add(vertices=64, radius=1, depth=0.1, location=(location[0], location[1], location[2] + 0.75))
    table_top = bpy.context.active_object
    table_top.name = "TableTop"
    
    # Table legs
    leg_locations = [
        (location[0] - 0.7, location[1] - 0.7, location[2] + 0.35),
        (location[0] - 0.7, location[1] + 0.7, location[2] + 0.35),
        (location[0] + 0.7, location[1] - 0.7, location[2] + 0.35),
        (location[0] + 0.7, location[1] + 0.7, location[2] + 0.35)
    ]
    
    for loc in leg_locations:
        bpy.ops.mesh.primitive_cylinder_add(vertices=32, radius=0.05, depth=0.7, location=loc)
        leg = bpy.context.active_object
        leg.name = "TableLeg"
    
    # Create table group
    table_group = bpy.data.collections.new("DiningTable")
    bpy.context.scene.collection.children.link(table_group)
    
    for obj in [table_top] + [obj for obj in bpy.context.selected_objects if "Leg" in obj.name]:
        bpy.context.scene.collection.objects.unlink(obj)
        table_group.objects.link(obj)
    
    # Add material
    mat = bpy.data.materials.new(name="TableMaterial")
    mat.use_nodes = True
    nodes =
