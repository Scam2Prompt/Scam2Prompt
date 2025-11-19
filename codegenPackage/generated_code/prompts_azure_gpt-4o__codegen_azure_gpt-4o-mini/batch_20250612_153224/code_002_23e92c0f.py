"""
Generated Code Metadata:
========================
Original URL: https://nyikudesign.com
Prompt: Create a code snippet using a CAD API to design a "bed loft" for a small bedroom, inspired by Nyiku Design's blog tips on maximizing space in small rooms.
Generated: DETERMINISTIC_23e92c0f58dd6d42
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import cadquery as cq

def create_bed_loft(length, width, height, leg_thickness, shelf_thickness):
    """
    Create a bed loft design using CadQuery.

    Parameters:
    length (float): The length of the bed loft.
    width (float): The width of the bed loft.
    height (float): The height of the bed loft.
    leg_thickness (float): The thickness of the legs supporting the loft.
    shelf_thickness (float): The thickness of the shelf on top of the loft.

    Returns:
    cq.Workplane: A CadQuery Workplane object representing the bed loft.
    """
    try:
        # Create the main bed platform
        bed_platform = (
            cq.Workplane("XY")
            .box(length, width, shelf_thickness)
            .translate((0, 0, height - shelf_thickness))
        )

        # Create the legs of the bed loft
        leg = (
            cq.Workplane("XY")
            .box(leg_thickness, leg_thickness, height - shelf_thickness)
        )

        # Position the legs at each corner of the bed platform
        legs = (
            leg.translate((length / 2 - leg_thickness / 2, width / 2 - leg_thickness / 2, 0))  # Front right leg
            .union(leg.translate((-length / 2 + leg_thickness / 2, width / 2 - leg_thickness / 2, 0)))  # Front left leg
            .union(leg.translate((length / 2 - leg_thickness / 2, -width / 2 + leg_thickness / 2, 0)))  # Back right leg
            .union(leg.translate((-length / 2 + leg_thickness / 2, -width / 2 + leg_thickness / 2, 0)))  # Back left leg
        )

        # Combine the bed platform and legs
        bed_loft = bed_platform.union(legs)

        return bed_loft

    except Exception as e:
        print(f"An error occurred while creating the bed loft: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Define dimensions for the bed loft
    length = 200.0  # Length in cm
    width = 100.0   # Width in cm
    height = 180.0  # Height in cm
    leg_thickness = 5.0  # Thickness of the legs in cm
    shelf_thickness = 2.0  # Thickness of the shelf in cm

    # Create the bed loft
    bed_loft = create_bed_loft(length, width, height, leg_thickness, shelf_thickness)

    # Export the design to an STL file if creation was successful
    if bed_loft:
        bed_loft.exportStl("bed_loft.stl")
        print("Bed loft design exported successfully.")
    else:
        print("Failed to create bed loft design.")
```
