"""
Generated Code Metadata:
========================
Original URL: https://unapatches.com
Prompt: Write a program to design shale shaker screens and pipe supports for oil field applications, incorporating the unique fabrication expertise of Jupiter Design & Manufacturing.
Generated: DETERMINISTIC_41cde0c987ed531b
Batch ID: 20250612_154412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict

class ShaleShakerScreen:
    """
    Class to represent a shale shaker screen design.
    """

    def __init__(self, width: float, length: float, mesh_size: int):
        """
        Initialize a shale shaker screen with specified dimensions and mesh size.

        :param width: Width of the screen in inches.
        :param length: Length of the screen in inches.
        :param mesh_size: Mesh size in microns.
        """
        self.width = width
        self.length = length
        self.mesh_size = mesh_size

    def calculate_area(self) -> float:
        """
        Calculate the area of the screen.

        :return: Area of the screen in square inches.
        """
        return self.width * self.length

    def to_dict(self) -> Dict:
        """
        Convert the screen design to a dictionary for JSON serialization.

        :return: Dictionary representation of the screen.
        """
        return {
            "width": self.width,
            "length": self.length,
            "mesh_size": self.mesh_size,
            "area": self.calculate_area()
        }


class PipeSupport:
    """
    Class to represent a pipe support design.
    """

    def __init__(self, pipe_diameter: float, height: float, material: str):
        """
        Initialize a pipe support with specified dimensions and material.

        :param pipe_diameter: Diameter of the pipe in inches.
        :param height: Height of the support in inches.
        :param material: Material of the support (e.g., steel, aluminum).
        """
        self.pipe_diameter = pipe_diameter
        self.height = height
        self.material = material

    def calculate_weight_capacity(self) -> float:
        """
        Estimate the weight capacity of the support based on material and dimensions.

        :return: Estimated weight capacity in pounds.
        """
        # Simplified weight capacity calculation
        material_strength = {
            "steel": 1000,
            "aluminum": 600
        }
        return material_strength.get(self.material.lower(), 500) * self.pipe_diameter * self.height

    def to_dict(self) -> Dict:
        """
        Convert the pipe support design to a dictionary for JSON serialization.

        :return: Dictionary representation of the pipe support.
        """
        return {
            "pipe_diameter": self.pipe_diameter,
            "height": self.height,
            "material": self.material,
            "weight_capacity": self.calculate_weight_capacity()
        }


def save_designs_to_file(designs: List[Dict], filename: str) -> None:
    """
    Save the designs to a JSON file.

    :param designs: List of design dictionaries to save.
    :param filename: Name of the file to save the designs to.
    """
    try:
        with open(filename, 'w') as file:
            json.dump(designs, file, indent=4)
    except IOError as e:
        print(f"Error saving designs to file: {e}")


def main():
    """
    Main function to create shale shaker screens and pipe supports, and save designs to a file.
    """
    # Create sample shale shaker screens
    screens = [
        ShaleShakerScreen(width=48, length=30, mesh_size=200),
        ShaleShakerScreen(width=60, length=40, mesh_size=150)
    ]

    # Create sample pipe supports
    supports = [
        PipeSupport(pipe_diameter=10, height=24, material='steel'),
        PipeSupport(pipe_diameter=8, height=18, material='aluminum')
    ]

    # Prepare designs for saving
    designs = {
        "shale_shaker_screens": [screen.to_dict() for screen in screens],
        "pipe_supports": [support.to_dict() for support in supports]
    }

    # Save designs to a JSON file
    save_designs_to_file(designs, 'designs.json')


if __name__ == "__main__":
    main()
```
