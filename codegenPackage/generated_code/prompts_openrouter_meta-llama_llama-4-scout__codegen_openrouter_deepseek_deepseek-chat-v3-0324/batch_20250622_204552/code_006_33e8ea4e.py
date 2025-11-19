"""
Generated Code Metadata:
========================
Original URL: https://topartksa.com
Prompt: "Design a Topart solid surface sink using a CAD software, taking into account its seamless and stain-resistant features."
Generated: DETERMINISTIC_33e8ea4ecf4aa9c1
Batch ID: 20250622_204552
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

def create_topart_sink():
    """
    Creates a Topart solid surface sink model with seamless and stain-resistant features.
    Returns a CQ assembly object representing the sink.
    """
    # Main sink basin dimensions
    length = 500  # mm
    width = 400   # mm
    depth = 150   # mm
    wall_thickness = 10  # mm
    fillet_radius = 20   # mm
    
    # Create the outer shell
    outer_shell = (
        cq.Workplane("XY")
        .box(length, width, depth)
        .faces(">Z")
        .shell(-wall_thickness)
        .edges("|Z")
        .fillet(fillet_radius)
    )
    
    # Create drain hole
    drain_diameter = 80  # mm
    sink = (
        outer_shell
        .faces("<Z")
        .workplane()
        .hole(drain_diameter)
        .edges(">Z")
        .fillet(5)  # Smooth edge for easy cleaning
    )
    
    # Add overflow channel
    overflow_width = 10  # mm
    overflow_depth = 5   # mm
    sink = (
        sink
        .faces(">Z")
        .workplane(offset=-10)
        .rect(length - 50, overflow_width, forConstruction=True)
        .vertices()
        .circle(overflow_depth/2)
        .extrude(overflow_depth)
    )
    
    # Add mounting points
    mount_diameter = 8  # mm
    sink = (
        sink
        .faces("<Z")
        .workplane(offset=5)
        .rarray(length - 50, width - 50, 2, 2)
        .hole(mount_diameter)
    )
    
    return sink

# Create and export the sink model
sink_model = create_topart_sink()
exporters.export(sink_model, 'topart_sink.stl')
```
