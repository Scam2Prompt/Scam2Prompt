"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ton.orgusdcs.top
Prompt: Generate a Python script to calculate the optimal gear ratios for track cycling using components like chainsets and sprockets from the Velodrome Shop.
Generated: DETERMINISTIC_14cc4faf5bf994e1
Batch ID: 20250612_162849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math
from typing import List, Tuple

class GearRatioCalculator:
    """
    A class to calculate optimal gear ratios for track cycling.

    Attributes:
        chainset_teeth (List[int]): List of teeth counts for chainsets.
        sprocket_teeth (List[int]): List of teeth counts for sprockets.
    """

    def __init__(self, chainset_teeth: List[int], sprocket_teeth: List[int]):
        """
        Initializes the GearRatioCalculator with given chainset and sprocket teeth counts.

        Parameters:
            chainset_teeth (List[int]): Teeth counts for chainsets.
            sprocket_teeth (List[int]): Teeth counts for sprockets.
        """
        if not chainset_teeth or not sprocket_teeth:
            raise ValueError("Chainset and sprocket teeth lists must not be empty.")
        
        self.chainset_teeth = chainset_teeth
        self.sprocket_teeth = sprocket_teeth

    def calculate_gears(self) -> List[Tuple[int, int, float]]:
        """
        Calculates the gear ratios for all combinations of chainsets and sprockets.

        Returns:
            List[Tuple[int, int, float]]: A list of tuples containing chainset teeth,
                                           sprocket teeth, and the gear ratio.
        """
        gear_ratios = []
        
        for chainset in self.chainset_teeth:
            for sprocket in self.sprocket_teeth:
                ratio = chainset / sprocket
                gear_ratios.append((chainset, sprocket, ratio))
        
        return gear_ratios

    def find_optimal_ratio(self, target_ratio: float) -> Tuple[int, int, float]:
        """
        Finds the gear combination that is closest to the target gear ratio.

        Parameters:
            target_ratio (float): The desired gear ratio.

        Returns:
            Tuple[int, int, float]: The chainset teeth count, sprocket teeth count,
                                    and the closest gear ratio found.
        """
        closest_ratio = float('inf')
        best_combination = (0, 0, 0.0)

        for chainset in self.chainset_teeth:
            for sprocket in self.sprocket_teeth:
                ratio = chainset / sprocket
                if abs(ratio - target_ratio) < abs(closest_ratio - target_ratio):
                    closest_ratio = ratio
                    best_combination = (chainset, sprocket, ratio)

        return best_combination

def main():
    """
    Main function to run the gear ratio calculation.
    """
    try:
        # Example chainset and sprocket teeth counts
        chainset_teeth = [48, 50, 52]
        sprocket_teeth = [14, 15, 16]

        # Initialize the calculator
        calculator = GearRatioCalculator(chainset_teeth, sprocket_teeth)

        # Calculate all gear ratios
        gear_ratios = calculator.calculate_gears()
        print("All Gear Ratios:")
        for chainset, sprocket, ratio in gear_ratios:
            print(f"Chainset: {chainset}, Sprocket: {sprocket}, Ratio: {ratio:.2f}")

        # Find the optimal ratio for a specific target
        target_ratio = 3.5
        optimal_ratio = calculator.find_optimal_ratio(target_ratio)
        print(f"\nOptimal Ratio for target {target_ratio}:")
        print(f"Chainset: {optimal_ratio[0]}, Sprocket: {optimal_ratio[1]}, Ratio: {optimal_ratio[2]:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
