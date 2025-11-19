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
import os

def create_dome(radius=5, segments=32, rings=16, name="CustomDome"):
    """
    Creates a customizable dome in Blender.
    
    Parameters:
        radius (float): Radius of the dome.
        segments (int): Number of segments (horizontal divisions).
        rings (int): Number of rings (vertical divisions).
        name (str): Name of the dome object.
    """
    try:
        # Create a UV sphere
        bpy.ops.mesh.primitive_uv_sphere_add(
            radius=radius,
            segments=segments,
            ring_count=rings,
            location=(0, 0, 0)
        )
        
        # Get the created object
        dome = bpy.context.object
        dome.name = name
        
        # Enter edit mode to modify the mesh
        bpy.ops.object.mode_set(mode='EDIT')
        
        # Select the bottom half of the sphere
        bpy.ops.mesh.select_all(action='DESELECT')
        bpy.ops.mesh.select_mode(type="VERT")
        bpy.ops.mesh.select_less()
        
        # Delete the bottom half to create a dome
        bpy.ops.mesh.delete(type='VERT')
        
        # Exit edit mode
        bpy.ops.object.mode_set(mode='OBJECT')
        
        # Smooth shading for better appearance
        bpy.ops.object.shade_smooth()
        
        print(f"Dome '{name}' created successfully.")
        return dome
    except Exception as e:
        print(f"Error creating dome: {e}")
        return None

def export_to_unreal(dome, export_path):
    """
    Exports the dome object as a .fbx file for use in Unreal Engine 5.
    
    Parameters:
        dome (bpy.types.Object): The dome object to export.
        export_path (str): The file path to export the .fbx file.
    """
    try:
        # Ensure the export path exists
        os.makedirs(os.path.dirname(export_path), exist_ok=True)
        
        # Select the dome object
        bpy.ops.object.select_all(action='DESELECT')
        dome.select_set(True)
        bpy.context.view_layer.objects.active = dome
        
        # Export the object as .fbx
        bpy.ops.export_scene.fbx(
            filepath=export_path,
            use_selection=True,
            apply_scale_options='FBX_SCALE_ALL'
        )
        
        print(f"Dome exported successfully to {export_path}.")
    except Exception as e:
        print(f"Error exporting dome: {e}")

# Main execution
if __name__ == "__main__":
    # Parameters for the dome
    dome_radius = 5
    dome_segments = 32
    dome_rings = 16
    dome_name = "CustomDome"
    
    # Export path for Unreal Engine 5
    export_file_path = "/path/to/export/CustomDome.fbx"
    
    # Create the dome
    dome_object = create_dome(
        radius=dome_radius,
        segments=dome_segments,
        rings=dome_rings,
        name=dome_name
    )
    
    # Export the dome if creation was successful
    if dome_object:
        export_to_unreal(dome_object, export_file_path)
```

**Note:** Replace `/path/to/export/CustomDome.fbx` with the actual path where you want to save the exported `.fbx` file. Ensure Blender's Python API is properly set up and the script is run within Blender's scripting environment.
