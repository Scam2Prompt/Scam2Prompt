"""
Generated Code Metadata:
========================
Original URL: https://topartksa.com
Prompt: "Compare the properties of Topart solid surface material with other materials used for countertops, sinks, and furniture, focusing on its benefits and drawbacks."
Generated: DETERMINISTIC_e946dd88358ed37e
Batch ID: 20250622_204552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# material_comparator.py

class Material:
    """Base class for materials."""

    def __init__(self, name, durability, maintenance, cost, aesthetic_appeal):
        """
        Initialize a material.

        Args:
            name (str): Material name.
            durability (int): Durability score (1-10).
            maintenance (int): Maintenance score (1-10).
            cost (int): Cost score (1-10).
            aesthetic_appeal (int): Aesthetic appeal score (1-10).
        """
        self.name = name
        self.durability = durability
        self.maintenance = maintenance
        self.cost = cost
        self.aesthetic_appeal = aesthetic_appeal

    def __str__(self):
        return f"{self.name}: Durability={self.durability}, Maintenance={self.maintenance}, Cost={self.cost}, Aesthetic Appeal={self.aesthetic_appeal}"


class TopartSolidSurface(Material):
    """Topart solid surface material."""

    def __init__(self):
        super().__init__("Topart Solid Surface", 8, 6, 7, 9)

    def benefits(self):
        return ["Non-porous", "Easy to clean", "Resistant to scratches"]

    def drawbacks(self):
        return ["Can be damaged by heat", "Not suitable for outdoor use"]


class Granite(Material):
    """Granite material."""

    def __init__(self):
        super().__init__("Granite", 9, 8, 8, 9)

    def benefits(self):
        return ["Highly durable", "Heat-resistant", "Aesthetically pleasing"]

    def drawbacks(self):
        return ["Porous", "Requires periodic sealing"]


class Quartz(Material):
    """Quartz material."""

    def __init__(self):
        super().__init__("Quartz", 8, 6, 8, 9)

    def benefits(self):
        return ["Low maintenance", "Non-porous", "Consistent color"]

    def drawbacks(self):
        return ["Can be expensive", "May appear artificial"]


class Laminate(Material):
    """Laminate material."""

    def __init__(self):
        super().__init__("Laminate", 6, 8, 5, 7)

    def benefits(self):
        return ["Affordable", "Easy to install", "Variety of patterns"]

    def drawbacks(self):
        return ["Less durable", "May appear cheap"]


def compare_materials(materials):
    """Compare materials based on their properties."""

    for material in materials:
        print(material)
        print(f"Benefits: {material.benefits()}")
        print(f"Drawbacks: {material.drawbacks()}")
        print("------------------------")


def main():
    try:
        topart = TopartSolidSurface()
        granite = Granite()
        quartz = Quartz()
        laminate = Laminate()

        materials = [topart, granite, quartz, laminate]
        compare_materials(materials)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
