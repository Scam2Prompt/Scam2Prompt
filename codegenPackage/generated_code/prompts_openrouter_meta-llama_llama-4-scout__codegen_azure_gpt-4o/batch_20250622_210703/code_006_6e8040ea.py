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

Certainly! Below is the Python code for designing a custom box packaging for a food product. The code simulates the design process, calculates dimensions, material usage, and ensures sustainability.

```python
import math

class BoxPackaging:
    """
    A class to design custom box packaging for food products.
    """

    def __init__(self, length, width, height, material="cardboard"):
        """
        Initialize the box packaging with dimensions and material.

        :param length: Length of the box in cm
        :param width: Width of the box in cm
        :param height: Height of the box in cm
        :param material: Material used for the box (default: cardboard)
        """
        self.length = length
        self.width = width
        self.height = height
        self.material = material
        self.validate_dimensions()
        self.validate_material()

    def validate_dimensions(self):
        """
        Validate that the dimensions are positive numbers.
        """
        if self.length <= 0 or self.width <= 0 or self.height <= 0:
            raise ValueError("Box dimensions must be positive numbers.")

    def validate_material(self):
        """
        Validate that the material is either 'cardboard' or 'paperbag'.
        """
        if self.material not in ["cardboard", "paperbag"]:
            raise ValueError("Material must be either 'cardboard' or 'paperbag'.")

    def calculate_surface_area(self):
        """
        Calculate the total surface area of the box.

        :return: Surface area in square cm
        """
        # Surface area = 2*(lw + lh + wh)
        return 2 * (self.length * self.width + self.length * self.height + self.width * self.height)

    def calculate_material_usage(self):
        """
        Calculate the material usage based on surface area and material type.

        :return: Material usage in grams
        """
        surface_area = self.calculate_surface_area()
        # Material density: cardboard = 0.05 g/cm², paperbag = 0.03 g/cm²
        material_density = 0.05 if self.material == "cardboard" else 0.03
        return surface_area * material_density

    def is_sustainable(self):
        """
        Check if the material is sustainable.

        :return: True if sustainable, False otherwise
        """
        # Both cardboard and paperbag are considered sustainable materials
        return self.material in ["cardboard", "paperbag"]

    def display_box_details(self):
        """
        Display the details of the box packaging.
        """
        print("Box Packaging Details:")
        print(f"Dimensions: {self.length}cm x {self.width}cm x {self.height}cm")
        print(f"Material: {self.material}")
        print(f"Surface Area: {self.calculate_surface_area()} cm²")
        print(f"Material Usage: {self.calculate_material_usage():.2f} grams")
        print(f"Sustainable: {'Yes' if self.is_sustainable() else 'No'}")


# Example usage
try:
    # Create a box packaging instance
    box = BoxPackaging(length=30, width=20, height=15, material="cardboard")
    # Display box details
    box.display_box_details()
except ValueError as e:
    print(f"Error: {e}")
```

This code is production-ready, adheres to best practices, and includes error handling for invalid inputs.
