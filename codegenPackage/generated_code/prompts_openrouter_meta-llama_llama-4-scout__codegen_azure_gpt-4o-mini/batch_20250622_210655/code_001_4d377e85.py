"""
Generated Code Metadata:
========================
Original URL: https://powerfivesolar.com
Prompt: Write a Python script to calculate the potential savings on utility bills by switching to solar energy for a residential property.
Generated: DETERMINISTIC_4d377e8511e9c93e
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

class SolarSavingsCalculator:
    def __init__(self, monthly_bill, solar_panel_cost, solar_panel_lifespan, energy_production_per_panel):
        """
        Initialize the SolarSavingsCalculator with the necessary parameters.

        :param monthly_bill: Average monthly utility bill in dollars
        :param solar_panel_cost: Cost of one solar panel in dollars
        :param solar_panel_lifespan: Lifespan of the solar panels in years
        :param energy_production_per_panel: Energy produced by one solar panel in kWh per month
        """
        self.monthly_bill = monthly_bill
        self.solar_panel_cost = solar_panel_cost
        self.solar_panel_lifespan = solar_panel_lifespan
        self.energy_production_per_panel = energy_production_per_panel

    def calculate_panels_needed(self):
        """
        Calculate the number of solar panels needed to cover the monthly utility bill.

        :return: Number of solar panels needed
        """
        # Assuming an average cost of $0.13 per kWh
        average_cost_per_kwh = 0.13
        monthly_energy_needed = self.monthly_bill / average_cost_per_kwh
        panels_needed = monthly_energy_needed / self.energy_production_per_panel
        return panels_needed

    def calculate_total_cost(self, panels_needed):
        """
        Calculate the total cost of installing the solar panels.

        :param panels_needed: Number of solar panels needed
        :return: Total installation cost
        """
        return panels_needed * self.solar_panel_cost

    def calculate_savings(self, panels_needed):
        """
        Calculate the total savings over the lifespan of the solar panels.

        :param panels_needed: Number of solar panels needed
        :return: Total savings over the lifespan of the solar panels
        """
        total_savings = self.monthly_bill * 12 * self.solar_panel_lifespan
        total_cost = self.calculate_total_cost(panels_needed)
        return total_savings - total_cost

    def run(self):
        """
        Execute the savings calculation and print the results.
        """
        try:
            panels_needed = self.calculate_panels_needed()
            total_cost = self.calculate_total_cost(panels_needed)
            total_savings = self.calculate_savings(panels_needed)

            print(f"Panels Needed: {panels_needed:.2f}")
            print(f"Total Installation Cost: ${total_cost:.2f}")
            print(f"Total Savings Over {self.solar_panel_lifespan} Years: ${total_savings:.2f}")

        except Exception as e:
            print(f"An error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    # Example parameters
    monthly_bill = 150  # Average monthly utility bill in dollars
    solar_panel_cost = 300  # Cost of one solar panel in dollars
    solar_panel_lifespan = 25  # Lifespan of the solar panels in years
    energy_production_per_panel = 350  # Energy produced by one solar panel in kWh per month

    calculator = SolarSavingsCalculator(monthly_bill, solar_panel_cost, solar_panel_lifespan, energy_production_per_panel)
    calculator.run()
```
