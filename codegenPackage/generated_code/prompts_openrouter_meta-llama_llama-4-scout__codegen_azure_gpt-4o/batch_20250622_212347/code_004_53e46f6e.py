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

Creating a CAD design for a rotary air lock used in rice milling requires specialized software like AutoCAD, SolidWorks, or Fusion 360. These tools use scripting languages such as Python (via APIs) or their own proprietary scripting environments. Below is Python code using the `cadquery` library, which is a Python-based CAD modeling framework. This code generates a simplified rotary air lock design.

```python
import cadquery as cq

# Parameters for the rotary air lock
body_diameter = 100  # Diameter of the main body in mm
body_length = 150    # Length of the main body in mm
shaft_diameter = 20  # Diameter of the central shaft in mm
shaft_length = 200   # Length of the shaft in mm
rotor_blade_count = 6  # Number of rotor blades
rotor_blade_thickness = 5  # Thickness of each rotor blade in mm
rotor_blade_length = 90  # Length of each rotor blade in mm

# Create the main cylindrical body
body = cq.Workplane("XY").circle(body_diameter / 2).extrude(body_length)

# Create the central shaft
shaft = (
    cq.Workplane("XY")
    .circle(shaft_diameter / 2)
    .extrude(shaft_length)
    .translate((0, 0, -shaft_length / 2))
)

# Create rotor blades
rotor_blades = cq.Workplane("XY")
for i in range(rotor_blade_count):
    angle = 360 / rotor_blade_count * i
    blade = (
        cq.Workplane("XY")
        .rect(rotor_blade_thickness, rotor_blade_length)
        .extrude(body_length)
        .translate((body_diameter / 2 - rotor_blade_length / 2, 0, 0))
        .rotate((0, 0, 0), (0, 0, 1), angle)
    )
    rotor_blades = rotor_blades.union(blade)

# Combine the body, shaft, and rotor blades
rotary_air_lock = body.union(shaft).union(rotor_blades)

# Export the design to a STEP file (widely used CAD format)
cq.exporters.export(rotary_air_lock, "rotary_air_lock.step")

# Display the design (optional, requires a viewer)
show_object(rotary_air_lock)
```

### Notes:
1. Install `cadquery` before running this code: `pip install cadquery`.
2. The generated STEP file (`rotary_air_lock.step`) can be opened in any CAD software for further refinement or visualization.
3. This is a simplified design and may need adjustments based on specific engineering requirements.
