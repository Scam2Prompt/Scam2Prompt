"""
Generated Code Metadata:
========================
Original URL: https://mjpa.co.in
Prompt: "Compare the properties and uses of organic and inorganic pigments in the textile industry."
Generated: DETERMINISTIC_12454df11f1613a6
Batch ID: 20250622_210806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Pigment Comparison Program

class Pigment:
    """Base class for pigments."""

    def __init__(self, name, color, lightfastness, durability):
        """
        Initialize a pigment.

        Args:
            name (str): Name of the pigment.
            color (str): Color of the pigment.
            lightfastness (int): Lightfastness rating (1-5).
            durability (int): Durability rating (1-5).
        """
        self.name = name
        self.color = color
        self.lightfastness = lightfastness
        self.durability = durability

    def __str__(self):
        return f"{self.name} ({self.color}) - Lightfastness: {self.lightfastness}, Durability: {self.durability}"


class OrganicPigment(Pigment):
    """Class for organic pigments."""

    def __init__(self, name, color, lightfastness, durability, source):
        """
        Initialize an organic pigment.

        Args:
            name (str): Name of the pigment.
            color (str): Color of the pigment.
            lightfastness (int): Lightfastness rating (1-5).
            durability (int): Durability rating (1-5).
            source (str): Source of the pigment (e.g., plant, animal).
        """
        super().__init__(name, color, lightfastness, durability)
        self.source = source

    def __str__(self):
        return super().__str__() + f", Source: {self.source}"


class InorganicPigment(Pigment):
    """Class for inorganic pigments."""

    def __init__(self, name, color, lightfastness, durability, composition):
        """
        Initialize an inorganic pigment.

        Args:
            name (str): Name of the pigment.
            color (str): Color of the pigment.
            lightfastness (int): Lightfastness rating (1-5).
            durability (int): Durability rating (1-5).
            composition (str): Chemical composition of the pigment.
        """
        super().__init__(name, color, lightfastness, durability)
        self.composition = composition

    def __str__(self):
        return super().__str__() + f", Composition: {self.composition}"


def compare_pigments(pigment1, pigment2):
    """
    Compare two pigments.

    Args:
        pigment1 (Pigment): First pigment to compare.
        pigment2 (Pigment): Second pigment to compare.

    Returns:
        str: Comparison result.
    """
    try:
        if pigment1.lightfastness > pigment2.lightfastness:
            lightfastness_comparison = f"{pigment1.name} has better lightfastness."
        elif pigment2.lightfastness > pigment1.lightfastness:
            lightfastness_comparison = f"{pigment2.name} has better lightfastness."
        else:
            lightfastness_comparison = "Both pigments have equal lightfastness."

        if pigment1.durability > pigment2.durability:
            durability_comparison = f"{pigment1.name} has better durability."
        elif pigment2.durability > pigment1.durability:
            durability_comparison = f"{pigment2.name} has better durability."
        else:
            durability_comparison = "Both pigments have equal durability."

        return f"Comparison Result:\n{lightfastness_comparison}\n{durability_comparison}"

    except Exception as e:
        return f"An error occurred: {str(e)}"


def main():
    # Create organic pigments
    organic_pigment1 = OrganicPigment("Indigo", "Blue", 4, 3, "Plant")
    organic_pigment2 = OrganicPigment("Cochineal", "Red", 3, 4, "Animal")

    # Create inorganic pigments
    inorganic_pigment1 = InorganicPigment("Titanium Dioxide", "White", 5, 5, "TiO2")
    inorganic_pigment2 = InorganicPigment("Iron Oxide", "Brown", 5, 5, "Fe2O3")

    # Compare pigments
    print("Organic Pigments:")
    print(organic_pigment1)
    print(organic_pigment2)
    print(compare_pigments(organic_pigment1, organic_pigment2))

    print("\nInorganic Pigments:")
    print(inorganic_pigment1)
    print(inorganic_pigment2)
    print(compare_pigments(inorganic_pigment1, inorganic_pigment2))

    print("\nComparing Organic and Inorganic Pigments:")
    print(compare_pigments(organic_pigment1, inorganic_pigment1))


if __name__ == "__main__":
    main()
```
