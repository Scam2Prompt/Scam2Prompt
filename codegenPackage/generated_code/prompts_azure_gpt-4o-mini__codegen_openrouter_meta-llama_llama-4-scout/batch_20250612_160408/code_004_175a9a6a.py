"""
Generated Code Metadata:
========================
Original URL: https://frigoterm.ro
Prompt: Create a function that calculates the cost savings of using a Gree inverter air conditioner compared to a standard model.
Generated: DETERMINISTIC_175a9a6a55ea3c03
Batch ID: 20250612_160408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_cost_savings(
    standard_ac_power_consumption: float, 
    gree_ac_power_consumption: float, 
    usage_hours_per_day: int, 
    days_per_year: int, 
    electricity_cost_per_kwh: float
) -> float:
    """
    Calculate the cost savings of using a Gree inverter air conditioner compared to a standard model.

    Args:
    - standard_ac_power_consumption (float): The power consumption of the standard air conditioner in kW.
    - gree_ac_power_consumption (float): The power consumption of the Gree inverter air conditioner in kW.
    - usage_hours_per_day (int): The number of hours the air conditioner is used per day.
    - days_per_year (int): The number of days the air conditioner is used per year.
    - electricity_cost_per_kwh (float): The cost of electricity per kWh.

    Returns:
    - float: The cost savings of using the Gree inverter air conditioner per year.

    Raises:
    - ValueError: If any of the input values are negative.
    """

    # Check for negative input values
    if (
        standard_ac_power_consumption < 0 or 
        gree_ac_power_consumption < 0 or 
        usage_hours_per_day < 0 or 
        days_per_year < 0 or 
        electricity_cost_per_kwh < 0
    ):
        raise ValueError("All input values must be non-negative.")

    # Calculate the annual energy consumption of the standard air conditioner
    standard_ac_annual_energy_consumption = standard_ac_power_consumption * usage_hours_per_day * days_per_year
    
    # Calculate the annual energy consumption of the Gree inverter air conditioner
    gree_ac_annual_energy_consumption = gree_ac_power_consumption * usage_hours_per_day * days_per_year

    # Calculate the annual cost of the standard air conditioner
    standard_ac_annual_cost = standard_ac_annual_energy_consumption * electricity_cost_per_kwh
    
    # Calculate the annual cost of the Gree inverter air conditioner
    gree_ac_annual_cost = gree_ac_annual_energy_consumption * electricity_cost_per_kwh

    # Calculate the cost savings of using the Gree inverter air conditioner
    cost_savings = standard_ac_annual_cost - gree_ac_annual_cost

    return cost_savings


def main():
    try:
        standard_ac_power_consumption = 1.5  # kW
        gree_ac_power_consumption = 1.2  # kW
        usage_hours_per_day = 8  # hours
        days_per_year = 365  # days
        electricity_cost_per_kwh = 0.20  # $/kWh

        cost_savings = calculate_cost_savings(
            standard_ac_power_consumption, 
            gree_ac_power_consumption, 
            usage_hours_per_day, 
            days_per_year, 
            electricity_cost_per_kwh
        )

        print(f"The cost savings of using the Gree inverter air conditioner is: ${cost_savings:.2f} per year")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
