"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mmgroupnepal.com
Prompt: Provide code examples for designing 3D models of PET bottles using CAD libraries, tailored to MM Group Nepal's expertise in transforming designs into packaging solutions.
Generated: DETERMINISTIC_48d202514f89beb7
Batch ID: 20250612_145238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Code for designing a 3D model of a PET bottle using the Python CAD library `cadquery`.
# Ensure you have CadQuery installed: pip install cadquery

import cadquery as cq

def create_pet_bottle(
    height=200,      # Height of the bottle in mm
    diameter=70,     # Diameter of the bottle in mm
    neck_diameter=30, # Diameter of the neck in mm
    neck_height=30,   # Height of the neck in mm
    wall_thickness=2  # Wall thickness of the bottle in mm
):
    """
    Function to create a 3D model of a PET bottle using CadQuery.

    Parameters:
    - height (int): Total height of the bottle in mm.
    - diameter (int): Diameter of the main body of the bottle in mm.
    - neck_diameter (int): Diameter of the neck of the bottle in mm.
    - neck_height (int): Height of the neck in mm.
    - wall_thickness (int): Wall thickness of the bottle in mm.

    Returns:
    - cq.Workplane: A CadQuery 3D model of the PET bottle.
    """
    try:
        # Create the main cylindrical body of the bottle
        body = (
            cq.Workplane("XY")
            .circle(diameter / 2)  # Outer diameter
            .extrude(height - neck_height)  # Extrude the body up to the neck base
        )

        # Create the neck of the bottle
        neck = (
            cq.Workplane("XY")
            .workplane(offset=height - neck_height)  # Start at the top of the body
            .circle(neck_diameter / 2)  # Outer diameter of the neck
            .extrude(neck_height)  # Extrude the neck
        )

        # Hollow out the bottle to create the wall thickness
        hollow_body = body.union(neck).faces(">Z").shell(-wall_thickness)

        # Add grooves or threads on the neck for screw caps (simplified example)
        threads = (
            cq.Workplane("XY")
            .workplane(offset=height - neck_height)
            .circle(neck_diameter / 2.2)  # Slightly smaller than the neck diameter
            .extrude(neck_height / 2)
        )

        # Combine the threads with the bottle
        bottle_with_threads = hollow_body.union(threads)

        return bottle_with_threads

    except Exception as e:
        print(f"Error creating PET bottle model: {e}")
        return None

# Generate a PET bottle model
pet_bottle = create_pet_bottle()

# Export the model to a STEP file for further use in packaging solutions
if pet_bottle:
    try:
        pet_bottle.exportStep("pet_bottle_model.step")
        print("3D PET bottle model exported successfully!")
    except Exception as export_error:
        print(f"Error exporting PET bottle model: {export_error}")
```

This code generates a simplified 3D model of a PET bottle, hollowed out with a specified wall thickness, and exports it as a `.step` file which can be used in CAD software for further processing. Ensure you have CadQuery installed and configured in your Python environment.
