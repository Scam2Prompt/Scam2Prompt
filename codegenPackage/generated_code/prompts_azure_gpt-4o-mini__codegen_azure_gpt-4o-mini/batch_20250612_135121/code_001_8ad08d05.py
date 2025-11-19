"""
Generated Code Metadata:
========================
Original URL: https://id.stromkonto.net
Prompt: Write a code snippet to calculate CO2 savings based on kWh generation and usage as described in the Stromkonto documentation.
Generated: DETERMINISTIC_8ad08d0524d82571
Batch ID: 20250612_135121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CO2SavingsCalculator:
    """
    A class to calculate CO2 savings based on kWh generation and usage.
    """

    def __init__(self, generation_kwh, usage_kwh, co2_per_kwh=0.5):
        """
        Initializes the CO2SavingsCalculator with generation and usage values.

        :param generation_kwh: Total kWh generated
        :param usage_kwh: Total kWh used
        :param co2_per_kwh: CO2 emissions per kWh (default is 0.5 kg CO2/kWh)
        """
        self.generation_kwh = generation_kwh
        self.usage_kwh = usage_kwh
        self.co2_per_kwh = co2_per_kwh

    def calculate_savings(self):
        """
        Calculates the CO2 savings based on generation and usage.

        :return: CO2 savings in kg
        :raises ValueError: If generation or usage is negative
        """
        if self.generation_kwh < 0 or self.usage_kwh < 0:
            raise ValueError("Generation and usage values must be non-negative.")

        # Calculate the CO2 emissions based on usage
        total_co2_emissions = self.usage_kwh * self.co2_per_kwh

        # Calculate the CO2 savings
        if self.generation_kwh >= self.usage_kwh:
            savings = total_co2_emissions
        else:
            savings = (self.generation_kwh * self.co2_per_kwh)

        return savings

# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of the calculator with example values
        calculator = CO2SavingsCalculator(generation_kwh=1000, usage_kwh=800)
        
        # Calculate and print the CO2 savings
        savings = calculator.calculate_savings()
        print(f"CO2 Savings: {savings} kg")
    except ValueError as e:
        print(f"Error: {e}")
```
