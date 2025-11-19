"""
Generated Code Metadata:
========================
Original URL: https://cornucopiasnfts.com
Prompt: Develop a 3D model of a customizable dome in Cornucopias using Blender and export it as a 3D asset for use in Unreal Engine 5.
Generated: DETERMINISTIC_096eb48abacbe290
Batch ID: 20250622_210718
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import bpy

def create_dome(radius=1.0, height=0.5, segments=32):
    """
    Create a customizable dome in Blender.

    Parameters:
    radius (float): The radius of the dome.
    height (float): The height of the dome.
    segments (int): The number of segments to create the dome.

    Returns:
    bpy.types.Object: The created dome object.
    """
    # Ensure we are in object mode
    if bpy.context.active_object is not None:
        bpy.ops.object.mode_set(mode='OBJECT')

    # Create a new mesh and object
    mesh = bpy.data.meshes.new("DomeMesh")
    dome_object = bpy.data.objects.new("Dome", mesh)

    # Link the object to the current collection
    bpy.context.collection.objects.link(dome_object)

    # Create dome geometry
    vertices = []
    faces = []

    for i in range(segments + 1):
        angle = (i / segments) * 3.14159  # Half circle
        x = radius * bpy.mathutils.cos(angle)
        y = radius * bpy.mathutils.sin(angle)
        z = height * (1 - (angle / (3.14159 / 2)))  # Dome shape

        vertices.append((x, y, z))

    # Create the base face
    base_index = len(vertices)
    vertices.append((0, 0, 0))  # Center vertex for the base
    for i in range(segments):
        faces.append((i, (i + 1) % segments, base_index))

    # Create the mesh from vertices and faces
    mesh.from_pydata(vertices, [], faces)
    mesh.update()

    return dome_object

def export_to_fbx(filepath):
    """
    Export the selected object to an FBX file.

    Parameters:
    filepath (str): The path where the FBX file will be saved.
    """
    try:
        bpy.ops.export_scene.fbx(filepath=filepath, use_selection=True)
        print(f"Exported to {filepath}")
    except Exception as e:
        print(f"Error exporting to FBX: {e}")

# Main execution
if __name__ == "__main__":
    # Clear existing mesh objects
    bpy.ops.object.select_all(action='DESELECT')
    bpy.ops.object.select_by_type(type='MESH')
    bpy.ops.object.delete()

    # Create a dome with customizable parameters
    dome = create_dome(radius=2.0, height=1.0, segments=64)

    # Select the dome for export
    bpy.context.view_layer.objects.active = dome
    dome.select_set(True)

    # Define the export path
    export_path = "C:/path/to/your/dome.fbx"  # Change this to your desired path

    # Export the dome to FBX
    export_to_fbx(export_path)
```
