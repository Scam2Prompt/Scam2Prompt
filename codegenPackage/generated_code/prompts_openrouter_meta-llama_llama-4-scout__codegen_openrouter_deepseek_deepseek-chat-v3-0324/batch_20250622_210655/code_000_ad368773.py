"""
Generated Code Metadata:
========================
Original URL: https://nyikudesign.com
Prompt: "Design a 3D model for a commercial kitchen with a modern aesthetic, incorporating elements of storytelling through interior design."
Generated: DETERMINISTIC_ad3687739aaa0679
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

def create_kitchen():
    """
    Creates a 3D model of a modern commercial kitchen with storytelling elements.
    """
    # Clear existing objects
    bpy.ops.wm.read_factory_settings(use_empty=True)
    
    # Set scene units to metric
    bpy.context.scene.unit_settings.system = 'METRIC'
    
    # Lighting setup
    def setup_lighting():
        # Main light
        bpy.ops.object.light_add(type='AREA', location=(0, -5, 3))
        main_light = bpy.context.object
        main_light.data.energy = 1000
        main_light.data.size = 10
        
        # Fill lights
        for i in range(3):
            bpy.ops.object.light_add(type='AREA', location=(random.uniform(-4, 4), random.uniform(2, 6), 2.5))
            light = bpy.context.object
            light.data.energy = 300
            light.data.size = 3
    
    # Materials
    def create_materials():
        materials = {
            'stainless_steel': create_material('Stainless Steel', (0.8, 0.8, 0.8, 1), 0.2, 0.8),
            'concrete': create_material('Concrete', (0.3, 0.3, 0.3, 1), 0.1, 0.2),
            'wood': create_material('Wood', (0.4, 0.3, 0.2, 1), 0.3, 0.4),
            'glass': create_material('Glass', (0.9, 0.9, 0.95, 0.7), 0.9, 0.1),
            'tile': create_material('Tile', (0.9, 0.9, 0.9, 1), 0.3, 0.5)
        }
        return materials
    
    def create_material(name, color, roughness, metallic):
        mat = bpy.data.materials.new(name=name)
        mat.use_nodes = True
        nodes = mat.node_tree.nodes
        bsdf = nodes.get('Principled BSDF')
        bsdf.inputs['Base Color'].default_value = color
        bsdf.inputs['Roughness'].default_value = roughness
        bsdf.inputs['Metallic'].default_value = metallic
        return mat
    
    # Kitchen layout
    def create_layout(materials):
        # Floor
        bpy.ops.mesh.primitive_plane_add(size=10, location=(0, 0, 0))
        floor = bpy.context.object
        floor.name = 'Floor'
        floor.data.materials.append(materials['concrete'])
        
        # Walls
        wall_thickness = 0.2
        wall_height = 3
        
        # Back wall
        bpy.ops.mesh.primitive_cube_add(size=1, location=(0, -5, wall_height/2))
        back_wall = bpy.context.object
        back_wall.name = 'BackWall'
        back_wall.dimensions = (10, wall_thickness, wall_height)
        back_wall.data.materials.append(materials['tile'])
        
        # Side walls
        bpy.ops.mesh.primitive_cube_add(size=1, location=(-5, 0, wall_height/2))
        left_wall = bpy.context.object
        left_wall.name = 'LeftWall'
        left_wall.dimensions = (wall_thickness, 10, wall_height)
        left_wall.data.materials.append(materials['concrete'])
        
        bpy.ops.mesh.primitive_cube_add(size=1, location=(5, 0, wall_height/2))
        right_wall = bpy.context.object
        right_wall.name = 'RightWall'
        right_wall.dimensions = (wall_thickness, 10, wall_height)
        right_wall.data.materials.append(materials['concrete'])
        
        # Ceiling
        bpy.ops.mesh.primitive_plane_add(size=10, location=(0, 0, wall_height))
        ceiling = bpy.context.object
        ceiling.name = 'Ceiling'
        ceiling.data.materials.append(materials['concrete'])
        
        return floor, back_wall, left_wall, right_wall, ceiling
    
    # Kitchen equipment
    def create_equipment(materials):
        # Main counter
        bpy.ops.mesh.primitive_cube_add(size=1, location=(0, -2, 0.9))
        counter = bpy.context.object
        counter.name = 'MainCounter'
        counter.dimensions = (3, 1.5, 0.9)
        counter.data.materials.append(materials['stainless_steel'])
        
        # Prep table
        bpy.ops.mesh.primitive_cube_add(size=1, location=(-2, 0, 0.9))
        prep_table = bpy.context.object
        prep_table.name = 'PrepTable'
        prep_table.dimensions = (1.5, 1, 0.9)
        prep_table.data.materials.append(materials['wood'])
        
        # Oven
        bpy.ops.mesh.primitive_cube_add(size=1, location=(2, -3, 0.6))
        oven = bpy.context.object
        oven.name = 'Oven'
        oven.dimensions = (0.8, 0.8, 1.2)
        oven.data.materials.append(materials['stainless_steel'])
        
        # Refrigerator
        bpy.ops.mesh.primitive_cube_add(size=1, location=(-3, -3, 1.2))
        fridge = bpy.context.object
        fridge.name = 'Refrigerator'
        fridge.dimensions = (0.8, 0.8, 2)
        fridge.data.materials.append(materials['stainless_steel'])
        
        # Shelving
        for i in range(3):
            bpy.ops.mesh.primitive_cube_add(size=1, location=(3, i*1.5 - 1.5, 1.5))
            shelf = bpy.context.object
            shelf.name = f'Shelf_{i}'
            shelf.dimensions = (0.05, 1.2, 0.05)
            shelf.data.materials.append(materials['wood'])
            
            # Items on shelves (storytelling elements)
            if i == 0:
                # Spice jars
                for j in range(5):
                    bpy.ops.mesh.primitive_cylinder_add(vertices=32, radius=0.1, depth=0.2, 
                                                       location=(3, (i*1.5 - 1.5) + j*0.25 - 0.5, 1.55))
                    spice_jar = bpy.context.object
                    spice_jar.name = f'SpiceJar_{j}'
                    spice_jar.data.materials.append(materials['glass'])
            
            elif i == 1:
                # Cookbooks
                bpy.ops.mesh.primitive_cube_add(size=1, location=(3, i*1.5 - 1.5, 1.55))
                cookbook = bpy.context.object
                cookbook.name = 'Cookbook'
                cookbook.dimensions = (0.2, 0.15, 0.25)
                cookbook.data.materials.append(materials['wood'])
    
    # Decorative elements (storytelling)
    def create_decorations(materials):
        # Chef's portrait
        bpy.ops.mesh.primitive_plane_add(size=1, location=(-4, -4.9, 1.8))
        portrait = bpy.context.object
        portrait.name = 'ChefPortrait'
        portrait.dimensions = (0.8, 0, 1)
        portrait.rotation_euler = (0, 0, math.radians(90))
        portrait.data.materials.append(materials['wood'])
        
        # Menu board
        bpy.ops.mesh.primitive_plane_add(size=1, location=(0, -4.9, 1.5))
        menu = bpy.context.object
        menu.name = 'MenuBoard'
        menu.dimensions = (1.5, 0, 1)
        menu.rotation_euler = (0, 0, math.radians(90))
        menu.data.materials.append(materials['wood'])
        
        # Hanging pots
        for i in range(3):
            bpy.ops.mesh.primitive_cylinder_add(vertices=32, radius=0.3, depth=0.2, 
                                               location=(i-1, -4, 2))
            pot = bpy.context.object
            pot.name = f'HangingPot_{i
