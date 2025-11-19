"""
Generated Code Metadata:
========================
Original URL: https://ethn.cc
Prompt: Create a Python script to generate summaries of gravel cycling gear tests, like the comparison of Abus AirBreaker and GameChanger 2.0 helmets on ETNH Gravel Magazine.
Generated: DETERMINISTIC_ffb0b7235fb32d10
Batch ID: 20250612_154226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# gravel_gear_summary_generator.py

import json
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class Gear:
    """Represents a piece of gravel cycling gear."""
    name: str
    brand: str
    weight: float
    price: float
    features: List[str]

@dataclass
class GearTest:
    """Represents a test of gravel cycling gear."""
    gear1: Gear
    gear2: Gear
    similarities: List[str]
    differences: List[str]
    recommendation: str

class GearSummaryGenerator:
    def __init__(self, gear_data: Dict[str, Gear]):
        """
        Initializes the GearSummaryGenerator with gear data.

        Args:
        gear_data (Dict[str, Gear]): A dictionary of gear names to Gear objects.
        """
        self.gear_data = gear_data

    def generate_summary(self, gear1_name: str, gear2_name: str) -> GearTest:
        """
        Generates a summary of a test between two pieces of gear.

        Args:
        gear1_name (str): The name of the first gear.
        gear2_name (str): The name of the second gear.

        Returns:
        GearTest: A GearTest object summarizing the test.

        Raises:
        ValueError: If either gear is not found in the gear data.
        """
        if gear1_name not in self.gear_data or gear2_name not in self.gear_data:
            raise ValueError("Both gears must be in the gear data")

        gear1 = self.gear_data[gear1_name]
        gear2 = self.gear_data[gear2_name]

        similarities = self._find_similarities(gear1, gear2)
        differences = self._find_differences(gear1, gear2)
        recommendation = self._make_recommendation(gear1, gear2)

        return GearTest(gear1, gear2, similarities, differences, recommendation)

    def _find_similarities(self, gear1: Gear, gear2: Gear) -> List[str]:
        """Finds similarities between two pieces of gear."""
        similarities = []
        if gear1.brand == gear2.brand:
            similarities.append(f"Both are from {gear1.brand}")
        if gear1.features and gear2.features:
            common_features = set(gear1.features) & set(gear2.features)
            similarities.extend(list(common_features))
        return similarities

    def _find_differences(self, gear1: Gear, gear2: Gear) -> List[str]:
        """Finds differences between two pieces of gear."""
        differences = []
        if gear1.weight != gear2.weight:
            differences.append(f"Weight: {gear1.name} ({gear1.weight}g) vs {gear2.name} ({gear2.weight}g)")
        if gear1.price != gear2.price:
            differences.append(f"Price: {gear1.name} (${gear1.price}) vs {gear2.name} (${gear2.price})")
        if gear1.features and gear2.features:
            unique_features1 = set(gear1.features) - set(gear2.features)
            unique_features2 = set(gear2.features) - set(gear1.features)
            if unique_features1:
                differences.append(f"{gear1.name} has: {', '.join(unique_features1)}")
            if unique_features2:
                differences.append(f"{gear2.name} has: {', '.join(unique_features2)}")
        return differences

    def _make_recommendation(self, gear1: Gear, gear2: Gear) -> str:
        """Makes a recommendation between two pieces of gear."""
        if gear1.price < gear2.price and gear1.weight <= gear2.weight:
            return f"Recommend {gear1.name} for its better value"
        elif gear2.price < gear1.price and gear2.weight <= gear1.weight:
            return f"Recommend {gear2.name} for its better value"
        else:
            return "Both gears are suitable, choose based on personal preference"

def main():
    gear_data = {
        "Abus AirBreaker": Gear("Abus AirBreaker", "Abus", 250, 200, ["aerodynamic", "adjustable"]),
        "GameChanger 2.0": Gear("GameChanger 2.0", "Abus", 230, 250, ["aerodynamic", " MIPS"]),
    }

    generator = GearSummaryGenerator(gear_data)
    try:
        summary = generator.generate_summary("Abus AirBreaker", "GameChanger 2.0")
        print(f"**Summary of {summary.gear1.name} vs {summary.gear2.name}**")
        print(f"**Similarities:** {', '.join(summary.similarities)}")
        print(f"**Differences:**")
        for difference in summary.differences:
            print(f"- {difference}")
        print(f"**Recommendation:** {summary.recommendation}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
