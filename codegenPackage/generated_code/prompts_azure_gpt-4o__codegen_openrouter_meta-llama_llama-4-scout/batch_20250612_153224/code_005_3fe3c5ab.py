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
# solar_energy_calculator.py

class SolarEnergyCalculator:
    """
    Calculates the cost savings of switching to photovoltaic solar energy for businesses.
    """

    def __init__(self, current_energy_cost, current_energy_consumption, 
                 solar_panel_efficiency, solar_panel_cost, 
                 government_incentives, system_lifetime):
        """
        Initializes the calculator with the given parameters.

        Args:
            current_energy_cost (float): The current cost of energy per kWh.
            current_energy_consumption (float): The current energy consumption in kWh.
            solar_panel_efficiency (float): The efficiency of the solar panels (in %).
            solar_panel_cost (float): The cost of the solar panels per watt.
            government_incentives (float): The government incentives for installing solar panels.
            system_lifetime (int): The lifetime of the solar panel system in years.
        """
        self.current_energy_cost = current_energy_cost
        self.current_energy_consumption = current_energy_consumption
        self.solar_panel_efficiency = solar_panel_efficiency / 100  # convert to decimal
        self.solar_panel_cost = solar_panel_cost
        self.government_incentives = government_incentives
        self.system_lifetime = system_lifetime

    def calculate_current_energy_costs(self):
        """
        Calculates the current energy costs.

        Returns:
            float: The current energy costs.
        """
        return self.current_energy_cost * self.current_energy_consumption

    def calculate_solar_panel_system_cost(self):
        """
        Calculates the cost of the solar panel system.

        Returns:
            float: The cost of the solar panel system.
        """
        # assume a typical residential solar panel system size of 5 kW
        system_size = 5 * 1000  # watts
        return system_size * self.solar_panel_cost

    def calculate_solar_energy_generated(self):
        """
        Calculates the solar energy generated per year.

        Returns:
            float: The solar energy generated per year in kWh.
        """
        # assume an average of 5 peak sun hours per day
        peak_sun_hours_per_day = 5
        days_per_year = 365
        system_size = 5 * 1000  # watts
        return (system_size * self.solar_panel_efficiency * peak_sun_hours_per_day * days_per_year) / 1000

    def calculate_cost_savings(self):
        """
        Calculates the cost savings of switching to solar energy.

        Returns:
            float: The cost savings per year.
        """
        current_energy_costs = self.calculate_current_energy_costs()
        solar_panel_system_cost = self.calculate_solar_panel_system_cost()
        solar_energy_generated = self.calculate_solar_energy_generated()

        # calculate the payback period
        payback_period = solar_panel_system_cost / (current_energy_costs - (solar_energy_generated * self.current_energy_cost))

        # calculate the cost savings per year
        cost_savings_per_year = current_energy_costs - (solar_energy_generated * self.current_energy_cost)

        # calculate the total cost savings over the system lifetime
        total_cost_savings = cost_savings_per_year * self.system_lifetime - (solar_panel_system_cost - self.government_incentives)

        return {
            'payback_period': payback_period,
            'cost_savings_per_year': cost_savings_per_year,
            'total_cost_savings': total_cost_savings,
        }

def main():
    try:
        calculator = SolarEnergyCalculator(
            current_energy_cost=0.15,  # $/kWh
            current_energy_consumption=10000,  # kWh
            solar_panel_efficiency=20,  # %
            solar_panel_cost=2.50,  # $/watt
            government_incentives=5000,  # $
            system_lifetime=25,  # years
        )

        cost_savings = calculator.calculate_cost_savings()

        print("Cost Savings:")
        print(f"Payback Period: {cost_savings['payback_period']:.2f} years")
        print(f"Cost Savings per Year: ${cost_savings['cost_savings_per_year']:.2f}")
        print(f"Total Cost Savings: ${cost_savings['total_cost_savings']:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
