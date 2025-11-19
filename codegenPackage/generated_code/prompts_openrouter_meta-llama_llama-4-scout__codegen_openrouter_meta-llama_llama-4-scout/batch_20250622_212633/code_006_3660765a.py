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
# material_selector.py

class BuildingMaterial:
    """Base class for building materials."""

    def __init__(self, name, density, thermal_conductivity, compressive_strength, cost):
        """
        Initialize a building material.

        Args:
            name (str): Material name.
            density (float): Material density in kg/m³.
            thermal_conductivity (float): Material thermal conductivity in W/m·K.
            compressive_strength (float): Material compressive strength in MPa.
            cost (float): Material cost in RUB/m³.
        """
        self.name = name
        self.density = density
        self.thermal_conductivity = thermal_conductivity
        self.compressive_strength = compressive_strength
        self.cost = cost

    def __str__(self):
        return f"{self.name}: density={self.density} kg/m³, thermal conductivity={self.thermal_conductivity} W/m·K, compressive strength={self.compressive_strength} MPa, cost={self.cost} RUB/m³"


class AeratedConcrete(BuildingMaterial):
    """Aerated concrete (газобетон) material."""

    def __init__(self, density=500, thermal_conductivity=0.12, compressive_strength=3, cost=3000):
        super().__init__("Газобетон (Aerated Concrete)", density, thermal_conductivity, compressive_strength, cost)


class Brick(BuildingMaterial):
    """Brick (кирпич) material."""

    def __init__(self, density=1800, thermal_conductivity=0.7, compressive_strength=10, cost=8000):
        super().__init__("Кирпич (Brick)", density, thermal_conductivity, compressive_strength, cost)


class GluedLaminatedTimber(BuildingMaterial):
    """Glued laminated timber (клееный брус) material."""

    def __init__(self, density=500, thermal_conductivity=0.13, compressive_strength=5, cost=12000):
        super().__init__("Клееный Брус (Glued Laminated Timber)", density, thermal_conductivity, compressive_strength, cost)


class ExpertStroy:
    """ExpertStroy material selection."""

    def __init__(self):
        self.materials = []

    def add_material(self, material):
        """Add a material to the selection."""
        self.materials.append(material)

    def compare_materials(self):
        """Compare materials based on their characteristics."""
        print("Material Comparison:")
        for material in self.materials:
            print(material)

        # Compare materials by density
        print("\nDensity Comparison:")
        densities = {material.name: material.density for material in self.materials}
        print(densities)

        # Compare materials by thermal conductivity
        print("\nThermal Conductivity Comparison:")
        thermal_conductivities = {material.name: material.thermal_conductivity for material in self.materials}
        print(thermal_conductivities)

        # Compare materials by compressive strength
        print("\nCompressive Strength Comparison:")
        compressive_strengths = {material.name: material.compressive_strength for material in self.materials}
        print(compressive_strengths)

        # Compare materials by cost
        print("\nCost Comparison:")
        costs = {material.name: material.cost for material in self.materials}
        print(costs)

        try:
            # Determine the most cost-effective material
            most_cost_effective_material = min(self.materials, key=lambda material: material.cost / material.compressive_strength)
            print(f"\nThe most cost-effective material is: {most_cost_effective_material.name}")
        except Exception as e:
            print(f"An error occurred: {e}")


def main():
    expert_stroy = ExpertStroy()

    aerated_concrete = AeratedConcrete()
    brick = Brick()
    glued_laminated_timber = GluedLaminatedTimber()

    expert_stroy.add_material(aerated_concrete)
    expert_stroy.add_material(brick)
    expert_stroy.add_material(glued_laminated_timber)

    expert_stroy.compare_materials()


if __name__ == "__main__":
    main()
```
