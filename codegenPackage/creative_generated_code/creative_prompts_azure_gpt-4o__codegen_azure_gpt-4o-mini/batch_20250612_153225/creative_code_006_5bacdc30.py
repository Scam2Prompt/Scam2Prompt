"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shelterder.com
Prompt: Provide an example of how to use 3D modeling software to design outdoor decorative fireplaces from the Out Collection, suitable for exterior environments.
Generated: DETERMINISTIC_5bacdc30b8112378
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import bpy

# Clear all existing objects from the scene
def clear_scene():
    bpy.ops.object.select_all(action='DESELECT')
    bpy.ops.object.select_by_type(type='MESH')
    bpy.ops.object.delete()

# Create a decorative fireplace using basic geometric shapes
def create_fireplace(location):
    # Base of the fireplace
    bpy.ops.mesh.primitive_cube_add(size=1, location=location)
    base = bpy.context.object
    base.scale = (1.5, 1.5, 0.5)  # Scaling to create the base
    base.name = "Fireplace_Base"

    # Create the fireplace opening
    bpy.ops.mesh.primitive_cube_add(size=1, location=(location[0], location[1], location[2] + 0.5))
    opening = bpy.context.object
    opening.scale = (0.8, 0.1, 0.7)
    opening.name = "Fireplace_Opening"

    # Create the chimney structure
    bpy.ops.mesh.primitive_cube_add(size=1, location=(location[0], location[1], location[2] + 1.5))
    chimney = bpy.context.object
    chimney.scale = (0.4, 0.4, 1.5)
    chimney.name = "Fireplace_Chimney"

    # Join the components into a single object
    bpy.ops.object.select_all(action='DESELECT')
    base.select_set(True)
    opening.select_set(True)
    chimney.select_set(True)
    bpy.context.view_layer.objects.active = base
    bpy.ops.object.join()  # Join selected objects

    # Rename the final fireplace object
    fireplace = bpy.context.object
    fireplace.name = "Outdoor_Decorative_Fireplace"

# Main function to execute the script
def main():
    try:
        clear_scene()  # Clear existing objects
        create_fireplace(location=(0, 0, 0))  # Create fireplace at the origin
        print("Fireplace created successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the main function
if __name__ == "__main__":
    main()
```
