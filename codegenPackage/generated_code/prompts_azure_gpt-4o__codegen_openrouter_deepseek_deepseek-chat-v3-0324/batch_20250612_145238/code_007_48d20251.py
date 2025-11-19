"""
Generated Code Metadata:
========================
Original URL: https://mmgroupnepal.com
Prompt: Provide code examples for designing 3D models of PET bottles using CAD libraries, tailored to MM Group Nepal's expertise in transforming designs into packaging solutions.
Generated: DETERMINISTIC_48d202514f89beb7
Batch ID: 20250612_145238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import cadquery as cq
from cadquery import exporters
import math

def create_pet_bottle(
    height=200, 
    diameter=50, 
    neck_height=25, 
    neck_diameter=25,
    wall_thickness=2,
    base_thickness=5
):
    """
    Creates a 3D model of a PET bottle with customizable dimensions.
    
    Args:
        height: Total height of the bottle (mm)
        diameter: Maximum diameter of the bottle body (mm)
        neck_height: Height of the neck section (mm)
        neck_diameter: Outer diameter of the neck (mm)
        wall_thickness: Thickness of the bottle walls (mm)
        base_thickness: Thickness of the base (mm)
        
    Returns:
        cadquery.Workplane: 3D model of the PET bottle
    """
    
    try:
        # Create the bottle body (tapered cylinder)
        body = (
            cq.Workplane("XY")
            .circle(diameter / 2)
            .workplane(offset=height - neck_height)
            .circle(neck_diameter / 2)
            .loft(combine=True)
        )
        
        # Hollow out the bottle
        inner_diameter = diameter - (2 * wall_thickness)
        inner_neck_diameter = neck_diameter - (2 * wall_thickness)
        
        inner_body = (
            cq.Workplane("XY")
            .circle(inner_diameter / 2)
            .workplane(offset=height - neck_height - base_thickness)
            .circle(inner_neck_diameter / 2)
            .loft(combine=True)
        )
        
        bottle = body.cut(inner_body)
        
        # Add the neck thread (simplified)
        thread = (
            cq.Workplane("XY")
            .workplane(offset=height - neck_height)
            .circle(neck_diameter / 2)
            .workplane(offset=neck_height)
            .circle(neck_diameter / 2)
            .loft(combine=True)
        )
        
        bottle = bottle.union(thread)
        
        # Add base reinforcement
        base = (
            cq.Workplane("XY")
            .circle(diameter / 2)
            .extrude(base_thickness)
        )
        
        bottle = bottle.union(base)
        
        # Add rounded edges
        bottle = bottle.edges("|Z").fillet(2)
        bottle = bottle.edges(">Z").fillet(1)
        
        return bottle
        
    except Exception as e:
        print(f"Error creating PET bottle model: {str(e)}")
        raise

def export_bottle(bottle, filename="pet_bottle.step"):
    """
    Exports the bottle model to a file.
    
    Args:
        bottle: cadquery.Workplane object
        filename: Output filename
    """
    try:
        exporters.export(bottle, filename)
        print(f"Successfully exported bottle to {filename}")
    except Exception as e:
        print(f"Error exporting bottle: {str(e)}")
        raise

# Example usage
if __name__ == "__main__":
    try:
        # Create a standard 500ml PET bottle
        bottle = create_pet_bottle(
            height=220,
            diameter=65,
            neck_height=30,
            neck_diameter=28
        )
        
        # Export to STEP file for manufacturing
        export_bottle(bottle, "mm_group_pet_bottle.step")
        
        # Show in CAD viewer (if running in Jupyter)
        show_object(bottle)
        
    except Exception as e:
        print(f"Error in main execution: {str(e)}")
```
