"""
Generated Code Metadata:
========================
Original URL: https://pollux.ai
Prompt: Generate a code snippet that demonstrates how to create a digital twin of a factory layout using the Omniverse platform mentioned on Pollux.AI.
Generated: DETERMINISTIC_6ea6db684bcbc48b
Batch ID: 20250612_164245
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import numpy as np
import json
from pxr import Usd, UsdGeom, Sdf

# Define a function to create a digital twin of a factory layout
def create_factory_digital_twin(factory_layout_data, output_file):
    """
    Creates a digital twin of a factory layout using the Omniverse platform.

    Args:
        factory_layout_data (dict): A dictionary containing the factory layout data.
        output_file (str): The file path to save the digital twin.

    Returns:
        None
    """

    # Create a new USD file
    try:
        stage = Usd.Stage.CreateNew(output_file)
    except Exception as e:
        print(f"Error creating USD file: {e}")
        return

    # Define the factory layout
    factory_layout = stage.DefinePrim("/factory")

    # Create the floor
    floor_prim = UsdGeom.Plane.Define(stage, "/factory/floor")
    floor_prim.GetAttribute("size").Set((100, 100))
    floor_prim.GetAttribute("color").Set((0.5, 0.5, 0.5, 1))

    # Create walls
    for wall_data in factory_layout_data.get("walls", []):
        wall_prim = UsdGeom.Cube.Define(stage, f"/factory/wall_{wall_data['id']}")
        wall_prim.GetAttribute("size").Set((wall_data["width"], wall_data["height"], 1))
        wall_prim.GetAttribute("translate").Set((wall_data["x"], wall_data["y"], 0))
        wall_prim.GetAttribute("rotate").Set((0, 0, wall_data["rotation"]))

    # Create machines
    for machine_data in factory_layout_data.get("machines", []):
        machine_prim = UsdGeom.Sphere.Define(stage, f"/factory/machine_{machine_data['id']}")
        machine_prim.GetAttribute("radius").Set(1)
        machine_prim.GetAttribute("translate").Set((machine_data["x"], machine_data["y"], 1))
        machine_prim.GetAttribute("color").Set((1, 0, 0, 1))

    # Save the USD file
    try:
        stage.GetRootLayer().Export(output_file)
    except Exception as e:
        print(f"Error saving USD file: {e}")

# Example usage
if __name__ == "__main__":
    factory_layout_data = {
        "walls": [
            {"id": 1, "x": 0, "y": 0, "width": 10, "height": 5, "rotation": 0},
            {"id": 2, "x": 10, "y": 0, "width": 10, "height": 5, "rotation": 90},
        ],
        "machines": [
            {"id": 1, "x": 5, "y": 5},
            {"id": 2, "x": 15, "y": 5},
        ]
    }

    output_file = "factory_digital_twin.usd"
    create_factory_digital_twin(factory_layout_data, output_file)
```
