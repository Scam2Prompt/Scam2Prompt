"""
Generated Code Metadata:
========================
Original URL: https://hoorainz.com
Prompt: "Generate a list of natural stone types and their properties, similar to those featured on Hoorainz, and suggest how they could be used in coding a product recommendation engine."
Generated: DETERMINISTIC_6cc60f01c8a55284
Batch ID: 20250622_211921
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# natural_stone.py

class NaturalStone:
    """Represents a natural stone type with its properties."""

    def __init__(self, name, description, color, hardness, durability, applications):
        """
        Initializes a NaturalStone object.

        Args:
            name (str): The name of the natural stone.
            description (str): A brief description of the natural stone.
            color (str): The typical color of the natural stone.
            hardness (int): The hardness of the natural stone on the Mohs scale.
            durability (str): A description of the natural stone's durability.
            applications (list): A list of common applications for the natural stone.
        """
        self.name = name
        self.description = description
        self.color = color
        self.hardness = hardness
        self.durability = durability
        self.applications = applications

    def __str__(self):
        return f"{self.name}: {self.description}"


class ProductRecommendationEngine:
    """Suggests natural stone types based on user input."""

    def __init__(self):
        self.stones = []

    def add_stone(self, stone):
        """Adds a natural stone to the engine's database."""
        self.stones.append(stone)

    def suggest_stones(self, color=None, hardness=None, durability=None, application=None):
        """
        Suggests natural stone types based on user input.

        Args:
            color (str, optional): The desired color of the natural stone. Defaults to None.
            hardness (int, optional): The desired hardness of the natural stone. Defaults to None.
            durability (str, optional): The desired durability of the natural stone. Defaults to None.
            application (str, optional): The desired application of the natural stone. Defaults to None.

        Returns:
            list: A list of suggested natural stone types.
        """
        suggested_stones = [stone for stone in self.stones
                            if (color is None or stone.color == color)
                            and (hardness is None or stone.hardness == hardness)
                            and (durability is None or stone.durability == durability)
                            and (application is None or application in stone.applications)]

        return suggested_stones


def main():
    engine = ProductRecommendationEngine()

    # Add natural stone types to the engine's database
    stones = [
        NaturalStone("Marble", "A metamorphic rock.", "White", 3, "High", ["construction", "decorative"]),
        NaturalStone("Granite", "A igneous rock.", "Gray", 6, "Very High", ["construction", "kitchen countertops"]),
        NaturalStone("Limestone", "A sedimentary rock.", "Beige", 3, "Medium", ["construction", "landscaping"]),
        NaturalStone("Sandstone", "A sedimentary rock.", "Brown", 6, "Medium", ["construction", "decorative"]),
        NaturalStone("Slate", "A metamorphic rock.", "Gray", 5, "High", ["roofing", "flooring"]),
    ]

    for stone in stones:
        engine.add_stone(stone)

    # Suggest natural stone types based on user input
    suggested_stones = engine.suggest_stones(color="Gray", application="construction")

    print("Suggested Natural Stone Types:")
    for stone in suggested_stones:
        print(stone)
        print(f"  Color: {stone.color}")
        print(f"  Hardness: {stone.hardness}")
        print(f"  Durability: {stone.durability}")
        print(f"  Applications: {', '.join(stone.applications)}")
        print()


if __name__ == "__main__":
    main()
```
