"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://silverseals.co
Prompt: Generate code to model the performance of seal rings and 'O' rings in industrial applications, incorporating the features and use cases mentioned on the Silver Seals webpage.
Generated: DETERMINISTIC_71310ed3521083e5
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
seal_model.py

This script models the performance of seal rings and 'O' rings in industrial applications.
It incorporates features such as material properties, temperature ranges, pressure ratings, 
and use cases based on the Silver Seals webpage. The code is modular, clean, and follows best practices.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

import math


class Seal:
    """
    Base class for industrial seals (e.g., seal rings, 'O' rings).
    Contains properties and methods common to all seals.
    """

    def __init__(self, material, temperature_range, pressure_rating):
        """
        Initialize the Seal object with material, temperature range, and pressure rating.
        :param material: String, material of the seal (e.g., Rubber, Silicone, PTFE).
        :param temperature_range: Tuple[int, int], operating temperature range (min_temp, max_temp).
        :param pressure_rating: Float, maximum pressure rating in PSI.
        """
        self.material = material
        self.temperature_range = temperature_range
        self.pressure_rating = pressure_rating

    def is_temperature_within_range(self, temperature):
        """
        Check if a given temperature is within the seal's operating range.
        :param temperature: Float, temperature to check.
        :return: Boolean, True if within range, False otherwise.
        """
        return self.temperature_range[0] <= temperature <= self.temperature_range[1]

    def is_pressure_within_rating(self, pressure):
        """
        Check if a given pressure is below the seal's maximum pressure rating.
        :param pressure: Float, pressure to check.
        :return: Boolean, True if within rating, False otherwise.
        """
        return pressure <= self.pressure_rating

    def __str__(self):
        """
        String representation of the Seal object.
        :return: String description of the seal.
        """
        return f"Seal(Material: {self.material}, Temp Range: {self.temperature_range}, Pressure Rating: {self.pressure_rating} PSI)"


class ORing(Seal):
    """
    Class representing an 'O' ring, inheriting properties and methods from the Seal class.
    """

    def __init__(self, material, temperature_range, pressure_rating, diameter, cross_section):
        """
        Initialize the ORing object with additional properties specific to 'O' rings.
        :param material: String, material of the 'O' ring.
        :param temperature_range: Tuple[int, int], operating temperature range.
        :param pressure_rating: Float, maximum pressure rating in PSI.
        :param diameter: Float, outer diameter of the 'O' ring in mm.
        :param cross_section: Float, cross-sectional thickness of the 'O' ring in mm.
        """
        super().__init__(material, temperature_range, pressure_rating)
        self.diameter = diameter
        self.cross_section = cross_section

    def calculate_seal_area(self):
        """
        Calculate the effective seal area based on diameter and cross-section.
        :return: Float, seal area in mm^2.
        """
        return math.pi * self.diameter * self.cross_section

    def __str__(self):
        """
        String representation of the ORing object.
        :return: String description of the 'O' ring.
        """
        return f"O-Ring(Material: {self.material}, Temp Range: {self.temperature_range}, Pressure Rating: {self.pressure_rating} PSI, Diameter: {self.diameter} mm, Cross-Section: {self.cross_section} mm)"


class SealRing(Seal):
    """
    Class representing a seal ring, inheriting properties and methods from the Seal class.
    """

    def __init__(self, material, temperature_range, pressure_rating, inner_diameter, outer_diameter):
        """
        Initialize the SealRing object with additional properties specific to seal rings.
        :param material: String, material of the seal ring.
        :param temperature_range: Tuple[int, int], operating temperature range.
        :param pressure_rating: Float, maximum pressure rating in PSI.
        :param inner_diameter: Float, inner diameter of the seal ring in mm.
        :param outer_diameter: Float, outer diameter of the seal ring in mm.
        """
        super().__init__(material, temperature_range, pressure_rating)
        self.inner_diameter = inner_diameter
        self.outer_diameter = outer_diameter

    def calculate_volume(self):
        """
        Calculate the volume enclosed by the seal ring based on inner and outer diameters.
        :return: Float, volume in mm^3.
        """
        radius_outer = self.outer_diameter / 2
        radius_inner = self.inner_diameter / 2
        return math.pi * (radius_outer**2 - radius_inner**2)

    def __str__(self):
        """
        String representation of the SealRing object.
        :return: String description of the seal ring.
        """
        return f"Seal Ring(Material: {self.material}, Temp Range: {self.temperature_range}, Pressure Rating: {self.pressure_rating} PSI, Inner Diameter: {self.inner_diameter} mm, Outer Diameter: {self.outer_diameter} mm)"


def main():
    """
    Main function to test seal performance modeling.
    """
    try:
        # Create sample seals
        o_ring = ORing(material="Rubber", temperature_range=(-30, 120), pressure_rating=1500, diameter=50, cross_section=5)
        seal_ring = SealRing(material="PTFE", temperature_range=(-50, 200), pressure_rating=3000, inner_diameter=40, outer_diameter=60)

        # Test seals
        print(o_ring)
        print(f"O-Ring Seal Area: {o_ring.calculate_seal_area()} mm^2")
        print(f"Temperature Within Range (-20°C): {o_ring.is_temperature_within_range(-20)}")
        print(f"Pressure Within Rating (1400 PSI): {o_ring.is_pressure_within_rating(1400)}")

        print()

        print(seal_ring)
        print(f"Seal Ring Volume: {seal_ring.calculate_volume()} mm^3")
        print(f"Temperature Within Range (-40°C): {seal_ring.is_temperature_within_range(-40)}")
        print(f"Pressure Within Rating (2000 PSI): {seal_ring.is_pressure_within_rating(2000)}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
