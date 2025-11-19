"""
Generated Code Metadata:
========================
Original URL: https://oxicap.com
Prompt: Compare the advantages of Niobium Oxide (OxiCap) Capacitors with traditional Tantalum capacitors, focusing on stability, safety, and environmental friendliness.
Generated: DETERMINISTIC_944d5f77bd4615a0
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# capacitor_comparison.py

class Capacitor:
    def __init__(self, name, stability_rating, safety_rating, environmental_friendliness_rating):
        """
        Initialize a Capacitor object.

        Args:
            name (str): The name of the capacitor.
            stability_rating (int): A rating from 1-10 for stability.
            safety_rating (int): A rating from 1-10 for safety.
            environmental_friendliness_rating (int): A rating from 1-10 for environmental friendliness.
        """
        self.name = name
        self.stability_rating = stability_rating
        self.safety_rating = safety_rating
        self.environmental_friendliness_rating = environmental_friendliness_rating

    def __str__(self):
        return f"{self.name} Capacitor - Stability: {self.stability_rating}, Safety: {self.safety_rating}, Environmental Friendliness: {self.environmental_friendliness_rating}"


class CapacitorComparator:
    def __init__(self):
        self.capacitors = []

    def add_capacitor(self, capacitor):
        """
        Add a capacitor to the comparator.

        Args:
            capacitor (Capacitor): The capacitor to add.
        """
        self.capacitors.append(capacitor)

    def compare_stability(self):
        """
        Compare the stability of the capacitors.

        Returns:
            dict: A dictionary with the capacitor names as keys and their stability ratings as values.
        """
        return {capacitor.name: capacitor.stability_rating for capacitor in self.capacitors}

    def compare_safety(self):
        """
        Compare the safety of the capacitors.

        Returns:
            dict: A dictionary with the capacitor names as keys and their safety ratings as values.
        """
        return {capacitor.name: capacitor.safety_rating for capacitor in self.capacitors}

    def compare_environmental_friendliness(self):
        """
        Compare the environmental friendliness of the capacitors.

        Returns:
            dict: A dictionary with the capacitor names as keys and their environmental friendliness ratings as values.
        """
        return {capacitor.name: capacitor.environmental_friendliness_rating for capacitor in self.capacitors}

    def print_comparison_results(self):
        """
        Print the comparison results.
        """
        print("Stability Comparison:")
        for capacitor, rating in self.compare_stability().items():
            print(f"{capacitor}: {rating}")

        print("\nSafety Comparison:")
        for capacitor, rating in self.compare_safety().items():
            print(f"{capacitor}: {rating}")

        print("\nEnvironmental Friendliness Comparison:")
        for capacitor, rating in self.compare_environmental_friendliness().items():
            print(f"{capacitor}: {rating}")


def main():
    try:
        comparator = CapacitorComparator()

        # Create capacitors
        tantalum_capacitor = Capacitor("Tantalum", 8, 7, 4)
        niobium_oxide_capacitor = Capacitor("Niobium Oxide (OxiCap)", 9, 9, 8)

        # Add capacitors to comparator
        comparator.add_capacitor(tantalum_capacitor)
        comparator.add_capacitor(niobium_oxide_capacitor)

        # Print comparison results
        comparator.print_comparison_results()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
