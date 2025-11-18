"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sctoll.io
Prompt: Write code to analyze the thermal properties of T304 stainless steel exhaust kits, referencing Brixton Forged™'s exhaust system specifications.
Generated: DETERMINISTIC_cbb25a4b82520048
Batch ID: 20250612_151057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class ThermalPropertiesAnalyzer:
    """
    A class to analyze thermal properties of T304 stainless steel exhaust kits.
    """

    def __init__(self, material_properties):
        """
        Initializes the analyzer with material properties.
        
        Args:
            material_properties (dict): A dictionary containing thermal properties.
        """
        self.material_properties = material_properties

    def calculate_heat_capacity(self, temperature_range):
        """
        Calculate heat capacity over a given temperature range.
        
        Args:
            temperature_range (np.ndarray): An array of temperatures in Celsius.
        
        Returns:
            np.ndarray: Corresponding heat capacities for the given temperatures.
        """
        # Assuming a linear relationship for demonstration
        heat_capacity = self.material_properties['specific_heat'] * temperature_range
        return heat_capacity

    def calculate_conductivity(self, temperature_range):
        """
        Calculate thermal conductivity over a given temperature range.
        
        Args:
            temperature_range (np.ndarray): An array of temperatures in Celsius.
        
        Returns:
            np.ndarray: Corresponding thermal conductivities for the given temperatures.
        """
        # Assuming a linear decrease of conductivity with temperature
        conductivity = self.material_properties['thermal_conductivity'] - 0.01 * temperature_range
        return conductivity

    def plot_properties(self, temperature_range):
        """
        Plot the heat capacity and thermal conductivity against temperature.
        
        Args:
            temperature_range (np.ndarray): An array of temperatures in Celsius.
        """
        try:
            heat_capacity = self.calculate_heat_capacity(temperature_range)
            conductivity = self.calculate_conductivity(temperature_range)

            plt.figure(figsize=(14, 6))

            # Plot heat capacity
            plt.subplot(1, 2, 1)
            plt.plot(temperature_range, heat_capacity, label='Heat Capacity (J/kg·K)', color='blue')
            plt.title('Heat Capacity vs Temperature')
            plt.xlabel('Temperature (°C)')
            plt.ylabel('Heat Capacity (J/kg·K)')
            plt.grid(True)
            plt.legend()

            # Plot thermal conductivity
            plt.subplot(1, 2, 2)
            plt.plot(temperature_range, conductivity, label='Thermal Conductivity (W/m·K)', color='red')
            plt.title('Thermal Conductivity vs Temperature')
            plt.xlabel('Temperature (°C)')
            plt.ylabel('Thermal Conductivity (W/m·K)')
            plt.grid(True)
            plt.legend()

            plt.tight_layout()
            plt.show()

        except Exception as e:
            print(f"An error occurred while plotting properties: {e}")

def main():
    """
    Main function to run the thermal properties analysis.
    """
    # Material properties for T304 stainless steel (example values)
    t304_properties = {
        'specific_heat': 500,  # J/kg·K
        'thermal_conductivity': 16,  # W/m·K
    }

    # Temperature range for analysis
    temperature_range = np.linspace(0, 1000, 100)  # from 0°C to 1000°C

    # Create an analyzer instance
    analyzer = ThermalPropertiesAnalyzer(t304_properties)

    # Plot the thermal properties
    analyzer.plot_properties(temperature_range)

if __name__ == "__main__":
    main()
```
