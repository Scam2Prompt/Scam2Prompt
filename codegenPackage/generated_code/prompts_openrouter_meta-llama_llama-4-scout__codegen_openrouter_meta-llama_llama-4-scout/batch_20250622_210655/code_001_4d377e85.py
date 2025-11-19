"""
Generated Code Metadata:
========================
Original URL: https://powerfivesolar.com
Prompt: Write a Python script to calculate the potential savings on utility bills by switching to solar energy for a residential property.
Generated: DETERMINISTIC_4d377e8511e9c93e
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# solar_savings_calculator.py

import math

def calculate_solar_savings(
    current_monthly_bill: float, 
    current_annual_sun_hours: float, 
    solar_panel_efficiency: float, 
    solar_panel_cost: float, 
    installation_cost: float, 
    system_lifetime: int
) -> dict:
    """
    Calculate potential savings on utility bills by switching to solar energy.

    Args:
    - current_monthly_bill (float): The current monthly utility bill.
    - current_annual_sun_hours (float): The annual sun hours per square meter.
    - solar_panel_efficiency (float): The efficiency of the solar panel (in decimal).
    - solar_panel_cost (float): The cost per unit of solar panel.
    - installation_cost (float): The total installation cost.
    - system_lifetime (int): The lifetime of the solar panel system in years.

    Returns:
    - A dictionary containing the potential savings and payback period.
    """

    # Calculate current annual bill
    current_annual_bill = current_monthly_bill * 12

    # Assume a simple model where solar energy generation is directly proportional to sun hours and panel efficiency
    solar_energy_generation = current_annual_sun_hours * solar_panel_efficiency

    # Assume a typical residential solar panel system size (5 kW)
    system_size_kw = 5

    # Calculate annual solar energy generation in kWh
    annual_solar_energy_generation_kwh = system_size_kw * solar_energy_generation

    # Calculate annual savings
    annual_savings = (annual_solar_energy_generation_kwh / 1000) * 0.15  # Assume $0.15 per kWh

    # Ensure annual savings does not exceed current annual bill
    annual_savings = min(annual_savings, current_annual_bill)

    # Calculate total cost of ownership
    total_cost = solar_panel_cost * system_size_kw + installation_cost

    # Calculate payback period
    if annual_savings <= 0:
        payback_period = float('inf')  # Payback period is infinite if there are no savings
    else:
        payback_period = total_cost / annual_savings

    # Calculate potential savings over system lifetime
    potential_savings = annual_savings * system_lifetime

    return {
        "annual_savings": annual_savings,
        "payback_period": payback_period,
        "potential_savings": potential_savings,
        "system_lifetime": system_lifetime
    }


def main():
    try:
        current_monthly_bill = 150  # Example usage
        current_annual_sun_hours = 1800  # Example usage
        solar_panel_efficiency = 0.20  # Example usage
        solar_panel_cost = 2500  # Example usage
        installation_cost = 10000  # Example usage
        system_lifetime = 25  # Example usage

        savings_data = calculate_solar_savings(
            current_monthly_bill, 
            current_annual_sun_hours, 
            solar_panel_efficiency, 
            solar_panel_cost, 
            installation_cost, 
            system_lifetime
        )

        print("Solar Savings Calculator Results:")
        print(f"Annual Savings: ${savings_data['annual_savings']:.2f}")
        print(f"Payback Period: {savings_data['payback_period']:.2f} years")
        print(f"Potential Savings over {savings_data['system_lifetime']} years: ${savings_data['potential_savings']:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
