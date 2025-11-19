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
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class SolarEnergySystem:
    """
    A class to simulate the energy production and cost savings of a grid-positive solar generation system.
    """

    def __init__(self, panel_capacity_kw, efficiency, installation_cost_per_kw, electricity_rate_per_kwh):
        """
        Initializes the solar energy system with the given parameters.

        :param panel_capacity_kw: Total capacity of the solar panels in kilowatts (kW)
        :param efficiency: Efficiency of the solar panels (0 to 1)
        :param installation_cost_per_kw: Installation cost per kilowatt (in dollars)
        :param electricity_rate_per_kwh: Rate of electricity (in dollars per kilowatt-hour)
        """
        self.panel_capacity_kw = panel_capacity_kw
        self.efficiency = efficiency
        self.installation_cost_per_kw = installation_cost_per_kw
        self.electricity_rate_per_kwh = electricity_rate_per_kwh
        self.total_installation_cost = self.calculate_installation_cost()

    def calculate_installation_cost(self):
        """
        Calculates the total installation cost of the solar energy system.

        :return: Total installation cost in dollars
        """
        return self.panel_capacity_kw * self.installation_cost_per_kw

    def simulate_energy_production(self, days=365, sunlight_hours=5):
        """
        Simulates the energy production over a specified number of days.

        :param days: Number of days to simulate
        :param sunlight_hours: Average sunlight hours per day
        :return: DataFrame containing daily energy production in kWh
        """
        try:
            daily_energy_production_kwh = self.panel_capacity_kw * sunlight_hours * self.efficiency
            energy_production = np.full(days, daily_energy_production_kwh)
            return pd.DataFrame({'Day': np.arange(1, days + 1), 'Energy_Produced_kWh': energy_production})
        except Exception as e:
            print(f"Error in simulating energy production: {e}")
            return None

    def calculate_cost_savings(self, energy_production_df):
        """
        Calculates the cost savings based on the energy produced.

        :param energy_production_df: DataFrame containing daily energy production
        :return: Total cost savings in dollars
        """
        try:
            energy_production_df['Cost_Savings'] = energy_production_df['Energy_Produced_kWh'] * self.electricity_rate_per_kwh
            total_savings = energy_production_df['Cost_Savings'].sum()
            return total_savings
        except Exception as e:
            print(f"Error in calculating cost savings: {e}")
            return None

    def plot_energy_production(self, energy_production_df):
        """
        Plots the energy production over the simulated days.

        :param energy_production_df: DataFrame containing daily energy production
        """
        try:
            plt.figure(figsize=(12, 6))
            plt.plot(energy_production_df['Day'], energy_production_df['Energy_Produced_kWh'], label='Energy Produced (kWh)', color='green')
            plt.title('Daily Energy Production from Solar System')
            plt.xlabel('Day')
            plt.ylabel('Energy Produced (kWh)')
            plt.grid()
            plt.legend()
            plt.show()
        except Exception as e:
            print(f"Error in plotting energy production: {e}")

# Example usage
if __name__ == "__main__":
    # Parameters for the solar energy system
    panel_capacity_kw = 100  # 100 kW system
    efficiency = 0.18  # 18% efficiency
    installation_cost_per_kw = 3000  # $3000 per kW
    electricity_rate_per_kwh = 0.12  # $0.12 per kWh

    # Create an instance of the SolarEnergySystem
    solar_system = SolarEnergySystem(panel_capacity_kw, efficiency, installation_cost_per_kw, electricity_rate_per_kwh)

    # Simulate energy production for 365 days
    energy_production_df = solar_system.simulate_energy_production(days=365)

    # Calculate cost savings
    total_savings = solar_system.calculate_cost_savings(energy_production_df)
    print(f"Total Cost Savings over 365 days: ${total_savings:.2f}")

    # Plot the energy production
    solar_system.plot_energy_production(energy_production_df)
```
