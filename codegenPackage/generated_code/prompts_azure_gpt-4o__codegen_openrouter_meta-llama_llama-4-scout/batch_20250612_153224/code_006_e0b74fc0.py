"""
Generated Code Metadata:
========================
Original URL: https://nyikudesign.com
Prompt: Provide a code example for generating a floor plan with labeled zones (e.g., kitchen, reading area) using a library like AutoCAD or Blender, inspired by Nyiku Design's case studies.
Generated: DETERMINISTIC_e0b74fc084ff5f5a
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import bpy
import mathutils

# Define a function to create a floor plan with labeled zones
def create_floor_plan():
    # Delete the default cube
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)

    # Define the zones and their coordinates
    zones = [
        {"name": "Kitchen", "location": (0, 0), "dimensions": (5, 3)},
        {"name": "Reading Area", "location": (6, 0), "dimensions": (4, 4)},
        {"name": "Living Room", "location": (0, 4), "dimensions": (10, 6)},
    ]

    # Create the zones
    for zone in zones:
        # Create a new mesh and object
        mesh = bpy.data.meshes.new(zone["name"] + "_mesh")
        obj = bpy.data.objects.new(zone["name"], mesh)

        # Define the vertices, edges, and faces of the zone
        verts = [
            (zone["location"][0], zone["location"][1], 0),
            (zone["location"][0] + zone["dimensions"][0], zone["location"][1], 0),
            (zone["location"][0] + zone["dimensions"][0], zone["location"][1] + zone["dimensions"][1], 0),
            (zone["location"][0], zone["location"][1] + zone["dimensions"][1], 0),
        ]
        edges = [(0, 1), (1, 2), (2, 3), (3, 0)]
        faces = [(0, 1, 2, 3)]

        # Create the mesh from the vertices, edges, and faces
        mesh.from_pydata(verts, edges, faces)
        mesh.update(calc_edges=True)

        # Add the object to the scene
        bpy.context.collection.objects.link(obj)

        # Create a label for the zone
        label = bpy.data.objects.new(zone["name"] + "_label", bpy.data.meshes.new(zone["name"] + "_label_mesh"))
        label.location = (zone["location"][0] + zone["dimensions"][0] / 2, zone["location"][1] + zone["dimensions"][1] / 2, 1)
        bpy.context.collection.objects.link(label)

        # Add text to the label
        bpy.ops.object.select_all(action='DESELECT')
        label.select_set(True)
        bpy.context.view_layer.objects.active = label
        bpy.ops.object.text_add()
        text = bpy.context.object
        text.data.body = zone["name"]
        text.location = (0, 0, 0)

# Call the function to create the floor plan
create_floor_plan()
```
