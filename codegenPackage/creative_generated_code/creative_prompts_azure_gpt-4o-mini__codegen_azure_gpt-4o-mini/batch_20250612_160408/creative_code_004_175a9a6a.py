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
class AirConditioner:
    def __init__(self, model: str, power_consumption: float, cost_per_kwh: float):
        """
        Initialize an air conditioner with a specific model, power consumption, and cost per kWh.

        Args:
            model (str): The model name of the air conditioner.
            power_consumption (float): Power consumption in kWh.
            cost_per_kwh (float): Cost of electricity per kWh.
        """
        self.model = model
        self.power_consumption = power_consumption  # in kWh
        self.cost_per_kwh = cost_per_kwh           # in currency units

    def calculate_monthly_cost(self, hours_per_day: float, days_per_month: int = 30) -> float:
        """
        Calculate the monthly operating cost of the air conditioner.

        Args:
            hours_per_day (float): Number of hours the air conditioner is used per day.
            days_per_month (int): Number of days in a month. Default is 30.

        Returns:
            float: Monthly operating cost in currency units.
        """
        if hours_per_day < 0 or days_per_month <= 0:
            raise ValueError("Hours per day must be non-negative and days per month must be positive.")
        
        monthly_usage_kwh = self.power_consumption * hours_per_day * days_per_month
        monthly_cost = monthly_usage_kwh * self.cost_per_kwh
        
        return monthly_cost


def calculate_cost_savings(gree_ac: AirConditioner, standard_ac: AirConditioner, hours_per_day: float) -> float:
    """
    Calculate the cost savings of using a Gree inverter air conditioner compared to a standard model.

    Args:
        gree_ac (AirConditioner): The Gree inverter air conditioner.
        standard_ac (AirConditioner): The standard air conditioner.
        hours_per_day (float): Number of hours both units are used per day.

    Returns:
        float: Monthly cost savings in currency units.
    """
    try:
        gree_cost = gree_ac.calculate_monthly_cost(hours_per_day)
        standard_cost = standard_ac.calculate_monthly_cost(hours_per_day)
        savings = standard_cost - gree_cost
        
        return savings
    except ValueError as e:
        print(f"Error calculating cost savings: {e}")
        return 0.0  # Return zero savings in case of error


# Example usage
if __name__ == "__main__":
    # Create instances of AirConditioner for Gree and standard models
    gree_inverter = AirConditioner(model="Gree Inverter", power_consumption=1.5, cost_per_kwh=0.12)
    standard_ac = AirConditioner(model="Standard AC", power_consumption=2.0, cost_per_kwh=0.12)

    # Calculate cost savings
    hours_per_day = 8
    savings = calculate_cost_savings(gree_inverter, standard_ac, hours_per_day)
    
    print(f"Monthly cost savings of Gree inverter over standard AC: ${savings:.2f}")
```
