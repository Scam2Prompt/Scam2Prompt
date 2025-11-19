"""
Generated Code Metadata:
========================
Original URL: https://imbcg.com
Prompt: Develop a Python function to calculate CO2 emissions reduction when switching from diesel-powered systems to solar-powered systems, referencing IMB Cambodia Group's CO2 Emissions Calculator.
Generated: DETERMINISTIC_a184fc9e993ca661
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_co2_reduction(
    diesel_consumption_liters_per_year: float, 
    solar_system_capacity_kw: float, 
    diesel_co2_emission_factor_kg_per_liter: float = 2.64, 
    solar_system_co2_emission_factor_kg_per_kwh: float = 0.05
) -> float:
    """
    Calculate CO2 emissions reduction when switching from diesel-powered systems to solar-powered systems.

    Args:
    - diesel_consumption_liters_per_year (float): Annual diesel consumption in liters.
    - solar_system_capacity_kw (float): Solar system capacity in kilowatts.
    - diesel_co2_emission_factor_kg_per_liter (float, optional): CO2 emission factor for diesel in kg/L. Defaults to 2.64.
    - solar_system_co2_emission_factor_kg_per_kwh (float, optional): CO2 emission factor for solar system in kg/kWh. Defaults to 0.05.

    Returns:
    - float: CO2 emissions reduction in kg per year.
    """

    # Calculate CO2 emissions from diesel consumption
    diesel_co2_emissions_kg_per_year = diesel_consumption_liters_per_year * diesel_co2_emission_factor_kg_per_liter

    # Assume solar system operates at 8760 hours per year (100% capacity factor for simplicity)
    solar_system_operation_hours_per_year = 8760

    # Calculate solar system energy production in kWh per year
    solar_system_energy_production_kwh_per_year = solar_system_capacity_kw * solar_system_operation_hours_per_year

    # Calculate CO2 emissions from solar system
    solar_system_co2_emissions_kg_per_year = solar_system_energy_production_kwh_per_year * solar_system_co2_emission_factor_kg_per_kwh

    # Calculate CO2 emissions reduction
    co2_reduction_kg_per_year = diesel_co2_emissions_kg_per_year - solar_system_co2_emissions_kg_per_year

    # Ensure CO2 reduction is not negative (i.e., solar system does not produce more emissions than diesel)
    if co2_reduction_kg_per_year < 0:
        raise ValueError("Solar system CO2 emissions exceed diesel CO2 emissions. Reduction is not possible.")

    return co2_reduction_kg_per_year


def main():
    try:
        diesel_consumption_liters_per_year = 10000  # Example diesel consumption
        solar_system_capacity_kw = 10  # Example solar system capacity

        co2_reduction = calculate_co2_reduction(diesel_consumption_liters_per_year, solar_system_capacity_kw)
        print(f"CO2 emissions reduction: {co2_reduction:.2f} kg/year")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
