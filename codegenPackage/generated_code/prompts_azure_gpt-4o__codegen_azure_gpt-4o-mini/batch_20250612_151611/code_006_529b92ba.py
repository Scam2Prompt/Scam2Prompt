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
class MetalFitting:
    def __init__(self, name, durability, corrosion_resistance):
        """
        Initialize a MetalFitting instance.

        :param name: str - The name of the metal fitting.
        :param durability: int - A rating from 1 to 10 for durability.
        :param corrosion_resistance: int - A rating from 1 to 10 for corrosion resistance.
        """
        self.name = name
        self.durability = durability
        self.corrosion_resistance = corrosion_resistance

    def __repr__(self):
        return f"{self.name} (Durability: {self.durability}, Corrosion Resistance: {self.corrosion_resistance})"


class MetalFittingRecommender:
    def __init__(self):
        """
        Initialize the recommender with a list of available metal fittings.
        """
        self.available_fittings = [
            MetalFitting("Hastelloy C276 Round Bars", 9, 10),
            MetalFitting("Inconel Alloy 600 Pipes", 8, 9),
            MetalFitting("Stainless Steel 316", 7, 7),
            MetalFitting("Titanium Grade 5", 9, 8),
            MetalFitting("Monel 400", 8, 9),
            MetalFitting("Hastelloy B2", 8, 10),
            MetalFitting("Inconel Alloy 625", 9, 9),
        ]

    def recommend(self, min_durability=5, min_corrosion_resistance=5):
        """
        Recommend metal fittings based on user preferences for durability and corrosion resistance.

        :param min_durability: int - Minimum durability rating (default is 5).
        :param min_corrosion_resistance: int - Minimum corrosion resistance rating (default is 5).
        :return: list - A list of recommended metal fittings.
        """
        if not (1 <= min_durability <= 10) or not (1 <= min_corrosion_resistance <= 10):
            raise ValueError("Durability and corrosion resistance ratings must be between 1 and 10.")

        recommendations = [
            fitting for fitting in self.available_fittings
            if fitting.durability >= min_durability and fitting.corrosion_resistance >= min_corrosion_resistance
        ]

        if not recommendations:
            print("No fittings found matching the criteria.")
        return recommendations


# Example usage
if __name__ == "__main__":
    recommender = MetalFittingRecommender()
    try:
        user_recommendations = recommender.recommend(min_durability=8, min_corrosion_resistance=8)
        print("Recommended Metal Fittings:")
        for fitting in user_recommendations:
            print(fitting)
    except ValueError as e:
        print(f"Error: {e}")
```
