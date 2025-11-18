"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nashekrashe.com
Prompt: Write a script in Python using the Blender API to create 3D shapes inspired by the "Spingly shapes" project described on NasheKrashe Design Studio's website.
Generated: DETERMINISTIC_26e973fbb5649a43
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import the necessary Blender modules
import bpy
import random
import math

# Function to create a spingly-inspired shape
def create_spingly_shape(name, location, size, twist_factor):
    """
    Creates a Spingly-inspired 3D shape using Blender API.
    
    Args:
        name (str): Name for the object.
        location (tuple): Location of the object in the 3D space (x, y, z).
        size (float): Overall size scale of the object.
        twist_factor (float): Degree of twisting applied to the shape.
    """
    # Create a new mesh and object
    mesh = bpy.data.meshes.new(name + "_mesh")
    obj = bpy.data.objects.new(name, mesh)
    bpy.context.collection.objects.link(obj)
    
    # Generate vertices for a twisted spiral cylinder
    vertices = []
    edges = []
    faces = []
    num_sides = 20  # Number of sides for circular cross-section
    num_layers = 50  # Number of layers for height
    height = size
    radius = size / 5
    
    for layer in range(num_layers):
        angle_offset = twist_factor * layer
        for side in range(num_sides):
            angle = (2 * math.pi * side / num_sides) + angle_offset
            x = math.cos(angle) * radius
            y = math.sin(angle) * radius
            z = (height / num_layers) * layer
            vertices.append((x, y, z))

    # Create faces connecting the vertices in a spiral manner
    for layer in range(num_layers - 1):
        for side in range(num_sides):
            next_side = (side + 1) % num_sides
            v1 = layer * num_sides + side
            v2 = layer * num_sides + next_side
            v3 = (layer + 1) * num_sides + next_side
            v4 = (layer + 1) * num_sides + side
            faces.append((v1, v2, v3, v4))

    # Assign the data to the mesh
    mesh.from_pydata(vertices, edges, faces)
    mesh.update()

    # Set object's location
    obj.location = location

# Function to delete all objects (for testing/cleanup purposes)
def delete_all_objects():
    """
    Deletes all objects in the current scene.
    """
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()

# Main function to create multiple spingly shapes
def main():
    """
    Main function to create Spingly-inspired shapes.
    """
    try:
        # Cleanup the scene
        delete_all_objects()

        # Create shapes with varying properties
        create_spingly_shape(
            name="SpinglyShape1",
            location=(0, 0, 0),
            size=2,
            twist_factor=0.1
        )
        create_spingly_shape(
            name="SpinglyShape2",
            location=(5, 0, 0),
            size=3,
            twist_factor=0.2
        )
        create_spingly_shape(
            name="SpinglyShape3",
            location=(-5, 0, 0),
            size=1.5,
            twist_factor=0.05
        )

        print("Spingly shapes created successfully!")
    except Exception as e:
        # Handle any errors
        print(f"An error occurred: {e}")

# Run the main function
if __name__ == "__main__":
    main()
```
