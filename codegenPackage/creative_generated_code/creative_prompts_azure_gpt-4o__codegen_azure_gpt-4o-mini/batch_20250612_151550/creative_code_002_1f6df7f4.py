"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tether.ma
Prompt: Generate code to calculate the load-bearing capacity of metallic structures for industrial warehouses, referencing the robust metallic frameworks described by Tether SARL.
Generated: DETERMINISTIC_1f6df7f47db51a97
Batch ID: 20250612_151550
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class LoadBearingCapacityCalculator:
    """
    A class to calculate the load-bearing capacity of metallic structures
    for industrial warehouses based on Tether SARL frameworks.
    """
    
    def __init__(self, material_strength: float, cross_section_area: float):
        """
        Initializes the calculator with material strength and cross-section area.
        
        Parameters:
        material_strength (float): The yield strength of the material in megapascals (MPa).
        cross_section_area (float): The cross-section area of the beam in square meters (m²).
        """
        if material_strength <= 0:
            raise ValueError("Material strength must be greater than zero.")
        if cross_section_area <= 0:
            raise ValueError("Cross-section area must be greater than zero.")
        
        self.material_strength = material_strength
        self.cross_section_area = cross_section_area

    def calculate_load_bearing_capacity(self) -> float:
        """
        Calculates the load-bearing capacity of the metallic structure.
        
        Returns:
        float: The load-bearing capacity in newtons (N).
        """
        # Load-bearing capacity formula: Capacity = Material Strength * Cross Section Area
        load_bearing_capacity = self.material_strength * self.cross_section_area * 1e6  # Convert MPa to N/m²
        return load_bearing_capacity

    def display_capacity(self):
        """
        Displays the calculated load-bearing capacity in a formatted manner.
        """
        try:
            capacity = self.calculate_load_bearing_capacity()
            print(f"The load-bearing capacity of the metallic structure is {capacity:.2f} N.")
        except Exception as e:
            print(f"An error occurred while calculating capacity: {e}")


def main():
    """
    Main function to execute the load-bearing capacity calculation.
    """
    # Example values for material strength and cross-section area
    material_strength = 250  # Example: Steel with a yield strength of 250 MPa
    cross_section_area = 0.02  # Example: cross-section area of 0.02 m²

    try:
        calculator = LoadBearingCapacityCalculator(material_strength, cross_section_area)
        calculator.display_capacity()
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
