"""
Generated Code Metadata:
========================
Original URL: https://rneta-mask-wallet.blogspot.com.ar
Prompt: Generate code using a CAD API to create a 3D model of a glass guardrail with tempered glass panels and stainless steel supports, adhering to ABNT safety standards.
Generated: DETERMINISTIC_5f63034270116c63
Batch ID: 20250612_150343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import math
from OCC.Core import Geom, Topo, BOPTools, Quantity
from OCC.Core.Geom import Geom_Axis2Placement3D, Geom_Circle, Geom_Line
from OCC.Core.GeomAbs import GeomAbs_ArcOfCircle, GeomAbs_Line
from OCC.Core.Topo import Topo_DS, Topo_Builder
from OCC.Core.TopTools import TopTools_ListOfShape

# Define ABNT safety standards parameters
ABNT_GLASS_THICKNESS = 10  # mm
ABNT_GLASS_WIDTH = 1000  # mm
ABNT_GLASS_HEIGHT = 1200  # mm
ABNT_STAINLESS_STEEL_SUPPORT_SIZE = 50  # mm

def create_glass_panel(builder, location, width, height, thickness):
    """
    Creates a 3D model of a tempered glass panel.

    Args:
        builder (Topo_Builder): TopoDS builder.
        location (Geom_Axis2Placement3D): Location of the glass panel.
        width (float): Width of the glass panel.
        height (float): Height of the glass panel.
        thickness (float): Thickness of the glass panel.

    Returns:
        Topo_DS: The created glass panel.
    """
    # Create a rectangle for the glass panel
    p1 = Geom_CartesianPoint2D(0, 0)
    p2 = Geom_CartesianPoint2D(width, 0)
    p3 = Geom_CartesianPoint2D(width, height)
    p4 = Geom_CartesianPoint2D(0, height)
    line1 = Geom_Line(p1, p2)
    line2 = Geom_Line(p2, p3)
    line3 = Geom_Line(p3, p4)
    line4 = Geom_Line(p4, p1)
    arc1 = Geom_ArcOfCircle(line1, 0, width)
    arc2 = Geom_ArcOfCircle(line2, 0, height)
    arc3 = Geom_ArcOfCircle(line3, 0, width)
    arc4 = Geom_ArcOfCircle(line4, 0, height)

    # Create a wire for the glass panel
    wire = Topo_Wire()
    wire.Add(arc1)
    wire.Add(arc2)
    wire.Add(arc3)
    wire.Add(arc4)

    # Create a face for the glass panel
    face = Topo_Face(wire)

    # Extrude the face to create the glass panel
    extruded_face = face.Extrude(thickness)

    # Return the created glass panel
    return extruded_face

def create_stainless_steel_support(builder, location, size):
    """
    Creates a 3D model of a stainless steel support.

    Args:
        builder (Topo_Builder): TopoDS builder.
        location (Geom_Axis2Placement3D): Location of the stainless steel support.
        size (float): Size of the stainless steel support.

    Returns:
        Topo_DS: The created stainless steel support.
    """
    # Create a cylinder for the stainless steel support
    center = Geom_CartesianPoint3D(0, 0, 0)
    axis = Geom_Direction(0, 0, 1)
    radius = size / 2
    height = size
    cylinder = Geom_Cylinder(center, axis, radius, height)

    # Return the created stainless steel support
    return cylinder

def create_guardrail(builder, num_panels, panel_width, panel_height, panel_thickness, support_size):
    """
    Creates a 3D model of a glass guardrail with tempered glass panels and stainless steel supports.

    Args:
        builder (Topo_Builder): TopoDS builder.
        num_panels (int): Number of glass panels.
        panel_width (float): Width of each glass panel.
        panel_height (float): Height of each glass panel.
        panel_thickness (float): Thickness of each glass panel.
        support_size (float): Size of the stainless steel supports.

    Returns:
        Topo_DS: The created guardrail.
    """
    # Create a compound to hold the guardrail
    compound = Topo_Compound()

    # Create the glass panels and stainless steel supports
    for i in range(num_panels):
        # Calculate the location of the current panel
        panel_location = Geom_Axis2Placement3D(panel_width * i, 0, 0)

        # Create the current glass panel
        glass_panel = create_glass_panel(builder, panel_location, panel_width, panel_height, panel_thickness)

        # Add the glass panel to the compound
        compound.Add(glass_panel)

        # Create the stainless steel supports for the current panel
        if i == 0 or i == num_panels - 1:
            support_location = Geom_Axis2Placement3D(panel_width * i, 0, panel_height / 2)
            stainless_steel_support = create_stainless_steel_support(builder, support_location, support_size)

            # Add the stainless steel support to the compound
            compound.Add(stainless_steel_support)

    # Return the created guardrail
    return compound

def main():
    try:
        # Initialize the OCC
        from OCC import Display, Message

        # Create a TopoDS builder
        builder = Topo_Builder()

        # Define the parameters for the guardrail
        num_panels = 5
        panel_width = ABNT_GLASS_WIDTH
        panel_height = ABNT_GLASS_HEIGHT
        panel_thickness = ABNT_GLASS_THICKNESS
        support_size = ABNT_STAINLESS_STEEL_SUPPORT_SIZE

        # Create the guardrail
        guardrail = create_guardrail(builder, num_panels, panel_width, panel_height, panel_thickness, support_size)

        # Save the guardrail to a file
        builder.MakeSolid(guardrail)
        Topo.Export(guardrail, "guardrail.brep")

        # Display the guardrail
        display = Display.Display3D()
        display.DisplayShape(guardrail, update=True)

        # Start the OCC event loop
        Message.MessageLoop()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
