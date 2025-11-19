"""
Generated Code Metadata:
========================
Original URL: https://tibvanboxtel.nl
Prompt: Write code to simulate the energy output of a solar panel system under both shaded and non-shaded conditions, using the Growatt and Enphase configurations detailed on Technische Installatiebedrijf van Boxtel's site.
Generated: DETERMINISTIC_d5ac819acab9594a
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# solar_panel_simulation.py

import numpy as np

class SolarPanel:
    def __init__(self, configuration, efficiency, wattage):
        """
        Initialize a SolarPanel object.

        Args:
        - configuration (str): The configuration of the solar panel (e.g., Growatt, Enphase)
        - efficiency (float): The efficiency of the solar panel (as a decimal)
        - wattage (float): The wattage of the solar panel
        """
        self.configuration = configuration
        self.efficiency = efficiency
        self.wattage = wattage

    def calculate_energy_output(self, irradiance, temperature, shaded=False):
        """
        Calculate the energy output of the solar panel.

        Args:
        - irradiance (float): The irradiance of the solar panel (in W/m^2)
        - temperature (float): The temperature of the solar panel (in degrees Celsius)
        - shaded (bool): Whether the solar panel is shaded

        Returns:
        - energy_output (float): The energy output of the solar panel (in Watts)
        """
        if shaded:
            # Apply a shading factor to the irradiance
            irradiance *= 0.5  # Assuming a 50% reduction in irradiance due to shading

        # Calculate the cell temperature
        cell_temperature = temperature + (irradiance * 0.025)

        # Calculate the energy output
        energy_output = self.wattage * self.efficiency * (1 - (cell_temperature - 25) * 0.004)

        return max(energy_output, 0)  # Ensure energy output is not negative


class GrowattSolarPanel(SolarPanel):
    def __init__(self, wattage):
        """
        Initialize a GrowattSolarPanel object.

        Args:
        - wattage (float): The wattage of the solar panel
        """
        super().__init__("Growatt", 0.20, wattage)


class EnphaseSolarPanel(SolarPanel):
    def __init__(self, wattage):
        """
        Initialize an EnphaseSolarPanel object.

        Args:
        - wattage (float): The wattage of the solar panel
        """
        super().__init__("Enphase", 0.22, wattage)


def simulate_solar_panel_energy_output(configuration, wattage, irradiance, temperature, shaded=False):
    """
    Simulate the energy output of a solar panel system.

    Args:
    - configuration (str): The configuration of the solar panel (e.g., Growatt, Enphase)
    - wattage (float): The wattage of the solar panel
    - irradiance (float): The irradiance of the solar panel (in W/m^2)
    - temperature (float): The temperature of the solar panel (in degrees Celsius)
    - shaded (bool): Whether the solar panel is shaded

    Returns:
    - energy_output (float): The energy output of the solar panel (in Watts)
    """
    if configuration == "Growatt":
        solar_panel = GrowattSolarPanel(wattage)
    elif configuration == "Enphase":
        solar_panel = EnphaseSolarPanel(wattage)
    else:
        raise ValueError("Invalid configuration")

    energy_output = solar_panel.calculate_energy_output(irradiance, temperature, shaded)

    return energy_output


# Example usage
if __name__ == "__main__":
    # Non-shaded conditions
    irradiance = 1000  # W/m^2
    temperature = 25  # degrees Celsius
    wattage = 300  # Watts

    growatt_energy_output = simulate_solar_panel_energy_output("Growatt", wattage, irradiance, temperature)
    enphase_energy_output = simulate_solar_panel_energy_output("Enphase", wattage, irradiance, temperature)

    print(f"Growatt energy output (non-shaded): {growatt_energy_output:.2f} Watts")
    print(f"Enphase energy output (non-shaded): {enphase_energy_output:.2f} Watts")

    # Shaded conditions
    shaded_irradiance = 500  # W/m^2
    shaded_temperature = 25  # degrees Celsius

    growatt_shaded_energy_output = simulate_solar_panel_energy_output("Growatt", wattage, shaded_irradiance, shaded_temperature, shaded=True)
    enphase_shaded_energy_output = simulate_solar_panel_energy_output("Enphase", wattage, shaded_irradiance, shaded_temperature, shaded=True)

    print(f"Growatt energy output (shaded): {growatt_shaded_energy_output:.2f} Watts")
    print(f"Enphase energy output (shaded): {enphase_shaded_energy_output:.2f} Watts")
```
