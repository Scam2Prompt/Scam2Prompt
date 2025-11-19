"""
Generated Code Metadata:
========================
Original URL: https://greystoneinfra.in
Prompt: Write code using Blender's Python API to design a virtual 3D model of a hospitality space, incorporating high-end furnishing and efficient themes as emphasized by Greystone Infra.
Generated: DETERMINISTIC_9509b9d2900f765d
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import bpy

# Function to create a plane for the floor
def create_floor(size=10):
    bpy.ops.mesh.primitive_plane_add(size=size, enter_editmode=False, align='WORLD', location=(0, 0, 0))
    floor = bpy.context.object
    floor.name = "Floor"
    return floor

# Function to create a wall
def create_wall(location, rotation, dimensions=(1, 0.1, 2)):
    bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', location=location)
    wall = bpy.context.object
    wall.name = "Wall"
    wall.scale = dimensions
    wall.rotation_euler = rotation
    return wall

# Function to create a high-end sofa
def create_sofa(location):
    bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', location=location)
    sofa = bpy.context.object
    sofa.name = "Sofa"
    sofa.scale = (1.5, 0.5, 0.5)  # Scale to resemble a sofa
    return sofa

# Function to create a table
def create_table(location):
    bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', location=location)
    table = bpy.context.object
    table.name = "Table"
    table.scale = (0.8, 0.8, 0.1)  # Scale to resemble a table
    return table

# Function to set up the hospitality space
def setup_hospitality_space():
    # Clear existing objects
    bpy.ops.object.select_all(action='DESELECT')
    bpy.ops.object.select_by_type(type='MESH')
    bpy.ops.object.delete()

    # Create floor
    create_floor(size=10)

    # Create walls
    wall_thickness = 0.1
    wall_height = 2
    create_wall(location=(5, 0, wall_height/2), rotation=(0, 0, 0), dimensions=(wall_thickness, 5, wall_height))  # Right wall
    create_wall(location=(-5, 0, wall_height/2), rotation=(0, 0, 0), dimensions=(wall_thickness, 5, wall_height))  # Left wall
    create_wall(location=(0, 5, wall_height/2), rotation=(0, 1.5708, 0), dimensions=(wall_thickness, 5, wall_height))  # Back wall
    create_wall(location=(0, -5, wall_height/2), rotation=(0, 1.5708, 0), dimensions=(wall_thickness, 5, wall_height))  # Front wall

    # Create furniture
    create_sofa(location=(0, -2, 0.25))  # Sofa in the center
    create_table(location=(0, 0, 0.05))  # Table in the center

# Run the setup function
if __name__ == "__main__":
    try:
        setup_hospitality_space()
        print("Hospitality space created successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
