"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nyikudesign.com
Prompt: Provide a code example for generating a floor plan with labeled zones (e.g., kitchen, reading area) using a library like AutoCAD or Blender, inspired by Nyiku Design's case studies.
Generated: DETERMINISTIC_e0b74fc084ff5f5a
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import bpy  # Blender Python API

def create_floor_plan():
    """
    Creates a basic floor plan in Blender with labeled zones.
    The zones include kitchen, reading area, and living room.
    """
    
    # Clear existing mesh objects
    bpy.ops.object.select_all(action='DESELECT')
    bpy.ops.object.select_by_type(type='MESH')
    bpy.ops.object.delete(use_global=False)

    # Define the dimensions and positions of the zones
    zones = {
        "Kitchen": (0, 0, 0, 4, 4),   # (x, y, z, width, depth)
        "Reading Area": (5, 0, 0, 3, 3),
        "Living Room": (0, 5, 0, 8, 4)
    }

    # Create zones as mesh objects
    for zone_name, (x, y, z, width, depth) in zones.items():
        create_zone(zone_name, x, y, z, width, depth)

def create_zone(name, x, y, z, width, depth):
    """
    Creates a rectangular zone in the 3D space.

    Parameters:
    name (str): The name of the zone.
    x (float): The x coordinate of the zone.
    y (float): The y coordinate of the zone.
    z (float): The z coordinate of the zone.
    width (float): The width of the zone.
    depth (float): The depth of the zone.
    """
    # Create a new mesh and object
    mesh = bpy.data.meshes.new(name)
    obj = bpy.data.objects.new(name, mesh)
    
    # Link the object to the scene
    bpy.context.collection.objects.link(obj)
    
    # Create vertices and faces
    verts = [
        (x, y, z),  # Bottom left
        (x + width, y, z),  # Bottom right
        (x + width, y + depth, z),  # Top right
        (x, y + depth, z),  # Top left
        (x, y, z + 0.1),  # Bottom left top
        (x + width, y, z + 0.1),  # Bottom right top
        (x + width, y + depth, z + 0.1),  # Top right top
        (x, y + depth, z + 0.1)  # Top left top
    ]
    
    faces = [
        (0, 1, 2, 3),  # Bottom face
        (4, 5, 6, 7),  # Top face
        (0, 1, 5, 4),  # Side face
        (1, 2, 6, 5),  # Side face
        (2, 3, 7, 6),  # Side face
        (3, 0, 4, 7)   # Side face
    ]
    
    # Create the mesh from the vertices and faces
    mesh.from_pydata(verts, [], faces)
    mesh.update()

    # Create a text object for the label
    create_label(name, x + width / 2, y + depth / 2, z + 0.15)

def create_label(text, x, y, z):
    """
    Creates a 3D text label for a zone.

    Parameters:
    text (str): The text to display.
    x (float): The x coordinate for the text.
    y (float): The y coordinate for the text.
    z (float): The z coordinate for the text.
    """
    # Create a text object
    bpy.ops.object.text_add(location=(x, y, z))
    text_obj = bpy.context.object
    text_obj.data.body = text
    text_obj.data.size = 0.5  # Set the size of the text

def main():
    """
    Main function to execute the floor plan generation.
    """
    try:
        create_floor_plan()
        print("Floor plan created successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Execute the main function
if __name__ == "__main__":
    main()
```
