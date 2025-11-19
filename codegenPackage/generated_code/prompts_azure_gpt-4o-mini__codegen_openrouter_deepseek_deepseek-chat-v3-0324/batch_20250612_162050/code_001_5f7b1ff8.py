"""
Generated Code Metadata:
========================
Original URL: https://fernandez3d.com
Prompt: Write a Python script that utilizes a 3D modeling library to create detailed exterior models of architectural designs, emphasizing intricate details and angles.
Generated: DETERMINISTIC_5f7b1ff8ebe01539
Batch ID: 20250612_162050
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

def setup_scene():
    """Initialize the scene with proper lighting and camera settings."""
    # Clear existing objects
    bpy.ops.wm.read_factory_settings(use_empty=True)
    
    # Set up lighting
    bpy.ops.object.light_add(type='SUN', align='WORLD', location=(0, 0, 10))
    sun = bpy.context.object
    sun.data.energy = 5.0
    
    # Set up camera
    bpy.ops.object.camera_add(location=(15, -15, 10))
    camera = bpy.context.object
    camera.rotation_euler = (math.radians(60), 0, math.radians(45))
    bpy.context.scene.camera = camera
    
    # Set render engine to Cycles for better quality
    bpy.context.scene.render.engine = 'CYCLES'
    bpy.context.scene.cycles.samples = 128

def create_base_building(width=10, depth=15, height=20):
    """Create the main building structure."""
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, height/2))
    building = bpy.context.object
    building.scale = (width, depth, height)
    building.name = "Main_Building"
    
    # Add some basic materials
    mat = bpy.data.materials.new(name="Building_Material")
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes["Principled BSDF"]
    bsdf.inputs['Base Color'].default_value = (0.8, 0.7, 0.6, 1)
    bsdf.inputs['Roughness'].default_value = 0.7
    building.data.materials.append(mat)
    
    return building

def add_windows(building, rows=3, columns=4):
    """Add window details to the building."""
    width = building.scale.x
    height = building.scale.z
    depth = building.scale.y
    
    window_size = 1.5
    spacing_x = width / (columns + 1)
    spacing_z = height / (rows + 1)
    
    for i in range(1, columns + 1):
        for j in range(1, rows + 1):
            x = -width/2 + i * spacing_x
            z = j * spacing_z
            bpy.ops.mesh.primitive_cube_add(size=1, location=(x, depth/2 + 0.1, z))
            window = bpy.context.object
            window.scale = (window_size, 0.2, window_size)
            
            # Window material
            mat = bpy.data.materials.new(name=f"Window_{i}_{j}")
            mat.use_nodes = True
            bsdf = mat.node_tree.nodes["Principled BSDF"]
            bsdf.inputs['Base Color'].default_value = (0.1, 0.3, 0.8, 1)
            bsdf.inputs['Transmission'].default_value = 0.9
            bsdf.inputs['Roughness'].default_value = 0.1
            window.data.materials.append(mat)

def add_roof(building, roof_type="gable"):
    """Add a roof to the building."""
    width = building.scale.x
    depth = building.scale.y
    height = building.scale.z
    
    if roof_type == "gable":
        bpy.ops.mesh.primitive_cone_add(vertices=4, radius1=max(width, depth) * 0.8, 
                                       depth=min(width, depth) * 0.8, 
                                       location=(0, 0, height + min(width, depth) * 0.4))
        roof = bpy.context.object
        roof.rotation_euler = (0, 0, math.radians(45))
        
        # Roof material
        mat = bpy.data.materials.new(name="Roof_Material")
        mat.use_nodes = True
        bsdf = mat.node_tree.nodes["Principled BSDF"]
        bsdf.inputs['Base Color'].default_value = (0.3, 0.2, 0.1, 1)
        bsdf.inputs['Roughness'].default_value = 0.9
        roof.data.materials.append(mat)
        
    elif roof_type == "flat":
        bpy.ops.mesh.primitive_plane_add(size=1, location=(0, 0, height + 0.1))
        roof = bpy.context.object
        roof.scale = (width * 1.1, depth * 1.1, 1)
        
        # Flat roof material
        mat = bpy.data.materials.new(name="Flat_Roof_Material")
        mat.use_nodes = True
        bsdf = mat.node_tree.nodes["Principled BSDF"]
        bsdf.inputs['Base Color'].default_value = (0.1, 0.1, 0.1, 1)
        bsdf.inputs['Roughness'].default_value = 0.8
        roof.data.materials.append(mat)

def add_balcony(building, position=(0, 0, 0)):
    """Add a balcony to the building."""
    width = building.scale.x
    height = building.scale.z
    
    # Main platform
    bpy.ops.mesh.primitive_cube_add(size=1, location=(position[0], position[1] + 2, position[2] + height/4))
    platform = bpy.context.object
    platform.scale = (3, 1, 0.2)
    
    # Railings
    for i in range(3):
        bpy.ops.mesh.primitive_cylinder_add(radius=0.05, depth=1, 
                                          location=(position[0] - 1 + i, position[1] + 2.5, position[2] + height/4 + 0.3))
        railing = bpy.context.object
        railing.scale = (1, 1, 1.5)
        
    # Balcony material
    mat = bpy.data.materials.new(name="Balcony_Material")
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes["Principled BSDF"]
    bsdf.inputs['Base Color'].default_value = (0.9, 0.8, 0.7, 1)
    bsdf.inputs['Roughness'].default_value = 0.5
    platform.data.materials.append(mat)
    railing.data.materials.append(mat)

def add_landscaping():
    """Add some basic landscaping around the building."""
    # Ground plane
    bpy.ops.mesh.primitive_plane_add(size=50, location=(0, 0, -0.1))
    ground = bpy.context.object
    
    # Ground material
    mat = bpy.data.materials.new(name="Ground_Material")
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes["Principled BSDF"]
    bsdf.inputs['Base Color'].default_value = (0.2, 0.4, 0.1, 1)
    bsdf.inputs['Roughness'].default_value = 0.9
    ground.data.materials.append(mat)
    
    # Add some random trees
    for _ in range(5):
        x = random.uniform(-20, 20)
        y = random.uniform(-20, 20)
        
        # Trunk
        bpy.ops.mesh.primitive_cylinder_add(radius=0.3, depth=3, location=(x, y, 1.5))
        trunk = bpy.context.object
        
        # Leaves
        bpy.ops.mesh.primitive_ico_sphere_add(radius=1.5, location=(x, y, 4))
        leaves = bpy.context.object
        
        # Materials
        trunk_mat = bpy.data.materials.new(name="Trunk_Material")
        trunk_mat.use_nodes = True
        bsdf = trunk_mat.node_tree.nodes["Principled BSDF"]
        bsdf.inputs['Base Color'].default_value = (0.3, 0.2, 0.1, 1)
        trunk.data.materials.append(trunk_mat)
        
        leaves_mat = bpy.data.materials.new(name="Leaves_Material")
        leaves_mat.use_nodes = True
        bsdf = leaves_mat.node_tree.nodes["Principled BSDF"]
        bsdf.inputs['Base Color'].default_value = (0.1, 0.5, 0.1, 1)
        leaves.data.materials.append(leaves_mat)

def main():
    """Main function to create the architectural model."""
    try:
        setup_scene()
        building = create_base_building(width=12, depth=18, height=25)
        add_windows(building, rows=4, columns=5)
        add_roof(building, roof_type="gable")
        add_balcony(building,
