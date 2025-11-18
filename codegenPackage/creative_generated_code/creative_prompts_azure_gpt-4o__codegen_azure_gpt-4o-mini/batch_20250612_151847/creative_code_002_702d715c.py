"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metalfabpro.com
Prompt: Create a script to calculate the durability of drive flanges with steel inserts and reinforced bolt holes, as described on Metal Fab Pro Race Shop's website.
Generated: DETERMINISTIC_702d715cac4de331
Batch ID: 20250612_151847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class DriveFlange:
    """
    A class to represent a drive flange with steel inserts and reinforced bolt holes.
    """

    def __init__(self, diameter: float, thickness: float, insert_strength: float, bolt_hole_strength: float):
        """
        Initializes the DriveFlange with given parameters.
        
        :param diameter: Diameter of the drive flange in inches.
        :param thickness: Thickness of the flange in inches.
        :param insert_strength: Strength of the steel insert in psi.
        :param bolt_hole_strength: Strength of the reinforced bolt holes in psi.
        """
        self.diameter = diameter
        self.thickness = thickness
        self.insert_strength = insert_strength
        self.bolt_hole_strength = bolt_hole_strength

    def calculate_area(self) -> float:
        """
        Calculates the effective area of the flange.
        
        :return: Effective area in square inches.
        """
        radius = self.diameter / 2
        area = math.pi * (radius ** 2) - math.pi * ((radius - self.thickness) ** 2)
        return area

    def calculate_durability(self) -> float:
        """
        Calculates the durability of the drive flange based on insert and bolt hole strengths.
        
        :return: Durability in psi.
        """
        try:
            area = self.calculate_area()
            durability = min(self.insert_strength, self.bolt_hole_strength) * area
            return durability
        except Exception as e:
            print(f"Error calculating durability: {e}")
            return 0.0

def main():
    """
    Main function to execute the durability calculation.
    """
    # Example parameters
    diameter = 10.0  # in inches
    thickness = 0.5  # in inches
    insert_strength = 60000.0  # in psi
    bolt_hole_strength = 50000.0  # in psi

    # Create an instance of DriveFlange
    drive_flange = DriveFlange(diameter, thickness, insert_strength, bolt_hole_strength)

    # Calculate and print the durability
    durability = drive_flange.calculate_durability()
    print(f"The durability of the drive flange is: {durability:.2f} psi")

if __name__ == "__main__":
    main()
```
