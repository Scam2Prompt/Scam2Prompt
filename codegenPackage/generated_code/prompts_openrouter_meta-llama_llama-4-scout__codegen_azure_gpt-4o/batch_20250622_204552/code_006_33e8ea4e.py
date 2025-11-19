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

<<<<<<< HEAD
def create_topart_sink():
    """
    Function to design a Topart solid surface sink using CADQuery.
    The sink is seamless and stain-resistant, with smooth edges and a modern design.
=======
# Function to create a Topart solid surface sink
def create_sink():
    """
    Creates a CAD model of a Topart solid surface sink.
    The sink is designed to be seamless and stain-resistant.
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
    """
    try:
        # Define dimensions for the sink
        sink_length = 600  # Length of the sink in mm
        sink_width = 400   # Width of the sink in mm
        sink_depth = 150   # Depth of the sink in mm
        wall_thickness = 10  # Thickness of the sink walls in mm

        # Create the outer shell of the sink
        outer_sink = (
            cq.Workplane("XY")
<<<<<<< HEAD
            .rect(sink_length, sink_width)
            .extrude(sink_depth)
=======
            .box(sink_length, sink_width, sink_depth)
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
        )

        # Create the inner hollow part of the sink
        inner_sink = (
            cq.Workplane("XY")
<<<<<<< HEAD
            .rect(sink_length - 2 * wall_thickness, sink_width - 2 * wall_thickness)
            .extrude(sink_depth - wall_thickness)
=======
            .box(sink_length - 2 * wall_thickness, 
                 sink_width - 2 * wall_thickness, 
                 sink_depth - wall_thickness)
            .translate((0, 0, wall_thickness / 2))  # Position inner sink correctly
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
        )

        # Subtract the inner hollow part from the outer shell to create the sink walls
        sink = outer_sink.cut(inner_sink)

<<<<<<< HEAD
        # Add a drain hole at the center of the sink
        drain_hole_diameter = 50  # Diameter of the drain hole in mm
        sink = (
            sink.faces(">Z")
=======
        # Add a drain hole at the center of the sink bottom
        drain_hole_diameter = 50  # Diameter of the drain hole in mm
        sink = (
            sink.faces(">Z")  # Select the bottom face of the sink
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
            .workplane(centerOption="CenterOfBoundBox")
            .hole(drain_hole_diameter)
        )

<<<<<<< HEAD
        # Smooth the edges for a seamless design
=======
        # Add rounded edges for seamless design
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
        sink = sink.edges().fillet(5)

        return sink

    except Exception as e:
<<<<<<< HEAD
        print(f"An error occurred while creating the sink: {e}")
        return None


# Generate the sink model
topart_sink = create_topart_sink()

# Export the sink model to a STEP file for use in CAD software
if topart_sink:
    topart_sink.exportStep("Topart_Solid_Surface_Sink.step")
    print("Sink design successfully exported to 'Topart_Solid_Surface_Sink.step'.")
else:
    print("Failed to create the sink design.")
=======
        # Handle any errors that occur during sink creation
        print(f"An error occurred while creating the sink: {e}")
        return None

# Generate the sink model
sink_model = create_sink()

# Export the sink model to a STEP file for use in CAD software
if sink_model:
    sink_model.exportStep("Topart_Solid_Surface_Sink.step")
    print("Sink model successfully created and exported to 'Topart_Solid_Surface_Sink.step'.")
else:
    print("Failed to create the sink model.")
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
```
