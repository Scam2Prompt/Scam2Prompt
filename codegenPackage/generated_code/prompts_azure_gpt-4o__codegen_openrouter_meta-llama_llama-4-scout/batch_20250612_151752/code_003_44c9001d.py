"""
Generated Code Metadata:
========================
Original URL: https://foundation.ru
Prompt: Provide a Python script for developing geotechnical models to assess the stability of foundations and structures, incorporating the principles of soil mechanics discussed on the Научно-образовательный центр «Геотехника» website.
Generated: DETERMINISTIC_44c9001d0b830009
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# geotechnical_model.py

import math

class Soil:
    """Represents a soil layer with its properties."""

    def __init__(self, name, cohesion, friction_angle, unit_weight, poisson_ratio):
        """
        Initializes a Soil object.

        Args:
            name (str): Name of the soil layer.
            cohesion (float): Cohesion of the soil (kPa).
            friction_angle (float): Friction angle of the soil (degrees).
            unit_weight (float): Unit weight of the soil (kN/m^3).
            poisson_ratio (float): Poisson's ratio of the soil.
        """
        self.name = name
        self.cohesion = cohesion
        self.friction_angle = math.radians(friction_angle)  # Convert to radians
        self.unit_weight = unit_weight
        self.poisson_ratio = poisson_ratio

    def calculate_shear_strength(self, normal_stress):
        """
        Calculates the shear strength of the soil.

        Args:
            normal_stress (float): Normal stress on the soil (kPa).

        Returns:
            float: Shear strength of the soil (kPa).
        """
        return self.cohesion + normal_stress * math.tan(self.friction_angle)


class Foundation:
    """Represents a foundation with its properties and methods."""

    def __init__(self, width, depth, soil):
        """
        Initializes a Foundation object.

        Args:
            width (float): Width of the foundation (m).
            depth (float): Depth of the foundation (m).
            soil (Soil): Soil object representing the soil layer.
        """
        self.width = width
        self.depth = depth
        self.soil = soil

    def calculate_bearing_capacity(self):
        """
        Calculates the bearing capacity of the foundation.

        Returns:
            float: Bearing capacity of the foundation (kPa).
        """
        # Using Terzaghi's bearing capacity equation for a strip footing
        q_u = (self.soil.cohesion * (2 + math.pi) + self.soil.unit_weight * self.depth * self.width * math.tan(self.soil.friction_angle)) / self.width
        return q_u

    def calculate_settlement(self, load):
        """
        Calculates the settlement of the foundation.

        Args:
            load (float): Load on the foundation (kN).

        Returns:
            float: Settlement of the foundation (m).
        """
        # Using a simple elastic settlement equation
        stress = load / (self.width * self.width)
        strain = stress / (self.soil.unit_weight * (1 - self.soil.poisson_ratio))
        settlement = strain * self.depth
        return settlement


def main():
    try:
        # Create a soil layer
        soil = Soil(
            name="Clay",
            cohesion=20,
            friction_angle=25,
            unit_weight=18,
            poisson_ratio=0.3
        )

        # Create a foundation
        foundation = Foundation(
            width=2,
            depth=3,
            soil=soil
        )

        # Calculate bearing capacity
        bearing_capacity = foundation.calculate_bearing_capacity()
        print(f"Bearing capacity: {bearing_capacity:.2f} kPa")

        # Calculate settlement
        load = 100  # kN
        settlement = foundation.calculate_settlement(load)
        print(f"Settlement under {load} kN load: {settlement:.2f} m")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
