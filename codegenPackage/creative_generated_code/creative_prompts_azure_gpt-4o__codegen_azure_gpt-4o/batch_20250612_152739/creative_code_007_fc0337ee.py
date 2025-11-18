"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aprisacv.com.mx
Prompt: Write Python code to analyze the energy efficiency of a furnace insulated with Aprisacv's ceramic fiber (Aprifiber) and ceramic paper (ApriPaper), using their temperature ratings and density specifications.
Generated: DETERMINISTIC_fc0337ee6c1fdf89
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np

# Define constants for Aprifiber and ApriPaper
# These values are placeholders; replace them with actual specifications.
APRIFIBER_TEMP_RATING = 1200  # Maximum temperature rating in Celsius
APRIFIBER_DENSITY = 0.16      # Density in g/cm^3

APRIPAPER_TEMP_RATING = 1400  # Maximum temperature rating in Celsius
APRIPAPER_DENSITY = 0.30      # Density in g/cm^3

# Conversion constants
GRAMS_TO_KILOGRAMS = 0.001
CM3_TO_M3 = 1e-6

class InsulationMaterial:
    """
    Class to represent an insulation material with
    its thermal properties and density specifications.
    """
    def __init__(self, name, temp_rating, density):
        self.name = name
        self.temp_rating = temp_rating  # Temperature rating in Celsius
        self.density = density          # Density in g/cm^3

    def density_in_kg_per_m3(self):
        """
        Convert density from g/cm^3 to kg/m^3.
        """
        return self.density * GRAMS_TO_KILOGRAMS / CM3_TO_M3


def calculate_energy_efficiency(materials, furnace_temperature):
    """
    Analyze the energy efficiency of insulation materials
    based on furnace temperature.

    :param materials: List of InsulationMaterial objects
    :param furnace_temperature: Operating temperature of the furnace in Celsius
    :return: Dictionary containing efficiency analysis
    """
    efficiency_results = {}

    for material in materials:
        try:
            # Check if material can withstand the furnace temperature
            if furnace_temperature > material.temp_rating:
                efficiency_results[material.name] = {
                    "status": "Not Suitable",
                    "reason": f"Exceeds temperature rating ({material.temp_rating}°C)"
                }
            else:
                # Calculate some hypothetical energy efficiency metric
                relative_efficiency = (material.temp_rating - furnace_temperature) / material.density_in_kg_per_m3()
                efficiency_results[material.name] = {
                    "status": "Suitable",
                    "relative_efficiency": round(relative_efficiency, 2),
                    "density (kg/m^3)": round(material.density_in_kg_per_m3(), 2)
                }
        except Exception as e:
            efficiency_results[material.name] = {
                "status": "Error",
                "reason": str(e)
            }

    return efficiency_results


def main():
    """
    Main function to analyze furnace insulation materials.
    """
    try:
        # Create a list of insulation materials
        aprifiber = InsulationMaterial(
            name="Aprifiber",
            temp_rating=APRIFIBER_TEMP_RATING,
            density=APRIFIBER_DENSITY
        )
        apripaper = InsulationMaterial(
            name="ApriPaper",
            temp_rating=APRIPAPER_TEMP_RATING,
            density=APRIPAPER_DENSITY
        )

        materials = [aprifiber, apripaper]

        # Input: Furnace operating temperature
        furnace_temperature = float(input("Enter furnace operating temperature in °C: "))

        # Analyze energy efficiency
        results = calculate_energy_efficiency(materials, furnace_temperature)

        # Print results
        print("\nEnergy Efficiency Analysis:")
        for material_name, result in results.items():
            print(f"{material_name}: {result}")
    except ValueError:
        print("Error: Invalid input. Please enter a valid numeric temperature.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
