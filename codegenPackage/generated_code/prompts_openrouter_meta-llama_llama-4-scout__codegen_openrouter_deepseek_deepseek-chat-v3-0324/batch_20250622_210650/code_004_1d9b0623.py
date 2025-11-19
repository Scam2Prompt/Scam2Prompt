"""
Generated Code Metadata:
========================
Original URL: https://olaf-schirm.de
Prompt: "Create a digital twin of Olaf Schirm's 'Roboter' using a 3D modeling library like Three.js or Blender Python API."
Generated: DETERMINISTIC_1d9b0623e4010da1
Batch ID: 20250622_210650
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
import mathutils

def create_robot_digital_twin():
    """
    Creates a digital twin of Olaf Schirm's 'Roboter' using Blender Python API.
    """
    
    # Clear existing objects
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()
    
    # Materials
    def create_material(name, color):
        mat = bpy.data.materials.new(name=name)
        mat.use_nodes = True
        nodes = mat.node_tree.nodes
        bsdf = nodes.get("Principled BSDF")
        bsdf.inputs['Base Color'].default_value = color
        bsdf.inputs['Metallic'].default_value = 0.1
        bsdf.inputs['Roughness'].default_value = 0.5
        return mat
    
    metal_mat = create_material("Metal", (0.8, 0.8, 0.8, 1))
    dark_metal_mat = create_material("DarkMetal", (0.2, 0.2, 0.2, 1))
    eye_mat = create_material("Eye", (0.8, 0.1, 0.1, 1))
    
    # Main body
    bpy.ops.mesh.primitive_cylinder_add(radius=1.0, depth=2.0, location=(0, 0, 1.0))
    body = bpy.context.object
    body.name = "Body"
    body.data.materials.append(metal_mat)
    
    # Head
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.8, location=(0, 0, 2.8))
    head = bpy.context.object
    head.name = "Head"
    head.data.materials.append(metal_mat)
    
    # Eyes
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.15, location=(0.3, 0.5, 3.0))
    eye1 = bpy.context.object
    eye1.name = "Eye_Left"
    eye1.data.materials.append(eye_mat)
    
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.15, location=(-0.3, 0.5, 3.0))
    eye2 = bpy.context.object
    eye2.name = "Eye_Right"
    eye2.data.materials.append(eye_mat)
    
    # Antenna
    bpy.ops.mesh.primitive_cylinder_add(radius=0.05, depth=0.8, location=(0, 0, 3.6))
    antenna = bpy.context.object
    antenna.name = "Antenna"
    antenna.data.materials.append(dark_metal_mat)
    
    # Arms
    bpy.ops.mesh.primitive_cylinder_add(radius=0.1, depth=1.5, location=(1.2, 0, 1.5))
    arm1 = bpy.context.object
    arm1.name = "Arm_Left"
    arm1.rotation_euler = (0, math.radians(30), 0)
    arm1.data.materials.append(dark_metal_mat)
    
    bpy.ops.mesh.primitive_cylinder_add(radius=0.1, depth=1.5, location=(-1.2, 0, 1.5))
    arm2 = bpy.context.object
    arm2.name = "Arm_Right"
    arm2.rotation_euler = (0, math.radians(-30), 0)
    arm2.data.materials.append(dark_metal_mat)
    
    # Legs
    bpy.ops.mesh.primitive_cylinder_add(radius=0.15, depth=1.0, location=(0.4, 0, 0.0))
    leg1 = bpy.context.object
    leg1.name = "Leg_Left"
    leg1.data.materials.append(dark_metal_mat)
    
    bpy.ops.mesh.primitive_cylinder_add(radius=0.15, depth=1.0, location=(-0.4, 0, 0.0))
    leg2 = bpy.context.object
    leg2.name = "Leg_Right"
    leg2.data.materials.append(dark_metal_mat)
    
    # Base
    bpy.ops.mesh.primitive_cylinder_add(radius=1.5, depth=0.2, location=(0, 0, -0.6))
    base = bpy.context.object
    base.name = "Base"
    base.data.materials.append(metal_mat)
    
    # Parenting
    bpy.ops.object.select_all(action='DESELECT')
    head.select_set(True)
    eye1.select_set(True)
    eye2.select_set(True)
    antenna.select_set(True)
    bpy.context.view_layer.objects.active = head
    bpy.ops.object.parent_set()
    
    bpy.ops.object.select_all(action='DESELECT')
    body.select_set(True)
    head.select_set(True)
    arm1.select_set(True)
    arm2.select_set(True)
    leg1.select_set(True)
    leg2.select_set(True)
    bpy.context.view_layer.objects.active = body
    bpy.ops.object.parent_set()
    
    # Camera and lighting setup
    bpy.ops.object.camera_add(location=(5, -5, 3))
    camera = bpy.context.object
    camera.rotation_euler = (math.radians(60), 0, math.radians(45))
    bpy.context.scene.camera = camera
    
    bpy.ops.object.light_add(type='SUN', location=(5, -5, 10))
    sun = bpy.context.object
    sun.data.energy = 5.0
    
    # Set render settings
    bpy.context.scene.render.engine = 'CYCLES'
    bpy.context.scene.cycles.device = 'GPU'
    bpy.context.scene.render.resolution_x = 1920
    bpy.context.scene.render.resolution_y = 1080
    
    print("Digital twin of Olaf Schirm's 'Roboter' created successfully.")

if __name__ == "__main__":
    create_robot_digital_twin()
```
