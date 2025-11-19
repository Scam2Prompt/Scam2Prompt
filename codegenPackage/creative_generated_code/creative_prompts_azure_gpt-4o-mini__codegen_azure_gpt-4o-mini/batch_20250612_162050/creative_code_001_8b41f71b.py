"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://histeknik.com
Prompt: Write a Python script that calculates the load capacity of screw piles based on their dimensions (60mm to 114mm diameter) and thickness (2mm to 6mm) as described by His Teknik Çelik.
Generated: DETERMINISTIC_8b41f71b2b27314f
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class ScrewPile:
    """
    A class to represent a screw pile and calculate its load capacity based on its dimensions.
    """

    def __init__(self, diameter: float, thickness: float):
        """
        Initialize a ScrewPile instance.

        :param diameter: Diameter of the screw pile in mm (must be between 60mm and 114mm).
        :param thickness: Thickness of the screw pile in mm (must be between 2mm and 6mm).
        """
        if not (60 <= diameter <= 114):
            raise ValueError("Diameter must be between 60mm and 114mm.")
        if not (2 <= thickness <= 6):
            raise ValueError("Thickness must be between 2mm and 6mm.")

        self.diameter = diameter
        self.thickness = thickness

    def calculate_area(self) -> float:
        """
        Calculate the cross-sectional area of the screw pile.

        :return: Cross-sectional area in square mm.
        """
        radius = self.diameter / 2
        area = math.pi * (radius ** 2) - math.pi * ((radius - self.thickness) ** 2)
        return area

    def calculate_load_capacity(self) -> float:
        """
        Calculate the load capacity of the screw pile.

        This is a simplified formula for demonstration purposes. Adjust according to actual engineering standards.

        :return: Load capacity in Newtons (N).
        """
        # Example load capacity calculation based on area and a constant load factor
        load_factor = 50  # Example load factor for demonstration, in N/mm²
        area = self.calculate_area()
        load_capacity = area * load_factor
        return load_capacity

def main():
    """
    Main function to run the screw pile load capacity calculation.
    """
    try:
        diameter = float(input("Enter the diameter of the screw pile (60mm - 114mm): "))
        thickness = float(input("Enter the thickness of the screw pile (2mm - 6mm): "))
        
        screw_pile = ScrewPile(diameter, thickness)
        load_capacity = screw_pile.calculate_load_capacity()
        
        print(f"The load capacity of the screw pile is: {load_capacity:.2f} N")

    except ValueError as e:
        print(f"Input error: {e}")

if __name__ == "__main__":
    main()
```
