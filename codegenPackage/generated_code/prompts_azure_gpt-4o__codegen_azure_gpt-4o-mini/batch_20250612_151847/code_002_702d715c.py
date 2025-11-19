"""
Generated Code Metadata:
========================
Original URL: https://metalfabpro.com
Prompt: Create a script to calculate the durability of drive flanges with steel inserts and reinforced bolt holes, as described on Metal Fab Pro Race Shop's website.
Generated: DETERMINISTIC_702d715cac4de331
Batch ID: 20250612_151847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class DriveFlange:
    """
    A class to represent a drive flange with steel inserts and reinforced bolt holes.
    """

    def __init__(self, diameter: float, thickness: float, bolt_hole_diameter: float, 
                 number_of_bolt_holes: int, material_strength: float):
        """
        Initializes the DriveFlange with the given parameters.

        :param diameter: Diameter of the flange in inches.
        :param thickness: Thickness of the flange in inches.
        :param bolt_hole_diameter: Diameter of the bolt holes in inches.
        :param number_of_bolt_holes: Number of bolt holes in the flange.
        :param material_strength: Material strength in psi (pounds per square inch).
        """
        self.diameter = diameter
        self.thickness = thickness
        self.bolt_hole_diameter = bolt_hole_diameter
        self.number_of_bolt_holes = number_of_bolt_holes
        self.material_strength = material_strength

    def calculate_area(self) -> float:
        """
        Calculates the effective area of the flange.

        :return: Effective area of the flange in square inches.
        """
        # Area of the flange (circular area)
        flange_area = math.pi * (self.diameter / 2) ** 2
        # Area of the bolt holes (subtracting the area of the holes)
        bolt_hole_area = self.number_of_bolt_holes * (math.pi * (self.bolt_hole_diameter / 2) ** 2)
        effective_area = flange_area - bolt_hole_area
        return effective_area

    def calculate_durability(self) -> float:
        """
        Calculates the durability of the drive flange based on material strength and effective area.

        :return: Durability of the flange in pounds.
        """
        effective_area = self.calculate_area()
        durability = effective_area * self.material_strength
        return durability

    def display_durability(self):
        """
        Displays the calculated durability of the drive flange.
        """
        try:
            durability = self.calculate_durability()
            print(f"The durability of the drive flange is: {durability:.2f} pounds.")
        except Exception as e:
            print(f"An error occurred while calculating durability: {e}")

if __name__ == "__main__":
    # Example parameters for the drive flange
    diameter = 12.0  # inches
    thickness = 0.5  # inches
    bolt_hole_diameter = 0.5  # inches
    number_of_bolt_holes = 6
    material_strength = 60000  # psi for steel

    # Create a DriveFlange instance
    drive_flange = DriveFlange(diameter, thickness, bolt_hole_diameter, number_of_bolt_holes, material_strength)

    # Display the durability of the drive flange
    drive_flange.display_durability()
```
