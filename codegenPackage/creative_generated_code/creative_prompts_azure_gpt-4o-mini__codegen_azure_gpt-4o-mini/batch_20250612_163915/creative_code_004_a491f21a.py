"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.steamcommunity.ru
Prompt: Create a tutorial on designing custom maps for Half-Life, focusing on object modeling and texture application as outlined in the technical documentation.
Generated: DETERMINISTIC_a491f21a762b38b7
Batch ID: 20250612_163915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for 3D modeling and texture application
import bpy
import os

# Constants for the Half-Life map design
MAP_NAME = "CustomMap"
TEXTURE_PATH = "path/to/your/textures/"
OBJECTS = [
    {"name": "Cube", "size": (1, 1, 1), "location": (0, 0, 0)},
    {"name": "Cylinder", "size": (1, 1, 2), "location": (2, 0, 1)},
]

# Function to create a new map
def create_map(map_name):
    """ Create a new Blender scene for the map. """
    bpy.ops.wm.read_factory_settings(use_empty=True)  # Clear existing scene
    bpy.context.scene.name = map_name
    print(f"Created new map: {map_name}")

# Function to create objects
def create_objects(objects):
    """ Create 3D objects based on provided specifications. """
    for obj in objects:
        if obj["name"].lower() == "cube":
            bpy.ops.mesh.primitive_cube_add(size=obj["size"][0], location=obj["location"])
        elif obj["name"].lower() == "cylinder":
            bpy.ops.mesh.primitive_cylinder_add(radius=obj["size"][0], depth=obj["size"][2], location=obj["location"])
        else:
            print(f"Warning: Object type {obj['name']} is not recognized.")
    print("Objects created successfully.")

# Function to apply textures
def apply_textures(objects):
    """ Apply textures to the created objects. """
    # Load texture images
    texture_files = [f for f in os.listdir(TEXTURE_PATH) if f.endswith(('.png', '.jpg', '.jpeg'))]
    
    for obj in objects:
        if obj["name"].lower() in ["cube", "cylinder"]:  # Only apply textures to these types
            # Create a new material
            material = bpy.data.materials.new(name=f"{obj['name']}_Material")
            material.use_nodes = True
            
            # Get the material node tree
            nodes = material.node_tree.nodes
            bsdf = nodes.get("Principled BSDF")

            # Check if a texture is available
            if texture_files:
                # Create an image texture node
                texture_node = nodes.new(type='ShaderNodeTexImage')
                texture_node.image = bpy.data.images.load(os.path.join(TEXTURE_PATH, texture_files[0]))
                # Connect the texture to the BSDF shader
                material.node_tree.links.new(texture_node.outputs["Color"], bsdf.inputs["Base Color"])

            # Assign the material to the object
            obj_obj = bpy.context.active_object
            if obj_obj.data.materials:
                obj_obj.data.materials[0] = material
            else:
                obj_obj.data.materials.append(material)
    
    print("Textures applied successfully.")

# Main execution flow
if __name__ == "__main__":
    try:
        create_map(MAP_NAME)
        create_objects(OBJECTS)
        apply_textures(OBJECTS)
        print("Custom map setup completed.")
    except Exception as e:
        print(f"An error occurred: {e}")
```

Make sure to replace `TEXTURE_PATH` with the actual path to your texture files. This script should be executed within Blender's scripting environment.
