"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imbcg.com
Prompt: Write a program to calculate the optimal configuration for a solar mini-grid system, using metrics like energy demand and storage capacity, as discussed by IMB Cambodia Group.
Generated: DETERMINISTIC_ac8a707e9412999f
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np

class SolarMiniGrid:
    """
    A class to represent a solar mini-grid system configuration.
    """

    def __init__(self, energy_demand_kwh, storage_capacity_kwh, solar_panel_efficiency=0.15, hours_of_sunlight=5):
        """
        Initializes the SolarMiniGrid object.

        :param energy_demand_kwh: Total daily energy demand in kilowatt-hours (kWh).
        :param storage_capacity_kwh: Storage capacity of the battery in kilowatt-hours (kWh).
        :param solar_panel_efficiency: Efficiency of the solar panels (default is 15%).
        :param hours_of_sunlight: Average hours of sunlight per day (default is 5 hours).
        """
        self.energy_demand_kwh = energy_demand_kwh
        self.storage_capacity_kwh = storage_capacity_kwh
        self.solar_panel_efficiency = solar_panel_efficiency
        self.hours_of_sunlight = hours_of_sunlight

    def calculate_required_solar_panels(self):
        """
        Calculates the number of solar panels required to meet the daily energy demand.

        :return: Number of solar panels needed.
        """
        # Assume average solar panel generates 300W
        panel_output_kw = 0.3  # 300W in kW
        daily_solar_generation_kwh = panel_output_kw * self.hours_of_sunlight

        # Calculate the required number of solar panels
        panels_needed = np.ceil(self.energy_demand_kwh / daily_solar_generation_kwh)
        return int(panels_needed)

    def calculate_battery_capacity(self):
        """
        Calculates the optimal battery capacity based on energy demand and storage capacity.

        :return: Recommended battery capacity in kWh.
        """
        # Optimal battery capacity should at least cover the daily demand
        # Consider the maximum storage capacity
        optimal_capacity = min(self.energy_demand_kwh, self.storage_capacity_kwh)
        return optimal_capacity

    def suggest_configuration(self):
        """
        Suggests the optimal configuration for the solar mini-grid system.

        :return: A dictionary containing the configuration details.
        """
        try:
            panels_needed = self.calculate_required_solar_panels()
            battery_capacity = self.calculate_battery_capacity()

            configuration = {
                "Required Solar Panels": panels_needed,
                "Recommended Battery Capacity": battery_capacity
            }
            return configuration

        except Exception as e:
            print(f"An error occurred while calculating configuration: {e}")
            return None


if __name__ == "__main__":
    # Example usage
    energy_demand = 30  # Daily energy demand in kWh
    storage_capacity = 20  # Storage capacity in kWh

    mini_grid = SolarMiniGrid(energy_demand, storage_capacity)
    configuration = mini_grid.suggest_configuration()

    if configuration:
        print("Optimal Solar Mini-Grid Configuration:")
        for key, value in configuration.items():
            print(f"{key}: {value}")
```
