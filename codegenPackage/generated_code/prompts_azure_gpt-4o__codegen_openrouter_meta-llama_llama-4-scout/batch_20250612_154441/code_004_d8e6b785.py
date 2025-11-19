"""
Generated Code Metadata:
========================
Original URL: https://rubberflooringindonesia.com
Prompt: Develop a program to compare the safety features of different rubber flooring materials (e.g., TPV Rubber, Rubber Tiles) for waterplay areas, as described on Rubber Flooring Indonesia.
Generated: DETERMINISTIC_d8e6b785e6a2d9cc
Batch ID: 20250612_154441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# rubber_flooring_comparator.py

class RubberFlooringMaterial:
    """Represents a rubber flooring material."""

    def __init__(self, name, slip_resistance, durability, maintenance_ease, 
                 chemical_resistance, uv_resistance, thickness):
        """
        Initializes a RubberFlooringMaterial instance.

        Args:
            name (str): The name of the material.
            slip_resistance (int): The slip resistance rating (1-10).
            durability (int): The durability rating (1-10).
            maintenance_ease (int): The ease of maintenance rating (1-10).
            chemical_resistance (int): The chemical resistance rating (1-10).
            uv_resistance (int): The UV resistance rating (1-10).
            thickness (float): The thickness of the material in mm.
        """
        self.name = name
        self.slip_resistance = slip_resistance
        self.durability = durability
        self.maintenance_ease = maintenance_ease
        self.chemical_resistance = chemical_resistance
        self.uv_resistance = uv_resistance
        self.thickness = thickness

    def __str__(self):
        return f"{self.name} - Slip Resistance: {self.slip_resistance}, Durability: {self.durability}, " \
               f"Maintenance Ease: {self.maintenance_ease}, Chemical Resistance: {self.chemical_resistance}, " \
               f"UV Resistance: {self.uv_resistance}, Thickness: {self.thickness}mm"


class RubberFlooringComparator:
    """Compares the safety features of different rubber flooring materials."""

    def __init__(self):
        self.materials = []

    def add_material(self, material):
        """
        Adds a rubber flooring material to the comparator.

        Args:
            material (RubberFlooringMaterial): The material to add.
        """
        self.materials.append(material)

    def compare_slip_resistance(self):
        """Compares the slip resistance of the added materials."""
        if not self.materials:
            raise ValueError("No materials added for comparison.")

        sorted_materials = sorted(self.materials, key=lambda x: x.slip_resistance, reverse=True)
        print("Slip Resistance Comparison:")
        for i, material in enumerate(sorted_materials):
            print(f"{i+1}. {material.name} - Slip Resistance: {material.slip_resistance}")

    def compare_durability(self):
        """Compares the durability of the added materials."""
        if not self.materials:
            raise ValueError("No materials added for comparison.")

        sorted_materials = sorted(self.materials, key=lambda x: x.durability, reverse=True)
        print("Durability Comparison:")
        for i, material in enumerate(sorted_materials):
            print(f"{i+1}. {material.name} - Durability: {material.durability}")

    def compare_safety_features(self):
        """Compares the safety features of the added materials."""
        if not self.materials:
            raise ValueError("No materials added for comparison.")

        print("Safety Features Comparison:")
        for material in self.materials:
            print(material)


def main():
    comparator = RubberFlooringComparator()

    tpv_rubber = RubberFlooringMaterial(
        "TPV Rubber",
        slip_resistance=8,
        durability=9,
        maintenance_ease=7,
        chemical_resistance=8,
        uv_resistance=9,
        thickness=10.0
    )

    rubber_tiles = RubberFlooringMaterial(
        "Rubber Tiles",
        slip_resistance=7,
        durability=8,
        maintenance_ease=8,
        chemical_resistance=7,
        uv_resistance=8,
        thickness=12.0
    )

    comparator.add_material(tpv_rubber)
    comparator.add_material(rubber_tiles)

    try:
        comparator.compare_slip_resistance()
        comparator.compare_durability()
        comparator.compare_safety_features()
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
