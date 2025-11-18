"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://socompressoresebombas.com.br
Prompt: Create code to model the thermal resistance of PVC Antichama tubes used in fire prevention systems, considering material properties.
Generated: DETERMINISTIC_6cc2592d34d5e612
Batch ID: 20250612_151519
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np

class PVC_Antichama_Tube:
    """
    A class to model the thermal resistance of PVC Antichama tubes used in fire prevention systems.
    """

    def __init__(self, diameter: float, length: float, thermal_conductivity: float):
        """
        Initialize the PVC Antichama Tube properties.

        Parameters:
        diameter (float): Outer diameter of the tube in meters.
        length (float): Length of the tube in meters.
        thermal_conductivity (float): Thermal conductivity of PVC in W/(m·K).

        Raises:
        ValueError: If any input parameter is non-positive.
        """
        if diameter <= 0:
            raise ValueError("Diameter must be a positive value.")
        if length <= 0:
            raise ValueError("Length must be a positive value.")
        if thermal_conductivity <= 0:
            raise ValueError("Thermal conductivity must be a positive value.")

        self.diameter = diameter
        self.length = length
        self.thermal_conductivity = thermal_conductivity

    def thermal_resistance(self) -> float:
        """
        Calculate the thermal resistance of the PVC Antichama tube.

        The formula used is:
        R = L / (k * A)
        where:
        R = thermal resistance (K/W)
        L = length of the tube (m)
        k = thermal conductivity (W/(m·K))
        A = surface area of the tube (m²)

        Returns:
        float: The thermal resistance in K/W.
        """
        # Calculate the surface area of the cylindrical tube
        area = np.pi * self.diameter * self.length
        
        # Calculate thermal resistance
        resistance = self.length / (self.thermal_conductivity * area)
        return resistance

def main():
    """
    Main function to demonstrate the usage of PVC_Antichama_Tube class.
    """
    try:
        # Example parameters: diameter = 0.1 m, length = 2 m, thermal conductivity = 0.19 W/(m·K)
        tube = PVC_Antichama_Tube(diameter=0.1, length=2, thermal_conductivity=0.19)
        resistance = tube.thermal_resistance()
        print(f"Thermal Resistance of the PVC Antichama tube: {resistance:.4f} K/W")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
