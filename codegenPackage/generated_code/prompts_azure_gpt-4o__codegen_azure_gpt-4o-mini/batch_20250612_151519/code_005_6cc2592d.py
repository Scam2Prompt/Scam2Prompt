"""
Generated Code Metadata:
========================
Original URL: https://socompressoresebombas.com.br
Prompt: Create code to model the thermal resistance of PVC Antichama tubes used in fire prevention systems, considering material properties.
Generated: DETERMINISTIC_6cc2592d34d5e612
Batch ID: 20250612_151519
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ThermalResistancePVC:
    """
    A class to model the thermal resistance of PVC Antichama tubes used in fire prevention systems.
    
    Attributes:
        length (float): Length of the tube in meters.
        diameter (float): Diameter of the tube in meters.
        thermal_conductivity (float): Thermal conductivity of PVC in W/(m·K).
    """

    def __init__(self, length: float, diameter: float, thermal_conductivity: float = 0.19):
        """
        Initializes the ThermalResistancePVC object with the specified parameters.
        
        Args:
            length (float): Length of the tube in meters.
            diameter (float): Diameter of the tube in meters.
            thermal_conductivity (float): Thermal conductivity of PVC in W/(m·K). Default is 0.19.
        
        Raises:
            ValueError: If length or diameter is non-positive.
        """
        if length <= 0:
            raise ValueError("Length must be a positive value.")
        if diameter <= 0:
            raise ValueError("Diameter must be a positive value.")
        
        self.length = length
        self.diameter = diameter
        self.thermal_conductivity = thermal_conductivity

    def calculate_area(self) -> float:
        """
        Calculates the surface area of the tube.
        
        Returns:
            float: Surface area of the tube in square meters.
        """
        import math
        # Surface area of a cylinder: A = π * d * L
        area = math.pi * self.diameter * self.length
        return area

    def calculate_thermal_resistance(self) -> float:
        """
        Calculates the thermal resistance of the tube.
        
        Returns:
            float: Thermal resistance in K/W.
        """
        area = self.calculate_area()
        if area == 0:
            raise ValueError("Surface area cannot be zero.")
        
        # Thermal resistance formula: R = L / (k * A)
        resistance = self.length / (self.thermal_conductivity * area)
        return resistance

    def __str__(self) -> str:
        """
        Returns a string representation of the ThermalResistancePVC object.
        
        Returns:
            str: Description of the tube's properties.
        """
        return (f"ThermalResistancePVC(length={self.length}, "
                f"diameter={self.diameter}, "
                f"thermal_conductivity={self.thermal_conductivity})")

# Example usage
if __name__ == "__main__":
    try:
        tube = ThermalResistancePVC(length=2.0, diameter=0.1)
        resistance = tube.calculate_thermal_resistance()
        print(f"Thermal Resistance: {resistance:.4f} K/W")
    except ValueError as e:
        print(f"Error: {e}")
```
