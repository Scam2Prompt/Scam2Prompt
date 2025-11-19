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
# solar_heater_system.py

import math

def calculate_solar_panel_area(daily_water_requirement, 
                                temperature_rise, 
                                efficiency=0.5, 
                                solar_irradiance=5.5):
    """
    Calculate the required solar panel area.

    Args:
    - daily_water_requirement (float): Daily water requirement in liters.
    - temperature_rise (float): Desired temperature rise in Celsius.
    - efficiency (float, optional): System efficiency. Defaults to 0.5.
    - solar_irradiance (float, optional): Solar irradiance in kW/m^2. Defaults to 5.5.

    Returns:
    - float: Required solar panel area in m^2.
    """
    # Specific heat capacity of water in kJ/kg°C
    specific_heat_capacity = 4.184

    # Density of water in kg/L
    water_density = 1

    # Calculate the total energy required
    total_energy_required = daily_water_requirement * water_density * specific_heat_capacity * temperature_rise / 3600  # Convert to kWh

    # Calculate the required solar panel area
    solar_panel_area = total_energy_required / (solar_irradiance * efficiency)

    return solar_panel_area


def calculate_water_tank_capacity(daily_water_requirement, 
                                  usage_hours):
    """
    Calculate the required water tank capacity.

    Args:
    - daily_water_requirement (float): Daily water requirement in liters.
    - usage_hours (float): Number of hours of usage.

    Returns:
    - float: Required water tank capacity in liters.
    """
    # Calculate the required water tank capacity
    water_tank_capacity = daily_water_requirement / (24 / usage_hours)

    return water_tank_capacity


def solar_heater_system_specification(
    daily_water_requirement, 
    temperature_rise, 
    usage_hours, 
    efficiency=0.5, 
    solar_irradiance=5.5):
    """
    Provide a technical specification for a solar heater system.

    Args:
    - daily_water_requirement (float): Daily water requirement in liters.
    - temperature_rise (float): Desired temperature rise in Celsius.
    - usage_hours (float): Number of hours of usage.
    - efficiency (float, optional): System efficiency. Defaults to 0.5.
    - solar_irradiance (float, optional): Solar irradiance in kW/m^2. Defaults to 5.5.

    Returns:
    - dict: Technical specification for the solar heater system.
    """
    try:
        solar_panel_area = calculate_solar_panel_area(
            daily_water_requirement, 
            temperature_rise, 
            efficiency, 
            solar_irradiance
        )

        water_tank_capacity = calculate_water_tank_capacity(
            daily_water_requirement, 
            usage_hours
        )

        # Cambodia's average solar irradiance is around 5.5 kWh/m^2/day
        # Assuming a system lifespan of 10 years
        system_lifespan = 10  # years

        technical_specification = {
            "solar_panel_area": round(solar_panel_area, 2),
            "water_tank_capacity": round(water_tank_capacity, 2),
            "system_lifespan": system_lifespan,
            "solar_irradiance": solar_irradiance,
            "efficiency": efficiency
        }

        return technical_specification

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


if __name__ == "__main__":
    daily_water_requirement = 500  # liters
    temperature_rise = 20  # Celsius
    usage_hours = 8

    technical_specification = solar_heater_system_specification(
        daily_water_requirement, 
        temperature_rise, 
        usage_hours
    )

    if technical_specification:
        print("Technical Specification:")
        for key, value in technical_specification.items():
            print(f"{key.capitalize().replace('_', ' ')}: {value}")
```
