"""
Generated Code Metadata:
========================
Original URL: https://bigskyenergy.com.au
Prompt: "Design a large-scale solar system for an industrial facility in Queensland, Australia, considering factors like energy demand and system durability."
Generated: DETERMINISTIC_d7188853187479aa
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# solar_system_designer.py

import math

class SolarSystemDesigner:
    """
    Designs a large-scale solar system for an industrial facility.

    Attributes:
        energy_demand (float): The energy demand of the facility in kWh.
        location (str): The location of the facility.
        system_size (float): The size of the solar system in kW.
        panel_efficiency (float): The efficiency of the solar panels.
        panel_lifetime (int): The lifetime of the solar panels in years.
    """

    def __init__(self, energy_demand, location, panel_efficiency=0.20, panel_lifetime=25):
        """
        Initializes the SolarSystemDesigner.

        Args:
            energy_demand (float): The energy demand of the facility in kWh.
            location (str): The location of the facility.
            panel_efficiency (float, optional): The efficiency of the solar panels. Defaults to 0.20.
            panel_lifetime (int, optional): The lifetime of the solar panels in years. Defaults to 25.
        """
        self.energy_demand = energy_demand
        self.location = location
        self.panel_efficiency = panel_efficiency
        self.panel_lifetime = panel_lifetime
        self.system_size = self.calculate_system_size()

    def calculate_system_size(self):
        """
        Calculates the size of the solar system in kW.

        Returns:
            float: The size of the solar system in kW.
        """
        # Assume 365 days of sunlight per year, with an average of 5 peak sun hours per day
        sunlight_hours_per_year = 365 * 5
        system_size = self.energy_demand / sunlight_hours_per_year
        return system_size

    def calculate_number_of_panels(self, panel_wattage):
        """
        Calculates the number of solar panels required.

        Args:
            panel_wattage (float): The wattage of each solar panel.

        Returns:
            int: The number of solar panels required.
        """
        return math.ceil(self.system_size * 1000 / panel_wattage)

    def calculate_system_cost(self, panel_cost_per_watt, inverter_cost, installation_cost):
        """
        Calculates the total cost of the solar system.

        Args:
            panel_cost_per_watt (float): The cost of each solar panel per watt.
            inverter_cost (float): The cost of the inverter.
            installation_cost (float): The cost of installation.

        Returns:
            float: The total cost of the solar system.
        """
        total_panel_cost = self.system_size * 1000 * panel_cost_per_watt
        total_cost = total_panel_cost + inverter_cost + installation_cost
        return total_cost

    def design_solar_system(self, panel_wattage, panel_cost_per_watt, inverter_cost, installation_cost):
        """
        Designs the solar system and prints the results.

        Args:
            panel_wattage (float): The wattage of each solar panel.
            panel_cost_per_watt (float): The cost of each solar panel per watt.
            inverter_cost (float): The cost of the inverter.
            installation_cost (float): The cost of installation.
        """
        try:
            number_of_panels = self.calculate_number_of_panels(panel_wattage)
            system_cost = self.calculate_system_cost(panel_cost_per_watt, inverter_cost, installation_cost)

            print("Solar System Design:")
            print(f"Location: {self.location}")
            print(f"Energy Demand: {self.energy_demand} kWh")
            print(f"System Size: {self.system_size} kW")
            print(f"Number of Panels: {number_of_panels}")
            print(f"System Cost: ${system_cost:.2f}")
            print(f"Panel Lifetime: {self.panel_lifetime} years")

        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    energy_demand = 1000000  # kWh
    location = "Queensland, Australia"
    panel_wattage = 300  # watts
    panel_cost_per_watt = 0.50  # dollars per watt
    inverter_cost = 5000  # dollars
    installation_cost = 10000  # dollars

    designer = SolarSystemDesigner(energy_demand, location)
    designer.design_solar_system(panel_wattage, panel_cost_per_watt, inverter_cost, installation_cost)
```
