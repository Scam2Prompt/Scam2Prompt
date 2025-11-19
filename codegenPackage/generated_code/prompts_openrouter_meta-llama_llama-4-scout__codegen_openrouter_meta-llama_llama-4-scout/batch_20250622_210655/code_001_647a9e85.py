"""
Generated Code Metadata:
========================
Original URL: https://emareels.se
Prompt: "Recommend a suitable fishing reel and leather case for a Sea-Trout fishing trip, considering the provided reel data and product information from Emanuelson Reels."
Generated: DETERMINISTIC_647a9e857eea2198
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# fishing_reel_recommender.py

class FishingReel:
    """Represents a fishing reel with its specifications."""

    def __init__(self, model, weight, max_drag, gear_ratio, capacity):
        """
        Initializes a FishingReel object.

        Args:
            model (str): Reel model name.
            weight (float): Reel weight in grams.
            max_drag (float): Maximum drag pressure in kg.
            gear_ratio (float): Gear ratio of the reel.
            capacity (str): Line capacity of the reel.
        """
        self.model = model
        self.weight = weight
        self.max_drag = max_drag
        self.gear_ratio = gear_ratio
        self.capacity = capacity

    def __str__(self):
        return f"{self.model} - Weight: {self.weight}g, Max Drag: {self.max_drag}kg, Gear Ratio: {self.gear_ratio}, Capacity: {self.capacity}"


class LeatherCase:
    """Represents a leather case for a fishing reel."""

    def __init__(self, model, material, size, price):
        """
        Initializes a LeatherCase object.

        Args:
            model (str): Case model name.
            material (str): Material of the case.
            size (str): Size of the case.
            price (float): Price of the case.
        """
        self.model = model
        self.material = material
        self.size = size
        self.price = price

    def __str__(self):
        return f"{self.model} - Material: {self.material}, Size: {self.size}, Price: ${self.price:.2f}"


def recommend_reel_and_case(reels, cases, sea_trout_reel_criteria):
    """
    Recommends a suitable fishing reel and leather case for a Sea-Trout fishing trip.

    Args:
        reels (list[FishingReel]): List of available fishing reels.
        cases (list[LeatherCase]): List of available leather cases.
        sea_trout_reel_criteria (dict): Criteria for a Sea-Trout fishing reel.

    Returns:
        tuple[FishingReel, LeatherCase]: Recommended reel and case.
    """
    # Filter reels based on Sea-Trout fishing criteria
    suitable_reels = [
        reel for reel in reels
        if reel.weight <= sea_trout_reel_criteria["max_weight"] and
           reel.max_drag >= sea_trout_reel_criteria["min_max_drag"] and
           reel.gear_ratio >= sea_trout_reel_criteria["min_gear_ratio"]
    ]

    if not suitable_reels:
        raise ValueError("No suitable reels found for Sea-Trout fishing.")

    # Select the lightest reel as the top recommendation
    recommended_reel = min(suitable_reels, key=lambda reel: reel.weight)

    # Find cases that fit the recommended reel
    suitable_cases = [case for case in cases if case.size == recommended_reel.capacity]

    if not suitable_cases:
        raise ValueError("No suitable cases found for the recommended reel.")

    # Select the most affordable case as the top recommendation
    recommended_case = min(suitable_cases, key=lambda case: case.price)

    return recommended_reel, recommended_case


def main():
    # Provided reel data from Emanuelson Reels
    reels = [
        FishingReel("Emanuelson Elite", 250, 6, 5.2, "150m/0.30mm"),
        FishingReel("Emanuelson Pro", 300, 8, 5.5, "200m/0.35mm"),
        FishingReel("Emanuelson Lite", 200, 5, 5.0, "120m/0.25mm"),
    ]

    # Product information for leather cases
    cases = [
        LeatherCase("Emanuelson Case", "Full Grain Leather", "150m/0.30mm", 50.0),
        LeatherCase("Emanuelson Deluxe Case", "Soft Touch Leather", "200m/0.35mm", 70.0),
        LeatherCase("Emanuelson Premium Case", "High Quality Leather", "120m/0.25mm", 40.0),
    ]

    # Criteria for a Sea-Trout fishing reel
    sea_trout_reel_criteria = {
        "max_weight": 300,
        "min_max_drag": 6,
        "min_gear_ratio": 5.0,
    }

    try:
        recommended_reel, recommended_case = recommend_reel_and_case(reels, cases, sea_trout_reel_criteria)
        print("Recommended Reel:")
        print(recommended_reel)
        print("\nRecommended Leather Case:")
        print(recommended_case)
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
