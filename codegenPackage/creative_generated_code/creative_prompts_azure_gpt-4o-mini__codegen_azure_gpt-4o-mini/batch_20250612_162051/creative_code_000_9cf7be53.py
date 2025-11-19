"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.nexenergetic.com
Prompt: Write a Python script that calculates the potential savings from implementing residential solar energy autoconsumption based on the information provided by Nexe Energetic.
Generated: DETERMINISTIC_9cf7be530e5a619e
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class SolarSavingsCalculator:
    def __init__(self, electricity_cost_per_kwh, solar_panel_output_kwh, daily_consumption_kwh, days_in_year=365):
        """
        Initialize the SolarSavingsCalculator with necessary parameters.

        :param electricity_cost_per_kwh: Cost of electricity per kilowatt-hour
        :param solar_panel_output_kwh: Daily output of solar panels in kilowatt-hours
        :param daily_consumption_kwh: Daily electricity consumption in kilowatt-hours
        :param days_in_year: Number of days in the year (default is 365)
        """
        self.electricity_cost_per_kwh = self.validate_positive_float(electricity_cost_per_kwh)
        self.solar_panel_output_kwh = self.validate_positive_float(solar_panel_output_kwh)
        self.daily_consumption_kwh = self.validate_positive_float(daily_consumption_kwh)
        self.days_in_year = days_in_year

    @staticmethod
    def validate_positive_float(value):
        """
        Validate that the input value is a positive float.

        :param value: Value to validate
        :return: Validated float value
        :raises ValueError: If the value is not a positive float
        """
        try:
            value = float(value)
            if value < 0:
                raise ValueError("Value must be a positive number.")
            return value
        except ValueError as e:
            raise ValueError(f"Invalid input: {e}")

    def calculate_annual_savings(self):
        """
        Calculate the annual savings from solar energy autoconsumption.

        :return: Estimated annual savings in currency
        """
        # Calculate daily savings based on the minimum of daily solar output and daily consumption
        daily_savings = min(self.solar_panel_output_kwh, self.daily_consumption_kwh) * self.electricity_cost_per_kwh

        # Total annual savings
        annual_savings = daily_savings * self.days_in_year
        return annual_savings

def main():
    """
    Main function to run the Solar Savings Calculator.
    """
    try:
        # Input parameters
        electricity_cost_per_kwh = float(input("Enter the electricity cost per kWh: "))
        solar_panel_output_kwh = float(input("Enter the daily solar panel output in kWh: "))
        daily_consumption_kwh = float(input("Enter the daily electricity consumption in kWh: "))

        # Initialize the calculator
        calculator = SolarSavingsCalculator(electricity_cost_per_kwh, solar_panel_output_kwh, daily_consumption_kwh)

        # Calculate savings
        savings = calculator.calculate_annual_savings()
        print(f"Estimated annual savings from solar energy autoconsumption: ${savings:.2f}")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
