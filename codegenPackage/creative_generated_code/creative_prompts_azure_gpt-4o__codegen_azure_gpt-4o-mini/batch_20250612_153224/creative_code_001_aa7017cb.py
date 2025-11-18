"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://filmdailyweb.com
Prompt: Recommend libraries or APIs for creating 3D animated videos, and explain how they align with the process described on Film Daily Web.
Generated: DETERMINISTIC_aa7017cb9eac059d
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for 3D animation and video creation
import bpy  # Blender's Python API for 3D graphics
import os    # To handle file paths

def create_3d_animation(scene_name, output_directory):
    """
    Create a 3D animated video in Blender.
    
    Parameters:
    scene_name (str): The name of the scene to be created.
    output_directory (str): The directory where the rendered video will be saved.
    
    Returns:
    None
    """
    try:
        # Ensure the output directory exists
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        # Clear existing mesh objects in the scene
        bpy.ops.object.select_all(action='DESELECT')
        bpy.ops.object.select_by_type(type='MESH')
        bpy.ops.object.delete()

        # Set the scene
        bpy.context.scene.name = scene_name
        
        # Create a simple cube as a sample object
        bpy.ops.mesh.primitive_cube_add(size=2, location=(0, 0, 0))
        cube = bpy.context.object
        
        # Animate the cube (move it along the x-axis)
        cube.keyframe_insert(data_path="location", frame=1)
        cube.location.x += 5
        cube.keyframe_insert(data_path="location", frame=50)

        # Set the output properties for the video
        bpy.context.scene.render.filepath = os.path.join(output_directory, f"{scene_name}.mp4")
        bpy.context.scene.render.image_settings.file_format = 'FFMPEG'
        bpy.context.scene.render.ffmpeg.format = 'MPEG4'

        # Render the animation
        bpy.ops.render.render(animation=True)
        print(f"Animation '{scene_name}' created successfully and saved to '{output_directory}'.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    create_3d_animation("SampleScene", "/tmp/3d_animations")  # Update output path as needed
```
