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
from math import radians

def create_dome(
    radius=5.0,
    segments=32,
    rings=16,
    thickness=0.2,
    subdivisions=2,
    smooth_shading=True
):
    """
    Creates a customizable dome mesh in Blender.
    
    Args:
        radius (float): Radius of the dome
        segments (int): Number of segments around the circumference
        rings (int): Number of rings from base to top
        thickness (float): Thickness of the dome shell
        subdivisions (int): Number of subdivisions for smoothing
        smooth_shading (bool): Apply smooth shading to the mesh
    """
    # Create the base sphere
    bpy.ops.mesh.primitive_uv_sphere_add(
        radius=radius,
        segments=segments,
        ring_count=rings,
        location=(0, 0, 0)
    )
    sphere = bpy.context.active_object
    sphere.name = "Dome_Base"
    
    # Remove the bottom half to create a dome
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.bisect(
        plane_co=(0, 0, 0),
        plane_no=(0, 0, -1),
        clear_inner=True,
        clear_outer=False,
        threshold=0.0001
    )
    bpy.ops.object.mode_set(mode='OBJECT')
    
    # Add thickness using solidify modifier
    solidify = sphere.modifiers.new(name="Solidify", type='SOLIDIFY')
    solidify.thickness = thickness
    solidify.offset = 1.0
    bpy.ops.object.modifier_apply(modifier="Solidify")
    
    # Add subdivisions for smoothing
    if subdivisions > 0:
        subdiv = sphere.modifiers.new(name="Subdivision", type='SUBSURF')
        subdiv.levels = subdivisions
        subdiv.render_levels = subdivisions
        bpy.ops.object.modifier_apply(modifier="Subdivision")
    
    # Apply smooth shading if requested
    if smooth_shading:
        bpy.ops.object.shade_smooth()
    
    return sphere

def setup_materials():
    """Sets up basic materials for the dome."""
    mat = bpy.data.materials.new(name="Dome_Material")
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    
    # Clear default nodes
    for node in nodes:
        nodes.remove(node)
    
    # Create PBR shader nodes
    output = nodes.new(type='ShaderNodeOutputMaterial')
    principled = nodes.new(type='ShaderNodeBsdfPrincipled')
    
    # Link nodes
    links.new(principled.outputs['BSDF'], output.inputs['Surface'])
    
    # Set some default values
    principled.inputs['Base Color'].default_value = (0.8, 0.8, 0.8, 1)
    principled.inputs['Roughness'].default_value = 0.4
    principled.inputs['Metallic'].default_value = 0.1
    
    return mat

def export_to_unreal(
    output_path="",
    file_name="dome_asset",
    export_format="FBX"
):
    """
    Exports the dome to a format compatible with Unreal Engine 5.
    
    Args:
        output_path (str): Directory to export to
        file_name (str): Base name for the exported file
        export_format (str): Format to export (FBX or GLTF)
    """
    if not output_path:
        output_path = os.path.join(os.path.expanduser("~"), "Documents")
    
    full_path = os.path.join(output_path, f"{file_name}.{export_format.lower()}")
    
    # Select the dome object
    dome = bpy.data.objects.get("Dome_Base")
    if not dome:
        raise ValueError("No dome object found to export")
    
    # Apply all transforms
    bpy.context.view_layer.objects.active = dome
    bpy.ops.object.select_all(action='DESELECT')
    dome.select_set(True)
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
    
    # Export based on format
    if export_format.upper() == "FBX":
        bpy.ops.export_scene.fbx(
            filepath=full_path,
            use_selection=True,
            apply_scale_options='FBX_SCALE_UNITS',
            mesh_smooth_type='FACE',
            use_mesh_modifiers=True,
            add_leaf_bones=False,
            bake_anim=False
        )
    elif export_format.upper() == "GLTF":
        bpy.ops.export_scene.gltf(
            filepath=full_path,
            export_format='GLB',
            export_selected=True,
            export_apply=True
        )
    else:
        raise ValueError(f"Unsupported export format: {export_format}")
    
    return full_path

def main():
    """Main function to create and export the dome."""
    try:
        # Clear existing objects
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete()
        
        # Create dome with default parameters
        dome = create_dome()
        
        # Setup materials
        mat = setup_materials()
        dome.data.materials.append(mat)
        
        # Export to Unreal-compatible format
        export_path = export_to_unreal()
        print(f"Dome successfully exported to: {export_path}")
        
    except Exception as e:
        print(f"Error creating dome: {str(e)}")
        raise

if __name__ == "__main__":
    main()
```
