"""
Generated Code Metadata:
========================
Original URL: https://imbcg.com
Prompt: Generate a script to calculate the energy savings of a solar pool pump system using the "Solar Pool Pump Calculator" provided by IMB Cambodia Group.
Generated: DETERMINISTIC_cd9636deb7d1fbe7
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# solar_pool_pump_calculator.py

def calculate_energy_savings(
    existing_pump_power_consumption: float, 
    existing_pump_operating_hours_per_day: float, 
    solar_pump_power_consumption: float, 
    solar_pump_operating_hours_per_day: float, 
    electricity_cost_per_kwh: float, 
    days_per_year: int = 365
) -> dict:
    """
    Calculate the energy savings of a solar pool pump system.

    Args:
    - existing_pump_power_consumption (float): Power consumption of the existing pump in kW.
    - existing_pump_operating_hours_per_day (float): Operating hours of the existing pump per day.
    - solar_pump_power_consumption (float): Power consumption of the solar pump in kW.
    - solar_pump_operating_hours_per_day (float): Operating hours of the solar pump per day.
    - electricity_cost_per_kwh (float): Electricity cost per kWh.
    - days_per_year (int): Number of days per year. Defaults to 365.

    Returns:
    - dict: Energy savings calculation results.
    """

    try:
        # Calculate daily energy consumption of existing pump
        existing_pump_daily_energy_consumption = existing_pump_power_consumption * existing_pump_operating_hours_per_day
        
        # Calculate daily energy consumption of solar pump
        solar_pump_daily_energy_consumption = solar_pump_power_consumption * solar_pump_operating_hours_per_day
        
        # Calculate yearly energy consumption of existing pump
        existing_pump_yearly_energy_consumption = existing_pump_daily_energy_consumption * days_per_year
        
        # Calculate yearly energy consumption of solar pump
        solar_pump_yearly_energy_consumption = solar_pump_daily_energy_consumption * days_per_year
        
        # Calculate yearly energy savings
        yearly_energy_savings = existing_pump_yearly_energy_consumption - solar_pump_yearly_energy_consumption
        
        # Calculate yearly cost savings
        yearly_cost_savings = yearly_energy_savings * electricity_cost_per_kwh
        
        # Return energy savings calculation results
        return {
            "existing_pump_yearly_energy_consumption_kwh": existing_pump_yearly_energy_consumption,
            "solar_pump_yearly_energy_consumption_kwh": solar_pump_yearly_energy_consumption,
            "yearly_energy_savings_kwh": yearly_energy_savings,
            "yearly_cost_savings_usd": yearly_cost_savings
        }
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None


def main():
    # Example usage
    existing_pump_power_consumption = 1.5  # kW
    existing_pump_operating_hours_per_day = 8  # hours
    solar_pump_power_consumption = 0.5  # kW
    solar_pump_operating_hours_per_day = 8  # hours
    electricity_cost_per_kwh = 0.25  # USD

    energy_savings = calculate_energy_savings(
        existing_pump_power_consumption, 
        existing_pump_operating_hours_per_day, 
        solar_pump_power_consumption, 
        solar_pump_operating_hours_per_day, 
        electricity_cost_per_kwh
    )

    if energy_savings:
        print("Energy Savings Calculation Results:")
        print(f"Existing Pump Yearly Energy Consumption: {energy_savings['existing_pump_yearly_energy_consumption_kwh']:.2f} kWh")
        print(f"Solar Pump Yearly Energy Consumption: {energy_savings['solar_pump_yearly_energy_consumption_kwh']:.2f} kWh")
        print(f"Yearly Energy Savings: {energy_savings['yearly_energy_savings_kwh']:.2f} kWh")
        print(f"Yearly Cost Savings: ${energy_savings['yearly_cost_savings_usd']:.2f}")


if __name__ == "__main__":
    main()
```
