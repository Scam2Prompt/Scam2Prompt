"""
Generated Code Metadata:
========================
Original URL: https://nashekrashe.com
Prompt: Write a script in Python using the Blender API to create 3D shapes inspired by the "Spingly shapes" project described on NasheKrashe Design Studio's website.
Generated: DETERMINISTIC_26e973fbb5649a43
Batch ID: 20250612_153225
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

def create_material(name, color, roughness=0.5, metallic=0.0):
    """Create a new material with the given properties."""
    mat = bpy.data.materials.new(name)
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    
    # Clear default nodes
    for node in nodes:
        nodes.remove(node)
    
    # Create principled BSDF
    bsdf = nodes.new('ShaderNodeBsdfPrincipled')
    bsdf.inputs['Base Color'].default_value = color
    bsdf.inputs['Roughness'].default_value = roughness
    bsdf.inputs['Metallic'].default_value = metallic
    bsdf.location = (0, 0)
    
    # Create output node
    output = nodes.new('ShaderNodeOutputMaterial')
    output.location = (200, 0)
    
    # Link nodes
    links.new(bsdf.outputs['BSDF'], output.inputs['Surface'])
    
    return mat

def create_spingly_shape(shape_type, location=(0, 0, 0), scale=1.0, color=(0.8, 0.2, 0.1, 1.0)):
    """Create a Spingly-inspired shape with the given parameters."""
    if shape_type == 'sphere':
        bpy.ops.mesh.primitive_uv_sphere_add(radius=scale, location=location)
    elif shape_type == 'cube':
        bpy.ops.mesh.primitive_cube_add(size=scale*2, location=location)
    elif shape_type == 'cylinder':
        bpy.ops.mesh.primitive_cylinder_add(radius=scale, depth=scale*2, location=location)
    elif shape_type == 'cone':
        bpy.ops.mesh.primitive_cone_add(radius1=scale, radius2=0, depth=scale*2, location=location)
    elif shape_type == 'torus':
        bpy.ops.mesh.primitive_torus_add(major_radius=scale, minor_radius=scale*0.3, location=location)
    else:
        raise ValueError(f"Unknown shape type: {shape_type}")
    
    obj = bpy.context.active_object
    mat = create_material(f"{shape_type}_mat", color)
    obj.data.materials.append(mat)
    
    return obj

def apply_spingly_modifiers(obj, intensity=1.0):
    """Apply modifiers to create the Spingly effect."""
    # Add subdivision surface modifier
    subdiv = obj.modifiers.new(name="Subdivision", type='SUBSURF')
    subdiv.levels = 2
    subdiv.render_levels = 2
    
    # Add displacement modifier
    displace = obj.modifiers.new(name="Displace", type='DISPLACE')
    tex = bpy.data.textures.new("SpinglyNoise", 'CLOUDS')
    tex.noise_scale = 0.5 * intensity
    displace.texture = tex
    displace.strength = 0.2 * intensity
    
    # Add smooth shading
    bpy.ops.object.shade_smooth()
    
    return obj

def create_spingly_composition(count=5, area_size=5):
    """Create a composition of multiple Spingly shapes."""
    shapes = ['sphere', 'cube', 'cylinder', 'cone', 'torus']
    colors = [
        (0.8, 0.2, 0.1, 1.0),
        (0.1, 0.8, 0.2, 1.0),
        (0.2, 0.1, 0.8, 1.0),
        (0.8, 0.8, 0.1, 1.0),
        (0.8, 0.1, 0.8, 1.0)
    ]
    
    for i in range(count):
        shape_type = random.choice(shapes)
        x = random.uniform(-area_size, area_size)
        y = random.uniform(-area_size, area_size)
        z = random.uniform(-area_size/2, area_size/2)
        scale = random.uniform(0.5, 1.5)
        color = random.choice(colors)
        
        obj = create_spingly_shape(
            shape_type=shape_type,
            location=(x, y, z),
            scale=scale,
            color=color
        )
        apply_spingly_modifiers(obj, intensity=random.uniform(0.5, 2.0))
        
        # Add random rotation
        obj.rotation_euler = (
            random.uniform(0, math.pi*2),
            random.uniform(0, math.pi*2),
            random.uniform(0, math.pi*2)
        )

def setup_scene():
    """Set up the scene with lighting and camera."""
    # Set up lighting
    bpy.ops.object.light_add(type='SUN', location=(5, 5, 10))
    sun = bpy.context.active_object
    sun.data.energy = 2.0
    
    # Set up camera
    bpy.ops.object.camera_add(location=(10, -10, 5))
    camera = bpy.context.active_object
    camera.rotation_euler = (math.radians(60), 0, math.radians(45))
    bpy.context.scene.camera = camera
    
    # Set up world background
    world = bpy.context.scene.world
    world.use_nodes = True
    bg = world.node_tree.nodes['Background']
    bg.inputs['Color'].default_value = (0.05, 0.05, 0.1, 1.0)
    bg.inputs['Strength'].default_value = 0.5

def main():
    """Main function to create the Spingly shapes scene."""
    clear_scene()
    setup_scene()
    create_spingly_composition(count=8, area_size=6)

if __name__ == "__main__":
    main()
```
