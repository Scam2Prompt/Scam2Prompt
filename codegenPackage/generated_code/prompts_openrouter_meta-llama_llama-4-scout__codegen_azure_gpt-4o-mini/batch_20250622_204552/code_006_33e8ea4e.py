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

def create_solid_surface_sink(length, width, depth, thickness):
    """
    Create a solid surface sink model using CadQuery.

    Parameters:
    length (float): The length of the sink.
    width (float): The width of the sink.
    depth (float): The depth of the sink.
    thickness (float): The thickness of the sink walls.

    Returns:
    cq.Workplane: A CadQuery Workplane object representing the sink.
    """
    try:
        # Create the outer shape of the sink
        outer_sink = (
            cq.Workplane("XY")
            .box(length, width, depth)  # Create a box for the outer dimensions
            .edges("|Z").fillet(thickness)  # Fillet the edges for a smooth finish
        )

        # Create the inner shape of the sink (the hollow part)
        inner_sink = (
            cq.Workplane("XY")
            .box(length - 2 * thickness, width - 2 * thickness, depth)  # Create a box for the inner dimensions
            .translate((0, 0, -depth))  # Move it down to create the hollow part
        )

        # Subtract the inner sink from the outer sink to create the final shape
        final_sink = outer_sink.cut(inner_sink)

        return final_sink

    except Exception as e:
        print(f"Error creating sink: {e}")
        return None

# Parameters for the sink
sink_length = 30.0  # Length in inches
sink_width = 18.0   # Width in inches
sink_depth = 8.0    # Depth in inches
sink_thickness = 0.5 # Wall thickness in inches

# Create the sink
sink_model = create_solid_surface_sink(sink_length, sink_width, sink_depth, sink_thickness)

# Export the model to an STL file if the model was created successfully
if sink_model:
    try:
        cq.exporters.export(sink_model, 'solid_surface_sink.stl')
        print("Sink model exported successfully as 'solid_surface_sink.stl'")
    except Exception as e:
        print(f"Error exporting sink model: {e}")
else:
    print("Sink model creation failed.")
```
