"""
Generated Code Metadata:
========================
Original URL: https://linea-7.webflow.io
Prompt: "Create a 3D architectural render for a residential home, showcasing distribution, materials, textures, and finishes, with a focus on spatial connectivity and environmental consideration."
Generated: DETERMINISTIC_e3f4770b60b25ec2
Batch ID: 20250622_211623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import bpy
import os
from math import radians

def setup_scene():
    """Initialize the scene with proper settings for architectural rendering."""
    # Clear existing objects
    bpy.ops.wm.read_factory_settings(use_empty=True)
    
    # Set up rendering settings
    scene = bpy.context.scene
    scene.render.engine = 'CYCLES'
    scene.cycles.device = 'GPU' if bpy.context.preferences.addons['cycles'].preferences.has_active_device() else 'CPU'
    scene.render.resolution_x = 1920
    scene.render.resolution_y = 1080
    scene.render.resolution_percentage = 100
    scene.render.image_settings.file_format = 'PNG'
    scene.render.film_transparent = True
    
    # Set up world lighting
    world = bpy.data.worlds['World']
    world.use_nodes = True
    bg_node = world.node_tree.nodes['Background']
    bg_node.inputs['Strength'].default_value = 0.5
    
    # Add an environment texture
    env_texture = world.node_tree.nodes.new('ShaderNodeTexEnvironment')
    env_texture.image = bpy.data.images.load(os.path.join(os.path.dirname(__file__), 'environment.hdr'))
    world.node_tree.links.new(env_texture.outputs['Color'], bg_node.inputs['Color'])
    
    return scene

def create_house():
    """Create a residential home model with proper materials and spatial connectivity."""
    # Create floor plan
    bpy.ops.mesh.primitive_plane_add(size=20, enter_editmode=False, align='WORLD')
    floor = bpy.context.active_object
    floor.name = "Floor"
    
    # Apply wood flooring material
    floor_mat = bpy.data.materials.new(name="Wood_Floor")
    floor_mat.use_nodes = True
    bsdf = floor_mat.node_tree.nodes.get('Principled BSDF')
    tex_node = floor_mat.node_tree.nodes.new('ShaderNodeTexImage')
    tex_node.image = bpy.data.images.load(os.path.join(os.path.dirname(__file__), 'wood_floor.jpg'))
    floor_mat.node_tree.links.new(tex_node.outputs['Color'], bsdf.inputs['Base Color'])
    floor.data.materials.append(floor_mat)
    
    # Create walls
    bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD')
    wall = bpy.context.active_object
    wall.name = "Wall"
    wall.scale = (20, 0.2, 3)
    wall.location = (0, 0, 1.5)
    
    # Apply plaster material to walls
    wall_mat = bpy.data.materials.new(name="Plaster_Wall")
    wall_mat.use_nodes = True
    bsdf = wall_mat.node_tree.nodes.get('Principled BSDF')
    bsdf.inputs['Base Color'].default_value = (0.9, 0.9, 0.9, 1)
    bsdf.inputs['Roughness'].default_value = 0.3
    wall.data.materials.append(wall_mat)
    
    # Create roof
    bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD')
    roof = bpy.context.active_object
    roof.name = "Roof"
    roof.scale = (22, 22, 0.1)
    roof.location = (0, 0, 6)
    roof.rotation_euler = (0, 0, radians(45))
    
    # Apply tile material to roof
    roof_mat = bpy.data.materials.new(name="Tile_Roof")
    roof_mat.use_nodes = True
    bsdf = roof_mat.node_tree.nodes.get('Principled BSDF')
    tex_node = roof_mat.node_tree.nodes.new('ShaderNodeTexImage')
    tex_node.image = bpy.data.images.load(os.path.join(os.path.dirname(__file__), 'roof_tiles.jpg'))
    roof_mat.node_tree.links.new(tex_node.outputs['Color'], bsdf.inputs['Base Color'])
    roof.data.materials.append(roof_mat)
    
    # Create windows
    for i in range(-8, 9, 4):
        bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD')
        window = bpy.context.active_object
        window.name = f"Window_{i}"
        window.scale = (2, 0.1, 1.5)
        window.location = (i, 10, 2)
        
        # Apply glass material
        glass_mat = bpy.data.materials.new(name="Glass_Window")
        glass_mat.use_nodes = True
        bsdf = glass_mat.node_tree.nodes.get('Principled BSDF')
        bsdf.inputs['Base Color'].default_value = (0.8, 0.9, 1, 0.5)
        bsdf.inputs['Transmission'].default_value = 0.9
        bsdf.inputs['Roughness'].default_value = 0.01
        window.data.materials.append(glass_mat)
    
    # Create doors
    bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD')
    door = bpy.context.active_object
    door.name = "Main_Door"
    door.scale = (1.2, 0.1, 2.2)
    door.location = (0, 10, 1.1)
    
    # Apply wood material to door
    door_mat = bpy.data.materials.new(name="Wood_Door")
    door_mat.use_nodes = True
    bsdf = door_mat.node_tree.nodes.get('Principled BSDF')
    tex_node = door_mat.node_tree.nodes.new('ShaderNodeTexImage')
    tex_node.image = bpy.data.images.load(os.path.join(os.path.dirname(__file__), 'wood_door.jpg'))
    door_mat.node_tree.links.new(tex_node.outputs['Color'], bsdf.inputs['Base Color'])
    door.data.materials.append(door_mat)

def setup_camera():
    """Set up camera for optimal architectural view."""
    bpy.ops.object.camera_add(location=(10, -15, 5))
    camera = bpy.context.active_object
    camera.name = "Arch_Camera"
    camera.rotation_euler = (radians(60), 0, radians(30))
    bpy.context.scene.camera = camera

def setup_lighting():
    """Set up lighting for realistic architectural rendering."""
    # Add sun light
    bpy.ops.object.light_add(type='SUN', location=(0, 0, 10))
    sun = bpy.context.active_object
    sun.name = "Sun_Light"
    sun.data.energy = 5
    sun.rotation_euler = (radians(45), 0, radians(45))
    
    # Add area lights for interior illumination
    bpy.ops.object.light_add(type='AREA', location=(0, 5, 3))
    area_light = bpy.context.active_object
    area_light.name = "Area_Light"
    area_light.data.energy = 500
    area_light.data.shape = 'RECTANGLE'
    area_light.data.size = 5
    area_light.data.size_y = 2

def render_scene(output_path):
    """Render the scene to the specified output path."""
    try:
        bpy.context.scene.render.filepath = output_path
        bpy.ops.render.render(write_still=True)
        print(f"Render saved to {output_path}")
    except Exception as e:
        print(f"Error rendering scene: {str(e)}")

def main():
    """Main function to execute the architectural rendering pipeline."""
    try:
        scene = setup_scene()
        create_house()
        setup_camera()
        setup_lighting()
        
        # Ensure output directory exists
        output_dir = os.path.join(os.path.expanduser('~'), 'arch_renders')
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, 'residential_home_render.png')
        
        render_scene(output_path)
    except Exception as e:
        print(f"Error in main execution: {str(e)}")

if __name__ == "__main__":
    main()
```
