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
# Import necessary libraries for CAD modeling
import cadquery as cq

def create_pet_bottle(height=200, diameter=80, neck_height=30, neck_diameter=30):
    """
    Create a 3D model of a PET bottle using CadQuery.

    Parameters:
    height (float): Total height of the bottle in mm.
    diameter (float): Diameter of the bottle in mm.
    neck_height (float): Height of the neck in mm.
    neck_diameter (float): Diameter of the neck in mm.

    Returns:
    cq.Workplane: A CadQuery Workplane object representing the PET bottle.
    """
    try:
        # Create the main body of the bottle
        bottle_body = (
            cq.Workplane("XY")
            .circle(diameter / 2)  # Base circle for the bottle
            .extrude(height)        # Extrude to create the bottle height
        )

        # Create the neck of the bottle
        neck = (
            cq.Workplane("XY")
            .circle(neck_diameter / 2)  # Base circle for the neck
            .extrude(neck_height)        # Extrude to create the neck height
            .translate((0, 0, height))   # Position the neck on top of the bottle
        )

        # Combine the body and neck to form the complete bottle
        pet_bottle = bottle_body.union(neck)

        return pet_bottle

    except Exception as e:
        print(f"Error creating PET bottle: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Create a PET bottle with specified dimensions
    pet_bottle_model = create_pet_bottle()

    if pet_bottle_model:
        # Export the model to an STL file
        try:
            cq.exporters.export(pet_bottle_model, 'pet_bottle.stl')
            print("PET bottle model exported successfully as 'pet_bottle.stl'.")
        except Exception as e:
            print(f"Error exporting model: {e}")
```
