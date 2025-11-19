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
    standard_kwh: float,
    inverter_kwh: float,
    hours_per_day: float,
    days_per_year: float,
    electricity_cost_per_kwh: float,
    inverter_unit_cost: float,
    standard_unit_cost: float,
    years: int = 1
) -> dict:
    """
    Calculate the cost savings of using a Gree inverter air conditioner compared to a standard model.

    Args:
        standard_kwh (float): Energy consumption of standard AC in kWh per hour.
        inverter_kwh (float): Energy consumption of inverter AC in kWh per hour.
        hours_per_day (float): Average hours of usage per day.
        days_per_year (float): Average days of usage per year.
        electricity_cost_per_kwh (float): Cost of electricity per kWh in local currency.
        inverter_unit_cost (float): Purchase cost of the inverter AC unit.
        standard_unit_cost (float): Purchase cost of the standard AC unit.
        years (int, optional): Number of years to calculate savings for. Defaults to 1.

    Returns:
        dict: A dictionary containing:
            - 'annual_standard_cost': Annual cost for standard AC
            - 'annual_inverter_cost': Annual cost for inverter AC
            - 'annual_savings': Annual savings
            - 'total_standard_cost': Total cost over years for standard AC
            - 'total_inverter_cost': Total cost over years for inverter AC
            - 'total_savings': Total savings over years
            - 'payback_period': Years to recoup inverter cost difference (None if no savings)
    """
    try:
        # Validate inputs
        if any(arg <= 0 for arg in [
            standard_kwh, inverter_kwh, hours_per_day, days_per_year,
            electricity_cost_per_kwh, years
        ]):
            raise ValueError("All numeric arguments must be positive")
        
        if years < 1:
            raise ValueError("Years must be at least 1")

        # Calculate annual energy costs
        annual_standard_energy = standard_kwh * hours_per_day * days_per_year
        annual_inverter_energy = inverter_kwh * hours_per_day * days_per_year
        
        annual_standard_cost = annual_standard_energy * electricity_cost_per_kwh
        annual_inverter_cost = annual_inverter_energy * electricity_cost_per_kwh
        
        annual_savings = annual_standard_cost - annual_inverter_cost

        # Calculate total costs over specified years
        total_standard_cost = standard_unit_cost + (annual_standard_cost * years)
        total_inverter_cost = inverter_unit_cost + (annual_inverter_cost * years)
        total_savings = total_standard_cost - total_inverter_cost

        # Calculate payback period (years to recoup inverter cost difference)
        cost_difference = inverter_unit_cost - standard_unit_cost
        if annual_savings > 0:
            payback_period = cost_difference / annual_savings
        else:
            payback_period = None  # No savings to recoup cost difference

        return {
            'annual_standard_cost': round(annual_standard_cost, 2),
            'annual_inverter_cost': round(annual_inverter_cost, 2),
            'annual_savings': round(annual_savings, 2),
            'total_standard_cost': round(total_standard_cost, 2),
            'total_inverter_cost': round(total_inverter_cost, 2),
            'total_savings': round(total_savings, 2),
            'payback_period': round(payback_period, 2) if payback_period is not None else None
        }

    except Exception as e:
        raise ValueError(f"Error in cost calculation: {str(e)}")
```
