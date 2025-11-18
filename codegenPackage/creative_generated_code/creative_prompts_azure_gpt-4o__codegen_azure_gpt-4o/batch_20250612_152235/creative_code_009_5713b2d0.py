"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sproutstudios.in
Prompt: Write code to create a CGI animation series for kids, inspired by Sprout Studios' projects like Cocomelon and Little Zoo.
Generated: DETERMINISTIC_5713b2d02dea5b38
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Creating a full CGI animation series for kids is an extensive project that involves various technologies like 3D modeling, animation, rendering, and scripting. Instead of actual animation code (which cannot be provided fully here due to complexity and size), here's a Python script that outlines a simplified workflow for generating frames using Blender's Python API. Blender is a popular open-source tool for creating CGI animations. You'll need Blender installed, and the script can be run from Blender's scripting editor.

```python
import bpy

def create_scene():
    """
    Sets up the basic Blender scene for the animation.
    Includes a camera, a light source, and a simple geometry object.
    """
    # Clear existing objects in the scene
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()

    # Add a camera
    bpy.ops.object.camera_add(location=(0, -10, 5))
    camera = bpy.context.object
    camera.rotation_euler = (1.1, 0, 0)  # Rotate to look at the center of the scene
    bpy.context.scene.camera = camera

    # Add a light source
    bpy.ops.object.light_add(type='POINT', location=(5, -5, 10))
    bpy.context.object.data.energy = 1000

    # Add a simple 3D object (e.g., a text-based character)
    bpy.ops.object.text_add(location=(0, 0, 0))
    text = bpy.context.object
    text.data.body = "Hello Kids!"
    text.data.extrude = 0.1  # Adds some depth to the text

def configure_render_settings(output_path, resolution_x=1920, resolution_y=1080, fps=30):
    """
    Configures render settings for animation output.
    """
    scene = bpy.context.scene
    scene.render.filepath = output_path
    scene.render.image_settings.file_format = 'FFMPEG'
    scene.render.ffmpeg.format = 'MPEG4'
    scene.render.resolution_x = resolution_x
    scene.render.resolution_y = resolution_y
    scene.render.fps = fps

def create_animation():
    """
    Adds basic animation to the scene.
    Animates the text rotating around the Z-axis.
    """
    text = bpy.data.objects['Text']  # Assumes there's an object named "Text"
    
    # Set initial rotation keyframe
    text.rotation_euler = (0, 0, 0)
    text.keyframe_insert(data_path="rotation_euler", frame=1)

    # Set final rotation keyframe
    text.rotation_euler = (0, 0, 6.28)  # 360 degrees in radians
    text.keyframe_insert(data_path="rotation_euler", frame=60)  # At frame 60

def render_animation():
    """
    Renders the animation to a video file.
    """
    bpy.ops.render.render(animation=True)

def main():
    """
    Main function to create the CGI animation scene for kids, inspired by projects like Cocomelon.
    """
    output_path = "/tmp/kids_animation.mp4"  # Change to your desired output path

    create_scene()
    configure_render_settings(output_path)
    create_animation()
    render_animation()

# Run the main function
if __name__ == "__main__":
    main()
```

### Notes:
1. Save the script as a `.py` file and run it in Blender's scripting editor.
2. Replace `/tmp/kids_animation.mp4` with the path where you want the rendered video to be saved.
3. The script is intentionally simple and focuses on the workflow. For production-quality animation, you'd need extensive modeling, rigging, texturing, and advanced animation techniques.

This script serves as a starting point for automating aspects of CGI animation creation. Let me know if you need additional features or enhancements.
