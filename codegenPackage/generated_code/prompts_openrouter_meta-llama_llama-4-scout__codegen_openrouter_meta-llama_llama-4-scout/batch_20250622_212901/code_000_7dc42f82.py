"""
Generated Code Metadata:
========================
Original URL: https://unitramabrazz.blogspot.com
Prompt: What are the different types of materials used for large-format printing, and how do they compare in terms of durability and application?
Generated: DETERMINISTIC_7dc42f82d0fd51c3
Batch ID: 20250622_212901
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# large_format_printing_materials.py

class LargeFormatPrintingMaterial:
    """Base class for large format printing materials."""

    def __init__(self, name, durability, application):
        """
        Initialize a large format printing material.

        Args:
            name (str): The name of the material.
            durability (str): The durability of the material (e.g., indoor, outdoor).
            application (str): The typical application of the material (e.g., advertising, decor).
        """
        self.name = name
        self.durability = durability
        self.application = application

    def __str__(self):
        return f"{self.name}: Durability - {self.durability}, Application - {self.application}"


class Vinyl(LargeFormatPrintingMaterial):
    """Vinyl material for large format printing."""

    def __init__(self, type):
        """
        Initialize a vinyl material.

        Args:
            type (str): The type of vinyl (e.g., calendered, cast).
        """
        if type not in ["calendered", "cast"]:
            raise ValueError("Invalid vinyl type")

        super().__init__("Vinyl", "medium to high", "advertising, decor")
        self.type = type

    def __str__(self):
        return super().__str__() + f", Type - {self.type}"


class Paper(LargeFormatPrintingMaterial):
    """Paper material for large format printing."""

    def __init__(self, weight):
        """
        Initialize a paper material.

        Args:
            weight (int): The weight of the paper in grams per square meter (gsm).
        """
        if weight < 50:
            raise ValueError("Paper weight must be 50 gsm or higher")

        super().__init__("Paper", "low", "indoor advertising, decor")
        self.weight = weight

    def __str__(self):
        return super().__str__() + f", Weight - {self.weight} gsm"


class Fabric(LargeFormatPrintingMaterial):
    """Fabric material for large format printing."""

    def __init__(self, material):
        """
        Initialize a fabric material.

        Args:
            material (str): The type of fabric (e.g., polyester, cotton).
        """
        super().__init__("Fabric", "medium", "decor, events")
        self.material = material

    def __str__(self):
        return super().__str__() + f", Material - {self.material}"


class RigidPanel(LargeFormatPrintingMaterial):
    """Rigid panel material for large format printing."""

    def __init__(self, type):
        """
        Initialize a rigid panel material.

        Args:
            type (str): The type of rigid panel (e.g., PVC, foam board).
        """
        super().__init__("Rigid Panel", "high", "advertising, exhibitions")
        self.type = type

    def __str__(self):
        return super().__str__() + f", Type - {self.type}"


def main():
    try:
        materials = [
            Vinyl("calendered"),
            Vinyl("cast"),
            Paper(80),
            Fabric("polyester"),
            RigidPanel("PVC"),
            RigidPanel("foam board"),
        ]

        for material in materials:
            print(material)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
