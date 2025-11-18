"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://karenfixing.com
Prompt: Write code to simulate the thermal insulation properties of "رانر آلومینیومی دوبل پایه دار خام" in a dry facade system, using Karen Fixing's product data.
Generated: DETERMINISTIC_093b2bb847a4b238
Batch ID: 20250612_153224
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

class ThermalInsulationSimulator:
    """
    A class to simulate the thermal insulation properties of 
    'رانر آلومینیومی دوبل پایه دار خام' in a dry facade system.
    """

    def __init__(self, thermal_conductivity, thickness, area):
        """
        Initializes the simulator with thermal conductivity,
        thickness of the insulation material, and area of the facade.
        
        :param thermal_conductivity: Thermal conductivity of the material (W/m·K)
        :param thickness: Thickness of the insulation (meters)
        :param area: Area of the facade (square meters)
        """
        self.thermal_conductivity = thermal_conductivity
        self.thickness = thickness
        self.area = area
        
    def calculate_heat_transfer(self, delta_temp):
        """
        Calculate the heat transfer through the insulation using Fourier's law.
        
        :param delta_temp: Temperature difference across the material (K)
        :return: Heat transfer rate (W)
        """
        try:
            if self.thickness <= 0:
                raise ValueError("Thickness must be greater than zero.")
            if delta_temp < 0:
                raise ValueError("Temperature difference must be non-negative.")
            
            # Calculate heat transfer rate (Q = k * A * ΔT / d)
            heat_transfer_rate = (self.thermal_conductivity * self.area * delta_temp) / self.thickness
            return heat_transfer_rate
            
        except ValueError as e:
            print(f"Error: {e}")
            return None

    def plot_heat_transfer(self, temperature_differences):
        """
        Plot heat transfer rates for given temperature differences.
        
        :param temperature_differences: List of temperature differences (K)
        """
        heat_transfer_rates = []

        for delta_temp in temperature_differences:
            rate = self.calculate_heat_transfer(delta_temp)
            if rate is not None:
                heat_transfer_rates.append(rate)

        plt.figure(figsize=(10, 6))
        plt.plot(temperature_differences, heat_transfer_rates, marker='o')
        plt.title('Heat Transfer Rate vs Temperature Difference')
        plt.xlabel('Temperature Difference (K)')
        plt.ylabel('Heat Transfer Rate (W)')
        plt.grid(True)
        plt.axhline(0, color='gray', lw=0.5, ls='--')
        plt.axvline(0, color='gray', lw=0.5, ls='--')
        plt.show()

# Example usage
if __name__ == "__main__":
    # Define properties for the aluminum runner insulation
    thermal_conductivity = 205  # W/m·K (typical value for aluminum)
    thickness = 0.005  # 5 mm
    area = 1.0  # 1 square meter

    # Create a simulator instance
    simulator = ThermalInsulationSimulator(thermal_conductivity, thickness, area)

    # Simulate heat transfer for a range of temperature differences
    temperature_differences = np.linspace(0, 100, 10)  # from 0 to 100 K
    simulator.plot_heat_transfer(temperature_differences)
```
