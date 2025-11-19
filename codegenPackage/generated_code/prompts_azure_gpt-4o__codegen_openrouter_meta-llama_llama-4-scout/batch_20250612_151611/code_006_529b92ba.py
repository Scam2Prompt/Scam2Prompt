"""
Generated Code Metadata:
========================
Original URL: https://specialmetals.co.in
Prompt: Write a function to recommend alternative metal fittings (e.g., Hastelloy C276 Round Bars or Inconel Alloy 600 Pipes) based on user preferences for durability and corrosion resistance, as described on the Dinkar Alloys webpage.
Generated: DETERMINISTIC_529b92babce325bd
Batch ID: 20250612_151611
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import Dict, List

class Durability(Enum):
    """Enum for durability levels"""
    LOW = 1
    MEDIUM = 2
    HIGH = 3

class CorrosionResistance(Enum):
    """Enum for corrosion resistance levels"""
    LOW = 1
    MEDIUM = 2
    HIGH = 3

class MetalFitting:
    """Class representing a metal fitting"""
    def __init__(self, name: str, durability: Durability, corrosion_resistance: CorrosionResistance):
        self.name = name
        self.durability = durability
        self.corrosion_resistance = corrosion_resistance

    def __str__(self):
        return f"{self.name} - Durability: {self.durability.name}, Corrosion Resistance: {self.corrosion_resistance.name}"

class MetalFittingRecommender:
    """Class for recommending metal fittings"""
    def __init__(self):
        self.metal_fittings: List[MetalFitting] = [
            MetalFitting("Hastelloy C276 Round Bars", Durability.HIGH, CorrosionResistance.HIGH),
            MetalFitting("Inconel Alloy 600 Pipes", Durability.HIGH, CorrosionResistance.HIGH),
            MetalFitting("Stainless Steel 304 Sheets", Durability.MEDIUM, CorrosionResistance.MEDIUM),
            MetalFitting("Copper Alloys", Durability.LOW, CorrosionResistance.LOW),
            MetalFitting("Titanium Alloys", Durability.HIGH, CorrosionResistance.HIGH),
        ]

    def recommend(self, durability: Durability, corrosion_resistance: CorrosionResistance) -> List[MetalFitting]:
        """Recommend metal fittings based on user preferences"""
        recommended_fittings = [fitting for fitting in self.metal_fittings 
                                if fitting.durability.value >= durability.value 
                                and fitting.corrosion_resistance.value >= corrosion_resistance.value]
        return recommended_fittings

def main():
    try:
        recommender = MetalFittingRecommender()
        print("Metal Fitting Recommendations")
        print("--------------------------------")

        durability_levels: Dict[str, Durability] = {
            "low": Durability.LOW,
            "medium": Durability.MEDIUM,
            "high": Durability.HIGH,
        }

        corrosion_resistance_levels: Dict[str, CorrosionResistance] = {
            "low": CorrosionResistance.LOW,
            "medium": CorrosionResistance.MEDIUM,
            "high": CorrosionResistance.HIGH,
        }

        durability_preference = input("Enter durability preference (low, medium, high): ")
        corrosion_resistance_preference = input("Enter corrosion resistance preference (low, medium, high): ")

        durability = durability_levels.get(durability_preference.lower())
        corrosion_resistance = corrosion_resistance_levels.get(corrosion_resistance_preference.lower())

        if durability is None or corrosion_resistance is None:
            print("Invalid input. Please enter low, medium, or high.")
            return

        recommended_fittings = recommender.recommend(durability, corrosion_resistance)

        if recommended_fittings:
            for fitting in recommended_fittings:
                print(fitting)
        else:
            print("No metal fittings found matching your preferences.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
