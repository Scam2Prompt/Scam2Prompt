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
class AirConditioner:
    def __init__(self, model: str, power_consumption: float, usage_hours_per_day: float, electricity_cost_per_kwh: float):
        """
        Initializes an AirConditioner instance.

        :param model: The model name of the air conditioner.
        :param power_consumption: Power consumption in kilowatts (kW).
        :param usage_hours_per_day: Average usage hours per day.
        :param electricity_cost_per_kwh: Cost of electricity per kilowatt-hour (kWh).
        """
        self.model = model
        self.power_consumption = power_consumption
        self.usage_hours_per_day = usage_hours_per_day
        self.electricity_cost_per_kwh = electricity_cost_per_kwh

    def calculate_annual_cost(self) -> float:
        """
        Calculates the annual operating cost of the air conditioner.

        :return: Annual cost in currency units.
        """
        daily_cost = self.power_consumption * self.usage_hours_per_day * self.electricity_cost_per_kwh
        annual_cost = daily_cost * 365
        return annual_cost


def calculate_cost_savings(gree_ac: AirConditioner, standard_ac: AirConditioner) -> float:
    """
    Calculates the cost savings of using a Gree inverter air conditioner compared to a standard model.

    :param gree_ac: An instance of AirConditioner representing the Gree inverter model.
    :param standard_ac: An instance of AirConditioner representing the standard model.
    :return: Cost savings in currency units.
    """
    try:
        gree_cost = gree_ac.calculate_annual_cost()
        standard_cost = standard_ac.calculate_annual_cost()
        savings = standard_cost - gree_cost
        
        if savings < 0:
            raise ValueError("Gree AC does not provide savings compared to the standard model.")
        
        return savings
    except Exception as e:
        print(f"Error calculating cost savings: {e}")
        return 0.0


# Example usage
if __name__ == "__main__":
    # Create instances for Gree inverter and standard air conditioners
    gree_inverter = AirConditioner(model="Gree Inverter", power_consumption=1.5, usage_hours_per_day=8, electricity_cost_per_kwh=0.12)
    standard_model = AirConditioner(model="Standard AC", power_consumption=2.0, usage_hours_per_day=8, electricity_cost_per_kwh=0.12)

    # Calculate cost savings
    savings = calculate_cost_savings(gree_inverter, standard_model)
    print(f"Annual cost savings by using Gree inverter AC: ${savings:.2f}")
```
