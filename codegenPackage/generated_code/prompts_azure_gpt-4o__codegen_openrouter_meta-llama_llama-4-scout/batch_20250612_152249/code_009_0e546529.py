"""
Generated Code Metadata:
========================
Original URL: https://kataskeui.gr
Prompt: Write a script to calculate the energy performance of a building and categorize it into one of the nine energy classes (A+ to H) based on Greek standards.
Generated: DETERMINISTIC_0e54652978283980
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# energy_performance_calculator.py

import math

def calculate_energy_performance(kWh_m2_year):
    """
    Calculate the energy performance class of a building based on Greek standards.

    Args:
        kWh_m2_year (float): The energy consumption of the building in kWh/m²/year.

    Returns:
        str: The energy performance class (A+ to H).
    """
    if kWh_m2_year <= 0:
        raise ValueError("Energy consumption must be greater than zero.")

    # Greek energy performance classes (kWh/m²/year)
    # Source: Greek Ministry of Environment and Energy
    if kWh_m2_year <= 15:
        return "A+"
    elif kWh_m2_year <= 30:
        return "A"
    elif kWh_m2_year <= 45:
        return "B"
    elif kWh_m2_year <= 60:
        return "C"
    elif kWh_m2_year <= 80:
        return "D"
    elif kWh_m2_year <= 110:
        return "E"
    elif kWh_m2_year <= 140:
        return "F"
    elif kWh_m2_year <= 170:
        return "G"
    else:
        return "H"


def calculate_specific_energy_consumption(total_energy_consumption, building_area):
    """
    Calculate the specific energy consumption of a building.

    Args:
        total_energy_consumption (float): The total energy consumption of the building in kWh/year.
        building_area (float): The area of the building in m².

    Returns:
        float: The specific energy consumption in kWh/m²/year.
    """
    if building_area <= 0:
        raise ValueError("Building area must be greater than zero.")

    return total_energy_consumption / building_area


def main():
    try:
        # Example usage
        total_energy_consumption = 100000  # kWh/year
        building_area = 1000  # m²

        specific_energy_consumption = calculate_specific_energy_consumption(total_energy_consumption, building_area)
        energy_performance_class = calculate_energy_performance(specific_energy_consumption)

        print(f"Specific energy consumption: {specific_energy_consumption:.2f} kWh/m²/year")
        print(f"Energy performance class: {energy_performance_class}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
