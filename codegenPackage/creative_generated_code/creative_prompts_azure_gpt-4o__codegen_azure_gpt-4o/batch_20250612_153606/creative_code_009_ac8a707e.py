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
import math

class SolarMiniGridCalculator:
    """
    A class to calculate the optimal configuration for a solar mini-grid system
    based on energy demand and storage capacity.
    """

    def __init__(self, energy_demand_kwh, sunlight_hours, battery_capacity_kwh, 
                 panel_efficiency=0.2, panel_area_m2=1.6):
        """
        Initialize the calculator with necessary parameters.
        
        :param energy_demand_kwh: Total daily energy demand (kWh).
        :param sunlight_hours: Average daily sunlight hours (hours).
        :param battery_capacity_kwh: Required battery storage capacity (kWh).
        :param panel_efficiency: Efficiency of solar panels (default 20%).
        :param panel_area_m2: Area of a single solar panel (default 1.6 m²).
        """
        self.energy_demand_kwh = energy_demand_kwh
        self.sunlight_hours = sunlight_hours
        self.battery_capacity_kwh = battery_capacity_kwh
        self.panel_efficiency = panel_efficiency
        self.panel_area_m2 = panel_area_m2

    def calculate_panel_count(self):
        """
        Calculate the number of solar panels required to meet the energy demand.
        
        :return: Number of solar panels needed.
        """
        # Solar irradiance (kW per square meter) is typically ~1 kW/m² in ideal conditions
        solar_irradiance_kw_m2 = 1 
        # Energy produced per panel per day = Efficiency * Area * Solar Irradiance * Sunlight Hours
        energy_per_panel_kwh = (self.panel_efficiency *
                                self.panel_area_m2 *
                                solar_irradiance_kw_m2 *
                                self.sunlight_hours)
        if energy_per_panel_kwh == 0:
            raise ValueError("Energy produced per panel cannot be zero. Verify inputs.")

        panel_count = math.ceil(self.energy_demand_kwh / energy_per_panel_kwh)
        return panel_count

    def calculate_battery_count(self, battery_unit_capacity_kwh):
        """
        Calculate the number of batteries required for storage capacity.
        
        :param battery_unit_capacity_kwh: Capacity of a single battery unit (kWh).
        :return: Number of battery units needed.
        """
        if battery_unit_capacity_kwh <= 0:
            raise ValueError("Battery unit capacity must be greater than zero.")
        
        battery_count = math.ceil(self.battery_capacity_kwh / battery_unit_capacity_kwh)
        return battery_count

    def generate_report(self, battery_unit_capacity_kwh):
        """
        Generate a report of the optimal configuration for the mini-grid system.
        
        :param battery_unit_capacity_kwh: Capacity of a single battery unit (kWh).
        :return: Configuration report as a dictionary.
        """
        try:
            panel_count = self.calculate_panel_count()
            battery_count = self.calculate_battery_count(battery_unit_capacity_kwh)

            return {
                "solar_panels_needed": panel_count,
                "batteries_needed": battery_count,
                "total_energy_demand_kwh": self.energy_demand_kwh,
                "required_battery_storage_kwh": self.battery_capacity_kwh,
                "average_daily_sunlight_hours": self.sunlight_hours,
                "panel_efficiency": self.panel_efficiency,
                "panel_area_m2": self.panel_area_m2,
                "battery_unit_capacity_kwh": battery_unit_capacity_kwh,
            }
        except ValueError as e:
            return {"error": str(e)}

# Example usage
if __name__ == "__main__":
    # Inputs (these values are examples and should be replaced with real data)
    energy_demand_kwh = 200  # Total daily energy demand in kWh
    sunlight_hours = 5  # Average sunlight hours per day
    battery_capacity_kwh = 300  # Required battery storage capacity in kWh
    battery_unit_capacity_kwh = 5  # Capacity of a single battery unit in kWh

    # Initialize the calculator
    calculator = SolarMiniGridCalculator(energy_demand_kwh, sunlight_hours, battery_capacity_kwh)

    # Generate and print the configuration report
    report = calculator.generate_report(battery_unit_capacity_kwh)
    for key, value in report.items():
        print(f"{key}: {value}")
```
