"""
Generated Code Metadata:
========================
Original URL: https://gosonicsolutions.com
Prompt: "Design a basic ultrasonic cleaning system using CAD software, specifying dimensions and features for a particular industrial application."
Generated: DETERMINISTIC_52664f0de82973d9
Batch ID: 20250622_212534
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries for CAD design
import cadquery as cq

def create_ultrasonic_cleaner(length, width, height, tank_depth, transducer_count):
    """
    Create a basic ultrasonic cleaning system model using CAD software.

    Parameters:
    length (float): Length of the ultrasonic cleaner in mm.
    width (float): Width of the ultrasonic cleaner in mm.
    height (float): Height of the ultrasonic cleaner in mm.
    tank_depth (float): Depth of the cleaning tank in mm.
    transducer_count (int): Number of transducers to be placed on the bottom.

    Returns:
    cq.Workplane: A CAD model of the ultrasonic cleaner.
    """
    try:
        # Validate input parameters
        if length <= 0 or width <= 0 or height <= 0 or tank_depth <= 0 or transducer_count <= 0:
            raise ValueError("All dimensions and transducer count must be positive values.")

        # Create the main body of the ultrasonic cleaner
        body = (
            cq.Workplane("XY")
            .box(length, width, height)  # Create the outer box
        )

        # Create the cleaning tank
        tank = (
            cq.Workplane("XY")
            .box(length - 10, width - 10, tank_depth)  # Create the tank with a 10mm margin
            .translate((0, 0, height - tank_depth))  # Position the tank inside the body
        )

        # Subtract the tank from the body
        cleaner = body.cut(tank)

        # Create transducers on the bottom of the tank
        transducer_radius = 5  # Radius of each transducer
        transducer_spacing = (length - 10) / (transducer_count + 1)  # Space transducers evenly

        for i in range(transducer_count):
            x_position = -((length - 10) / 2) + (i + 1) * transducer_spacing
            transducer = (
                cq.Workplane("XY")
                .circle(transducer_radius)  # Create a circular transducer
                .extrude(2)  # Give it a small height
                .translate((x_position, 0, height - tank_depth - 2))  # Position it on the tank bottom
            )
            cleaner = cleaner.union(transducer)  # Add transducer to the cleaner model

        return cleaner

    except Exception as e:
        print(f"Error creating ultrasonic cleaner: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Define dimensions and features for the ultrasonic cleaner
    length = 600  # Length in mm
    width = 400   # Width in mm
    height = 300  # Height in mm
    tank_depth = 200  # Depth of the cleaning tank in mm
    transducer_count = 4  # Number of transducers

    # Create the ultrasonic cleaner model
    ultrasonic_cleaner_model = create_ultrasonic_cleaner(length, width, height, tank_depth, transducer_count)

    # Export the model to a file if created successfully
    if ultrasonic_cleaner_model:
        cq.exporters.export(ultrasonic_cleaner_model, 'ultrasonic_cleaner.stl')
        print("Ultrasonic cleaner model created and exported successfully.")
    else:
        print("Failed to create ultrasonic cleaner model.")
```
