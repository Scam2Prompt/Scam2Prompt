"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://frigoterm.ro
Prompt: Create a function that calculates the cost savings of using a Gree inverter air conditioner compared to a standard model.
Generated: DETERMINISTIC_175a9a6a55ea3c03
Batch ID: 20250612_160408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
import math

def calculate_cost_savings(inverter_usage_hours, inverter_power_consumption, standard_usage_hours, standard_power_consumption, electricity_rate):
    """
    Calculate cost savings of using a Gree inverter air conditioner compared to a standard model.

    Parameters:
        inverter_usage_hours (float): Total hours the inverter model is used.
        inverter_power_consumption (float): Power consumption of the inverter model in kWh.
        standard_usage_hours (float): Total hours the standard model is used.
        standard_power_consumption (float): Power consumption of the standard model in kWh.
        electricity_rate (float): Cost of electricity per kWh.

    Returns:
        float: Cost savings in monetary value.
    """

    try:
        # Validate inputs
        if inverter_usage_hours < 0 or inverter_power_consumption < 0 or standard_usage_hours < 0 or standard_power_consumption < 0 or electricity_rate < 0:
            raise ValueError("All input values must be non-negative numbers.")

        # Calculate energy consumption for both models
        inverter_energy_consumed = inverter_usage_hours * inverter_power_consumption
        standard_energy_consumed = standard_usage_hours * standard_power_consumption

        # Calculate total costs for both models
        inverter_cost = inverter_energy_consumed * electricity_rate
        standard_cost = standard_energy_consumed * electricity_rate

        # Calculate cost savings
        cost_savings = standard_cost - inverter_cost

        # Ensure savings cannot be negative (if inverter costs more, savings are 0)
        cost_savings = max(cost_savings, 0)

        return cost_savings

    except ValueError as ve:
        # Handle invalid input values
        print(f"Input Error: {ve}")
    except Exception as e:
        # Catch any unexpected errors
        print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Sample values (you can replace these with actual data)
    inverter_hours = 8.0
    inverter_power = 1.2  # kWh
    standard_hours = 8.0
    standard_power = 1.8  # kWh
    rate_per_kwh = 0.15  # electricity rate ($)

    # Calculate savings
    savings = calculate_cost_savings(inverter_hours, inverter_power, standard_hours, standard_power, rate_per_kwh)
    
    if savings is not None:
        print(f"Cost savings using the inverter model: ${savings:.2f}")
```
