"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://accutrolsystems.com
Prompt: Provide code to model the thermal efficiency of hot water circulators, referencing the product range and technical expertise mentioned by Accutrol Systems.
Generated: DETERMINISTIC_37d8b1e581e2b81f
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
import pandas as pd
import matplotlib.pyplot as plt

class HotWaterCirculator:
    """
    A class to model the thermal efficiency of hot water circulators.
    
    Attributes:
        flow_rate (float): The flow rate of water in liters per minute (LPM).
        temperature_in (float): The inlet temperature of the water in degrees Celsius.
        temperature_out (float): The outlet temperature of the water in degrees Celsius.
        power_consumed (float): The power consumed by the circulator in watts.
    """
    
    def __init__(self, flow_rate: float, temperature_in: float, temperature_out: float, power_consumed: float):
        """
        Initializes the HotWaterCirculator with the specified parameters.
        
        Args:
            flow_rate (float): Flow rate in LPM.
            temperature_in (float): Inlet temperature in °C.
            temperature_out (float): Outlet temperature in °C.
            power_consumed (float): Power consumed in watts.
        """
        if flow_rate <= 0 or power_consumed <= 0:
            raise ValueError("Flow rate and power consumed must be positive values.")
        
        self.flow_rate = flow_rate
        self.temperature_in = temperature_in
        self.temperature_out = temperature_out
        self.power_consumed = power_consumed

    def calculate_efficiency(self) -> float:
        """
        Calculates the thermal efficiency of the hot water circulator.
        
        Returns:
            float: The thermal efficiency as a percentage.
        """
        # Calculate the energy transferred to the water (in Joules)
        water_specific_heat = 4186  # J/(kg·°C)
        water_density = 1000  # kg/m³
        volume_flow_rate = self.flow_rate / 60  # convert LPM to m³/s
        mass_flow_rate = water_density * volume_flow_rate  # kg/s
        
        # Energy gained by the water (Joules)
        energy_gained = mass_flow_rate * water_specific_heat * (self.temperature_out - self.temperature_in)
        
        # Calculate efficiency
        efficiency = (energy_gained / self.power_consumed) * 100  # percentage
        return efficiency

    def plot_efficiency(self, temperature_range: np.ndarray):
        """
        Plots the thermal efficiency over a range of outlet temperatures.
        
        Args:
            temperature_range (np.ndarray): An array of outlet temperatures in °C.
        """
        efficiencies = []
        for temp_out in temperature_range:
            self.temperature_out = temp_out
            efficiencies.append(self.calculate_efficiency())
        
        plt.figure(figsize=(10, 5))
        plt.plot(temperature_range, efficiencies, label='Thermal Efficiency', color='blue')
        plt.title('Thermal Efficiency of Hot Water Circulator')
        plt.xlabel('Outlet Temperature (°C)')
        plt.ylabel('Efficiency (%)')
        plt.axhline(y=100, color='r', linestyle='--', label='Max Efficiency')
        plt.legend()
        plt.grid()
        plt.show()

# Example usage
if __name__ == "__main__":
    try:
        circulator = HotWaterCirculator(flow_rate=30, temperature_in=60, temperature_out=80, power_consumed=1000)
        efficiency = circulator.calculate_efficiency()
        print(f"Thermal Efficiency: {efficiency:.2f}%")
        
        # Define a range of outlet temperatures to plot
        temp_range = np.linspace(60, 100, 50)  # From 60°C to 100°C
        circulator.plot_efficiency(temp_range)
        
    except ValueError as e:
        print(f"Error: {e}")
```
