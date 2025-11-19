"""
Generated Code Metadata:
========================
Original URL: https://ledgerreclaim.com
Prompt: "Compare different types of building materials used in Russian construction, such as газобетон (aerated concrete), кирпич (brick), and клееный брус (glued laminated timber), from the perspective of ExpertStroy's material selection."
Generated: DETERMINISTIC_3660765ad383162b
Batch ID: 20250622_212633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

class BuildingMaterial:
    """
    A class to represent a building material and its properties.
    """

    def __init__(self, name, thermal_conductivity, compressive_strength, cost_per_m2):
        """
        Initializes a new building material.

        :param name: Name of the building material
        :param thermal_conductivity: Thermal conductivity (W/m·K)
        :param compressive_strength: Compressive strength (MPa)
        :param cost_per_m2: Cost per square meter (RUB)
        """
        self.name = name
        self.thermal_conductivity = thermal_conductivity
        self.compressive_strength = compressive_strength
        self.cost_per_m2 = cost_per_m2

    def __repr__(self):
        return f"{self.name}: Thermal Conductivity={self.thermal_conductivity}, Compressive Strength={self.compressive_strength}, Cost={self.cost_per_m2}"

def compare_materials(materials):
    """
    Compares different building materials based on their properties.

    :param materials: List of BuildingMaterial objects
    :return: DataFrame containing the comparison of materials
    """
    # Create a DataFrame from the materials list
    data = {
        'Material': [material.name for material in materials],
        'Thermal Conductivity (W/m·K)': [material.thermal_conductivity for material in materials],
        'Compressive Strength (MPa)': [material.compressive_strength for material in materials],
        'Cost per m² (RUB)': [material.cost_per_m2 for material in materials]
    }
    
    return pd.DataFrame(data)

def main():
    """
    Main function to execute the material comparison.
    """
    try:
        # Define building materials
        materials = [
            BuildingMaterial("Газобетон", 0.12, 5, 3000),
            BuildingMaterial("Кирпич", 0.7, 25, 4500),
            BuildingMaterial("Клееный брус", 0.15, 15, 6000)
        ]

        # Compare materials
        comparison_df = compare_materials(materials)

        # Display the comparison
        print("Building Materials Comparison:")
        print(comparison_df)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
