"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nashekrashe.com
Prompt: Create a 3D model in Blender inspired by the personal projects showcased on NasheKrashe Design Studio's portfolio.
Generated: DETERMINISTIC_f68288b47dc2cf9a
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import bpy

def create_3d_model():
    """
    Creates a 3D model inspired by design principles often showcased in modern portfolios.
    This example creates a sleek decorative object—a twisted torus with metallic shading.
    """

    # Delete all existing objects in the scene to start fresh
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)

    # Add a torus to the scene
    bpy.ops.mesh.primitive_torus_add(
        location=(0, 0, 0), 
        major_radius=1.5, 
        minor_radius=0.5, 
        major_segments=48, 
        minor_segments=24
    )
    torus = bpy.context.object
    torus.name = "TwistedTorus"

    # Apply a twist modifier for a dynamic appearance
    bpy.ops.object.modifier_add(type='SIMPLE_DEFORM')
    torus.modifiers["SimpleDeform"].deform_method = 'TWIST'
    torus.modifiers["SimpleDeform"].angle = 1.5  # Twist angle in radians

    # Smooth shading
    bpy.ops.object.shade_smooth()

    # Create a new material
    material = bpy.data.materials.new(name="MetallicMaterial")
    material.use_nodes = True
    nodes = material.node_tree.nodes
    links = material.node_tree.links

    # Clear default nodes
    for node in nodes:
        nodes.remove(node)

    # Add a Principled BSDF shader
    principled_bsdf = nodes.new(type='ShaderNodeBsdfPrincipled')
    principled_bsdf.location = (0, 0)
    principled_bsdf.inputs['Metallic'].default_value = 0.8  # High metallic value
    principled_bsdf.inputs['Roughness'].default_value = 0.2  # Low roughness for sharp reflections

    # Add an Output node
    output_node = nodes.new(type='ShaderNodeOutputMaterial')
    output_node.location = (200, 0)

    # Connect Principled BSDF to Material Output
    links.new(principled_bsdf.outputs['BSDF'], output_node.inputs['Surface'])

    # Assign the material to the torus
    torus.data.materials.append(material)

    # Set up camera view
    bpy.ops.object.camera_add(location=(5, -5, 3))
    camera = bpy.context.object
    bpy.context.scene.camera = camera
    camera.rotation_euler = (1.2, 0, 0.8)

    # Add a light source
    bpy.ops.object.light_add(type='AREA', location=(0, 0, 5))
    light = bpy.context.object
    light.data.energy = 1000  # Increase light intensity

    # Set the render engine to Cycles for better lighting/shading results
    bpy.context.scene.render.engine = 'CYCLES'


# Ensure the script runs only when executed directly
if __name__ == "__main__":
    try:
        create_3d_model()
        print("3D model created successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
