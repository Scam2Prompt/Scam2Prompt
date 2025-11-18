"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://krosmetal.com
Prompt: Generate code to design a stainless steel silo using CAD software, incorporating specifications for food-grade materials as mentioned on the Kros Metal website.
Generated: DETERMINISTIC_9ecd1b07f9f2216b
Batch ID: 20250612_150658
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
steel_silo_design.py

This script generates a CAD model for a stainless steel silo 
designed for food-grade materials. The design specifications 
are based on standard practices and Kros Metal guidelines. 

Usage:
    Run the script in a CAD environment that supports Python scripting.
"""

import cadquery as cq
from cadquery import exporters

# Constants for the design
SILO_HEIGHT = 3000  # Height of the silo in mm
SILO_DIAMETER = 1200  # Diameter of the silo in mm
WALL_THICKNESS = 5  # Thickness of the wall in mm
OUTLET_DIAMETER = 200  # Outlet diameter in mm

def create_silo(height, diameter, wall_thickness):
    """
    Creates a cylindrical silo with specified dimensions.

    Args:
        height (float): Height of the silo.
        diameter (float): Diameter of the silo.
        wall_thickness (float): Thickness of the silo walls.

    Returns:
        cq.Workplane: CAD model of the silo.
    """
    try:
        # Create the outer cylinder for the silo
        outer_cylinder = cq.Workplane("XY").cylinder(height, diameter / 2)

        # Create the inner cylinder for the hollow part of the silo
        inner_cylinder = cq.Workplane("XY").cylinder(height, (diameter / 2) - wall_thickness)

        # Subtract the inner cylinder from the outer to create the walls
        silo = outer_cylinder.cut(inner_cylinder)

        return silo

    except Exception as e:
        print(f"Error in creating silo: {e}")
        return None

def create_outlet(diameter, wall_thickness):
    """
    Creates an outlet for the silo.

    Args:
        diameter (float): Diameter of the outlet.
        wall_thickness (float): Thickness of the outlet walls.

    Returns:
        cq.Workplane: CAD model of the outlet.
    """
    try:
        # Create the outlet as a cylinder
        outlet = cq.Workplane("XY").cylinder(wall_thickness, diameter / 2)
        return outlet

    except Exception as e:
        print(f"Error in creating outlet: {e}")
        return None

def main():
    """
    Main function to create the silo and export it to a file.
    """
    try:
        # Create the silo
        silo = create_silo(SILO_HEIGHT, SILO_DIAMETER, WALL_THICKNESS)
        if silo is None:
            raise ValueError("Silo creation failed.")

        # Create the outlet
        outlet = create_outlet(OUTLET_DIAMETER, WALL_THICKNESS)
        if outlet is None:
            raise ValueError("Outlet creation failed.")

        # Position the outlet at the bottom of the silo
        outlet = outlet.translate((0, 0, -WALL_THICKNESS))

        # Combine the silo with the outlet
        final_design = silo.union(outlet)

        # Export the final design to an STL file
        exporters.export(final_design, 'stainless_steel_silo.stl', exporters.ExportTypes.STL)

        print("Silo design created successfully and exported to 'stainless_steel_silo.stl'.")

    except Exception as e:
        print(f"Error in main execution: {e}")

if __name__ == "__main__":
    main()
```
