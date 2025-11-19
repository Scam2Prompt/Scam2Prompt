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
# Import necessary libraries
import pandas as pd

# Define a class to represent building materials
class BuildingMaterial:
    def __init__(self, name, durability, thermal_insulation, cost, environmental_impact):
        """
        Initialize a BuildingMaterial object.

        :param name: Name of the material
        :param durability: Durability score (1-10)
        :param thermal_insulation: Thermal insulation score (1-10)
        :param cost: Cost per square meter (in USD)
        :param environmental_impact: Environmental impact score (1-10, lower is better)
        """
        self.name = name
        self.durability = durability
        self.thermal_insulation = thermal_insulation
        self.cost = cost
        self.environmental_impact = environmental_impact

    def to_dict(self):
        """
        Convert the material properties to a dictionary for easy comparison.

        :return: Dictionary representation of the material
        """
        return {
            "Name": self.name,
            "Durability": self.durability,
            "Thermal Insulation": self.thermal_insulation,
            "Cost (USD/m²)": self.cost,
            "Environmental Impact": self.environmental_impact,
        }

# Define a function to compare building materials
def compare_materials(materials):
    """
    Compare a list of building materials and display their properties in a tabular format.

    :param materials: List of BuildingMaterial objects
    """
    try:
        # Convert materials to a DataFrame for better visualization
        materials_data = [material.to_dict() for material in materials]
        df = pd.DataFrame(materials_data)

        # Display the comparison table
        print("Comparison of Building Materials:")
        print(df)
    except Exception as e:
        print(f"An error occurred while comparing materials: {e}")

# Create instances of BuildingMaterial for different materials
aerated_concrete = BuildingMaterial(
    name="Газобетон (Aerated Concrete)",
    durability=7,
    thermal_insulation=8,
    cost=30,
    environmental_impact=6,
)

brick = BuildingMaterial(
    name="Кирпич (Brick)",
    durability=9,
    thermal_insulation=6,
    cost=50,
    environmental_impact=7,
)

glued_laminated_timber = BuildingMaterial(
    name="Клееный брус (Glued Laminated Timber)",
    durability=8,
    thermal_insulation=9,
    cost=70,
    environmental_impact=4,
)

# Compare the materials
materials = [aerated_concrete, brick, glued_laminated_timber]
compare_materials(materials)
```

This code is ready to run in a Python environment with the `pandas` library installed. It compares the specified building materials based on durability, thermal insulation, cost, and environmental impact, displaying the results in a tabular format.
