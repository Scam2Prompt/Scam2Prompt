"""
Generated Code Metadata:
========================
Original URL: https://engeloutdoors.com
Prompt: "Recommend a suitable Engel cooler for a family of four going on a week-long camping trip, considering factors such as size, insulation, and durability."
Generated: DETERMINISTIC_6aaf62636964d196
Batch ID: 20250622_204817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import math

class EngelCooler:
    def __init__(self, name, size, insulation_thickness, durability_rating):
        """
        Initialize an EngelCooler object.

        Args:
            name (str): Name of the cooler.
            size (float): Size of the cooler in liters.
            insulation_thickness (float): Thickness of the insulation in mm.
            durability_rating (int): Durability rating out of 10.
        """
        self.name = name
        self.size = size
        self.insulation_thickness = insulation_thickness
        self.durability_rating = durability_rating

    def __str__(self):
        return f"{self.name}: {self.size}L, {self.insulation_thickness}mm insulation, Durability: {self.durability_rating}/10"


class CoolerRecommender:
    def __init__(self):
        """
        Initialize a CoolerRecommender object.
        """
        self.coolers = [
            EngelCooler("Engel MR40F-U1", 40, 30, 9),
            EngelCooler("Engel MR60F-U1", 60, 35, 9),
            EngelCooler("Engel MR20F-U1", 20, 25, 8),
            EngelCooler("Engel MR80F-U1", 80, 40, 9),
        ]

    def recommend_cooler(self, family_size, trip_duration):
        """
        Recommend a suitable Engel cooler based on family size and trip duration.

        Args:
            family_size (int): Number of people in the family.
            trip_duration (int): Duration of the trip in days.

        Returns:
            EngelCooler: Recommended cooler.
        """
        # Calculate required cooler size in liters ( assume 10L per person per day)
        required_size = family_size * trip_duration * 10

        # Filter coolers that meet the size requirement
        suitable_coolers = [cooler for cooler in self.coolers if cooler.size >= required_size]

        if not suitable_coolers:
            raise ValueError("No suitable coolers found. Please consider a larger size.")

        # Sort suitable coolers by durability rating and then by insulation thickness
        suitable_coolers.sort(key=lambda x: (-x.durability_rating, -x.insulation_thickness))

        return suitable_coolers[0]


def main():
    try:
        family_size = 4
        trip_duration = 7
        recommender = CoolerRecommender()
        recommended_cooler = recommender.recommend_cooler(family_size, trip_duration)
        print("Recommended Cooler:")
        print(recommended_cooler)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
