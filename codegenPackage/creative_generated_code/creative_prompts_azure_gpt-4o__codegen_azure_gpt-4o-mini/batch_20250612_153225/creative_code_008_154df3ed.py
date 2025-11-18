"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aayraint.com
Prompt: Write a program to simulate the extrusion process for polypropylene yarn and PP spun-bound fabrics, incorporating the use of stainless steel wire mesh filters as described by Aayra International.
Generated: DETERMINISTIC_154df3ed2f47b07a
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

class ExtrusionProcess:
    """
    A class to simulate the extrusion process for polypropylene yarn and PP spun-bound fabrics.
    """
    
    def __init__(self, material_type: str, temperature: float, pressure: float, mesh_size: float):
        """
        Initialize the extrusion process parameters.
        
        Parameters:
        material_type (str): Type of material (either 'yarn' or 'fabric').
        temperature (float): Temperature in degrees Celsius.
        pressure (float): Pressure in bars.
        mesh_size (float): Size of the stainless steel wire mesh filter in microns.
        """
        self.material_type = material_type
        self.temperature = temperature
        self.pressure = pressure
        self.mesh_size = mesh_size

        if self.material_type not in ['yarn', 'fabric']:
            raise ValueError("Material type must be either 'yarn' or 'fabric'.")

    def extrusion_rate(self) -> float:
        """
        Calculate the extrusion rate based on the material type, temperature, and pressure.
        
        Returns:
        float: The calculated extrusion rate in kg/h.
        """
        if self.material_type == 'yarn':
            rate = (self.temperature * 0.1) + (self.pressure * 0.2)  # Example formula for yarn extrusion
        else:  # self.material_type == 'fabric'
            rate = (self.temperature * 0.15) + (self.pressure * 0.25)  # Example formula for fabric extrusion

        return rate

    def filter_efficiency(self) -> float:
        """
        Simulate the efficiency of the wire mesh filter.
        
        Returns:
        float: The calculated filter efficiency as a percentage.
        """
        if self.mesh_size < 10:
            efficiency = 98.0  # High efficiency for small mesh sizes
        elif 10 <= self.mesh_size <= 50:
            efficiency = 90.0  # Moderate efficiency for medium mesh sizes
        else:
            efficiency = 70.0  # Lower efficiency for larger mesh sizes

        return efficiency

    def run_simulation(self):
        """
        Run the extrusion simulation and print the results.
        """
        try:
            extrusion_rate = self.extrusion_rate()
            efficiency = self.filter_efficiency()

            print(f"Extrusion Rate for {self.material_type}: {extrusion_rate:.2f} kg/h")
            print(f"Filter Efficiency: {efficiency:.2f}%")

            self.plot_results(extrusion_rate, efficiency)

        except Exception as e:
            print(f"An error occurred during the simulation: {e}")

    def plot_results(self, extrusion_rate: float, efficiency: float):
        """
        Plot the results of the extrusion simulation.
        
        Parameters:
        extrusion_rate (float): The extrusion rate calculated.
        efficiency (float): The filter efficiency calculated.
        """
        categories = ['Extrusion Rate (kg/h)', 'Filter Efficiency (%)']
        values = [extrusion_rate, efficiency]

        plt.bar(categories, values, color=['blue', 'green'])
        plt.xlabel('Category')
        plt.ylabel('Value')
        plt.title('Extrusion Process Simulation Results')
        plt.ylim(0, max(values) + 10)  # Set Y-axis limit for better visibility
        plt.show()

if __name__ == "__main__":
    # Example usage of the ExtrusionProcess class
    try:
        extrusion = ExtrusionProcess(material_type='yarn', temperature=220, pressure=30, mesh_size=20)
        extrusion.run_simulation()
    except Exception as e:
        print(f"Failed to create ExtrusionProcess: {e}")
```
