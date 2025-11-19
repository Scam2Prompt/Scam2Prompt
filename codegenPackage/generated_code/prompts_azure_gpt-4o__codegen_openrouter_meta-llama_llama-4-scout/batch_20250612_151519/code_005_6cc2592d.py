"""
Generated Code Metadata:
========================
Original URL: https://socompressoresebombas.com.br
Prompt: Create code to model the thermal resistance of PVC Antichama tubes used in fire prevention systems, considering material properties.
Generated: DETERMINISTIC_6cc2592d34d5e612
Batch ID: 20250612_151519
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np

class MaterialProperties:
    """Material properties of PVC Antichama tubes"""
    def __init__(self, thermal_conductivity, specific_heat_capacity, density):
        """
        Initialize material properties.

        Args:
            thermal_conductivity (float): Thermal conductivity of the material in W/mK.
            specific_heat_capacity (float): Specific heat capacity of the material in J/kgK.
            density (float): Density of the material in kg/m^3.
        """
        self.thermal_conductivity = thermal_conductivity
        self.specific_heat_capacity = specific_heat_capacity
        self.density = density

class PVCAntichamaTube:
    """Model for PVC Antichama tubes used in fire prevention systems"""
    def __init__(self, outer_radius, inner_radius, material_properties):
        """
        Initialize PVC Antichama tube properties.

        Args:
            outer_radius (float): Outer radius of the tube in meters.
            inner_radius (float): Inner radius of the tube in meters.
            material_properties (MaterialProperties): Material properties of the tube.
        """
        self.outer_radius = outer_radius
        self.inner_radius = inner_radius
        self.material_properties = material_properties

    def calculate_thermal_resistance(self):
        """
        Calculate thermal resistance of the tube.

        Returns:
            float: Thermal resistance of the tube in K/W.
        """
        try:
            if self.outer_radius <= self.inner_radius:
                raise ValueError("Outer radius must be greater than inner radius")

            if self.material_properties.thermal_conductivity <= 0:
                raise ValueError("Thermal conductivity must be greater than zero")

            thermal_resistance = (np.log(self.outer_radius / self.inner_radius)) / (2 * np.pi * self.material_properties.thermal_conductivity)
            return thermal_resistance

        except ValueError as e:
            print(f"Error: {e}")
            return None

    def calculate_heat_transfer(self, temperature_difference):
        """
        Calculate heat transfer through the tube.

        Args:
            temperature_difference (float): Temperature difference across the tube in Kelvin.

        Returns:
            float: Heat transfer through the tube in Watts.
        """
        thermal_resistance = self.calculate_thermal_resistance()
        if thermal_resistance is not None:
            heat_transfer = temperature_difference / thermal_resistance
            return heat_transfer
        else:
            return None


def main():
    # Example usage
    material_properties = MaterialProperties(
        thermal_conductivity=0.16,  # W/mK
        specific_heat_capacity=1000,  # J/kgK
        density=1400  # kg/m^3
    )

    tube = PVCAntichamaTube(
        outer_radius=0.02,  # meters
        inner_radius=0.015,  # meters
        material_properties=material_properties
    )

    thermal_resistance = tube.calculate_thermal_resistance()
    print(f"Thermal Resistance: {thermal_resistance} K/W")

    heat_transfer = tube.calculate_heat_transfer(temperature_difference=50)  # 50K temperature difference
    print(f"Heat Transfer: {heat_transfer} Watts")


if __name__ == "__main__":
    main()
```
