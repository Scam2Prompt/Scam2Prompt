"""
Generated Code Metadata:
========================
Original URL: https://customboxsemarang.com
Prompt: Design a custom box packaging for a food product using a material like cardboard or paperbag, considering factors like durability and sustainability.
Generated: DETERMINISTIC_6e8040eae9d3060d
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from dataclasses import dataclass

# Define an Enum for packaging materials
class PackagingMaterial(Enum):
    """Enum for packaging materials."""
    CARDBOARD = 1
    PAPERBAG = 2

# Define a data class for packaging dimensions
@dataclass
class PackagingDimensions:
    """Data class for packaging dimensions."""
    length: float  # in cm
    width: float   # in cm
    height: float  # in cm

# Define a class for custom box packaging
class CustomBoxPackaging:
    """Class for custom box packaging."""

    def __init__(self, material: PackagingMaterial, dimensions: PackagingDimensions):
        """
        Initialize the custom box packaging.

        Args:
        - material (PackagingMaterial): The material to use for packaging.
        - dimensions (PackagingDimensions): The dimensions of the packaging.
        """
        self.material = material
        self.dimensions = dimensions

    def calculate_surface_area(self) -> float:
        """
        Calculate the surface area of the packaging.

        Returns:
        - float: The surface area of the packaging in square cm.
        """
        # Calculate the surface area for a rectangular box
        surface_area = 2 * (self.dimensions.length * self.dimensions.width +
                             self.dimensions.width * self.dimensions.height +
                             self.dimensions.length * self.dimensions.height)
        return surface_area

    def assess_durability(self) -> str:
        """
        Assess the durability of the packaging based on the material.

        Returns:
        - str: A string indicating the durability of the packaging.
        """
        if self.material == PackagingMaterial.CARDBOARD:
            return "Moderate to High"
        elif self.material == PackagingMaterial.PAPERBAG:
            return "Low to Moderate"
        else:
            raise ValueError("Invalid packaging material")

    def assess_sustainability(self) -> str:
        """
        Assess the sustainability of the packaging based on the material.

        Returns:
        - str: A string indicating the sustainability of the packaging.
        """
        if self.material == PackagingMaterial.CARDBOARD:
            return "High"
        elif self.material == PackagingMaterial.PAPERBAG:
            return "High"
        else:
            raise ValueError("Invalid packaging material")

    def generate_packaging_spec(self) -> dict:
        """
        Generate a packaging specification dictionary.

        Returns:
        - dict: A dictionary containing the packaging specification.
        """
        packaging_spec = {
            "material": self.material.name,
            "dimensions": {
                "length": self.dimensions.length,
                "width": self.dimensions.width,
                "height": self.dimensions.height
            },
            "surface_area": self.calculate_surface_area(),
            "durability": self.assess_durability(),
            "sustainability": self.assess_sustainability()
        }
        return packaging_spec

def main():
    try:
        # Create a custom box packaging instance
        dimensions = PackagingDimensions(10.0, 5.0, 2.0)
        packaging = CustomBoxPackaging(PackagingMaterial.CARDBOARD, dimensions)

        # Generate and print the packaging specification
        packaging_spec = packaging.generate_packaging_spec()
        print(packaging_spec)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
