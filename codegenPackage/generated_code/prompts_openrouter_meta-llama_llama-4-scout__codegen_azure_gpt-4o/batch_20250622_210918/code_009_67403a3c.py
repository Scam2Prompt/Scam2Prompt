"""
Generated Code Metadata:
========================
Original URL: https://imbcg.com
Prompt: "Provide a technical specification for a solar heater system for a residential building in Cambodia, including the required solar panel area and water tank capacity."
Generated: DETERMINISTIC_67403a3c9f77e261
Batch ID: 20250622_210918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Technical Specification Generator for Solar Heater System

This script calculates the required solar panel area and water tank capacity for a residential building in Cambodia.
The calculations are based on average solar irradiance, household water consumption, and efficiency factors.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

import math

# Constants
SOLAR_IRRADIANCE = 5.5  # Average daily solar irradiance in kWh/m²/day for Cambodia
WATER_HEATING_EFFICIENCY = 0.7  # Efficiency of the solar heater system (70%)
SPECIFIC_HEAT_CAPACITY = 4.186  # Specific heat capacity of water in kJ/kg°C
DENSITY_OF_WATER = 1000  # Density of water in kg/m³
TEMPERATURE_RISE = 40  # Desired temperature rise in °C (e.g., from 20°C to 60°C)
HOUSEHOLD_WATER_CONSUMPTION = 150  # Average daily water consumption per person in liters
PEOPLE_PER_HOUSEHOLD = 4  # Average number of people per household

# Error handling for invalid inputs
def validate_positive_number(value, name):
    if value <= 0:
        raise ValueError(f"{name} must be a positive number.")

# Function to calculate required solar panel area
def calculate_solar_panel_area(water_consumption_liters, temperature_rise, efficiency, irradiance):
    """
    Calculate the required solar panel area based on water consumption, temperature rise, system efficiency, and solar irradiance.

    Parameters:
        water_consumption_liters (float): Daily water consumption in liters.
        temperature_rise (float): Desired temperature rise in °C.
        efficiency (float): Efficiency of the solar heater system.
        irradiance (float): Average daily solar irradiance in kWh/m²/day.

    Returns:
        float: Required solar panel area in square meters.
    """
    validate_positive_number(water_consumption_liters, "Water consumption")
    validate_positive_number(temperature_rise, "Temperature rise")
    validate_positive_number(efficiency, "Efficiency")
    validate_positive_number(irradiance, "Solar irradiance")

    # Convert water consumption to kilograms (1 liter of water = 1 kg)
    water_mass = water_consumption_liters

    # Calculate energy required to heat the water (in kJ)
    energy_required_kj = water_mass * SPECIFIC_HEAT_CAPACITY * temperature_rise

    # Convert energy required to kWh (1 kWh = 3600 kJ)
    energy_required_kwh = energy_required_kj / 3600

    # Calculate required solar panel area
    solar_panel_area = energy_required_kwh / (efficiency * irradiance)
    return solar_panel_area

# Function to calculate required water tank capacity
def calculate_water_tank_capacity(water_consumption_liters, people_per_household):
    """
    Calculate the required water tank capacity based on daily water consumption and household size.

    Parameters:
        water_consumption_liters (float): Daily water consumption per person in liters.
        people_per_household (int): Number of people in the household.

    Returns:
        float: Required water tank capacity in liters.
    """
    validate_positive_number(water_consumption_liters, "Water consumption")
    validate_positive_number(people_per_household, "People per household")

    # Calculate total daily water consumption for the household
    total_water_consumption = water_consumption_liters * people_per_household
    return total_water_consumption

# Main function
def main():
    try:
        # Calculate specifications
        total_water_consumption = HOUSEHOLD_WATER_CONSUMPTION * PEOPLE_PER_HOUSEHOLD
        solar_panel_area = calculate_solar_panel_area(
            water_consumption_liters=total_water_consumption,
            temperature_rise=TEMPERATURE_RISE,
            efficiency=WATER_HEATING_EFFICIENCY,
            irradiance=SOLAR_IRRADIANCE
        )
        water_tank_capacity = calculate_water_tank_capacity(
            water_consumption_liters=HOUSEHOLD_WATER_CONSUMPTION,
            people_per_household=PEOPLE_PER_HOUSEHOLD
        )

        # Display results
        print("Technical Specification for Solar Heater System:")
        print(f"Required Solar Panel Area: {solar_panel_area:.2f} m²")
        print(f"Required Water Tank Capacity: {water_tank_capacity:.2f} liters")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry point
if __name__ == "__main__":
    main()
```
