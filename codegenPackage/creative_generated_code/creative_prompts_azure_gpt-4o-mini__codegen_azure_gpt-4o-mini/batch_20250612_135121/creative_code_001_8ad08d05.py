"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://id.stromkonto.net
Prompt: Write a code snippet to calculate CO2 savings based on kWh generation and usage as described in the Stromkonto documentation.
Generated: DETERMINISTIC_8ad08d0524d82571
Batch ID: 20250612_135121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CO2SavingsCalculator:
    """
    A class to calculate CO2 savings based on electricity generation
    and usage in kilowatt-hours (kWh).
    """

    CO2_EMISSION_FACTOR = 0.5  # kg CO2 emitted per kWh from traditional sources

    def __init__(self, generated_kwh: float, used_kwh: float):
        """
        Initializes the CO2SavingsCalculator with generated and used kWh.

        :param generated_kwh: The amount of energy generated in kWh.
        :param used_kwh: The amount of energy used in kWh.
        :raises ValueError: If generated_kwh or used_kwh is negative.
        """
        if generated_kwh < 0:
            raise ValueError("Generated kWh cannot be negative.")
        if used_kwh < 0:
            raise ValueError("Used kWh cannot be negative.")

        self.generated_kwh = generated_kwh
        self.used_kwh = used_kwh

    def calculate_savings(self) -> float:
        """
        Calculates the potential CO2 savings based on the difference
        between generated and used energy.

        :return: The CO2 savings in kilograms.
        """
        # Calculate the net energy generated
        net_generated_kwh = self.generated_kwh - self.used_kwh
        if net_generated_kwh < 0:
            return 0.0  # No savings if usage exceeds generation

        # Calculate CO2 savings based on the net generated energy
        savings = net_generated_kwh * self.CO2_EMISSION_FACTOR
        return savings

# Example usage:
if __name__ == "__main__":
    try:
        # Replace these values with actual kWh data
        generated_kwh = 1200.0  # Example: 1200 kWh generated
        used_kwh = 800.0        # Example: 800 kWh used

        # Initialize the calculator
        co2_calculator = CO2SavingsCalculator(generated_kwh, used_kwh)

        # Calculate and print CO2 savings
        savings = co2_calculator.calculate_savings()
        print(f"CO2 Savings: {savings:.2f} kg")
    except ValueError as e:
        print(f"Error: {e}")
```
