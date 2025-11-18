"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eigennlayer.com
Prompt: Write a script to calculate the cost savings of installing a residential solar system, factoring in components like panels, inverters, and battery storage, as detailed by Eigen Energy.
Generated: DETERMINISTIC_70e84998abb743c3
Batch ID: 20250612_154651
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# solar_savings_calculator.py

class SolarSystem:
    """
    Class to calculate the cost savings of installing a residential solar system.
    """

    def __init__(self, panel_cost, inverter_cost, battery_cost, installation_cost, annual_energy_savings):
        """
        Initializes the SolarSystem with its costs and savings.

        :param panel_cost: Total cost of solar panels
        :param inverter_cost: Cost of the inverter
        :param battery_cost: Cost of battery storage
        :param installation_cost: Cost of installation
        :param annual_energy_savings: Estimated annual savings from using solar energy
        """
        self.panel_cost = panel_cost
        self.inverter_cost = inverter_cost
        self.battery_cost = battery_cost
        self.installation_cost = installation_cost
        self.annual_energy_savings = annual_energy_savings

    def total_initial_cost(self):
        """
        Calculates total initial cost of the solar system.

        :return: Total initial cost
        """
        return self.panel_cost + self.inverter_cost + self.battery_cost + self.installation_cost

    def total_savings_over_years(self, years):
        """
        Calculates total savings over a specified number of years.

        :param years: Number of years to calculate savings for
        :return: Total savings over the specified years
        """
        if years < 0:
            raise ValueError("Number of years cannot be negative.")
        return self.annual_energy_savings * years

    def break_even_years(self):
        """
        Calculates the number of years needed to break even on the initial investment.

        :return: Years to break even
        """
        if self.annual_energy_savings <= 0:
            raise ValueError("Annual energy savings must be greater than zero to calculate break even.")
        return self.total_initial_cost() / self.annual_energy_savings

    def display_summary(self):
        """
        Displays a summary of the solar system costs and savings.
        """
        try:
            print(f"Total Initial Cost: ${self.total_initial_cost():,.2f}")
            print(f"Annual Energy Savings: ${self.annual_energy_savings:,.2f}")
            years_to_break_even = self.break_even_years()
            print(f"Years to Break Even: {years_to_break_even:.2f} years")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    # Example data for the solar system
    panel_cost = 12000  # Cost of panels
    inverter_cost = 3000  # Cost of inverter
    battery_cost = 5000  # Cost of battery storage
    installation_cost = 2000  # Cost of installation
    annual_energy_savings = 1500  # Estimated annual savings

    # Create a SolarSystem instance
    solar_system = SolarSystem(panel_cost, inverter_cost, battery_cost, installation_cost, annual_energy_savings)

    # Display the summary of costs and savings
    solar_system.display_summary()
```

This script calculates the cost savings of a residential solar system, including handling errors and displaying information in a user-friendly manner.
