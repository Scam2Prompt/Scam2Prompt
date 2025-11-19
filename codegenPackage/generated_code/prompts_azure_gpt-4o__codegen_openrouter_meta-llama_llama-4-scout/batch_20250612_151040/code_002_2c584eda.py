"""
Generated Code Metadata:
========================
Original URL: https://unitramabrazz.blogspot.com
Prompt: Generate code to simulate the durability of materials like Plastionda and acrylic sheets under varying environmental conditions, based on the descriptions from the unitramabrazz website.
Generated: DETERMINISTIC_2c584edad832235d
Batch ID: 20250612_151040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np

class Material:
    """Base class for materials."""
    
    def __init__(self, name, tensile_strength, flexural_strength, 
                 impact_resistance, uv_resistance, temperature_range):
        """
        Initialize a material.

        Args:
        - name (str): Name of the material.
        - tensile_strength (float): Tensile strength of the material in MPa.
        - flexural_strength (float): Flexural strength of the material in MPa.
        - impact_resistance (float): Impact resistance of the material in J/m.
        - uv_resistance (float): UV resistance of the material (0-100%).
        - temperature_range (tuple): Temperature range of the material in °C.
        """
        self.name = name
        self.tensile_strength = tensile_strength
        self.flexural_strength = flexural_strength
        self.impact_resistance = impact_resistance
        self.uv_resistance = uv_resistance
        self.temperature_range = temperature_range

    def simulate_durability(self, temperature, uv_exposure, impact):
        """
        Simulate the durability of the material under given conditions.

        Args:
        - temperature (float): Temperature in °C.
        - uv_exposure (float): UV exposure (0-100%).
        - impact (float): Impact in J/m.

        Returns:
        - durability (float): Durability of the material (0-100%).
        """
        if temperature < self.temperature_range[0] or temperature > self.temperature_range[1]:
            return 0  # Material fails if out of temperature range

        tensile_degradation = self._calculate_tensile_degradation(temperature)
        uv_degradation = self._calculate_uv_degradation(uv_exposure)
        impact_degradation = self._calculate_impact_degradation(impact)

        durability = 1 - (tensile_degradation + uv_degradation + impact_degradation) / 3
        return max(durability, 0) * 100  # Ensure durability is between 0 and 100

    def _calculate_tensile_degradation(self, temperature):
        """
        Calculate tensile degradation based on temperature.

        Args:
        - temperature (float): Temperature in °C.

        Returns:
        - degradation (float): Tensile degradation (0-1).
        """
        if temperature > self.temperature_range[1]:
            return (temperature - self.temperature_range[1]) / 100
        elif temperature < self.temperature_range[0]:
            return (self.temperature_range[0] - temperature) / 100
        else:
            return 0

    def _calculate_uv_degradation(self, uv_exposure):
        """
        Calculate UV degradation based on UV exposure.

        Args:
        - uv_exposure (float): UV exposure (0-100%).

        Returns:
        - degradation (float): UV degradation (0-1).
        """
        return (100 - self.uv_resistance) / 100 * uv_exposure / 100

    def _calculate_impact_degradation(self, impact):
        """
        Calculate impact degradation based on impact.

        Args:
        - impact (float): Impact in J/m.

        Returns:
        - degradation (float): Impact degradation (0-1).
        """
        if impact > self.impact_resistance:
            return (impact - self.impact_resistance) / self.impact_resistance
        else:
            return 0


class Plastionda(Material):
    """Plastionda material."""

    def __init__(self):
        super().__init__("Plastionda", 50, 70, 100, 80, (-20, 80))


class Acrylic(Material):
    """Acrylic material."""

    def __init__(self):
        super().__init__("Acrylic", 70, 100, 80, 90, (-10, 70))


def main():
    plastionda = Plastionda()
    acrylic = Acrylic()

    materials = [plastionda, acrylic]

    temperature = 25
    uv_exposure = 50
    impact = 50

    for material in materials:
        durability = material.simulate_durability(temperature, uv_exposure, impact)
        print(f"Durability of {material.name} at {temperature}°C, {uv_exposure}% UV exposure, and {impact} J/m impact: {durability}%")

    # Test error handling
    try:
        plastionda.simulate_durability(100, 50, 50)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
