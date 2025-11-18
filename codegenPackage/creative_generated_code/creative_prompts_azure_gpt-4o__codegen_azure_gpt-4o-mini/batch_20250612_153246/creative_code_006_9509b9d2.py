"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://greystoneinfra.in
Prompt: Write code using Blender's Python API to design a virtual 3D model of a hospitality space, incorporating high-end furnishing and efficient themes as emphasized by Greystone Infra.
Generated: DETERMINISTIC_9509b9d2900f765d
Batch ID: 20250612_153246
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

def create_material(name, color):
    """Create a new material with a given name and color."""
    mat = bpy.data.materials.new(name=name)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    bsdf.inputs['Base Color'].default_value = color
    return mat

def create_cube(location, size, name, material):
    """Create a cube at the specified location, size, and name, with a given material."""
    bpy.ops.mesh.primitive_cube_add(size=size, location=location)
    cube = bpy.context.object
    cube.name = name
    if material:
        if material.name not in bpy.data.materials:
            raise ValueError(f"Material '{material.name}' not found.")
        if len(cube.data.materials) == 0:
            cube.data.materials.append(material)
        else:
            cube.data.materials[0] = material
    return cube

def create_furniture():
    """Create high-end furniture for the hospitality space."""
    # Define materials
    wood_material = create_material("Wood", (0.545, 0.271, 0.075, 1))
    fabric_material = create_material("Fabric", (0.8, 0.3, 0.3, 1))

    # Create a sofa
    create_cube(location=(0, 0, 1), size=2, name="Sofa", material=fabric_material)
    
    # Create a coffee table
    create_cube(location=(0, 1.5, 0.5), size=1, name="CoffeeTable", material=wood_material)

def setup_scene():
    """Set up the scene for the hospitality space."""
    # Clear existing objects
    bpy.ops.object.select_all(action='DESELECT')
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)

    # Set the world background color
    world = bpy.data.worlds.new("World")
    bpy.context.scene.world = world
    world.color = (0.8, 0.8, 0.8)

def main():
    """Main function to build the hospitality space."""
    try:
        setup_scene()
        create_furniture()
        print("Hospitality space created successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the main function
main()
```
