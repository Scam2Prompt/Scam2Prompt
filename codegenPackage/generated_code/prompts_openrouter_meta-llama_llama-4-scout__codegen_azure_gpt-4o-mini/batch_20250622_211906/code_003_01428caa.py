"""
Generated Code Metadata:
========================
Original URL: https://lsinterior.com.my
Prompt: "Create a 3D design for a Malaysian office space using LS Interior's creative home design approach and renovation services."
Generated: DETERMINISTIC_01428caa849a9d2c
Batch ID: 20250622_211906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import bpy

# Function to create a wall
def create_wall(location, rotation, dimensions):
    bpy.ops.mesh.primitive_cube_add(size=1, location=location)
    wall = bpy.context.object
    wall.scale = dimensions
    wall.rotation_euler = rotation
    return wall

# Function to create a window
def create_window(location, dimensions):
    bpy.ops.mesh.primitive_plane_add(size=1, location=location)
    window = bpy.context.object
    window.scale = dimensions
    window.name = "Window"
    return window

# Function to create a door
def create_door(location, dimensions):
    bpy.ops.mesh.primitive_cube_add(size=1, location=location)
    door = bpy.context.object
    door.scale = dimensions
    door.name = "Door"
    return door

# Function to set up the office space
def setup_office_space():
    # Clear existing mesh objects
    bpy.ops.object.select_all(action='DESELECT')
    bpy.ops.object.select_by_type(type='MESH')
    bpy.ops.object.delete()

    # Create walls
    create_wall(location=(0, 0, 2.5), rotation=(0, 0, 0), dimensions=(5, 0.1, 2.5))  # Front wall
    create_wall(location=(5, 0, 2.5), rotation=(0, 1.5708, 0), dimensions=(0.1, 5, 2.5))  # Right wall
    create_wall(location=(0, 5, 2.5), rotation=(0, 0, 0), dimensions=(5, 0.1, 2.5))  # Back wall
    create_wall(location=(-0.1, 0, 2.5), rotation=(0, 1.5708, 0), dimensions=(0.1, 5, 2.5))  # Left wall

    # Create windows
    create_window(location=(2.5, 0.1, 2.5), dimensions=(1, 0.05, 1))  # Front window
    create_window(location=(4.9, 2.5, 2.5), dimensions=(0.05, 1, 1))  # Right window

    # Create door
    create_door(location=(0, 2.5, 1), dimensions=(0.1, 0.05, 1))  # Door

# Main function to execute the script
def main():
    try:
        setup_office_space()
        print("Office space created successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the main function
if __name__ == "__main__":
    main()
```
