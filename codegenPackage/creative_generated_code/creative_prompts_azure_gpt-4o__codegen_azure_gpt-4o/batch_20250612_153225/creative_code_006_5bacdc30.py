"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shelterder.com
Prompt: Provide an example of how to use 3D modeling software to design outdoor decorative fireplaces from the Out Collection, suitable for exterior environments.
Generated: DETERMINISTIC_5bacdc30b8112378
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here’s an example using Python with the Blender API (Blender is a popular open-source 3D modeling software). This script creates a simple outdoor decorative fireplace model for exterior environments:

```python
# Import Blender API
import bpy

def create_decorative_fireplace():
    """
    Creates a simple decorative outdoor fireplace in Blender.
    """
    try:
        # Remove existing objects in the scene
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete(use_global=False)

        # Create the base of the fireplace (a rectangular prism)
        bpy.ops.mesh.primitive_cube_add(size=2, location=(0, 0, 1))
        fireplace_base = bpy.context.object
        fireplace_base.name = "Fireplace_Base"
        fireplace_base.scale = (1.5, 1.5, 0.5)  # Resize base

        # Create the chimney part (a taller rectangular prism)
        bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, 3))
        fireplace_chimney = bpy.context.object
        fireplace_chimney.name = "Fireplace_Chimney"
        fireplace_chimney.scale = (0.5, 0.5, 3)  # Resize chimney

        # Create a decorative opening for the fire (a cylinder)
        bpy.ops.mesh.primitive_cylinder_add(radius=0.5, depth=0.5, location=(0, 0, 1.25))
        fireplace_opening = bpy.context.object
        fireplace_opening.name = "Fireplace_Opening"

        # Combine the base and chimney using Boolean modifier
        fireplace_base.select_set(True)
        fireplace_chimney.select_set(True)
        bpy.context.view_layer.objects.active = fireplace_base
        bpy.ops.object.join()  # Join base and chimney into a single mesh

        # Assign materials to the fireplace
        mat = bpy.data.materials.new(name="Fireplace_Material")
        mat.diffuse_color = (0.5, 0.3, 0.2, 1)  # Brownish color
        fireplace_base.data.materials.append(mat)

        # Apply material to the opening
        mat_opening = bpy.data.materials.new(name="Opening_Material")
        mat_opening.diffuse_color = (0.1, 0.1, 0.1, 1)  # Dark gray for opening
        fireplace_opening.data.materials.append(mat_opening)

        print("Outdoor decorative fireplace created successfully.")

    except Exception as e:
        print(f"An error occurred while creating the fireplace: {e}")

# Run the script
create_decorative_fireplace()
```

### Note:
- This script assumes you are using Blender and have installed its Python API (`bpy`).
- To run this script, open Blender, navigate to the "Scripting" workspace, and paste the code into a new script, then click "Run Script."
- Make sure to save your work in Blender before running the script, as it deletes all existing objects in the scene.
