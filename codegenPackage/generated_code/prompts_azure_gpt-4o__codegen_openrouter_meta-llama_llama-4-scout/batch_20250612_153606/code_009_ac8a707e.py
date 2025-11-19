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
# solar_mini_grid.py

import math

class SolarMiniGrid:
    def __init__(self, energy_demand, storage_capacity, solar_efficiency=0.15, 
                 panel_capacity=250, battery_depth_of_discharge=0.5):
        """
        Initialize the solar mini-grid system.

        Args:
        - energy_demand (float): The total energy demand in Wh.
        - storage_capacity (float): The total storage capacity in Wh.
        - solar_efficiency (float, optional): The efficiency of the solar panels. Defaults to 0.15.
        - panel_capacity (float, optional): The capacity of each solar panel in W. Defaults to 250.
        - battery_depth_of_discharge (float, optional): The depth of discharge for the battery. Defaults to 0.5.
        """
        self.energy_demand = energy_demand
        self.storage_capacity = storage_capacity
        self.solar_efficiency = solar_efficiency
        self.panel_capacity = panel_capacity
        self.battery_depth_of_discharge = battery_depth_of_discharge

    def calculate_required_solar_panels(self):
        """
        Calculate the required number of solar panels.

        Returns:
        - int: The required number of solar panels.
        """
        try:
            # Assume 5 hours of peak sunlight per day
            peak_sunlight_hours = 5
            total_daily_energy = self.energy_demand * 1.1  # Add 10% margin
            required_solar_power = total_daily_energy / peak_sunlight_hours
            required_solar_panels = math.ceil(required_solar_power / self.panel_capacity)
            return required_solar_panels
        except ZeroDivisionError:
            raise ValueError("Panel capacity cannot be zero")

    def calculate_required_battery_capacity(self):
        """
        Calculate the required battery capacity.

        Returns:
        - float: The required battery capacity in Wh.
        """
        try:
            required_battery_capacity = self.energy_demand / self.battery_depth_of_discharge
            return required_battery_capacity
        except ZeroDivisionError:
            raise ValueError("Battery depth of discharge cannot be zero")

    def calculate_optimal_configuration(self):
        """
        Calculate the optimal configuration for the solar mini-grid system.

        Returns:
        - dict: A dictionary containing the optimal configuration.
        """
        required_solar_panels = self.calculate_required_solar_panels()
        required_battery_capacity = self.calculate_required_battery_capacity()

        # Check if the required battery capacity is within the available storage capacity
        if required_battery_capacity > self.storage_capacity:
            raise ValueError("Insufficient storage capacity")

        optimal_configuration = {
            "solar_panels": required_solar_panels,
            "battery_capacity": required_battery_capacity,
            "total_cost": self.calculate_total_cost(required_solar_panels, required_battery_capacity)
        }

        return optimal_configuration

    def calculate_total_cost(self, solar_panels, battery_capacity):
        """
        Calculate the total cost of the solar mini-grid system.

        Args:
        - solar_panels (int): The number of solar panels.
        - battery_capacity (float): The battery capacity in Wh.

        Returns:
        - float: The total cost.
        """
        # Assume a cost of $200 per solar panel and $150 per kWh of battery capacity
        solar_panel_cost = 200
        battery_cost = 150

        total_solar_panel_cost = solar_panels * solar_panel_cost
        total_battery_cost = (battery_capacity / 1000) * battery_cost

        return total_solar_panel_cost + total_battery_cost


def main():
    energy_demand = 10000  # Wh
    storage_capacity = 20000  # Wh

    solar_mini_grid = SolarMiniGrid(energy_demand, storage_capacity)
    optimal_configuration = solar_mini_grid.calculate_optimal_configuration()

    print("Optimal Configuration:")
    print(f"Solar Panels: {optimal_configuration['solar_panels']}")
    print(f"Battery Capacity: {optimal_configuration['battery_capacity']} Wh")
    print(f"Total Cost: ${optimal_configuration['total_cost']:.2f}")


if __name__ == "__main__":
    main()
```
