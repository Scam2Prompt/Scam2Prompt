"""
Generated Code Metadata:
========================
Original URL: https://www.ablakvaros.hu
Prompt: Create a Python program to calculate the UV állóság (UV resistance) and durability of színes műanyag ablak (colored plastic windows) under different sunlight exposure conditions.
Generated: DETERMINISTIC_cf9e41496bbf6e6c
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Colored Plastic Window UV Resistance and Durability Calculator

Calculates the UV resistance and durability of colored plastic windows under different sunlight exposure conditions.
"""

import math

class ColoredPlasticWindow:
    def __init__(self, material, color, thickness):
        """
        Initializes a ColoredPlasticWindow object.

        Args:
            material (str): The material of the window (e.g., PVC, ABS).
            color (str): The color of the window.
            thickness (float): The thickness of the window in mm.
        """
        self.material = material
        self.color = color
        self.thickness = thickness

    def calculate_uv_resistance(self, sunlight_exposure):
        """
        Calculates the UV resistance of the window.

        Args:
            sunlight_exposure (float): The sunlight exposure in hours per day.

        Returns:
            float: The UV resistance of the window (higher is better).
        """
        # UV resistance formula based on material and color
        uv_resistance_formula = {
            'PVC': {'white': 0.8, 'gray': 0.7, 'brown': 0.6},
            'ABS': {'white': 0.7, 'gray': 0.6, 'brown': 0.5}
        }

        material_uv_resistance = uv_resistance_formula.get(self.material, {}).get(self.color, 0.5)
        uv_resistance = material_uv_resistance * math.exp(-0.01 * sunlight_exposure)
        return uv_resistance

    def calculate_durability(self, uv_resistance, years):
        """
        Calculates the durability of the window.

        Args:
            uv_resistance (float): The UV resistance of the window.
            years (int): The number of years the window is exposed.

        Returns:
            float: The durability of the window (higher is better).
        """
        # Durability formula based on UV resistance and years
        durability = uv_resistance ** years * self.thickness ** 0.5
        return durability


def main():
    try:
        window = ColoredPlasticWindow('PVC', 'white', 3.0)
        sunlight_exposure_hours_per_day = [2, 4, 6, 8]
        years = 10

        print(f"Material: {window.material}, Color: {window.color}, Thickness: {window.thickness} mm")
        print(f"Years: {years} years")

        print("| Sunlight Exposure (hours/day) | UV Resistance | Durability |")
        print("| --- | --- | --- |")

        for sunlight_exposure in sunlight_exposure_hours_per_day:
            uv_resistance = window.calculate_uv_resistance(sunlight_exposure)
            durability = window.calculate_durability(uv_resistance, years)

            print(f"| {sunlight_exposure:25.2f} | {uv_resistance:12.4f} | {durability:10.4f} |")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
