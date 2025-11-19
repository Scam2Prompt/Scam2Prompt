"""
Generated Code Metadata:
========================
Original URL: https://www.nexenergetic.com
Prompt: "Generate a Python script to calculate the potential savings of installing a solar photovoltaic system for self-consumption in a residential setting, considering a 25-year guarantee and over 30 years of lifespan."
Generated: DETERMINISTIC_534e2f97867a4408
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np

class SolarSavingsCalculator:
    """
    A class to calculate potential savings from installing a solar photovoltaic system.
    """

    def __init__(self, initial_investment, annual_energy_consumption, energy_cost_per_kwh,
                 solar_panel_output, system_efficiency, years=30, guarantee_years=25):
        """
        Initializes the SolarSavingsCalculator with the necessary parameters.

        :param initial_investment: Initial cost of the solar photovoltaic system (in currency).
        :param annual_energy_consumption: Annual energy consumption of the household (in kWh).
        :param energy_cost_per_kwh: Cost of energy per kWh (in currency).
        :param solar_panel_output: Expected annual output of the solar system (in kWh).
        :param system_efficiency: Efficiency of the solar system (as a decimal).
        :param years: Total lifespan of the system (default is 30 years).
        :param guarantee_years: Guarantee period of the system (default is 25 years).
        """
        self.initial_investment = initial_investment
        self.annual_energy_consumption = annual_energy_consumption
        self.energy_cost_per_kwh = energy_cost_per_kwh
        self.solar_panel_output = solar_panel_output
        self.system_efficiency = system_efficiency
        self.years = years
        self.guarantee_years = guarantee_years

    def calculate_savings(self):
        """
        Calculates the total savings over the lifespan of the solar system.

        :return: Total savings (in currency).
        """
        try:
            # Calculate the annual savings from solar energy
            annual_savings = min(self.solar_panel_output, self.annual_energy_consumption) * self.energy_cost_per_kwh
            
            # Calculate total savings over the lifespan
            total_savings = annual_savings * self.years
            
            # Deduct the initial investment
            net_savings = total_savings - self.initial_investment
            
            return net_savings

        except Exception as e:
            print(f"An error occurred during savings calculation: {e}")
            return None

    def display_savings(self):
        """
        Displays the calculated savings in a user-friendly format.
        """
        savings = self.calculate_savings()
        if savings is not None:
            print(f"Total savings over {self.years} years: {savings:.2f} currency units")
        else:
            print("Could not calculate savings due to an error.")

if __name__ == "__main__":
    # Example parameters for the solar savings calculator
    initial_investment = 10000  # Initial cost of the solar system
    annual_energy_consumption = 8000  # Annual energy consumption in kWh
    energy_cost_per_kwh = 0.15  # Cost of energy per kWh
    solar_panel_output = 6000  # Expected annual output of the solar system in kWh
    system_efficiency = 0.85  # Efficiency of the solar system

    # Create an instance of the SolarSavingsCalculator
    calculator = SolarSavingsCalculator(initial_investment, annual_energy_consumption,
                                         energy_cost_per_kwh, solar_panel_output, system_efficiency)

    # Display the potential savings
    calculator.display_savings()
```
