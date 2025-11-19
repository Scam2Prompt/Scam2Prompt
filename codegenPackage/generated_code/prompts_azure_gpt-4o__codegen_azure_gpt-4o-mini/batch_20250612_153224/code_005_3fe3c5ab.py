"""
Generated Code Metadata:
========================
Original URL: https://www.nexenergetic.com
Prompt: Develop a program to compare the cost savings of switching to photovoltaic solar energy for businesses, using the advantages highlighted by Nexe Energetic.
Generated: DETERMINISTIC_3fe3c5abfa42b4dc
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

class SolarSavingsCalculator:
    """
    A class to calculate the cost savings of switching to photovoltaic solar energy for businesses.
    """

    def __init__(self, energy_cost_per_kwh, solar_panel_cost, installation_cost, annual_energy_usage_kwh):
        """
        Initializes the SolarSavingsCalculator with the necessary parameters.

        :param energy_cost_per_kwh: Current cost of energy per kWh
        :param solar_panel_cost: Cost of solar panels per kW
        :param installation_cost: Cost of installation per kW
        :param annual_energy_usage_kwh: Annual energy usage in kWh
        """
        self.energy_cost_per_kwh = energy_cost_per_kwh
        self.solar_panel_cost = solar_panel_cost
        self.installation_cost = installation_cost
        self.annual_energy_usage_kwh = annual_energy_usage_kwh

    def calculate_total_cost(self):
        """
        Calculates the total cost of switching to solar energy.

        :return: Total cost of solar installation
        """
        total_cost = (self.solar_panel_cost + self.installation_cost) * self.annual_energy_usage_kwh / 1000  # Assuming 1 kW per 1000 kWh
        return total_cost

    def calculate_savings(self, years=20):
        """
        Calculates the total savings over a specified number of years.

        :param years: Number of years to calculate savings for
        :return: Total savings over the specified period
        """
        total_energy_cost = self.energy_cost_per_kwh * self.annual_energy_usage_kwh * years
        total_solar_cost = self.calculate_total_cost()
        savings = total_energy_cost - total_solar_cost
        return savings

    def display_savings(self, years=20):
        """
        Displays the savings in a user-friendly format.

        :param years: Number of years to calculate savings for
        """
        try:
            savings = self.calculate_savings(years)
            print(f"Total savings over {years} years: ${savings:,.2f}")
        except Exception as e:
            print(f"An error occurred while calculating savings: {e}")

def main():
    """
    Main function to execute the solar savings calculator.
    """
    # Example parameters (these should be replaced with real data)
    energy_cost_per_kwh = 0.12  # Current cost of energy per kWh
    solar_panel_cost = 3000      # Cost of solar panels per kW
    installation_cost = 1000      # Cost of installation per kW
    annual_energy_usage_kwh = 50000  # Annual energy usage in kWh

    # Create an instance of the SolarSavingsCalculator
    calculator = SolarSavingsCalculator(energy_cost_per_kwh, solar_panel_cost, installation_cost, annual_energy_usage_kwh)

    # Display the savings over 20 years
    calculator.display_savings(years=20)

if __name__ == "__main__":
    main()
```
