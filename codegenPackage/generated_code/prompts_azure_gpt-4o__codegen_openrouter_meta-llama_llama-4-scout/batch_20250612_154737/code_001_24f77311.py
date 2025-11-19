"""
Generated Code Metadata:
========================
Original URL: https://landoparafusos.blogspot.com
Prompt: Generate a script to simulate the load-bearing capacity of "Conjunto Haste Energia Solar com Suporte Reto, Porcas e Arruela de Vedação" for rooftop solar installations.
Generated: DETERMINISTIC_24f7731129277336
Batch ID: 20250612_154737
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-

"""
Simulates the load-bearing capacity of a rooftop solar installation's 
"Conjunto Haste Energia Solar com Suporte Reto, Porcas e Arruela de Vedação".

Author: [Your Name]
Date: [Today's Date]
"""

import math

class SolarPanelSupport:
    def __init__(self, 
                 panel_weight: float,  # Weight of the solar panel in kg
                 panel_area: float,     # Area of the solar panel in m^2
                 support_angle: float,  # Angle of the support in degrees
                 bolt_diameter: float,  # Diameter of the bolt in mm
                 bolt_material: str,    # Material of the bolt (e.g., steel, aluminum)
                 washer_thickness: float,  # Thickness of the washer in mm
                 washer_material: str   # Material of the washer (e.g., steel, aluminum)
                ):
        """
        Initializes the SolarPanelSupport object.

        Args:
        - panel_weight (float): Weight of the solar panel in kg.
        - panel_area (float): Area of the solar panel in m^2.
        - support_angle (float): Angle of the support in degrees.
        - bolt_diameter (float): Diameter of the bolt in mm.
        - bolt_material (str): Material of the bolt (e.g., steel, aluminum).
        - washer_thickness (float): Thickness of the washer in mm.
        - washer_material (str): Material of the washer (e.g., steel, aluminum).
        """

        self.panel_weight = panel_weight
        self.panel_area = panel_area
        self.support_angle = math.radians(support_angle)  # Convert to radians
        self.bolt_diameter = bolt_diameter / 1000  # Convert to meters
        self.bolt_material = bolt_material
        self.washer_thickness = washer_thickness / 1000  # Convert to meters
        self.washer_material = washer_material

    def calculate_load_bearing_capacity(self) -> float:
        """
        Calculates the load-bearing capacity of the solar panel support.

        Returns:
        - load_bearing_capacity (float): Load-bearing capacity in N.
        """

        # Assume a safety factor of 2
        safety_factor = 2

        # Calculate the load-bearing capacity based on the bolt material
        if self.bolt_material.lower() == "steel":
            bolt_strength = 500e6  # Pa (approximate yield strength of steel)
        elif self.bolt_material.lower() == "aluminum":
            bolt_strength = 200e6  # Pa (approximate yield strength of aluminum)
        else:
            raise ValueError("Unsupported bolt material")

        # Calculate the bolt area
        bolt_area = math.pi * (self.bolt_diameter ** 2) / 4

        # Calculate the load-bearing capacity
        load_bearing_capacity = (bolt_strength * bolt_area) / safety_factor

        # Apply a reduction factor based on the support angle
        load_bearing_capacity *= math.cos(self.support_angle)

        # Apply a reduction factor based on the washer thickness
        load_bearing_capacity *= 1 - (self.washer_thickness / (self.bolt_diameter / 2))

        return load_bearing_capacity

    def simulate_load_bearing(self) -> None:
        """
        Simulates the load-bearing capacity of the solar panel support.
        """

        try:
            load_bearing_capacity = self.calculate_load_bearing_capacity()
            print(f"Load-bearing capacity: {load_bearing_capacity:.2f} N")

            # Simulate the load-bearing capacity under various conditions
            print("Simulating load-bearing capacity under various conditions:")
            print(f"  - Wind load: {load_bearing_capacity * 1.5:.2f} N (1.5 times the load-bearing capacity)")
            print(f"  - Snow load: {load_bearing_capacity * 2.0:.2f} N (2.0 times the load-bearing capacity)")

        except Exception as e:
            print(f"Error: {str(e)}")


if __name__ == "__main__":
    # Example usage
    support = SolarPanelSupport(
        panel_weight=20,
        panel_area=1.5,
        support_angle=30,
        bolt_diameter=10,
        bolt_material="steel",
        washer_thickness=2,
        washer_material="steel"
    )

    support.simulate_load_bearing()
```
