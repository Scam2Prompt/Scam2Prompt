"""
Generated Code Metadata:
========================
Original URL: https://imbcg.com
Prompt: Write a program to calculate the optimal configuration for a solar mini-grid system, using metrics like energy demand and storage capacity, as discussed by IMB Cambodia Group.
Generated: DETERMINISTIC_ac8a707e9412999f
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np

class SolarMiniGrid:
    def __init__(self, energy_demand_kwh, storage_capacity_kwh, solar_panel_capacity_kw, hours_of_sunlight):
        """
        Initialize the SolarMiniGrid system with the required parameters.

        :param energy_demand_kwh: Total energy demand in kilowatt-hours (kWh)
        :param storage_capacity_kwh: Total storage capacity in kilowatt-hours (kWh)
        :param solar_panel_capacity_kw: Capacity of solar panels in kilowatts (kW)
        :param hours_of_sunlight: Average hours of sunlight per day
        """
        self.energy_demand_kwh = energy_demand_kwh
        self.storage_capacity_kwh = storage_capacity_kwh
        self.solar_panel_capacity_kw = solar_panel_capacity_kw
        self.hours_of_sunlight = hours_of_sunlight

    def calculate_daily_energy_production(self):
        """
        Calculate the daily energy production from the solar panels.

        :return: Daily energy production in kilowatt-hours (kWh)
        """
        return self.solar_panel_capacity_kw * self.hours_of_sunlight

    def calculate_days_of_autonomy(self):
        """
        Calculate the number of days the system can operate without additional solar input.

        :return: Number of days of autonomy
        """
        if self.energy_demand_kwh <= 0:
            raise ValueError("Energy demand must be greater than zero.")
        return self.storage_capacity_kwh / self.energy_demand_kwh

    def calculate_optimal_configuration(self):
        """
        Calculate the optimal configuration for the solar mini-grid system.

        :return: A dictionary containing daily energy production, days of autonomy, and configuration recommendations
        """
        daily_energy_production = self.calculate_daily_energy_production()
        days_of_autonomy = self.calculate_days_of_autonomy()

        # Configuration recommendations based on production and demand
        recommendations = {
            "Daily Energy Production (kWh)": daily_energy_production,
            "Days of Autonomy": days_of_autonomy,
            "Is Configuration Optimal": daily_energy_production >= self.energy_demand_kwh
        }

        return recommendations

def main():
    """
    Main function to execute the solar mini-grid configuration calculation.
    """
    try:
        # Example parameters for the solar mini-grid system
        energy_demand_kwh = 30  # Total energy demand in kWh
        storage_capacity_kwh = 60  # Total storage capacity in kWh
        solar_panel_capacity_kw = 5  # Capacity of solar panels in kW
        hours_of_sunlight = 5  # Average hours of sunlight per day

        # Create an instance of SolarMiniGrid
        mini_grid = SolarMiniGrid(energy_demand_kwh, storage_capacity_kwh, solar_panel_capacity_kw, hours_of_sunlight)

        # Calculate the optimal configuration
        optimal_config = mini_grid.calculate_optimal_configuration()

        # Print the results
        print("Optimal Configuration for Solar Mini-Grid:")
        for key, value in optimal_config.items():
            print(f"{key}: {value}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
