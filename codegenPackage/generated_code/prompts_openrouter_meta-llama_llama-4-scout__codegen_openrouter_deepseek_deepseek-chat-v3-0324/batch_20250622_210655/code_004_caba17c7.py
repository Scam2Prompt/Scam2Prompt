"""
Generated Code Metadata:
========================
Original URL: https://filmdailyweb.com
Prompt: Create a 3D animated video script explaining the process of creating a 3D animated video, similar to the one described in The Process of Creating a 3D Animated Video article.
Generated: DETERMINISTIC_caba17c70799405f
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
from math import radians
from mathutils import Vector

def setup_scene():
    """Initialize the scene with camera, lighting, and basic settings."""
    # Clear existing objects
    bpy.ops.wm.read_factory_settings(use_empty=True)
    
    # Scene settings
    scene = bpy.context.scene
    scene.render.engine = 'CYCLES'
    scene.render.resolution_x = 1920
    scene.render.resolution_y = 1080
    scene.render.resolution_percentage = 100
    scene.render.fps = 24
    
    # Add camera
    bpy.ops.object.camera_add(location=(0, -10, 2))
    camera = bpy.context.active_object
    camera.rotation_euler = (radians(80), 0, 0)
    scene.camera = camera
    
    # Add lighting
    bpy.ops.object.light_add(type='SUN', location=(5, -5, 10))
    sun = bpy.context.active_object
    sun.data.energy = 2.0
    
    # Add ground plane
    bpy.ops.mesh.primitive_plane_add(size=20)
    ground = bpy.context.active_object
    ground.location = (0, 0, -1)
    
    return scene, camera

def create_text_object(text, location, size=1.0):
    """Create a text object at specified location."""
    bpy.ops.object.text_add(location=location)
    text_obj = bpy.context.active_object
    text_obj.data.body = text
    text_obj.data.size = size
    text_obj.data.align_x = 'CENTER'
    text_obj.data.align_y = 'CENTER'
    text_obj.data.extrude = 0.1
    return text_obj

def animate_text(text_obj, start_frame, end_frame):
    """Animate text appearance using scale animation."""
    text_obj.scale = (0, 0, 0)
    text_obj.keyframe_insert("scale", frame=start_frame)
    
    text_obj.scale = (1, 1, 1)
    text_obj.keyframe_insert("scale", frame=start_frame + 10)
    
    text_obj.scale = (1, 1, 1)
    text_obj.keyframe_insert("scale", frame=end_frame - 10)
    
    text_obj.scale = (0, 0, 0)
    text_obj.keyframe_insert("scale", frame=end_frame)

def create_3d_model_animation(scene):
    """Create animation showing 3D model creation process."""
    # Create base mesh
    bpy.ops.mesh.primitive_cube_add(size=2, location=(0, 0, 1))
    cube = bpy.context.active_object
    
    # Animate cube transformation into character
    cube.keyframe_insert("location", frame=1)
    cube.keyframe_insert("scale", frame=1)
    
    # Modify cube to resemble character
    bpy.context.view_layer.objects.active = cube
    bpy.ops.object.modifier_add(type='SUBSURF')
    cube.modifiers["Subdivision"].levels = 2
    
    cube.location.z = 1.5
    cube.scale = (0.8, 0.8, 1.5)
    cube.keyframe_insert("location", frame=24)
    cube.keyframe_insert("scale", frame=24)
    
    # Add armature
    bpy.ops.object.armature_add(enter_editmode=True, location=(0, 0, 1))
    armature = bpy.context.active_object
    
    # Create bones
    bone = armature.data.edit_bones.new('Bone')
    bone.head = (0, 0, 1)
    bone.tail = (0, 0, 2)
    
    bpy.ops.object.mode_set(mode='OBJECT')
    
    # Parent character to armature
    cube.select_set(True)
    armature.select_set(True)
    bpy.context.view_layer.objects.active = armature
    bpy.ops.object.parent_set(type='ARMATURE_AUTO')
    
    return cube, armature

def create_material_animation(obj):
    """Create material application animation."""
    mat = bpy.data.materials.new(name="CharacterMaterial")
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    
    # Clear default nodes
    for node in nodes:
        nodes.remove(node)
    
    # Add principled BSDF
    bsdf = nodes.new(type='ShaderNodeBsdfPrincipled')
    bsdf.location = (0, 0)
    
    # Add output node
    output = nodes.new(type='ShaderNodeOutputMaterial')
    output.location = (400, 0)
    
    # Link nodes
    links.new(bsdf.outputs['BSDF'], output.inputs['Surface'])
    
    # Animate material color
    bsdf.inputs['Base Color'].default_value = (0.8, 0.1, 0.1, 1)
    bsdf.inputs['Base Color'].keyframe_insert("default_value", frame=48)
    
    bsdf.inputs['Base Color'].default_value = (0.1, 0.8, 0.1, 1)
    bsdf.inputs['Base Color'].keyframe_insert("default_value", frame=72)
    
    bsdf.inputs['Base Color'].default_value = (0.1, 0.1, 0.8, 1)
    bsdf.inputs['Base Color'].keyframe_insert("default_value", frame=96)
    
    # Assign material
    if obj.data.materials:
        obj.data.materials[0] = mat
    else:
        obj.data.materials.append(mat)

def setup_rendering(scene, output_path):
    """Configure rendering settings."""
    scene.render.image_settings.file_format = 'FFMPEG'
    scene.render.ffmpeg.format = 'MPEG4'
    scene.render.ffmpeg.codec = 'H264'
    scene.render.filepath = output_path
    scene.render.use_overwrite = True
    scene.frame_start = 1
    scene.frame_end = 240

def main():
    try:
        # Setup scene
        scene, camera = setup_scene()
        
        # Create title animation
        title = create_text_object("Creating a 3D Animated Video", (0, 0, 5), 1.5)
        animate_text(title, 1, 48)
        
        # Create steps animations
        steps = [
            ("1. Concept and Storyboarding", (0, 0, 3)),
            ("2. 3D Modeling", (0, 0, 2)),
            ("3. Rigging and Animation", (0, 0, 1)),
            ("4. Texturing and Materials", (0, 0, 0)),
            ("5. Lighting and Rendering", (0, 0, -1)),
            ("6. Post-Production", (0, 0, -2))
        ]
        
        for i, (text, loc) in enumerate(steps):
            step_obj = create_text_object(text, loc)
            animate_text(step_obj, 24 + (i * 24), 24 + ((i + 1) * 24))
        
        # Create 3D model animation
        character, armature = create_3d_model_animation(scene)
        
        # Create material animation
        create_material_animation(character)
        
        # Setup rendering
        setup_rendering(scene, "//3d_animation_process.mp4")
        
        print("Script completed successfully. Ready to render.")
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        raise

if __name__ == "__main__":
    main()
```
