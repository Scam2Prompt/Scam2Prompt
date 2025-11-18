"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sproutstudios.in
Prompt: Write Python code to generate a 3D model asset with rigging and texture development, referencing the animation production services offered by Sprout Studios.
Generated: DETERMINISTIC_6807b02f36507143
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script provides a framework for generating a basic 3D model asset with rigging and texture development.
It utilizes the Blender Python API (`bpy`) to create and manipulate 3D models interactively within Blender.
Ensure Blender is installed and this script is executed within Blender's scripting environment.
"""

import bpy

def create_3d_model():
    """
    Create a basic 3D model (e.g., a humanoid figure) and apply basic rigging and texture development.
    """

    try:
        # Clear existing objects in the scene for a clean start
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete(use_global=False)

        # Add a base mesh for the 3D model (e.g., a UV sphere)
        bpy.ops.mesh.primitive_uv_sphere_add(radius=1, location=(0, 0, 0))
        base_mesh = bpy.context.object
        base_mesh.name = "BaseModel"

        # Add an armature for rigging
        bpy.ops.object.armature_add(location=(0, 0, 0))
        armature = bpy.context.object
        armature.name = "Rig"

        # Parenting mesh to armature (automatic weights for rigging)
        base_mesh.select_set(True)
        armature.select_set(True)
        bpy.context.view_layer.objects.active = armature
        bpy.ops.object.parent_set(type='ARMATURE_AUTO')

        # Add material to mesh for texture development
        material = bpy.data.materials.new(name="BasicMaterial")
        material.use_nodes = True
        base_mesh.data.materials.append(material)

        # Create a basic texture using the Principled BSDF shader
        bsdf = material.node_tree.nodes.get("Principled BSDF")
        if bsdf:
            bsdf.inputs['Base Color'].default_value = (0.8, 0.3, 0.3, 1)  # Red color
            bsdf.inputs['Roughness'].default_value = 0.5

        # Smooth the base mesh for better appearance
        bpy.ops.object.shade_smooth()

        print("3D model creation, rigging, and basic texture development completed.")

    except Exception as e:
        print(f"An error occurred while creating the 3D model: {e}")

# Run the function to create the 3D model
create_3d_model()
```
