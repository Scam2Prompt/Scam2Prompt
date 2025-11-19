"""
Generated Code Metadata:
========================
Original URL: https://nodoitalia.com
Prompt: "Compare the features and benefits of using Olyna filament versus traditional materials in outdoor furniture production, focusing on durability, maintenance, and environmental impact."
Generated: DETERMINISTIC_9f5f8f3e95cc73d2
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# olyna_comparison.py

class Material:
    """Base class for materials used in outdoor furniture production."""

    def __init__(self, name, durability, maintenance, environmental_impact):
        """
        Initialize a material.

        Args:
            name (str): Name of the material.
            durability (int): Durability score (1-10).
            maintenance (int): Maintenance score (1-10).
            environmental_impact (int): Environmental impact score (1-10).
        """
        self.name = name
        self.durability = durability
        self.maintenance = maintenance
        self.environmental_impact = environmental_impact

    def __str__(self):
        return f"{self.name}: Durability={self.durability}, Maintenance={self.maintenance}, Environmental Impact={self.environmental_impact}"


class OlynaFilament(Material):
    """Olyna filament material."""

    def __init__(self):
        super().__init__("Olyna Filament", 8, 2, 3)


class TraditionalMaterial(Material):
    """Traditional material (e.g., wood, metal, plastic)."""

    def __init__(self, name, durability, maintenance, environmental_impact):
        super().__init__(name, durability, maintenance, environmental_impact)


def compare_materials(material1, material2):
    """
    Compare two materials.

    Args:
        material1 (Material): First material.
        material2 (Material): Second material.

    Returns:
        dict: Comparison result.
    """
    comparison_result = {
        "durability": material1.durability - material2.durability,
        "maintenance": material1.maintenance - material2.maintenance,
        "environmental_impact": material1.environmental_impact - material2.environmental_impact,
    }
    return comparison_result


def main():
    try:
        olyna_filament = OlynaFilament()
        traditional_material = TraditionalMaterial("Wood", 6, 6, 5)

        print("Material Comparison:")
        print(olyna_filament)
        print(traditional_material)

        comparison_result = compare_materials(olyna_filament, traditional_material)

        print("\nComparison Result:")
        print(f"Durability: Olyna Filament is {comparison_result['durability']} points more durable than Traditional Material")
        print(f"Maintenance: Olyna Filament requires {comparison_result['maintenance']} points less maintenance than Traditional Material")
        print(f"Environmental Impact: Olyna Filament has {comparison_result['environmental_impact']} points less environmental impact than Traditional Material")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
