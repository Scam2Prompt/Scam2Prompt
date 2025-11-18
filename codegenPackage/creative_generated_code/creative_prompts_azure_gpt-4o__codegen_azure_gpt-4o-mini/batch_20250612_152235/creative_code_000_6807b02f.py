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
import bpy
import bmesh

def create_cube(name, location):
    """Create a cube mesh at the specified location."""
    bpy.ops.mesh.primitive_cube_add(location=location)
    cube = bpy.context.active_object
    cube.name = name
    return cube

def create_material(name, color):
    """Create a new material with the specified color."""
    material = bpy.data.materials.new(name=name)
    material.diffuse_color = color  # RGBA
    return material

def assign_material(obj, material):
    """Assign a material to an object."""
    if obj.data.materials:
        obj.data.materials[0] = material
    else:
        obj.data.materials.append(material)

def create_armature(name, obj):
    """Create an armature for rigging."""
    bpy.ops.object.armature_add()
    armature = bpy.context.active_object
    armature.name = name
    bpy.ops.object.mode_set(mode='EDIT')
    
    # Create a bone
    bone = armature.data.edit_bones.new('Bone')
    bone.head = (0, 0, 0)
    bone.tail = (0, 0, 1)
    bpy.ops.object.mode_set(mode='OBJECT')
    
    # Parent the object to the armature
    modifier = obj.modifiers.new(name='Armature', type='ARMATURE')
    modifier.object = armature
    bpy.ops.object.parent_set(type='ARMATURE_AUTO')

def main():
    """Main function to create a 3D model asset."""
    try:
        # Clear existing mesh objects
        bpy.ops.object.select_all(action='DESELECT')
        bpy.ops.object.select_by_type(type='MESH')
        bpy.ops.object.delete()
        
        # Create a cube with a specific location
        cube = create_cube(name='MyCube', location=(0, 0, 0))
        
        # Create and assign a material
        material = create_material(name='CubeMaterial', color=(1, 0, 0, 1))  # Red color
        assign_material(cube, material)

        # Create armature for rigging
        create_armature(name='CubeArmature', obj=cube)
        
        print("3D model asset created successfully.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
