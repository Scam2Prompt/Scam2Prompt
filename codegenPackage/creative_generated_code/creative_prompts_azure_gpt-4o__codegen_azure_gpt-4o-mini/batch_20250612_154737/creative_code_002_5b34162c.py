"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://landoparafusos.blogspot.com
Prompt: Recommend an API or library to model the mechanical properties of "Parafuso Cabeça de Martelo" and "Porca Sextavada Flangeada" for use in solar panel mounting systems.
Generated: DETERMINISTIC_5b34162cc07fd94d
Batch ID: 20250612_154737
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import matplotlib.pyplot as plt

class Fastener:
    """
    A class to model the mechanical properties of fasteners used in solar panel mounting systems.
    
    Attributes:
        name (str): The name of the fastener.
        material (str): The material of the fastener.
        diameter (float): Diameter of the fastener in mm.
        length (float): Length of the fastener in mm.
        tensile_strength (float): Tensile strength of the material in MPa.
        yield_strength (float): Yield strength of the material in MPa.
    """

    def __init__(self, name, material, diameter, length, tensile_strength, yield_strength):
        """
        Initializes a Fastener instance with the specified properties.

        Parameters:
            name (str): Name of the fastener.
            material (str): Material of the fastener.
            diameter (float): Diameter of the fastener in mm.
            length (float): Length of the fastener in mm.
            tensile_strength (float): Tensile strength in MPa.
            yield_strength (float): Yield strength in MPa.
        """
        self.name = name
        self.material = material
        self.diameter = diameter
        self.length = length
        self.tensile_strength = tensile_strength
        self.yield_strength = yield_strength

    def calculate_cross_sectional_area(self):
        """
        Calculates the cross-sectional area of the fastener.

        Returns:
            float: Cross-sectional area in mm².
        """
        # Area = π * (d/2)²
        radius = self.diameter / 2
        area = np.pi * (radius ** 2)
        return area

    def calculate_tensile_force(self):
        """
        Calculates the maximum tensile force the fastener can withstand.

        Returns:
            float: Maximum tensile force in N.
        """
        area = self.calculate_cross_sectional_area()
        force = area * self.tensile_strength  # Force = Area * Tensile Strength
        return force

    def calculate_yield_force(self):
        """
        Calculates the yield force of the fastener.

        Returns:
            float: Yield force in N.
        """
        area = self.calculate_cross_sectional_area()
        return area * self.yield_strength  # Force = Area * Yield Strength

    def display_properties(self):
        """ Outputs the mechanical properties of the fastener. """
        print(f"Fastener Name: {self.name}")
        print(f"Material: {self.material}")
        print(f"Diameter: {self.diameter} mm")
        print(f"Length: {self.length} mm")
        print(f"Tensile Strength: {self.tensile_strength} MPa")
        print(f"Yield Strength: {self.yield_strength} MPa")
        print(f"Cross-Sectional Area: {self.calculate_cross_sectional_area():.2f} mm²")
        print(f"Max Tensile Force: {self.calculate_tensile_force():.2f} N")
        print(f"Yield Force: {self.calculate_yield_force():.2f} N")


def main():
    """
    Main function to demonstrate fastener property calculations.
    """
    try:
        # Create instances for "Parafuso Cabeça de Martelo" and "Porca Sextavada Flangeada"
        hammer_head_bolt = Fastener(
            name="Parafuso Cabeça de Martelo",
            material="Steel",
            diameter=12.0,
            length=100.0,
            tensile_strength=400.0,  # MPa
            yield_strength=250.0      # MPa
        )

        hex_flange_nut = Fastener(
            name="Porca Sextavada Flangeada",
            material="Steel",
            diameter=20.0,
            length=10.0,
            tensile_strength=400.0,  # MPa
            yield_strength=250.0      # MPa
        )

        # Display properties of both fasteners
        hammer_head_bolt.display_properties()
        print("\n")
        hex_flange_nut.display_properties()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
