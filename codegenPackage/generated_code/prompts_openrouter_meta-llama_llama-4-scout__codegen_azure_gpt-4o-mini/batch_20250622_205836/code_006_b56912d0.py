"""
Generated Code Metadata:
========================
Original URL: https://sproutstudios.in
Prompt: "Generate a 3D model and animation of a character, similar to the ones created by Sprout Studios for their projects, using a library like Blender or Maya."
Generated: DETERMINISTIC_b56912d0c1ba597b
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import bpy

# Function to create a simple character model
def create_character():
    # Clear existing mesh objects
    bpy.ops.object.select_all(action='DESELECT')
    bpy.ops.object.select_by_type(type='MESH')
    bpy.ops.object.delete()

    # Create a basic body using a UV sphere
    bpy.ops.mesh.primitive_uv_sphere_add(radius=1, location=(0, 0, 1))
    body = bpy.context.object
    body.name = "CharacterBody"

    # Create a head using another UV sphere
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.5, location=(0, 0, 2))
    head = bpy.context.object
    head.name = "CharacterHead"

    # Create arms using cylinders
    bpy.ops.mesh.primitive_cylinder_add(radius=0.2, depth=1, location=(-1, 0, 1))
    left_arm = bpy.context.object
    left_arm.name = "LeftArm"

    bpy.ops.mesh.primitive_cylinder_add(radius=0.2, depth=1, location=(1, 0, 1))
    right_arm = bpy.context.object
    right_arm.name = "RightArm"

    # Create legs using cylinders
    bpy.ops.mesh.primitive_cylinder_add(radius=0.3, depth=1.5, location=(-0.5, 0, -0.5))
    left_leg = bpy.context.object
    left_leg.name = "LeftLeg"

    bpy.ops.mesh.primitive_cylinder_add(radius=0.3, depth=1.5, location=(0.5, 0, -0.5))
    right_leg = bpy.context.object
    right_leg.name = "RightLeg"

    # Join all parts into a single object
    bpy.ops.object.select_all(action='DESELECT')
    for obj in [body, head, left_arm, right_arm, left_leg, right_leg]:
        obj.select_set(True)
    bpy.context.view_layer.objects.active = body
    bpy.ops.object.join()

    # Rename the joined object
    bpy.context.object.name = "Character"

# Function to create a simple animation for the character
def animate_character():
    character = bpy.data.objects.get("Character")
    if character is None:
        raise ValueError("Character object not found. Please create the character first.")

    # Set the start and end frames for the animation
    start_frame = 1
    end_frame = 60

    # Insert keyframes for a simple up and down motion
    character.location.z = 1  # Start position
    character.keyframe_insert(data_path="location", frame=start_frame)

    character.location.z = 1.5  # End position
    character.keyframe_insert(data_path="location", frame=end_frame)

    # Set interpolation type to linear for a constant speed
    for fcurve in character.animation_data.action.fcurves:
        for keyframe in fcurve.keyframe_points:
            keyframe.interpolation = 'LINEAR'

# Main function to execute the script
def main():
    try:
        create_character()
        animate_character()
        print("Character created and animated successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the main function
if __name__ == "__main__":
    main()
```

This code is designed to be run in Blender's scripting environment. It creates a simple character model and animates it with a basic up-and-down motion. Make sure to run this script in Blender's Python console or script editor.
