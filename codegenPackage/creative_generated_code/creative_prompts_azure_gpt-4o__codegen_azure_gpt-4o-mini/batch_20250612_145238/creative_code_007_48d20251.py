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
# Import necessary CAD library for 3D modeling
import cadquery as cq

def create_pet_bottle(height=200, base_radius=30, neck_radius=15, neck_height=25):
    """
    Create a 3D model of a PET bottle using CadQuery.

    Parameters:
    height (float): The total height of the bottle in mm.
    base_radius (float): The radius of the bottle's base in mm.
    neck_radius (float): The radius of the bottle's neck in mm.
    neck_height (float): The height of the bottle's neck in mm.

    Returns:
    cq.Workplane: A CadQuery Workplane object representing the PET bottle.
    """

    try:
        # Create the base of the bottle
        bottle_base = (
            cq.Workplane("XY")
            .circle(base_radius)
            .extrude(height - neck_height)  # Create the body of the bottle
        )

        # Create the neck of the bottle
        bottle_neck = (
            cq.Workplane("XY")
            .workplane(offset=height - neck_height)  # Position to top of the body
            .circle(neck_radius)
            .extrude(neck_height)  # Create the neck of the bottle
        )
        
        # Combine the body and neck to form the complete bottle
        pet_bottle = bottle_base.add(bottle_neck)

        return pet_bottle

    except Exception as e:
        print(f"An error occurred while creating the PET bottle: {e}")
        return None

if __name__ == "__main__":
    # Create a PET bottle and export it to an STL file
    bottle = create_pet_bottle()
    
    if bottle is not None:
        # Export the bottle model to a file
        try:
            bottle.val().exportStl("pet_bottle.stl")
            print("PET bottle model created successfully and exported as 'pet_bottle.stl'.")
        except Exception as e:
            print(f"An error occurred while exporting the model: {e}")
    else:
        print("Failed to create the PET bottle model.")
```
