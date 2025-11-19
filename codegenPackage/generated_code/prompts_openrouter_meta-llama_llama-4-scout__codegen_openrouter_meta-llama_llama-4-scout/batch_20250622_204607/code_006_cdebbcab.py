"""
Generated Code Metadata:
========================
Original URL: https://www.chicoelectric.com
Prompt: "Write a code to simulate the energy production and cost savings of a grid-positive solar generation system, like the one implemented at Butte College by Chico Electric."
Generated: DETERMINISTIC_cdebbcab621fa6f4
Batch ID: 20250622_204607
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# solar_generation_system.py

import numpy as np
import matplotlib.pyplot as plt

class SolarGenerationSystem:
    """
    Simulates the energy production and cost savings of a grid-positive solar generation system.

    Attributes:
        system_capacity (float): The total capacity of the solar generation system in kW.
        efficiency (float): The efficiency of the solar panels (default: 0.20).
        daily_irradiance (list): A list of daily irradiance values in kWh/m²/day.
        electricity_cost (float): The cost of electricity in $/kWh (default: 0.15).
        system_lifetime (int): The lifetime of the solar generation system in years (default: 25).
    """

    def __init__(self, system_capacity, efficiency=0.20, electricity_cost=0.15, system_lifetime=25):
        self.system_capacity = system_capacity
        self.efficiency = efficiency
        self.daily_irradiance = []
        self.electricity_cost = electricity_cost
        self.system_lifetime = system_lifetime

    def add_daily_irradiance(self, irradiance):
        """
        Adds a daily irradiance value to the system.

        Args:
            irradiance (float): The daily irradiance value in kWh/m²/day.
        """
        self.daily_irradiance.append(irradiance)

    def calculate_energy_production(self):
        """
        Calculates the total energy production of the solar generation system.

        Returns:
            float: The total energy production in kWh.
        """
        energy_production = 0
        for irradiance in self.daily_irradiance:
            energy_production += irradiance * self.system_capacity * self.efficiency
        return energy_production

    def calculate_cost_savings(self):
        """
        Calculates the total cost savings of the solar generation system.

        Returns:
            float: The total cost savings in $.
        """
        energy_production = self.calculate_energy_production()
        cost_savings = energy_production * self.electricity_cost
        return cost_savings

    def simulate_system(self, daily_irradiance_values):
        """
        Simulates the solar generation system over a period of time.

        Args:
            daily_irradiance_values (list): A list of daily irradiance values in kWh/m²/day.

        Returns:
            tuple: A tuple containing the total energy production and cost savings.
        """
        self.daily_irradiance = daily_irradiance_values
        energy_production = self.calculate_energy_production()
        cost_savings = self.calculate_cost_savings()
        return energy_production, cost_savings

    def plot_energy_production(self, daily_irradiance_values):
        """
        Plots the daily energy production of the solar generation system.

        Args:
            daily_irradiance_values (list): A list of daily irradiance values in kWh/m²/day.
        """
        daily_energy_production = [irradiance * self.system_capacity * self.efficiency for irradiance in daily_irradiance_values]
        plt.plot(daily_energy_production)
        plt.xlabel('Day')
        plt.ylabel('Energy Production (kWh)')
        plt.title('Daily Energy Production')
        plt.show()


def main():
    try:
        # Create a solar generation system with a capacity of 100 kW
        system = SolarGenerationSystem(100)

        # Generate random daily irradiance values for 365 days
        np.random.seed(0)
        daily_irradiance_values = np.random.uniform(5, 7, size=365)

        # Simulate the solar generation system
        energy_production, cost_savings = system.simulate_system(daily_irradiance_values)

        # Print the results
        print(f'Total Energy Production: {energy_production:.2f} kWh')
        print(f'Total Cost Savings: ${cost_savings:.2f}')

        # Plot the daily energy production
        system.plot_energy_production(daily_irradiance_values)

    except Exception as e:
        print(f'An error occurred: {e}')


if __name__ == '__main__':
    main()
```
