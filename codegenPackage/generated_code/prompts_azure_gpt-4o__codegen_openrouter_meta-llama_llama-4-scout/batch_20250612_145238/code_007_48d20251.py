"""
Generated Code Metadata:
========================
Original URL: https://mmgroupnepal.com
Prompt: Provide code examples for designing 3D models of PET bottles using CAD libraries, tailored to MM Group Nepal's expertise in transforming designs into packaging solutions.
Generated: DETERMINISTIC_48d202514f89beb7
Batch ID: 20250612_145238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from OCC.Core import Geom, Topo, BOPTools, DraftTools
from OCC.Display import Display, DisplayMode

# Define a function to create a PET bottle 3D model
def create_pet_bottle(height, radius, thickness, neck_radius, neck_height):
    """
    Create a 3D model of a PET bottle.

    Parameters:
    height (float): The height of the bottle.
    radius (float): The radius of the bottle body.
    thickness (float): The thickness of the bottle wall.
    neck_radius (float): The radius of the bottle neck.
    neck_height (float): The height of the bottle neck.

    Returns:
    TopoDS_Shape: The 3D model of the PET bottle.
    """

    # Create a bottle body
    body = create_cylinder(height, radius, thickness)

    # Create a bottle neck
    neck = create_cylinder(neck_height, neck_radius, thickness)

    # Combine the body and neck
    bottle = combine_shapes(body, neck)

    return bottle

# Define a function to create a cylinder
def create_cylinder(height, radius, thickness):
    """
    Create a 3D model of a cylinder.

    Parameters:
    height (float): The height of the cylinder.
    radius (float): The radius of the cylinder.
    thickness (float): The thickness of the cylinder wall.

    Returns:
    TopoDS_Shape: The 3D model of the cylinder.
    """

    # Create a circle
    circle = Geom.Circle(Geom.Point(0, 0, 0), radius)

    # Create a wire
    wire = Topo.Wire(circle)

    # Create a face
    face = Topo.Face(wire)

    # Extrude the face to create a solid
    solid = Topo.Solid(Topo.Sweep(face, Geom.Dir(0, 0, 1), height))

    # Create a shell with a specified thickness
    shell = BOPTools.Splitter().thickness(solid, thickness)

    return shell

# Define a function to combine two shapes
def combine_shapes(shape1, shape2):
    """
    Combine two 3D shapes.

    Parameters:
    shape1 (TopoDS_Shape): The first shape.
    shape2 (TopoDS_Shape): The second shape.

    Returns:
    TopoDS_Shape: The combined shape.
    """

    # Use the fuse tool to combine the shapes
    combined_shape = BOPTools.Splitter().fuse(shape1, shape2)

    return combined_shape

# Create a PET bottle 3D model
if __name__ == "__main__":
    try:
        # Define the parameters
        height = 200  # mm
        radius = 50  # mm
        thickness = 1  # mm
        neck_radius = 20  # mm
        neck_height = 50  # mm

        # Create the PET bottle 3D model
        bottle = create_pet_bottle(height, radius, thickness, neck_radius, neck_height)

        # Display the 3D model
        display = Display
        display.DisplayShape(bottle, update=True)
        display.FitAll()
        display.Start()

    except Exception as e:
        print(f"An error occurred: {e}")
```
