"""
Generated Code Metadata:
========================
Original URL: https://nyikudesign.com
Prompt: "Design a 3D model for a commercial kitchen with a modern aesthetic, incorporating elements of storytelling through interior design."
Generated: DETERMINISTIC_ad3687739aaa0679
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import bpy

# Function to create a modern kitchen layout
def create_modern_kitchen():
    # Clear existing mesh objects
    bpy.ops.object.select_all(action='DESELECT')
    bpy.ops.object.select_by_type(type='MESH')
    bpy.ops.object.delete()

    # Create the main kitchen island
    create_kitchen_island(location=(0, 0, 0))

    # Create cabinets
    create_cabinet(location=(-3, 0, 0), width=1, height=2, depth=0.5)
    create_cabinet(location=(3, 0, 0), width=1, height=2, depth=0.5)

    # Create appliances
    create_appliance(location=(-2, 0, 0), width=1, height=1.5, depth=0.6, appliance_type='fridge')
    create_appliance(location=(2, 0, 0), width=1, height=1.5, depth=0.6, appliance_type='oven')

    # Create a dining area
    create_dining_table(location=(0, 3, 0), width=2, height=0.75, depth=1)
    create_chairs(location=(0, 3.5, 0), num_chairs=4)

# Function to create a kitchen island
def create_kitchen_island(location):
    bpy.ops.mesh.primitive_cube_add(size=1, location=location)
    island = bpy.context.object
    island.scale = (2, 1, 0.75)  # Scale to create an island shape
    island.name = "Kitchen Island"
    set_material(island, color=(0.8, 0.8, 0.8, 1))  # Light gray color

# Function to create a cabinet
def create_cabinet(location, width, height, depth):
    bpy.ops.mesh.primitive_cube_add(size=1, location=location)
    cabinet = bpy.context.object
    cabinet.scale = (width, depth, height)  # Scale to cabinet dimensions
    cabinet.name = "Cabinet"
    set_material(cabinet, color=(0.6, 0.3, 0.2, 1))  # Wood color

# Function to create an appliance
def create_appliance(location, width, height, depth, appliance_type):
    bpy.ops.mesh.primitive_cube_add(size=1, location=location)
    appliance = bpy.context.object
    appliance.scale = (width, depth, height)  # Scale to appliance dimensions
    appliance.name = appliance_type.capitalize()
    set_material(appliance, color=(0.9, 0.9, 0.9, 1))  # Stainless steel color

# Function to create a dining table
def create_dining_table(location, width, height, depth):
    bpy.ops.mesh.primitive_cube_add(size=1, location=location)
    table = bpy.context.object
    table.scale = (width, depth, height)  # Scale to table dimensions
    table.name = "Dining Table"
    set_material(table, color=(0.5, 0.25, 0.1, 1))  # Dark wood color

# Function to create chairs around the dining table
def create_chairs(location, num_chairs):
    for i in range(num_chairs):
        chair_location = (location[0] + (i % 2) * 1.5 - 0.75, location[1] + (i // 2) * 1.5 - 0.75, location[2])
        create_chair(location=chair_location)

# Function to create a single chair
def create_chair(location):
    bpy.ops.mesh.primitive_cube_add(size=1, location=location)
    chair = bpy.context.object
    chair.scale = (0.5, 0.5, 0.5)  # Scale to chair dimensions
    chair.name = "Chair"
    set_material(chair, color=(0.4, 0.2, 0.1, 1))  # Chair color

# Function to set material for an object
def set_material(obj, color):
    mat = bpy.data.materials.new(name="Material")
    mat.diffuse_color = color
    obj.data.materials.append(mat)

# Main execution
if __name__ == "__main__":
    try:
        create_modern_kitchen()
        print("Modern kitchen model created successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
