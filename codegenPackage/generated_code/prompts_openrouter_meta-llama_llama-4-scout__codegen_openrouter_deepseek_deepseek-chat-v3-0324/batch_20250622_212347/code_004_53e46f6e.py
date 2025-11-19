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
from cadquery import exporters

def create_rotary_airlock():
    """
    Creates a rotary airlock design for rice milling applications.
    Returns a CadQuery assembly of the airlock components.
    """
    # Parameters (in mm)
    housing_diameter = 200
    housing_length = 300
    wall_thickness = 10
    rotor_diameter = 180
    rotor_length = 290
    vane_count = 8
    vane_thickness = 5
    shaft_diameter = 30
    bearing_diameter = 50
    bearing_width = 20
    flange_thickness = 15
    flange_width = 30
    
    try:
        # Create housing cylinder
        housing = (
            cq.Workplane("XY")
            .circle(housing_diameter/2)
            .extrude(housing_length)
            .faces(">Z")
            .circle((housing_diameter/2) - wall_thickness)
            .cutThruAll()
        )
        
        # Add flanges
        housing = (
            housing.faces("<Z")
            .workplane()
            .circle(housing_diameter/2 + flange_width)
            .extrude(flange_thickness)
            .faces(">Z")
            .workplane()
            .circle(housing_diameter/2)
            .cutBlind(flange_thickness)
        )
        
        housing = (
            housing.faces(">Z")
            .workplane()
            .circle(housing_diameter/2 + flange_width)
            .extrude(flange_thickness)
            .faces("<Z")
            .workplane()
            .circle(housing_diameter/2)
            .cutBlind(flange_thickness)
        )
        
        # Create rotor
        rotor = (
            cq.Workplane("XY")
            .circle(rotor_diameter/2)
            .extrude(rotor_length)
        )
        
        # Add shaft
        rotor = (
            rotor.faces("<Z")
            .workplane()
            .circle(shaft_diameter/2)
            .extrude(-50)
            .faces(">Z")
            .workplane()
            .circle(shaft_diameter/2)
            .extrude(50)
        )
        
        # Add vanes
        angle_step = 360 / vane_count
        for i in range(vane_count):
            rotor = (
                rotor.workplane(offset=rotor_length/2)
                .transformed(rotate=(0, 0, angle_step * i))
                .rect(vane_thickness, rotor_diameter, centered=False)
                .extrude(rotor_length/2, both=True)
            )
        
        # Create bearings
        bearing1 = (
            cq.Workplane("XY")
            .workplane(offset=-25)
            .circle(bearing_diameter/2)
            .extrude(bearing_width)
            .faces(">Z")
            .workplane()
            .circle(shaft_diameter/2)
            .cutThruAll()
        )
        
        bearing2 = (
            cq.Workplane("XY")
            .workplane(offset=housing_length + 25)
            .circle(bearing_diameter/2)
            .extrude(bearing_width)
            .faces(">Z")
            .workplane()
            .circle(shaft_diameter/2)
            .cutThruAll()
        )
        
        # Create assembly
        assembly = cq.Assembly()
        assembly.add(housing, color=cq.Color(0.8, 0.8, 0.8))
        assembly.add(rotor, loc=cq.Location((0, 0, 0)), color=cq.Color(0.5, 0.5, 0.5))
        assembly.add(bearing1, color=cq.Color(0.2, 0.2, 0.2))
        assembly.add(bearing2, color=cq.Color(0.2, 0.2, 0.2))
        
        return assembly
        
    except Exception as e:
        print(f"Error creating rotary airlock: {str(e)}")
        return None

# Generate and export the design
if __name__ == "__main__":
    airlock = create_rotary_airlock()
    if airlock:
        exporters.export(airlock.toCompound(), "rotary_airlock.step")
```
