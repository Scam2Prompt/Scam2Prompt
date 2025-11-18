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
import numpy as np
import matplotlib.pyplot as plt

class SolarPanelSystem:
    def __init__(self, panel_area, efficiency, shading_factor=1.0):
        """
        Initializes the solar panel system with the given parameters.

        :param panel_area: Total area of the solar panel system in square meters.
        :param efficiency: Efficiency of the solar panels, as a decimal (e.g., 0.18 for 18%).
        :param shading_factor: Factor by which the output is reduced due to shading (1.0 = no shading).
        """
        self.panel_area = panel_area
        self.efficiency = efficiency
        self.shading_factor = shading_factor

    def calculate_energy_output(self, solar_irradiance, hours):
        """
        Calculates the energy output of the solar panel system.

        :param solar_irradiance: Solar irradiance in W/m².
        :param hours: Number of sunlight hours.
        :return: Energy output in kWh.
        """
        if solar_irradiance < 0 or hours < 0:
            raise ValueError("Solar irradiance and hours must be non-negative.")

        # Calculate the energy output in watt-hours
        energy_output_wh = solar_irradiance * self.panel_area * self.efficiency * self.shading_factor * hours
        
        # Convert to kilowatt-hours
        return energy_output_wh / 1000  # kWh

def simulate_solar_panel_systems():
    # Define constants for the simulation
    SOLAR_IRRADIANCE = 1000  # W/m² (standard test conditions)
    HOURS_OF_SUNLIGHT = 5     # Average hours of sunlight per day

    # Growatt configuration
    growatt_panel_system = SolarPanelSystem(panel_area=40, efficiency=0.18)

    # Enphase configuration
    enphase_panel_system = SolarPanelSystem(panel_area=30, efficiency=0.20, shading_factor=0.85)

    # Calculate energy outputs
    growatt_output = growatt_panel_system.calculate_energy_output(SOLAR_IRRADIANCE, HOURS_OF_SUNLIGHT)
    enphase_output = enphase_panel_system.calculate_energy_output(SOLAR_IRRADIANCE, HOURS_OF_SUNLIGHT)

    # Print results
    print(f"Growatt Energy Output: {growatt_output:.2f} kWh")
    print(f"Enphase Energy Output: {enphase_output:.2f} kWh")

    # Visualization
    labels = ['Growatt', 'Enphase']
    outputs = [growatt_output, enphase_output]

    plt.bar(labels, outputs, color=['blue', 'green'])
    plt.ylabel('Energy Output (kWh)')
    plt.title('Energy Output of Solar Panel Systems')
    plt.ylim(0, max(outputs) + 1)
    plt.show()

if __name__ == "__main__":
    try:
        simulate_solar_panel_systems()
    except Exception as e:
        print(f"An error occurred: {e}")
```
