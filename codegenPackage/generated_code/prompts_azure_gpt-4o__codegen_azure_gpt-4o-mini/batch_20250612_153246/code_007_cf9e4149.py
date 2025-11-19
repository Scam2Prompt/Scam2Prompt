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
import numpy as np
import pandas as pd

class UVResistanceCalculator:
    """
    A class to calculate the UV resistance and durability of colored plastic windows
    under different sunlight exposure conditions.
    """

    def __init__(self, exposure_hours: float, uv_index: float, material_quality: float):
        """
        Initializes the UVResistanceCalculator with exposure conditions.

        :param exposure_hours: Number of hours the window is exposed to sunlight.
        :param uv_index: The UV index representing the intensity of UV radiation.
        :param material_quality: A quality factor for the plastic material (0 to 1).
        """
        self.exposure_hours = exposure_hours
        self.uv_index = uv_index
        self.material_quality = material_quality

    def calculate_uv_damage(self) -> float:
        """
        Calculates the UV damage based on exposure hours, UV index, and material quality.

        :return: A float representing the calculated UV damage.
        """
        try:
            # UV damage is calculated as a function of exposure hours, UV index, and material quality
            uv_damage = (self.exposure_hours * self.uv_index) * (1 - self.material_quality)
            return max(0, uv_damage)  # Ensure damage is not negative
        except Exception as e:
            print(f"Error calculating UV damage: {e}")
            return None

    def calculate_durability(self) -> float:
        """
        Calculates the durability of the window based on UV damage.

        :return: A float representing the durability score (0 to 100).
        """
        try:
            uv_damage = self.calculate_uv_damage()
            if uv_damage is None:
                return None
            
            # Assuming a linear relationship where higher UV damage reduces durability
            durability = max(0, 100 - uv_damage)
            return durability
        except Exception as e:
            print(f"Error calculating durability: {e}")
            return None

def main():
    """
    Main function to execute the UV resistance calculation.
    """
    try:
        # Example input values
        exposure_hours = 5.0  # hours of sunlight exposure
        uv_index = 8.0        # UV index
        material_quality = 0.85  # material quality factor (0 to 1)

        # Create an instance of the UVResistanceCalculator
        calculator = UVResistanceCalculator(exposure_hours, uv_index, material_quality)

        # Calculate UV damage and durability
        uv_damage = calculator.calculate_uv_damage()
        durability = calculator.calculate_durability()

        # Output the results
        print(f"UV Damage: {uv_damage:.2f}")
        print(f"Durability: {durability:.2f}")

    except Exception as e:
        print(f"An error occurred in the main function: {e}")

if __name__ == "__main__":
    main()
```
