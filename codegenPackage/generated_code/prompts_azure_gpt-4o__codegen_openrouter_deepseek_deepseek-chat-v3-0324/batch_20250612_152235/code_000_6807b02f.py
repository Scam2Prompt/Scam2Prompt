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
from mathutils import Vector

class Sprout3DModelGenerator:
    """
    A class to generate 3D models with rigging and textures inspired by Sprout Studios' animation services.
    """
    
    def __init__(self, model_name="SproutCharacter"):
        self.model_name = model_name
        self.texture_path = None
        self.rig = None
        
    def create_base_mesh(self):
        """Create a basic humanoid mesh for the character."""
        bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=True)
        bpy.ops.mesh.subdivide(number_cuts=3)
        bpy.ops.mesh.to_curve()
        bpy.context.object.name = self.model_name
        
    def setup_rigging(self):
        """Setup armature and basic rigging for the character."""
        # Create armature
        bpy.ops.object.armature_add(enter_editmode=True)
        self.rig = bpy.context.object
        self.rig.name = f"{self.model_name}_Rig"
        
        # Create bones
        bpy.ops.armature.bone_primitive_add()
        root_bone = self.rig.data.edit_bones[-1]
        root_bone.name = "Root"
        
        # Spine bones
        for i in range(3):
            bpy.ops.armature.extrude_move(
                ARMATURE_OT_extrude={"forked": False},
                TRANSFORM_OT_translate={"value": (0, 0, 0.5)}
            )
            self.rig.data.edit_bones[-1].name = f"Spine_{i+1}"
        
        # Exit edit mode
        bpy.ops.object.mode_set(mode='OBJECT')
        
        # Parent mesh to armature
        mesh = bpy.data.objects[self.model_name]
        modifier = mesh.modifiers.new(type='ARMATURE', name="Armature")
        modifier.object = self.rig
        mesh.parent = self.rig
        
        # Automatic weights
        bpy.context.view_layer.objects.active = mesh
        bpy.ops.object.mode_set(mode='POSE')
        bpy.ops.pose.armature_apply()
        bpy.ops.object.mode_set(mode='OBJECT')
        
    def apply_texture(self, texture_path=None):
        """Apply texture to the model."""
        if texture_path and os.path.exists(texture_path):
            self.texture_path = texture_path
            
            # Create material
            mat = bpy.data.materials.new(name=f"{self.model_name}_Material")
            mat.use_nodes = True
            bsdf = mat.node_tree.nodes.get('Principled BSDF')
            
            # Add texture
            tex_image = mat.node_tree.nodes.new('ShaderNodeTexImage')
            tex_image.image = bpy.data.images.load(texture_path)
            mat.node_tree.links.new(bsdf.inputs['Base Color'], tex_image.outputs['Color'])
            
            # Assign to object
            obj = bpy.data.objects[self.model_name]
            if obj.data.materials:
                obj.data.materials[0] = mat
            else:
                obj.data.materials.append(mat)
        else:
            print("Warning: Texture path not provided or invalid. Using default material.")
            
    def setup_animation(self):
        """Setup basic animation controls."""
        if not self.rig:
            print("Error: Rig not created. Cannot setup animation.")
            return
            
        bpy.context.view_layer.objects.active = self.rig
        bpy.ops.object.mode_set(mode='POSE')
        
        # Create animation action
        action = bpy.data.actions.new(name=f"{self.model_name}_Action")
        self.rig.animation_data_create()
        self.rig.animation_data.action = action
        
    def export_model(self, output_path, format='FBX'):
        """Export the model to specified format."""
        if not os.path.exists(os.path.dirname(output_path)):
            os.makedirs(os.path.dirname(output_path))
            
        bpy.ops.object.select_all(action='DESELECT')
        bpy.data.objects[self.model_name].select_set(True)
        self.rig.select_set(True)
        
        if format.upper() == 'FBX':
            bpy.ops.export_scene.fbx(
                filepath=output_path,
                use_selection=True,
                apply_scale_options='FBX_SCALE_ALL',
                bake_anim=True,
                add_leaf_bones=False
            )
        elif format.upper() == 'OBJ':
            bpy.ops.export_scene.obj(
                filepath=output_path,
                use_selection=True,
                use_materials=True
            )
        else:
            raise ValueError(f"Unsupported export format: {format}")

def generate_sprout_character(model_name, texture_path=None, output_path=None):
    """
    Generate a complete 3D character with rigging and textures.
    
    Args:
        model_name (str): Name for the model
        texture_path (str, optional): Path to texture image
        output_path (str, optional): Path to save exported model
    """
    try:
        # Clear existing objects
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete()
        
        generator = Sprout3DModelGenerator(model_name)
        generator.create_base_mesh()
        generator.setup_rigging()
        
        if texture_path:
            generator.apply_texture(texture_path)
            
        generator.setup_animation()
        
        if output_path:
            generator.export_model(output_path)
            
        return generator
    except Exception as e:
        print(f"Error generating character: {str(e)}")
        return None

# Example usage
if __name__ == "__main__":
    # This would be run within Blender's Python environment
    generate_sprout_character(
        model_name="SproutCharacter",
        texture_path="/path/to/texture.png",
        output_path="/path/to/export/character.fbx"
    )
```
