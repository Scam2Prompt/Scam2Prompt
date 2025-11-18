"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aprisacv.com.mx
Prompt: Write a Python program to simulate heat transfer in a furnace wall using Aprisacv's ceramic paper (ApriPaper) as insulation, based on its thickness and thermal properties.
Generated: DETERMINISTIC_d72e751bcb655798
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class FurnaceWallSimulation:
    """
    A class to simulate heat transfer through a furnace wall using Aprisacv's ceramic paper (ApriPaper) as insulation.
    """
    
    def __init__(self, thickness, thermal_conductivity, area, temperature_inside, temperature_outside):
        """
        Initialize the simulation parameters.
        
        :param thickness: Thickness of the insulation (meters).
        :param thermal_conductivity: Thermal conductivity of the insulation material (W/mK).
        :param area: Surface area of the furnace wall (square meters).
        :param temperature_inside: Temperature inside the furnace (Kelvin).
        :param temperature_outside: Temperature outside the furnace (Kelvin).
        """
        self.thickness = thickness
        self.thermal_conductivity = thermal_conductivity
        self.area = area
        self.temperature_inside = temperature_inside
        self.temperature_outside = temperature_outside

    def calculate_heat_transfer(self):
        """
        Calculate the heat transfer through the furnace wall using Fourier's law.
        
        Fourier’s law formula: Q = (k * A * ΔT) / d
        Where:
        Q = Heat transfer rate (Watts)
        k = Thermal conductivity (W/mK)
        A = Area of the wall (m^2)
        ΔT = Temperature difference (Kelvin)
        d = Thickness of the insulation (m)
        
        :return: Heat transfer rate in Watts.
        """
        try:
            delta_temp = abs(self.temperature_inside - self.temperature_outside)  # Absolute temperature difference
            heat_transfer_rate = (self.thermal_conductivity * self.area * delta_temp) / self.thickness
            return heat_transfer_rate
        except ZeroDivisionError:
            # Handle case where thickness is zero
            raise ValueError("Insulation thickness cannot be zero.")
        except Exception as e:
            # Handle other unexpected errors
            raise RuntimeError(f"An error occurred during calculation: {e}")

def main():
    """
    Main function to run the furnace wall heat transfer simulation.
    """
    print("Welcome to the Furnace Wall Heat Transfer Simulation!")
    
    try:
        # User-provided input
        thickness = float(input("Enter the insulation thickness (meters): "))
        thermal_conductivity = float(input("Enter the thermal conductivity of ApriPaper (W/mK): "))
        area = float(input("Enter the surface area of the furnace wall (m^2): "))
        temperature_inside = float(input("Enter the temperature inside the furnace (Kelvin): "))
        temperature_outside = float(input("Enter the temperature outside the furnace (Kelvin): "))
        
        # Create a simulation instance
        simulation = FurnaceWallSimulation(thickness, thermal_conductivity, area, temperature_inside, temperature_outside)
        
        # Calculate the heat transfer rate
        heat_transfer_rate = simulation.calculate_heat_transfer()
        
        print(f"\nHeat Transfer Rate: {heat_transfer_rate:.2f} Watts")
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except RuntimeError as re:
        print(f"Runtime Error: {re}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
```
