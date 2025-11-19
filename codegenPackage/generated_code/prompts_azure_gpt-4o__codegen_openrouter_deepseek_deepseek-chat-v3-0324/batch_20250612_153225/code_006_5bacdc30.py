"""
Generated Code Metadata:
========================
Original URL: https://shelterder.com
Prompt: Provide an example of how to use 3D modeling software to design outdoor decorative fireplaces from the Out Collection, suitable for exterior environments.
Generated: DETERMINISTIC_5bacdc30b8112378
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import bpy
import math
import os
from mathutils import Vector

class OutdoorFireplaceDesigner:
    """
    A class to design outdoor decorative fireplaces from the Out Collection using Blender's Python API.
    """

    def __init__(self):
        """Initialize the designer with default settings."""
        self.materials = {}
        self.scale = 1.0
        self.unit_scale = 0.01  # Blender units to meters
        self.fireplace_collection = None

    def setup_scene(self):
        """Set up the Blender scene for fireplace design."""
        # Clear existing objects
        bpy.ops.wm.read_factory_settings(use_empty=True)
        
        # Set units to metric
        bpy.context.scene.unit_settings.system = 'METRIC'
        bpy.context.scene.unit_settings.scale_length = self.unit_scale
        
        # Create collection for fireplace
        if "Out Collection" not in bpy.data.collections:
            self.fireplace_collection = bpy.data.collections.new("Out Collection")
            bpy.context.scene.collection.children.link(self.fireplace_collection)
        else:
            self.fireplace_collection = bpy.data.collections["Out Collection"]

    def create_base_materials(self):
        """Create standard materials for outdoor fireplace."""
        try:
            # Stone material
            stone_mat = bpy.data.materials.new(name="Outdoor_Stone")
            stone_mat.use_nodes = True
            nodes = stone_mat.node_tree.nodes
            nodes.clear()
            
            # Create principled BSDF
            bsdf = nodes.new(type='ShaderNodeBsdfPrincipled')
            bsdf.inputs['Base Color'].default_value = (0.3, 0.3, 0.3, 1)
            bsdf.inputs['Roughness'].default_value = 0.7
            bsdf.inputs['Specular'].default_value = 0.1
            
            # Create output node
            output = nodes.new(type='ShaderNodeOutputMaterial')
            
            # Link nodes
            links = stone_mat.node_tree.links
            links.new(bsdf.outputs['BSDF'], output.inputs['Surface'])
            
            self.materials['stone'] = stone_mat
            
            # Metal material
            metal_mat = bpy.data.materials.new(name="Outdoor_Metal")
            metal_mat.use_nodes = True
            nodes = metal_mat.node_tree.nodes
            nodes.clear()
            
            bsdf = nodes.new(type='ShaderNodeBsdfPrincipled')
            bsdf.inputs['Base Color'].default_value = (0.1, 0.1, 0.1, 1)
            bsdf.inputs['Metallic'].default_value = 1.0
            bsdf.inputs['Roughness'].default_value = 0.3
            
            output = nodes.new(type='ShaderNodeOutputMaterial')
            links = metal_mat.node_tree.links
            links.new(bsdf.outputs['BSDF'], output.inputs['Surface'])
            
            self.materials['metal'] = metal_mat
            
        except Exception as e:
            print(f"Error creating materials: {e}")
            raise

    def create_fireplace_base(self, width=1.5, depth=1.0, height=0.5):
        """
        Create the base structure of the fireplace.
        
        Args:
            width (float): Width in meters
            depth (float): Depth in meters
            height (float): Height in meters
        """
        try:
            # Convert to Blender units
            width *= self.scale / self.unit_scale
            depth *= self.scale / self.unit_scale
            height *= self.scale / self.unit_scale
            
            # Create base cube
            bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD')
            base = bpy.context.active_object
            base.name = "Fireplace_Base"
            base.dimensions = (width, depth, height)
            base.location = (0, 0, height/2)
            
            # Assign stone material
            if base.data.materials:
                base.data.materials[0] = self.materials['stone']
            else:
                base.data.materials.append(self.materials['stone'])
            
            # Link to collection
            if self.fireplace_collection:
                if base.name not in self.fireplace_collection.objects:
                    bpy.context.scene.collection.objects.unlink(base)
                    self.fireplace_collection.objects.link(base)
            
            return base
            
        except Exception as e:
            print(f"Error creating fireplace base: {e}")
            raise

    def create_fireplace_opening(self, base_obj, width=0.8, height=0.6, depth=0.8):
        """
        Create the fireplace opening using boolean modifier.
        
        Args:
            base_obj: The base object to cut from
            width (float): Opening width in meters
            height (float): Opening height in meters
            depth (float): How far back the opening goes in meters
        """
        try:
            # Convert to Blender units
            width *= self.scale / self.unit_scale
            height *= self.scale / self.unit_scale
            depth *= self.scale / self.unit_scale
            
            # Create cutter object
            bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD')
            cutter = bpy.context.active_object
            cutter.name = "Fireplace_Opening_Cutter"
            cutter.dimensions = (width, depth, height)
            
            # Position cutter
            base_dims = base_obj.dimensions
            cutter.location = (0, base_dims.y/2 - depth/2, height/2 + 0.1)
            
            # Add boolean modifier
            bool_mod = base_obj.modifiers.new(name="Fireplace_Opening", type='BOOLEAN')
            bool_mod.operation = 'DIFFERENCE'
            bool_mod.object = cutter
            
            # Apply modifier
            bpy.context.view_layer.objects.active = base_obj
            bpy.ops.object.modifier_apply(modifier=bool_mod.name)
            
            # Remove cutter
            bpy.data.objects.remove(cutter)
            
        except Exception as e:
            print(f"Error creating fireplace opening: {e}")
            raise

    def create_chimney(self, base_obj, width=0.4, depth=0.4, height=1.5):
        """
        Create the chimney structure.
        
        Args:
            base_obj: The base object to build upon
            width (float): Chimney width in meters
            depth (float): Chimney depth in meters
            height (float): Chimney height in meters
        """
        try:
            # Convert to Blender units
            width *= self.scale / self.unit_scale
            depth *= self.scale / self.unit_scale
            height *= self.scale / self.unit_scale
            
            # Create chimney
            bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD')
            chimney = bpy.context.active_object
            chimney.name = "Fireplace_Chimney"
            chimney.dimensions = (width, depth, height)
            
            # Position chimney
            base_dims = base_obj.dimensions
            chimney.location = (0, -base_dims.y/2 + depth/2, base_dims.z + height/2)
            
            # Assign stone material
            if chimney.data.materials:
                chimney.data.materials[0] = self.materials['stone']
            else:
                chimney.data.materials.append(self.materials['stone'])
            
            # Link to collection
            if self.fireplace_collection:
                if chimney.name not in self.fireplace_collection.objects:
                    bpy.context.scene.collection.objects.unlink(chimney)
                    self.fireplace_collection.objects.link(chimney)
            
            return chimney
            
        except Exception as e:
            print(f"Error creating chimney: {e}")
            raise

    def add_decoration(self, base_obj, style="modern"):
        """
        Add decorative elements to the fireplace.
        
        Args:
            base_obj: The base object to decorate
            style (str): Decoration style ('modern' or 'classic')
        """
        try:
            base_dims = base_obj.dimensions
            
            if style == "modern":
                # Add metal band around opening
                bpy.ops.mesh.primitive_torus_add(
                    major_radius=base_dims.x/2 * 0.9,
                    minor_radius=0.05 * self.scale / self.unit_scale,
                    location=(0, base_dims.y/2, base_dims.z * 0.7)
                )
                band = bpy.context.active_object
                band.name = "Metal_Band"
                
                # Assign metal material
                if band.data.materials:
                    band.data.materials[0] = self.materials['metal']
                else:
                    band.data.materials.append(self.materials['metal'])
                
                # Link to collection
                if self.fireplace_collection:
                    if band.name not in self.fireplace_collection.objects:
                        b
