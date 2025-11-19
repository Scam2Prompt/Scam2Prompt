"""
Generated Code Metadata:
========================
Original URL: https://ablakvaros.hu.ablak-nyilaszaro.hu
Prompt: Generate code to simulate the impact of different légkamrák (air chamber) configurations on the thermal efficiency of Rehau Geneo 86 windows.
Generated: DETERMINISTIC_00ab0cefd13450cd
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import matplotlib.pyplot as plt

class Window:
    """
    A class to represent a Rehau Geneo 86 window and its thermal efficiency.
    """

    def __init__(self, area, u_value, air_chamber_config):
        """
        Initialize the window with area, U-value, and air chamber configuration.

        :param area: Area of the window in square meters.
        :param u_value: U-value of the window in W/m²K.
        :param air_chamber_config: List of air chamber configurations (thickness in mm).
        """
        self.area = area
        self.u_value = u_value
        self.air_chamber_config = air_chamber_config

    def calculate_thermal_efficiency(self):
        """
        Calculate the thermal efficiency based on the U-value and area.

        :return: Thermal efficiency in Watts.
        """
        return self.u_value * self.area

    def simulate_efficiency(self):
        """
        Simulate the impact of different air chamber configurations on thermal efficiency.

        :return: List of thermal efficiencies for each configuration.
        """
        efficiencies = []
        for chamber in self.air_chamber_config:
            # Adjust U-value based on air chamber thickness (simplified model)
            adjusted_u_value = self.u_value * (1 - (chamber / 1000) * 0.1)
            self.u_value = max(adjusted_u_value, 0)  # Ensure U-value does not go negative
            efficiencies.append(self.calculate_thermal_efficiency())
        return efficiencies

def plot_efficiency(air_chamber_config, efficiencies):
    """
    Plot the thermal efficiency against air chamber configurations.

    :param air_chamber_config: List of air chamber configurations.
    :param efficiencies: List of calculated thermal efficiencies.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(air_chamber_config, efficiencies, marker='o')
    plt.title('Thermal Efficiency vs Air Chamber Configuration')
    plt.xlabel('Air Chamber Thickness (mm)')
    plt.ylabel('Thermal Efficiency (W)')
    plt.grid()
    plt.xticks(air_chamber_config)
    plt.show()

def main():
    """
    Main function to execute the simulation.
    """
    try:
        # Define window parameters
        window_area = 1.5  # in square meters
        initial_u_value = 1.2  # in W/m²K
        air_chamber_config = [20, 30, 40, 50, 60]  # in mm

        # Create a Window instance
        window = Window(window_area, initial_u_value, air_chamber_config)

        # Simulate thermal efficiencies
        efficiencies = window.simulate_efficiency()

        # Plot the results
        plot_efficiency(air_chamber_config, efficiencies)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
