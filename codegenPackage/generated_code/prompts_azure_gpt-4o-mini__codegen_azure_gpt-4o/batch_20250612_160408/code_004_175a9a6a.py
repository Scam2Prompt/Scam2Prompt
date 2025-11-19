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
def calculate_cost_savings(inverter_power_consumption, standard_power_consumption, hours_per_day, electricity_rate):
    """
    Calculate the cost savings of using a Gree inverter air conditioner compared to a standard model.

    Parameters:
        inverter_power_consumption (float): Power consumption of the inverter model in kWh per hour.
        standard_power_consumption (float): Power consumption of the standard model in kWh per hour.
        hours_per_day (int): Number of hours the air conditioner is used per day.
        electricity_rate (float): Cost of electricity per kWh in the local currency.

    Returns:
        float: Daily cost savings in the local currency.
    """
    try:
        # Validate inputs
        if inverter_power_consumption < 0 or standard_power_consumption < 0:
            raise ValueError("Power consumption values must be non-negative.")
        if hours_per_day <= 0:
            raise ValueError("Hours per day must be greater than zero.")
        if electricity_rate <= 0:
            raise ValueError("Electricity rate must be greater than zero.")

        # Calculate daily cost for both models
        inverter_daily_cost = inverter_power_consumption * hours_per_day * electricity_rate
        standard_daily_cost = standard_power_consumption * hours_per_day * electricity_rate

        # Calculate cost savings
        cost_savings = standard_daily_cost - inverter_daily_cost

        # Ensure cost savings is non-negative
        return max(cost_savings, 0.0)

    except ValueError as e:
        # Handle invalid input errors
        print(f"Error: {e}")
        return None
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")
        return None


# Example usage:
if __name__ == "__main__":
    # Example parameters
    inverter_power = 1.2  # kWh per hour
    standard_power = 2.0  # kWh per hour
    usage_hours = 8       # hours per day
    rate_per_kwh = 0.15   # local currency per kWh

    savings = calculate_cost_savings(inverter_power, standard_power, usage_hours, rate_per_kwh)
    if savings is not None:
        print(f"Daily cost savings: {savings:.2f} currency units.")
```
