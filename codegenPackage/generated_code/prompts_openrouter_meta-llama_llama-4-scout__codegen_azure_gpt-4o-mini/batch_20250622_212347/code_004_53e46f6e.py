"""
Generated Code Metadata:
========================
Original URL: https://mechanosolutions.in
Prompt: "Generate a CAD design for a rotary air lock used in rice milling."
Generated: DETERMINISTIC_53e46f6e482508fc
Batch ID: 20250622_212347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import cadquery as cq

def create_rotary_air_lock(diameter: float, height: float, wall_thickness: float, num_ports: int) -> cq.Workplane:
    """
    Create a CAD design for a rotary air lock used in rice milling.

    Parameters:
    diameter (float): The outer diameter of the rotary air lock.
    height (float): The height of the rotary air lock.
    wall_thickness (float): The thickness of the walls of the rotary air lock.
    num_ports (int): The number of ports on the rotary air lock.

    Returns:
    cq.Workplane: A CadQuery Workplane object representing the rotary air lock.
    """
    try:
        # Create the outer cylinder for the rotary air lock
        outer_cylinder = cq.Workplane("XY").cylinder(height, diameter / 2)

        # Create the inner cylinder to hollow out the rotary air lock
        inner_cylinder = cq.Workplane("XY").cylinder(height, (diameter / 2) - wall_thickness)

        # Subtract the inner cylinder from the outer cylinder to create the hollow structure
        rotary_air_lock = outer_cylinder.cut(inner_cylinder)

        # Create ports on the rotary air lock
        for i in range(num_ports):
            angle = (360 / num_ports) * i
            port = (
                cq.Workplane("XY")
                .circle(diameter / 4)  # Port diameter
                .extrude(wall_thickness)  # Port depth
                .translate((0, 0, height / 2))  # Position the port in the middle of the height
                .rotate((0, 0, 1), angle)  # Rotate to the correct angle
            )
            rotary_air_lock = rotary_air_lock.cut(port)

        return rotary_air_lock

    except Exception as e:
        print(f"Error creating rotary air lock: {e}")
        return None

# Parameters for the rotary air lock
diameter = 300.0  # Outer diameter in mm
height = 200.0    # Height in mm
wall_thickness = 10.0  # Wall thickness in mm
num_ports = 6     # Number of ports

# Generate the rotary air lock design
rotary_air_lock_design = create_rotary_air_lock(diameter, height, wall_thickness, num_ports)

# Export the design to an STL file if the design was created successfully
if rotary_air_lock_design:
    rotary_air_lock_design.val().exportStl("rotary_air_lock.stl")
    print("Rotary air lock design exported successfully.")
else:
    print("Failed to create rotary air lock design.")
```
