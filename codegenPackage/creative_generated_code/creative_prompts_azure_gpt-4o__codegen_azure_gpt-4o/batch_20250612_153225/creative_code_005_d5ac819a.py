"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tibvanboxtel.nl
Prompt: Write code to simulate the energy output of a solar panel system under both shaded and non-shaded conditions, using the Growatt and Enphase configurations detailed on Technische Installatiebedrijf van Boxtel's site.
Generated: DETERMINISTIC_d5ac819acab9594a
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class SolarPanelSystem:
    def __init__(self, name, efficiency, panel_area, sunlight_hours, shading_factor=1.0):
        """
        Initialize a solar panel system configuration.

        :param name: Name of the configuration (e.g., 'Growatt' or 'Enphase').
        :param efficiency: Efficiency of the solar panel system (e.g., 0.18 for 18%).
        :param panel_area: Total area of the solar panels in square meters.
        :param sunlight_hours: Average hours of sunlight per day.
        :param shading_factor: Fraction of energy output due to shading (default is 1.0 for no shading).
        """
        self.name = name
        self.efficiency = efficiency
        self.panel_area = panel_area
        self.sunlight_hours = sunlight_hours
        self.shading_factor = shading_factor

    def calculate_energy_output(self):
        """
        Calculate the daily energy output of the solar panel system in kilowatt-hours (kWh).

        :return: Energy output in kWh.
        """
        # Solar constant (average power of sunlight per square meter in kW)
        solar_constant = 1.0  # kW/m^2
        try:
            # Compute energy output
            energy_output = (
                self.panel_area
                * solar_constant
                * self.sunlight_hours
                * self.efficiency
                * self.shading_factor
            )
            return energy_output
        except Exception as e:
            # Handle unexpected errors
            print(f"Error calculating energy output for {self.name}: {e}")
            return 0.0

def simulate_solar_panel_systems():
    """
    Simulate energy output of Growatt and Enphase solar panel systems under shaded and non-shaded conditions.
    """
    # Define configurations for Growatt and Enphase systems
    configs = [
        SolarPanelSystem(name="Growatt Non-Shaded", efficiency=0.18, panel_area=20, sunlight_hours=5),
        SolarPanelSystem(name="Growatt Shaded", efficiency=0.18, panel_area=20, sunlight_hours=5, shading_factor=0.7),
        SolarPanelSystem(name="Enphase Non-Shaded", efficiency=0.22, panel_area=25, sunlight_hours=5),
        SolarPanelSystem(name="Enphase Shaded", efficiency=0.22, panel_area=25, sunlight_hours=5, shading_factor=0.8),
    ]

    # Simulate energy output for each configuration
    for config in configs:
        energy_output = config.calculate_energy_output()
        print(f"{config.name}: {energy_output:.2f} kWh/day")

if __name__ == "__main__":
    simulate_solar_panel_systems()
```
