"""
Generated Code Metadata:
========================
Original URL: https://stethevent.org
Prompt: Provide step-by-step instructions to design and 3D print a rotating drying station for fishing lures, similar to the "3D Printed Fishing Lure Rotating Drying Station" project on Instructables.
Generated: DETERMINISTIC_dcfd78c4febb6c22
Batch ID: 20250612_153713
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import cadquery as cq
import math

# Constants
BASE_DIAMETER = 120  # mm
BASE_HEIGHT = 10  # mm
ROD_DIAMETER = 10  # mm
ROD_HEIGHT = 200  # mm
ARM_LENGTH = 100  # mm
ARM_WIDTH = 15  # mm
ARM_THICKNESS = 5  # mm
HOOK_HOLE_DIAMETER = 3  # mm
NUM_ARMS = 8  # Number of rotating arms
BEARING_OD = 22  # mm (608 bearing outer diameter)
BEARING_ID = 8  # mm (608 bearing inner diameter)
BEARING_HEIGHT = 7  # mm

def create_base():
    """Create the circular base of the drying station."""
    base = (
        cq.Workplane("XY")
        .circle(BASE_DIAMETER / 2)
        .extrude(BASE_HEIGHT)
    )
    
    # Add bearing housing
    bearing_housing = (
        cq.Workplane("XY")
        .workplane(offset=BASE_HEIGHT)
        .circle(BEARING_OD / 2 + 2)  # Add 2mm for press fit
        .extrude(BEARING_HEIGHT + 2)  # Extra 2mm for bearing retention
    )
    
    # Cut bearing hole
    bearing_hole = (
        cq.Workplane("XY")
        .workplane(offset=BASE_HEIGHT)
        .circle(BEARING_OD / 2)
        .extrude(BEARING_HEIGHT)
    )
    
    # Combine base with bearing housing
    base = base.union(bearing_housing)
    base = base.cut(bearing_hole)
    
    # Add center hole for rod
    center_hole = (
        cq.Workplane("XY")
        .workplane(offset=BASE_HEIGHT)
        .circle(BEARING_ID / 2)
        .extrude(ROD_HEIGHT)
    )
    base = base.cut(center_hole)
    
    return base

def create_rod():
    """Create the central rod that holds the rotating arms."""
    rod = (
        cq.Workplane("XY")
        .workplane(offset=BASE_HEIGHT)
        .circle(ROD_DIAMETER / 2)
        .extrude(ROD_HEIGHT)
    )
    
    # Add bearing press-fit section at bottom
    bearing_section = (
        cq.Workplane("XY")
        .workplane(offset=BASE_HEIGHT)
        .circle(BEARING_ID / 2 - 0.1)  # Slightly smaller for press fit
        .extrude(BEARING_HEIGHT)
    )
    rod = rod.union(bearing_section)
    
    return rod

def create_arm():
    """Create a single rotating arm for holding lures."""
    arm = (
        cq.Workplane("XY")
        .rect(ARM_LENGTH, ARM_WIDTH)
        .extrude(ARM_THICKNESS)
    )
    
    # Add hook holes along the arm
    for i in range(5):
        hole_pos = ARM_LENGTH / 6 * (i + 1)
        arm = (
            arm.faces(">Z")
            .workplane()
            .center(hole_pos - ARM_LENGTH/2, 0)
            .hole(HOOK_HOLE_DIAMETER)
        )
    
    # Add connection point to rod
    connection = (
        cq.Workplane("XY")
        .circle(ROD_DIAMETER / 2 + 1)  # Slightly larger for easy rotation
        .extrude(ARM_THICKNESS)
    )
    arm = arm.union(connection)
    
    return arm

def create_top_plate():
    """Create the top plate to hold the arms in place."""
    plate = (
        cq.Workplane("XY")
        .workplane(offset=ROD_HEIGHT - 10)  # Position near top of rod
        .circle(BASE_DIAMETER / 3)  # Smaller than base
        .extrude(5)  # 5mm thickness
    )
    
    # Add center hole
    center_hole = (
        cq.Workplane("XY")
        .workplane(offset=ROD_HEIGHT - 10)
        .circle(ROD_DIAMETER / 2 + 0.5)  # Slightly larger for rotation
        .extrude(10)
    )
    plate = plate.cut(center_hole)
    
    return plate

def assemble_drying_station():
    """Assemble all components into the complete drying station."""
    base = create_base()
    rod = create_rod()
    top_plate = create_top_plate()
    
    # Create and position arms
    arms = []
    for i in range(NUM_ARMS):
        arm = create_arm()
        angle = 360 / NUM_ARMS * i
        arm = arm.rotate((0, 0, 0), (0, 0, 1), angle)
        arm = arm.translate((0, 0, ROD_HEIGHT / 2))
        arms.append(arm)
    
    # Combine all parts
    drying_station = base.add(rod)
    for arm in arms:
        drying_station = drying_station.add(arm)
    drying_station = drying_station.add(top_plate)
    
    return drying_station

def export_stl(part, filename):
    """Export a part to STL format."""
    try:
        cq.exporters.export(part, filename, tolerance=0.001, angularTolerance=0.1)
        print(f"Successfully exported {filename}")
    except Exception as e:
        print(f"Error exporting {filename}: {str(e)}")

def main():
    """Main function to generate and export all parts."""
    # Generate individual parts
    base = create_base()
    rod = create_rod()
    arm = create_arm()
    top_plate = create_top_plate()
    
    # Export individual parts for printing
    export_stl(base, "drying_station_base.stl")
    export_stl(rod, "drying_station_rod.stl")
    export_stl(arm, "drying_station_arm.stl")
    export_stl(top_plate, "drying_station_top_plate.stl")
    
    # Generate and export assembled version for visualization
    assembled = assemble_drying_station()
    export_stl(assembled, "drying_station_assembled.stl")

if __name__ == "__main__":
    main()
```
