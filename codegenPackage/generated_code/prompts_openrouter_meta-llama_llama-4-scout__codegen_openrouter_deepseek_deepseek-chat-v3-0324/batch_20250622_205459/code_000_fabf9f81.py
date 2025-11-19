"""
Generated Code Metadata:
========================
Original URL: https://aavego.dk
Prompt: Design a Nordic-inspired holiday home in Denmark that incorporates natural materials and modern furniture classics to create a calm atmosphere.
Generated: DETERMINISTIC_fabf9f81094c72d6
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Nordic Holiday Home Design System
This script generates a 3D model of a Nordic-inspired holiday home in Denmark.
It incorporates natural materials and modern furniture classics.
"""

import bpy
import math
import random
from mathutils import Vector

# Clean up existing scene
def clear_scene():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()
    bpy.ops.outliner.orphans_purge()

# House dimensions
HOUSE_WIDTH = 10
HOUSE_LENGTH = 12
HOUSE_HEIGHT = 3.5
ROOF_HEIGHT = 2.5

# Material creation functions
def create_wood_material(name, color):
    mat = bpy.data.materials.new(name=name)
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    
    # Clear default nodes
    for node in nodes:
        nodes.remove(node)
    
    # Create shader nodes
    bsdf = nodes.new('ShaderNodeBsdfPrincipled')
    bsdf.inputs['Base Color'].default_value = color
    bsdf.inputs['Roughness'].default_value = 0.3
    
    tex_coord = nodes.new('ShaderNodeTexCoord')
    mapping = nodes.new('ShaderNodeMapping')
    noise = nodes.new('ShaderNodeTexNoise')
    noise.inputs['Scale'].default_value = 50.0
    noise.inputs['Detail'].default_value = 2.0
    
    bump = nodes.new('ShaderNodeBump')
    bump.inputs['Strength'].default_value = 0.1
    
    output = nodes.new('ShaderNodeOutputMaterial')
    
    # Link nodes
    links.new(tex_coord.outputs['Object'], mapping.inputs['Vector'])
    links.new(mapping.outputs['Vector'], noise.inputs['Vector'])
    links.new(noise.outputs['Fac'], bump.inputs['Height'])
    links.new(bump.outputs['Normal'], bsdf.inputs['Normal'])
    links.new(bsdf.outputs['BSDF'], output.inputs['Surface'])
    
    return mat

def create_concrete_material(name):
    mat = bpy.data.materials.new(name=name)
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    
    bsdf = nodes.get('Principled BSDF')
    bsdf.inputs['Base Color'].default_value = (0.8, 0.8, 0.8, 1)
    bsdf.inputs['Roughness'].default_value = 0.7
    
    return mat

def create_glass_material(name):
    mat = bpy.data.materials.new(name=name)
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    
    bsdf = nodes.get('Principled BSDF')
    bsdf.inputs['Base Color'].default_value = (0.9, 0.9, 0.9, 0.7)
    bsdf.inputs['Roughness'].default_value = 0.1
    bsdf.inputs['IOR'].default_value = 1.45
    bsdf.inputs['Transmission'].default_value = 1.0
    
    return mat

# House construction functions
def create_foundation():
    foundation = bpy.ops.mesh.primitive_cube_add(
        size=1,
        location=(0, 0, -0.1),
        scale=(HOUSE_WIDTH + 1, HOUSE_LENGTH + 1, 0.2)
    )
    foundation_obj = bpy.context.object
    foundation_obj.name = "Foundation"
    
    mat = create_concrete_material("Concrete")
    foundation_obj.data.materials.append(mat)
    
    return foundation_obj

def create_walls():
    # Front wall
    front_wall = bpy.ops.mesh.primitive_cube_add(
        size=1,
        location=(0, -HOUSE_LENGTH/2, HOUSE_HEIGHT/2),
        scale=(HOUSE_WIDTH, 0.2, HOUSE_HEIGHT)
    )
    front_wall_obj = bpy.context.object
    front_wall_obj.name = "Front_Wall"
    
    # Back wall
    back_wall = bpy.ops.mesh.primitive_cube_add(
        size=1,
        location=(0, HOUSE_LENGTH/2, HOUSE_HEIGHT/2),
        scale=(HOUSE_WIDTH, 0.2, HOUSE_HEIGHT)
    )
    back_wall_obj = bpy.context.object
    back_wall_obj.name = "Back_Wall"
    
    # Left wall
    left_wall = bpy.ops.mesh.primitive_cube_add(
        size=1,
        location=(-HOUSE_WIDTH/2, 0, HOUSE_HEIGHT/2),
        scale=(0.2, HOUSE_LENGTH, HOUSE_HEIGHT)
    )
    left_wall_obj = bpy.context.object
    left_wall_obj.name = "Left_Wall"
    
    # Right wall
    right_wall = bpy.ops.mesh.primitive_cube_add(
        size=1,
        location=(HOUSE_WIDTH/2, 0, HOUSE_HEIGHT/2),
        scale=(0.2, HOUSE_LENGTH, HOUSE_HEIGHT)
    )
    right_wall_obj = bpy.context.object
    right_wall_obj.name = "Right_Wall"
    
    # Apply wood material
    wood_mat = create_wood_material("Wood", (0.8, 0.6, 0.4, 1))
    for wall in [front_wall_obj, back_wall_obj, left_wall_obj, right_wall_obj]:
        wall.data.materials.append(wood_mat)
    
    return [front_wall_obj, back_wall_obj, left_wall_obj, right_wall_obj]

def create_roof():
    roof_verts = [
        (-HOUSE_WIDTH/2, -HOUSE_LENGTH/2, HOUSE_HEIGHT),
        (HOUSE_WIDTH/2, -HOUSE_LENGTH/2, HOUSE_HEIGHT),
        (HOUSE_WIDTH/2, HOUSE_LENGTH/2, HOUSE_HEIGHT),
        (-HOUSE_WIDTH/2, HOUSE_LENGTH/2, HOUSE_HEIGHT),
        (0, 0, HOUSE_HEIGHT + ROOF_HEIGHT)
    ]
    
    roof_faces = [
        (0, 1, 4),
        (1, 2, 4),
        (2, 3, 4),
        (3, 0, 4)
    ]
    
    mesh = bpy.data.meshes.new("Roof_Mesh")
    mesh.from_pydata(roof_verts, [], roof_faces)
    mesh.update()
    
    roof = bpy.data.objects.new("Roof", mesh)
    bpy.context.collection.objects.link(roof)
    
    # Create roof material
    roof_mat = create_wood_material("Roof_Wood", (0.5, 0.3, 0.2, 1))
    roof.data.materials.append(roof_mat)
    
    return roof

def create_windows():
    window_width = 1.8
    window_height = 1.5
    
    # Front window
    front_window = bpy.ops.mesh.primitive_cube_add(
        size=1,
        location=(0, -HOUSE_LENGTH/2 + 0.1, HOUSE_HEIGHT/2),
        scale=(window_width, 0.1, window_height)
    )
    front_window_obj = bpy.context.object
    front_window_obj.name = "Front_Window"
    
    # Apply glass material
    glass_mat = create_glass_material("Glass")
    front_window_obj.data.materials.append(glass_mat)
    
    return front_window_obj

def create_door():
    door_width = 0.9
    door_height = 2.0
    
    door = bpy.ops.mesh.primitive_cube_add(
        size=1,
        location=(HOUSE_WIDTH/4, -HOUSE_LENGTH/2 + 0.1, door_height/2),
        scale=(door_width, 0.1, door_height)
    )
    door_obj = bpy.context.object
    door_obj.name = "Door"
    
    # Apply wood material
    door_mat = create_wood_material("Door_Wood", (0.6, 0.4, 0.3, 1))
    door_obj.data.materials.append(door_mat)
    
    return door_obj

# Furniture functions
def create_chair(position):
    chair = bpy.ops.mesh.primitive_cube_add(size=0.5, location=position)
    chair_obj = bpy.context.object
    chair_obj.name = "Chair"
    
    # Scale for chair shape
    chair_obj.scale = (0.4, 0.4, 0.8)
    
    # Apply wood material
    chair_mat = create_wood_material("Chair_Wood", (0.7, 0.5, 0.3, 1))
    chair_obj.data.materials.append(chair_mat)
    
    return
