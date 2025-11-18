"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.ablakvaros.hu
Prompt: Create a Python program to calculate the UV állóság (UV resistance) and durability of színes műanyag ablak (colored plastic windows) under different sunlight exposure conditions.
Generated: DETERMINISTIC_cf9e41496bbf6e6c
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class UVResistanceCalculator:
    """
    This class calculates the UV resistance and durability of colored plastic windows
    under varying sunlight exposure conditions.
    """

    def __init__(self, uv_index, exposure_hours, material_type):
        """
        Initialize the UVResistanceCalculator with necessary parameters.

        :param uv_index: Average UV index (scale 0-11+)
        :param exposure_hours: Total hours of sunlight exposure per year
        :param material_type: Type of plastic material (e.g., 'ABS', 'PVC', 'Polycarbonate')
        """
        self.uv_index = uv_index
        self.exposure_hours = exposure_hours
        self.material_type = material_type

    def calculate_uv_resistance(self):
        """
        Calculate the UV resistance score based on material type and UV index.
        
        :return: UV resistance score (higher is better)
        """
        material_resistance_factors = {
            'ABS': 0.8,             # ABS has moderate UV resistance
            'PVC': 0.6,             # PVC has lower UV resistance
            'Polycarbonate': 1.0    # Polycarbonate has high UV resistance
        }

        # Default resistance factor if material type is unknown
        resistance_factor = material_resistance_factors.get(self.material_type, 0.5)

        # UV resistance score calculation
        uv_resistance_score = resistance_factor / (1 + math.exp(self.uv_index - 5))
        return uv_resistance_score

    def calculate_durability(self):
        """
        Estimate the durability (in years) of the material based on UV resistance
        and sunlight exposure hours.

        :return: Estimated durability in years
        """
        uv_resistance_score = self.calculate_uv_resistance()
        
        # Durability formula: Higher UV resistance and lower exposure hours increase lifespan
        durability_years = (uv_resistance_score * 1000) / self.exposure_hours
        return round(durability_years, 2)

    def display_results(self):
        """
        Display the UV resistance and durability results.
        """
        uv_resistance = self.calculate_uv_resistance()
        durability = self.calculate_durability()

        print(f"Material Type: {self.material_type}")
        print(f"UV Index: {self.uv_index}")
        print(f"Exposure Hours Per Year: {self.exposure_hours}")
        print(f"Calculated UV Resistance Score: {uv_resistance:.2f}")
        print(f"Estimated Durability: {durability} years")


def main():
    """
    Main function to execute the UV resistance and durability calculations.
    """
    try:
        # Input parameters from the user
        uv_index = float(input("Enter the average UV index (0-11+): "))
        exposure_hours = int(input("Enter the total sunlight exposure hours per year: "))
        material_type = input("Enter the material type (e.g., 'ABS', 'PVC', 'Polycarbonate'): ").strip()

        # Ensure input values are valid
        if uv_index < 0 or uv_index > 11:
            raise ValueError("UV index must be between 0 and 11.")
        if exposure_hours <= 0:
            raise ValueError("Exposure hours must be a positive integer.")
        if material_type not in ['ABS', 'PVC', 'Polycarbonate']:
            raise ValueError("Unsupported material type. Choose between 'ABS', 'PVC', or 'Polycarbonate'.")

        # Create an instance of UVResistanceCalculator and display results
        calculator = UVResistanceCalculator(uv_index, exposure_hours, material_type)
        calculator.display_results()

    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
