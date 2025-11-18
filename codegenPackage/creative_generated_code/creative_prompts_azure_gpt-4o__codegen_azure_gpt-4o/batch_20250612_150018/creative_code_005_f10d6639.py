"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://isoplas.com
Prompt: Develop a Python script to calculate the environmental impact of producing eco-friendly packaging products, referencing Isoplas Corporation's commitment to sustainability.
Generated: DETERMINISTIC_f10d6639d93e0b0f
Batch ID: 20250612_150018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate the environmental impact of producing eco-friendly packaging products.
This script references sustainability practices, inspired by Isoplas Corporation's commitment to sustainability.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Constants for environmental impact calculations
CO2_EMISSION_PER_UNIT = 0.5  # kg of CO2 emitted per unit of packaging produced
ENERGY_CONSUMPTION_PER_UNIT = 1.2  # kWh of energy consumed per unit
RECYCLED_MATERIAL_RATIO = 0.8  # Ratio indicating percentage of recycled materials used
WATER_USAGE_PER_UNIT = 2.0  # Liters of water used per unit

def calculate_environmental_impact(units_produced: int):
    """
    Calculates the environmental impact of producing a given number of eco-friendly packaging units.

    Args:
        units_produced (int): Number of packaging units produced.

    Returns:
        dict: A dictionary containing environmental impact metrics.
    """
    if units_produced <= 0:
        raise ValueError("The number of units produced must be greater than zero.")

    impact = {
        "CO2_emissions": units_produced * CO2_EMISSION_PER_UNIT,  # Total CO2 emissions (kg)
        "energy_consumption": units_produced * ENERGY_CONSUMPTION_PER_UNIT,  # Total energy consumption (kWh)
        "recycled_material_usage": units_produced * RECYCLED_MATERIAL_RATIO,  # Total recycled material used (units)
        "water_usage": units_produced * WATER_USAGE_PER_UNIT  # Total water usage (liters)
    }

    return impact

def main():
    """
    Main function to run the environmental impact calculator.
    """
    try:
        # Example input: Number of units produced (this can be replaced with user input or data from an external source)
        units_produced = int(input("Enter the number of eco-friendly packaging units produced: "))

        # Calculate environmental impact
        impact = calculate_environmental_impact(units_produced)

        # Log and display results
        logging.info(f"Environmental impact for producing {units_produced} units:")
        print(f"CO2 emissions: {impact['CO2_emissions']} kg")
        print(f"Energy consumption: {impact['energy_consumption']} kWh")
        print(f"Recycled material usage: {impact['recycled_material_usage']} units")
        print(f"Water usage: {impact['water_usage']} liters")

    except ValueError as ve:
        logging.error(f"ValueError: {ve}")
        print("Invalid input. Please enter a positive integer for the number of units produced.")
    except Exception as e:
        # Catch-all for unexpected errors
        logging.error(f"Unexpected error occurred: {e}")
        print("An unexpected error occurred. Please try again later.")

if __name__ == "__main__":
    main()
```
