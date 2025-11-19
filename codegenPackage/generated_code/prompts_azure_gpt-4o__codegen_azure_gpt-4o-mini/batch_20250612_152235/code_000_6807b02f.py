"""
Generated Code Metadata:
========================
Original URL: https://sproutstudios.in
Prompt: Write Python code to generate a 3D model asset with rigging and texture development, referencing the animation production services offered by Sprout Studios.
Generated: DETERMINISTIC_6807b02f36507143
Batch ID: 20250612_152235
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

# Constants for the asset generation
ASSET_NAME = "My3DModel"
TEXTURE_PATH = "path/to/your/texture.png"
RIGGING_BONE_COUNT = 5

def create_3d_model():
    """Create a simple 3D model (a cube) in Blender."""
    try:
        # Delete existing objects
        bpy.ops.object.select_all(action='DESELECT')
        bpy.ops.object.select_by_type(type='MESH')
        bpy.ops.object.delete()

        # Create a cube
        bpy.ops.mesh.primitive_cube_add(size=2)
        model = bpy.context.object
        model.name = ASSET_NAME

        return model
    except Exception as e:
        print(f"Error creating 3D model: {e}")

def apply_texture(model):
    """Apply a texture to the given model."""
    try:
        # Load the texture image
        if not os.path.exists(TEXTURE_PATH):
            raise FileNotFoundError(f"Texture file not found: {TEXTURE_PATH}")

        # Create a new material
        material = bpy.data.materials.new(name="ModelMaterial")
        material.use_nodes = True
        bsdf = material.node_tree.nodes.get("Principled BSDF")

        # Load the texture image
        img = bpy.data.images.load(TEXTURE_PATH)
        texture_node = material.node_tree.nodes.new('ShaderNodeTexImage')
        texture_node.image = img

        # Connect the texture to the material
        material.node_tree.links.new(bsdf.inputs['Base Color'], texture_node.outputs['Color'])

        # Assign the material to the model
        if model.data.materials:
            model.data.materials[0] = material
        else:
            model.data.materials.append(material)

    except Exception as e:
        print(f"Error applying texture: {e}")

def create_rig(model):
    """Create a simple rig for the model."""
    try:
        # Create an armature
        bpy.ops.object.armature_add()
        armature = bpy.context.object
        armature.name = f"{ASSET_NAME}_Armature"

        # Enter edit mode to create bones
        bpy.ops.object.mode_set(mode='EDIT')
        for i in range(RIGGING_BONE_COUNT):
            bone = armature.data.edit_bones.new(f"Bone.{i}")
            bone.head = (0, 0, i)
            bone.tail = (0, 0, i + 1)

        # Return to object mode
        bpy.ops.object.mode_set(mode='OBJECT')

        # Parent the model to the armature
        bpy.ops.object.select_all(action='DESELECT')
        model.select_set(True)
        armature.select_set(True)
        bpy.context.view_layer.objects.active = armature
        bpy.ops.object.parent_set(type='ARMATURE_AUTO')

    except Exception as e:
        print(f"Error creating rig: {e}")

def main():
    """Main function to generate the 3D model asset."""
    model = create_3d_model()
    if model:
        apply_texture(model)
        create_rig(model)

# Run the main function
if __name__ == "__main__":
    main()
```

**Note:** Ensure that you have Blender installed and running this script in Blender's scripting environment. Adjust the `TEXTURE_PATH` to point to a valid texture image on your system.
