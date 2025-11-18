"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://powerafricasolar.com
Prompt: Write Python code to calculate the energy savings from installing Power Africa Solar's PV panels, factoring in energy storage solutions and residential power demands.
Generated: DETERMINISTIC_404352a16e35f0d1
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime


class EnergySavingsCalculator:
    """
    A class to calculate energy savings from installing Power Africa Solar's PV panels.
    Includes energy storage solutions and residential power demands.
    """

    def __init__(self, daily_power_demand, panel_output_per_day, storage_capacity, grid_cost_per_kwh):
        """
        Initializes the calculator with household and panel details.

        :param daily_power_demand: Average daily power demand of the household in kWh.
        :param panel_output_per_day: Daily output of the solar panels in kWh.
        :param storage_capacity: Energy storage capacity in kWh (e.g., battery storage systems).
        :param grid_cost_per_kwh: Cost of electricity per kWh from the grid in USD.
        """
        self.daily_power_demand = daily_power_demand
        self.panel_output_per_day = panel_output_per_day
        self.storage_capacity = storage_capacity
        self.grid_cost_per_kwh = grid_cost_per_kwh

    def calculate_savings(self):
        """
        Calculates energy savings based on power demand, solar generation, and storage.

        :return: Dictionary containing savings details.
        """
        # Ensure we do not exceed daily power demand or storage capacity
        usable_solar_energy = min(self.panel_output_per_day, self.daily_power_demand)
        stored_energy = min(usable_solar_energy, self.storage_capacity)

        # Calculate grid energy usage
        grid_energy_usage = max(0, self.daily_power_demand - (usable_solar_energy + stored_energy))

        # Compute savings
        grid_energy_cost = grid_energy_usage * self.grid_cost_per_kwh
        solar_savings = self.daily_power_demand * self.grid_cost_per_kwh - grid_energy_cost

        return {
            "Daily_Power_Demand_kWh": self.daily_power_demand,
            "Solar_Output_kWh": self.panel_output_per_day,
            "Usable_Solar_Energy_kWh": usable_solar_energy,
            "Stored_Energy_kWh": stored_energy,
            "Grid_Energy_Usage_kWh": grid_energy_usage,
            "Grid_Cost_USD": grid_energy_cost,
            "Solar_Savings_USD": solar_savings
        }


def main():
    """
    Main function to demonstrate the energy savings calculation.
    """
    try:
        # Example inputs
        daily_power_demand = 30  # in kWh
        panel_output_per_day = 25  # in kWh
        storage_capacity = 10  # in kWh
        grid_cost_per_kwh = 0.12  # in USD

        # Instantiate the calculator
        calculator = EnergySavingsCalculator(daily_power_demand, panel_output_per_day, storage_capacity, grid_cost_per_kwh)

        # Calculate savings
        savings = calculator.calculate_savings()

        # Print results
        print("Energy Savings Calculation:")
        for key, value in savings.items():
            print(f"{key}: {value}")
        
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
