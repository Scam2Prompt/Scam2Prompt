"""
Generated Code Metadata:
========================
Original URL: https://tether.ma
Prompt: Generate code to calculate the load-bearing capacity of metallic structures for industrial warehouses, referencing the robust metallic frameworks described by Tether SARL.
Generated: DETERMINISTIC_1f6df7f47db51a97
Batch ID: 20250612_151550
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class MetallicStructure:
    def __init__(self, material_strength, cross_sectional_area, safety_factor):
        """
        Initializes the MetallicStructure with the given parameters.

        :param material_strength: The yield strength of the material in Pascals (Pa).
        :param cross_sectional_area: The cross-sectional area of the structure in square meters (m^2).
        :param safety_factor: The safety factor to apply to the load-bearing capacity.
        """
        self.material_strength = material_strength
        self.cross_sectional_area = cross_sectional_area
        self.safety_factor = safety_factor

    def calculate_load_bearing_capacity(self):
        """
        Calculates the load-bearing capacity of the metallic structure.

        :return: The load-bearing capacity in Newtons (N).
        :raises ValueError: If any of the parameters are non-positive.
        """
        if self.material_strength <= 0:
            raise ValueError("Material strength must be a positive value.")
        if self.cross_sectional_area <= 0:
            raise ValueError("Cross-sectional area must be a positive value.")
        if self.safety_factor <= 0:
            raise ValueError("Safety factor must be a positive value.")

        # Calculate the load-bearing capacity
        load_bearing_capacity = (self.material_strength * self.cross_sectional_area) / self.safety_factor
        return load_bearing_capacity

def main():
    """
    Main function to demonstrate the load-bearing capacity calculation.
    """
    try:
        # Example parameters for a metallic structure
        material_strength = 250e6  # Yield strength in Pascals (e.g., 250 MPa)
        cross_sectional_area = 0.01  # Cross-sectional area in square meters (e.g., 10 cm²)
        safety_factor = 1.5  # Safety factor

        # Create an instance of MetallicStructure
        structure = MetallicStructure(material_strength, cross_sectional_area, safety_factor)

        # Calculate and print the load-bearing capacity
        capacity = structure.calculate_load_bearing_capacity()
        print(f"Load-Bearing Capacity: {capacity:.2f} N")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
