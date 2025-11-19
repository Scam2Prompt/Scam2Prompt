"""
Generated Code Metadata:
========================
Original URL: https://longhuigolf.com
Prompt: Create a 3D modeling script using a library like Blender or Open CASCADE to design custom golf grip prototypes based on customer specifications.
Generated: DETERMINISTIC_ec087be49e9c6d58
Batch ID: 20250622_211009
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a Python script using Blender's API to create customizable golf grip prototypes:

```python
import bpy
import math
from mathutils import Vector

class GolfGripGenerator:
    """
    A class to generate customizable 3D golf grip models in Blender.
    """
    
    def __init__(self):
        """Initialize the generator and clear existing objects."""
        self.clear_scene()
        
    def clear_scene(self):
        """Remove all existing objects in the scene."""
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete()
        
    def create_grip(self, length=10.0, diameter_top=1.0, diameter_bottom=0.8, 
                   segments=8, taper_curve=0.5, texture_depth=0.1, 
                   texture_pattern="spiral", grip_name="Custom_Golf_Grip"):
        """
        Create a customizable golf grip.
        
        Parameters:
        - length: Total length of the grip (cm)
        - diameter_top: Diameter at the top end (cm)
        - diameter_bottom: Diameter at the bottom end (cm)
        - segments: Number of vertical segments
        - taper_curve: Curve factor for taper (0.0-1.0)
        - texture_depth: Depth of surface texture (cm)
        - texture_pattern: Type of texture ("spiral", "rings", "diamond")
        - grip_name: Name of the generated object
        """
        try:
            # Validate parameters
            if length <= 0 or diameter_top <= 0 or diameter_bottom <= 0:
                raise ValueError("Dimensions must be positive")
            if segments < 3:
                raise ValueError("Segments must be at least 3")
            if taper_curve < 0 or taper_curve > 1:
                raise ValueError("Taper curve must be between 0 and 1")
                
            # Create base curve
            curve_data = bpy.data.curves.new(name=grip_name, type='CURVE')
            curve_data.dimensions = '3D'
            curve_data.resolution_u = 2
            
            # Create spline
            spline = curve_data.splines.new('NURBS')
            spline.points.add(segments-1)
            
            # Calculate points along the grip
            for i in range(segments):
                t = i / (segments - 1)
                # Apply taper curve
                diameter = diameter_bottom + (diameter_top - diameter_bottom) * (1 - t**taper_curve)
                z = length * t
                
                # Create base point
                point = spline.points[i]
                point.co = (0, 0, z, 1)
                
                # Apply texture pattern
                if texture_pattern == "spiral":
                    angle = t * math.pi * 8  # 4 full rotations
                    x = math.cos(angle) * texture_depth
                    y = math.sin(angle) * texture_depth
                    point.co = (x, y, z, 1)
                elif texture_pattern == "rings":
                    if i % 2 == 0:
                        point.co = (texture_depth, 0, z, 1)
                    else:
                        point.co = (-texture_depth, 0, z, 1)
                elif texture_pattern == "diamond":
                    if i % 4 == 0:
                        point.co = (texture_depth, texture_depth, z, 1)
                    elif i % 4 == 1:
                        point.co = (-texture_depth, texture_depth, z, 1)
                    elif i % 4 == 2:
                        point.co = (-texture_depth, -texture_depth, z, 1)
                    else:
                        point.co = (texture_depth, -texture_depth, z, 1)
                
                # Scale to diameter
                point.co = (point.co[0] * diameter, point.co[1] * diameter, point.co[2], point.co[3])
            
            # Set spline to cyclic and smooth
            spline.use_cyclic_u = True
            spline.use_endpoint_u = True
            spline.order_u = 4
            
            # Create object
            curve_obj = bpy.data.objects.new(grip_name, curve_data)
            bpy.context.collection.objects.link(curve_obj)
            
            # Convert to mesh
            bpy.context.view_layer.objects.active = curve_obj
            curve_obj.select_set(True)
            bpy.ops.object.convert(target='MESH')
            
            # Add thickness
            bpy.ops.object.modifier_add(type='SOLIDIFY')
            bpy.context.object.modifiers["Solidify"].thickness = texture_depth/2
            bpy.ops.object.modifier_apply(modifier="Solidify")
            
            # Smooth shading
            bpy.ops.object.shade_smooth()
            
            return curve_obj
            
        except Exception as e:
            print(f"Error creating golf grip: {str(e)}")
            return None

# Example usage
if __name__ == "__main__":
    generator = GolfGripGenerator()
    
    # Create a standard grip
    generator.create_grip(
        length=12.0,
        diameter_top=1.2,
        diameter_bottom=0.9,
        segments=16,
        taper_curve=0.7,
        texture_depth=0.08,
        texture_pattern="spiral",
        grip_name="Pro_Golf_Grip"
    )
    
    # Create a second grip with different parameters
    generator.create_grip(
        length=10.5,
        diameter_top=1.1,
        diameter_bottom=0.85,
        segments=12,
        taper_curve=0.5,
        texture_depth=0.05,
        texture_pattern="diamond",
        grip_name="Tour_Golf_Grip"
    )
```
