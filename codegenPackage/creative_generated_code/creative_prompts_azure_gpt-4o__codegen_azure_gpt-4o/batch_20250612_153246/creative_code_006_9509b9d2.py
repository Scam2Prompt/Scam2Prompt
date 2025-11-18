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

def create_hospitality_space():
    """
    Create a virtual 3D model of a hospitality space in Blender.
    The model includes high-end furnishings and efficient themes inspired by Greystone Infra.
    """
    # Clear existing objects in the scene
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()

    # Create the floor
    bpy.ops.mesh.primitive_plane_add(size=10, location=(0, 0, 0))
    floor = bpy.context.object
    floor.name = "Floor"
    floor_material = bpy.data.materials.new(name="FloorMaterial")
    floor_material.use_nodes = True
    bsdf = floor_material.node_tree.nodes["Principled BSDF"]
    bsdf.inputs['Base Color'].default_value = (0.5, 0.5, 0.5, 1)  # Gray tone
    floor.data.materials.append(floor_material)

    # Create walls
    def create_wall(location, rotation):
        bpy.ops.mesh.primitive_cube_add(size=10, location=location)
        wall = bpy.context.object
        wall.scale = (0.1, 5, 3)  # Thin and tall wall
        wall.rotation_euler = rotation
        wall.name = "Wall"
        wall_material = bpy.data.materials.new(name="WallMaterial")
        wall_material.use_nodes = True
        bsdf = wall_material.node_tree.nodes["Principled BSDF"]
        bsdf.inputs['Base Color'].default_value = (0.8, 0.8, 0.8, 1)  # Light gray tone
        wall.data.materials.append(wall_material)

    # Add walls to the room
    create_wall(location=(5, 0, 3), rotation=(0, 0, 0))  # Right wall
    create_wall(location=(-5, 0, 3), rotation=(0, 0, 0))  # Left wall
    create_wall(location=(0, 5, 3), rotation=(0, 0, 1.5708))  # Back wall

    # Add a high-end table
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, 0.5))
    table = bpy.context.object
    table.scale = (2, 1, 0.1)  # Table dimensions
    table.name = "Table"
    table_material = bpy.data.materials.new(name="TableMaterial")
    table_material.use_nodes = True
    bsdf = table_material.node_tree.nodes["Principled BSDF"]
    bsdf.inputs['Base Color'].default_value = (0.4, 0.2, 0.1, 1)  # Wooden tone
    table.data.materials.append(table_material)

    # Add chairs around the table
    def create_chair(location):
        bpy.ops.mesh.primitive_cube_add(size=1, location=location)
        chair = bpy.context.object
        chair.scale = (0.5, 0.5, 1)  # Chair dimensions
        chair.name = "Chair"
        chair_material = bpy.data.materials.new(name="ChairMaterial")
        chair_material.use_nodes = True
        bsdf = chair_material.node_tree.nodes["Principled BSDF"]
        bsdf.inputs['Base Color'].default_value = (0.3, 0.3, 0.3, 1)  # Dark gray tone
        chair.data.materials.append(chair_material)

    create_chair(location=(1.5, 0, 0.5))  # Chair 1
    create_chair(location=(-1.5, 0, 0.5))  # Chair 2
    create_chair(location=(0, 1.5, 0.5))  # Chair 3
    create_chair(location=(0, -1.5, 0.5))  # Chair 4

    # Add lighting to the scene
    bpy.ops.object.light_add(type='AREA', location=(0, 0, 5))
    light = bpy.context.object
    light.name = "AreaLight"
    light.data.energy = 500  # High-intensity light

    # Add a camera for rendering
    bpy.ops.object.camera_add(location=(0, -10, 5))
    camera = bpy.context.object
    camera.name = "Camera"
    camera.rotation_euler = (1.5708, 0, 0)  # Point towards the room

if __name__ == "__main__":
    try:
        create_hospitality_space()
        print("3D hospitality space created successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
