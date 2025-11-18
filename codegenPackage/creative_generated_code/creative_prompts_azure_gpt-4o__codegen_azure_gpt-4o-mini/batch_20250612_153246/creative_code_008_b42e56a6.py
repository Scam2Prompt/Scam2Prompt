"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://engenhariawpj.com
Prompt: Write code to simulate the thermal performance of a building using StoTherm systems, referencing the insulation properties described on the Engenharia WPJ website.
Generated: DETERMINISTIC_b42e56a6bbebc513
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

class BuildingThermalSimulation:
    """
    A class to simulate the thermal performance of a building using StoTherm systems.
    
    Attributes:
        insulation_thickness (float): Thickness of the insulation layer in meters.
        thermal_conductivity (float): Thermal conductivity of the insulation material in W/(m·K).
        indoor_temperature (float): Indoor temperature in degrees Celsius.
        outdoor_temperature (float): Outdoor temperature in degrees Celsius.
        area (float): Surface area of the building in square meters.
    """

    def __init__(self, insulation_thickness: float, thermal_conductivity: float, 
                 indoor_temperature: float, outdoor_temperature: float, area: float):
        """
        Initializes the BuildingThermalSimulation with the given parameters.
        
        Parameters:
            insulation_thickness (float): Thickness of insulation (m).
            thermal_conductivity (float): Thermal conductivity (W/(m·K)).
            indoor_temperature (float): Indoor temperature (°C).
            outdoor_temperature (float): Outdoor temperature (°C).
            area (float): Surface area of the building (m²).
        """
        self.insulation_thickness = insulation_thickness
        self.thermal_conductivity = thermal_conductivity
        self.indoor_temperature = indoor_temperature
        self.outdoor_temperature = outdoor_temperature
        self.area = area

    def calculate_heat_transfer(self) -> float:
        """
        Calculates the heat transfer through the insulation using Fourier's law.
        
        Returns:
            float: Heat transfer in Watts.
        """
        try:
            # Calculate the temperature difference
            delta_T = self.indoor_temperature - self.outdoor_temperature
            
            # Calculate heat transfer using Fourier's law: Q = (k * A * ΔT) / d
            heat_transfer = (self.thermal_conductivity * self.area * delta_T) / self.insulation_thickness
            
            return heat_transfer
        
        except ZeroDivisionError:
            print("Error: Insulation thickness cannot be zero.")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None

    def simulate(self, time_period: int):
        """
        Simulates the thermal performance over a specified time period.
        
        Parameters:
            time_period (int): The time period for the simulation in hours.
        """
        heat_transfers = []
        for hour in range(time_period):
            # In a real-world scenario, adjust indoor/outdoor temperatures dynamically
            heat_transfer = self.calculate_heat_transfer()
            heat_transfers.append(heat_transfer)
        
        self.plot_results(heat_transfers)

    def plot_results(self, heat_transfers):
        """
        Plots the heat transfer results over time.
        
        Parameters:
            heat_transfers (list): List of heat transfer values over time.
        """
        try:
            plt.figure(figsize=(10, 5))
            plt.plot(heat_transfers, label='Heat Transfer (W)', color='blue')
            plt.title('Building Thermal Performance Simulation')
            plt.xlabel('Time (hours)')
            plt.ylabel('Heat Transfer (W)')
            plt.legend()
            plt.grid()
            plt.show()
        
        except Exception as e:
            print(f"Error while plotting results: {e}")

# Example usage:
if __name__ == "__main__":
    # Constants based on StoTherm systems and Engenharia WPJ
    insulation_thickness = 0.1  # meters
    thermal_conductivity = 0.035  # W/(m·K)
    indoor_temperature = 22  # °C
    outdoor_temperature = 5  # °C
    area = 150  # m²

    # Create a simulation instance
    building_simulation = BuildingThermalSimulation(insulation_thickness, thermal_conductivity, 
                                                   indoor_temperature, outdoor_temperature, area)

    # Run the simulation for 24 hours
    building_simulation.simulate(time_period=24)
```
