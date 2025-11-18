"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cartoansurperu.com
Prompt: Develop a Python script to optimize the storage space for rolls of corrugated cardboard, considering the customizable sizes and weights described in Cartonerías Andinas del Sur's product catalog.
Generated: DETERMINISTIC_375b914fc554adba
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import itertools
from typing import List, Tuple

class CardboardRoll:
    """
    Class to represent a cardboard roll with size and weight.
    """

    def __init__(self, diameter: float, width: float, weight: float):
        """
        Initialize a CardboardRoll instance.
        
        :param diameter: Diameter of the roll in meters.
        :param width: Width of the roll in meters.
        :param weight: Weight of the roll in kilograms.
        """
        self.diameter = diameter
        self.width = width
        self.weight = weight

    def volume(self) -> float:
        """
        Calculate the volume of the roll.
        
        :return: Volume of the roll in cubic meters.
        """
        radius = self.diameter / 2
        return 3.14159 * (radius ** 2) * self.width

def optimize_storage(rolls: List[CardboardRoll], max_weight: float) -> List[CardboardRoll]:
    """
    Optimize the storage of cardboard rolls based on weight and volume.
    
    :param rolls: List of CardboardRoll objects to optimize.
    :param max_weight: Maximum weight allowed for storage in kilograms.
    :return: List of CardboardRoll objects that fit within the weight limit.
    """
    best_combination = []
    best_volume = 0

    # Generate combinations of rolls to find the best fitting set
    for r in range(1, len(rolls) + 1):
        for combo in itertools.combinations(rolls, r):
            total_weight = sum(roll.weight for roll in combo)
            if total_weight <= max_weight:
                total_volume = sum(roll.volume() for roll in combo)
                # Check if this combination has a better volume than previous best
                if total_volume > best_volume:
                    best_volume = total_volume
                    best_combination = combo

    return list(best_combination)

def main():
    """
    Main function to execute the storage optimization.
    """
    try:
        # Sample data: diameter (m), width (m), weight (kg)
        rolls_data = [
            (1.0, 0.5, 10.0),
            (1.2, 0.6, 12.0),
            (0.8, 0.4, 8.0),
            (1.5, 0.7, 15.0),
            (1.1, 0.5, 11.0)
        ]

        # Create CardboardRoll instances
        rolls = [CardboardRoll(diameter, width, weight) for diameter, width, weight in rolls_data]

        # Set maximum weight for storage
        max_weight = 30.0  # kg

        # Optimize storage
        optimized_rolls = optimize_storage(rolls, max_weight)

        # Display results
        print("Optimized Storage Rolls:")
        for roll in optimized_rolls:
            print(f"Diameter: {roll.diameter} m, Width: {roll.width} m, Weight: {roll.weight} kg")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
