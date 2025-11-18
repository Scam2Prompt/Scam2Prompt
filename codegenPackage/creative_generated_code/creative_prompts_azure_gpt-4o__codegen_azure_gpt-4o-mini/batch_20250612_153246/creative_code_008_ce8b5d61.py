"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://accutrolsystems.com
Prompt: Develop a Python script to calculate the cost savings of switching to solar water heaters, using assumptions based on the products and services described on the Accutrol Systems website.
Generated: DETERMINISTIC_ce8b5d61d2a7c718
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class SolarWaterHeaterCalculator:
    def __init__(self, current_usage, current_cost, solar_cost, installation_cost, lifespan_years):
        """
        Initialize the calculator with user parameters.

        :param current_usage: Annual hot water usage in kWh
        :param current_cost: Current cost of energy per kWh
        :param solar_cost: Annual cost of operating solar water heater
        :param installation_cost: Initial installation cost of solar water heater
        :param lifespan_years: Expected lifespan of the solar water heater in years
        """
        self.current_usage = current_usage
        self.current_cost = current_cost
        self.solar_cost = solar_cost
        self.installation_cost = installation_cost
        self.lifespan_years = lifespan_years

    def calculate_current_cost(self):
        """
        Calculate the current annual cost of heating water.

        :return: Annual cost of current water heating method
        """
        return self.current_usage * self.current_cost

    def calculate_solar_cost(self):
        """
        Calculate the total cost of using a solar water heater over its lifespan.

        :return: Total cost of solar water heating over lifespan
        """
        total_operating_cost = self.solar_cost * self.lifespan_years
        return self.installation_cost + total_operating_cost

    def calculate_savings(self):
        """
        Calculate the savings achieved by switching to a solar water heater.

        :return: Total savings over lifespan
        """
        total_current_cost = self.calculate_current_cost() * self.lifespan_years
        total_solar_cost = self.calculate_solar_cost()
        savings = total_current_cost - total_solar_cost
        return savings

def main():
    """
    Main function to execute the savings calculation based on user input.
    """
    try:
        # Assumed values for the calculations
        current_usage = 4000  # kWh per year
        current_cost = 0.12  # Cost per kWh in dollars
        solar_cost = 200  # Annual cost for solar water heater in dollars
        installation_cost = 5000  # Installation cost in dollars
        lifespan_years = 20  # Lifespan of the heater in years

        # Create an instance of the SolarWaterHeaterCalculator
        calculator = SolarWaterHeaterCalculator(
            current_usage,
            current_cost,
            solar_cost,
            installation_cost,
            lifespan_years
        )

        # Calculate and display the savings
        savings = calculator.calculate_savings()
        print(f"Total savings from switching to solar water heaters over {lifespan_years} years: ${savings:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
