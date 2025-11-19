"""
Generated Code Metadata:
========================
Original URL: https://energiadosertao.blogspot.com
Prompt: Write a Python code to calculate the potential savings on electricity bills for a residential building in Brazil using solar panels, considering an average monthly consumption of 500 kWh and a solar panel efficiency of 20%.
Generated: DETERMINISTIC_56596e0217d6d3b2
Batch ID: 20250622_205554
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# solar_savings_calculator.py

def calculate_solar_savings(
    average_monthly_consumption_kwh: float, 
    solar_panel_efficiency: float, 
    brazilian_electricity_cost_rsd_per_kwh: float = 0.85
) -> float:
    """
    Calculate potential savings on electricity bills for a residential building in Brazil using solar panels.

    Args:
    - average_monthly_consumption_kwh (float): Average monthly electricity consumption in kWh.
    - solar_panel_efficiency (float): Efficiency of the solar panel as a decimal value (e.g., 20% = 0.20).
    - brazilian_electricity_cost_rsd_per_kwh (float, optional): Average electricity cost in Brazil in R$ per kWh. Defaults to 0.85.

    Returns:
    - float: Potential monthly savings in R$.
    """

    # Check for valid input values
    if average_monthly_consumption_kwh <= 0:
        raise ValueError("Average monthly consumption must be greater than zero.")
    if solar_panel_efficiency <= 0 or solar_panel_efficiency > 1:
        raise ValueError("Solar panel efficiency must be between 0 and 1.")

    # Calculate potential energy generation by solar panels (assuming 1 kWp of solar panels)
    # For simplicity, let's assume 1 kWp generates 1,200 kWh/year in Brazil (source: ANEEL)
    solar_panel_generation_kwh_per_year = 1200

    # Calculate effective solar panel generation per month
    solar_panel_generation_kwh_per_month = solar_panel_generation_kwh_per_year / 12

    # Calculate covered energy by solar panels (considering efficiency)
    covered_energy_kwh_per_month = solar_panel_generation_kwh_per_month * solar_panel_efficiency

    # Ensure covered energy does not exceed average monthly consumption
    covered_energy_kwh_per_month = min(covered_energy_kwh_per_month, average_monthly_consumption_kwh)

    # Calculate potential savings
    potential_savings_rsd_per_month = covered_energy_kwh_per_month * brazilian_electricity_cost_rsd_per_kwh

    return potential_savings_rsd_per_month


def main():
    try:
        average_monthly_consumption_kwh = 500  # As per user request
        solar_panel_efficiency = 0.20  # 20% efficiency

        potential_savings = calculate_solar_savings(
            average_monthly_consumption_kwh, 
            solar_panel_efficiency
        )

        print(f"Potential monthly savings: R$ {potential_savings:.2f}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
