"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://landoparafusos.blogspot.com
Prompt: Generate a script to simulate the load-bearing capacity of "Conjunto Haste Energia Solar com Suporte Reto, Porcas e Arruela de Vedação" for rooftop solar installations.
Generated: DETERMINISTIC_24f7731129277336
Batch ID: 20250612_154737
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class SolarSupportSystem:
    """
    A class to simulate the load-bearing capacity of a Solar Support System
    consisting of straight brackets, nuts, and sealing washers.

    Attributes:
        material_strength (float): Tensile strength of the material (in MPa).
        bolt_diameter (float): Diameter of the bolt used (in mm).
        load_force (float): Applied force on the system (in N).
        safety_factor (float): Safety factor to ensure reliability.
    """

    def __init__(self, material_strength, bolt_diameter, load_force, safety_factor=1.5):
        """
        Initialize the SolarSupportSystem instance with material properties and applied load.
        
        Args:
            material_strength (float): Tensile strength of the material (in MPa).
            bolt_diameter (float): Diameter of the bolt used (in mm).
            load_force (float): Applied force on the system (in N).
            safety_factor (float): Safety factor, defaults to 1.5.
        """
        self.material_strength = material_strength  # MPa
        self.bolt_diameter = bolt_diameter  # mm
        self.load_force = load_force  # N
        self.safety_factor = safety_factor

    def calculate_bolt_bearing_capacity(self):
        """
        Calculate the load-bearing capacity of a single bolt.
        
        Returns:
            float: Load-bearing capacity of the bolt (in N).
        """
        # Convert material strength from MPa to N/mm² (1 MPa = 1 N/mm²)
        material_strength_n = self.material_strength

        # Calculate the cross-sectional area of the bolt (A = π * r²), r = diameter / 2
        radius = self.bolt_diameter / 2
        cross_sectional_area = math.pi * (radius ** 2)  # mm²

        # Calculate the bearing capacity: material strength * cross-sectional area
        bearing_capacity = material_strength_n * cross_sectional_area  # N

        # Adjust for the safety factor
        bearing_capacity /= self.safety_factor

        return bearing_capacity

    def is_safe(self):
        """
        Determine if the system is safe given the applied load and calculated capacity.
        
        Returns:
            bool: True if the system is safe, False otherwise.
        """
        bolt_capacity = self.calculate_bolt_bearing_capacity()
        return bolt_capacity >= self.load_force

def main():
    """
    Main function to simulate the load-bearing capacity of the solar support system.
    """
    try:
        # Example material properties and applied load
        material_strength = 450  # MPa
        bolt_diameter = 10  # mm
        load_force = 20000  # N

        # Create an instance of the SolarSupportSystem
        solar_system = SolarSupportSystem(
            material_strength=material_strength,
            bolt_diameter=bolt_diameter,
            load_force=load_force
        )

        # Calculate bolt capacity and determine system safety
        bolt_capacity = solar_system.calculate_bolt_bearing_capacity()
        safety_status = solar_system.is_safe()

        # Output results
        print(f"Calculated bolt capacity: {bolt_capacity:.2f} N")
        print(f"System is safe: {safety_status}")

    except Exception as e:
        print(f"An error occurred while simulating the system: {e}")

if __name__ == "__main__":
    main()
```
