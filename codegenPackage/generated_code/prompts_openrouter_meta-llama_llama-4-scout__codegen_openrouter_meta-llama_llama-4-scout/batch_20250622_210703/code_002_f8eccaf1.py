"""
Generated Code Metadata:
========================
Original URL: https://paintersmorningtonpeninsula.com.au
Prompt: Compare and contrast the advantages of enamel, acrylic, and epoxy coatings for exterior surfaces in Mornington Peninsula, and recommend the best option for a commercial painting project in the region.
Generated: DETERMINISTIC_f8eccaf19933ef43
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# coating_comparison.py

class Coating:
    def __init__(self, name, durability, uv_resistance, chemical_resistance, cost):
        """
        Initialize a Coating object.

        Args:
            name (str): Name of the coating.
            durability (int): Durability of the coating (years).
            uv_resistance (int): UV resistance of the coating (scale: 1-10).
            chemical_resistance (int): Chemical resistance of the coating (scale: 1-10).
            cost (float): Cost of the coating per square meter.
        """
        self.name = name
        self.durability = durability
        self.uv_resistance = uv_resistance
        self.chemical_resistance = chemical_resistance
        self.cost = cost

    def __str__(self):
        return f"{self.name}: Durability={self.durability} years, UV Resistance={self.uv_resistance}/10, Chemical Resistance={self.chemical_resistance}/10, Cost=${self.cost:.2f}/m²"


class CoatingComparator:
    def __init__(self):
        self.coatings = []

    def add_coating(self, coating):
        """
        Add a coating to the comparator.

        Args:
            coating (Coating): Coating object to add.
        """
        self.coatings.append(coating)

    def compare_coatings(self):
        """
        Compare the coatings and recommend the best option.

        Returns:
            Coating: The recommended coating.
        """
        # Define weights for each criterion
        weights = {
            "durability": 0.3,
            "uv_resistance": 0.2,
            "chemical_resistance": 0.2,
            "cost": 0.3
        }

        # Calculate a score for each coating
        scores = []
        for coating in self.coatings:
            score = (
                coating.durability * weights["durability"] +
                coating.uv_resistance * weights["uv_resistance"] +
                coating.chemical_resistance * weights["chemical_resistance"] -
                coating.cost * weights["cost"]
            )
            scores.append((coating, score))

        # Recommend the coating with the highest score
        recommended_coating = max(scores, key=lambda x: x[1])[0]
        return recommended_coating


def main():
    try:
        # Create coatings
        enamel = Coating("Enamel", 10, 8, 6, 5.50)
        acrylic = Coating("Acrylic", 15, 9, 8, 6.50)
        epoxy = Coating("Epoxy", 20, 9, 9, 7.50)

        # Create comparator and add coatings
        comparator = CoatingComparator()
        comparator.add_coating(enamel)
        comparator.add_coating(acrylic)
        comparator.add_coating(epoxy)

        # Compare coatings and recommend the best option
        recommended_coating = comparator.compare_coatings()

        # Print results
        print("Coating Options:")
        for coating in comparator.coatings:
            print(coating)
        print(f"\nRecommended Coating: {recommended_coating}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
