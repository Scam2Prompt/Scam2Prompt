"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://accutrolsystems.com
Prompt: Write Python code to calculate the energy efficiency of a solar water heater system using specifications similar to the Calpak Solar Energy products mentioned on the Accutrol Systems website.
Generated: DETERMINISTIC_70cb2a50b197cff3
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


def calculate_solar_water_heater_efficiency(
        solar_irradiance, collector_area, collector_efficiency, water_flow_rate, water_temperature_inlet,
        water_temperature_outlet):
    """
    Calculate the energy efficiency of a solar water heater system.

    Parameters:
        solar_irradiance (float): Solar irradiance in watts per square meter (W/m^2).
        collector_area (float): Area of the solar collector in square meters (m^2).
        collector_efficiency (float): Efficiency of the solar collector (value between 0 and 1).
        water_flow_rate (float): Water flow rate in liters per hour (L/h).
        water_temperature_inlet (float): Inlet water temperature in degrees Celsius (°C).
        water_temperature_outlet (float): Outlet water temperature in degrees Celsius (°C).

    Returns:
        dict: A dictionary containing the calculated results:
            - Thermal energy (kWh)
            - Solar energy input (kWh)
            - Efficiency percentage (%)

    Raises:
        ValueError: If input parameters are out of expected range or invalid.
    """
    # Validate input parameters
    if not (0 <= collector_efficiency <= 1):
        raise ValueError("Collector efficiency must be between 0 and 1.")
    if water_flow_rate <= 0:
        raise ValueError("Water flow rate must be a positive value.")
    if collector_area <= 0:
        raise ValueError("Collector area must be a positive value.")
    if solar_irradiance <= 0:
        raise ValueError("Solar irradiance must be a positive value.")
    if water_temperature_outlet <= water_temperature_inlet:
        raise ValueError("Outlet temperature must be higher than inlet temperature.")

    # Physical constants
    specific_heat_capacity_water = 4.186  # Specific heat capacity of water in kJ/kg°C
    density_of_water = 1.0  # Density of water in kg/L

    # Convert water flow rate from liters per hour to kg per second
    water_flow_rate_kg_per_sec = water_flow_rate * density_of_water / 3600

    # Calculate thermal energy gained by water
    temperature_difference = water_temperature_outlet - water_temperature_inlet
    thermal_energy_kwh = (
        water_flow_rate_kg_per_sec *
        specific_heat_capacity_water *
        temperature_difference / 3600  # Convert kJ to kWh
    )

    # Calculate solar energy input
    solar_energy_input_kwh = collector_area * solar_irradiance * collector_efficiency / 1000  # Convert W to kWh

    # Calculate efficiency percentage
    if solar_energy_input_kwh == 0:
        efficiency_percentage = 0
    else:
        efficiency_percentage = (thermal_energy_kwh / solar_energy_input_kwh) * 100

    # Return results in a dictionary
    return {
        "Thermal Energy (kWh)": round(thermal_energy_kwh, 2),
        "Solar Energy Input (kWh)": round(solar_energy_input_kwh, 2),
        "Efficiency (%)": round(efficiency_percentage, 2)
    }


if __name__ == "__main__":
    # Example usage
    try:
        # User-provided values (replace these with actual values for your system)
        solar_irradiance = 800  # W/m^2
        collector_area = 2.5  # m^2
        collector_efficiency = 0.75  # 75% efficiency
        water_flow_rate = 100  # L/h
        water_temperature_inlet = 15  # °C
        water_temperature_outlet = 55  # °C

        results = calculate_solar_water_heater_efficiency(
            solar_irradiance, collector_area, collector_efficiency,
            water_flow_rate, water_temperature_inlet, water_temperature_outlet
        )
        print("Solar Water Heater Efficiency Results:")
        for key, value in results.items():
            print(f"{key}: {value}")
    except ValueError as e:
        print(f"Error: {e}")
```
