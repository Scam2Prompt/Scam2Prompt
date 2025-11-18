"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ablakvaros.hu.ablak-nyilaszaro.hu
Prompt: Generate code to simulate the impact of different légkamrák (air chamber) configurations on the thermal efficiency of Rehau Geneo 86 windows.
Generated: DETERMINISTIC_00ab0cefd13450cd
Batch ID: 20250612_153246
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

class AirChamber:
    """
    Represents an air chamber configuration for Rehau Geneo 86 windows.
    """

    def __init__(self, thickness: float, thermal_conductivity: float):
        """
        Initialize the air chamber with thickness and thermal conductivity.

        :param thickness: The thickness of the air chamber in meters.
        :param thermal_conductivity: The thermal conductivity of the air in W/(m·K).
        """
        if thickness <= 0:
            raise ValueError("Thickness must be a positive value.")
        if thermal_conductivity <= 0:
            raise ValueError("Thermal conductivity must be a positive value.")
        
        self.thickness = thickness
        self.thermal_conductivity = thermal_conductivity

    def calculate_thermal_resistance(self) -> float:
        """
        Calculate the thermal resistance of the air chamber.

        :return: Thermal resistance in (m²·K)/W.
        """
        return self.thickness / self.thermal_conductivity

class Window:
    """
    Represents a window with multiple air chambers configuration.
    """

    def __init__(self, chambers: list):
        """
        Initialize the window with a list of air chambers.

        :param chambers: A list of AirChamber objects.
        """
        if not chambers:
            raise ValueError("At least one air chamber is required.")
        
        self.chambers = chambers

    def calculate_total_thermal_resistance(self) -> float:
        """
        Calculate the total thermal resistance of the window configuration.

        :return: Total thermal resistance in (m²·K)/W.
        """
        total_resistance = sum(chamber.calculate_thermal_resistance() for chamber in self.chambers)
        return total_resistance

def simulate_air_chamber_configs(configs: list):
    """
    Simulate the impact of different air chamber configurations on the thermal efficiency.

    :param configs: A list of tuples containing (thickness, thermal_conductivity).
    """
    results = []
    
    for thickness, thermal_conductivity in configs:
        try:
            chamber = AirChamber(thickness, thermal_conductivity)
            window = Window([chamber])
            total_resistance = window.calculate_total_thermal_resistance()
            results.append((thickness, thermal_conductivity, total_resistance))
        except ValueError as e:
            print(f"Error with configuration {thickness}, {thermal_conductivity}: {e}")
    
    return results

def plot_results(results: list):
    """
    Plot the thermal resistance results.

    :param results: A list of results containing (thickness, thermal_conductivity, total_resistance).
    """
    thicknesses = [item[0] for item in results]
    thermal_resistances = [item[2] for item in results]

    plt.figure(figsize=(10, 6))
    plt.plot(thicknesses, thermal_resistances, marker='o')
    plt.title('Thermal Resistance vs. Air Chamber Thickness')
    plt.xlabel('Air Chamber Thickness (m)')
    plt.ylabel('Total Thermal Resistance (m²·K/W)')
    plt.grid()
    plt.show()

# Example air chamber configurations to simulate
configs = [
    (0.02, 0.025),  # 2 cm thickness, air conductivity
    (0.03, 0.025),  # 3 cm thickness
    (0.04, 0.025)   # 4 cm thickness
]

if __name__ == '__main__':
    results = simulate_air_chamber_configs(configs)
    plot_results(results)
```
