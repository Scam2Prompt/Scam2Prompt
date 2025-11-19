"""
Generated Code Metadata:
========================
Original URL: https://emareels.se
Prompt: "Write a Python code to compare the specifications of different fishing reels, such as Old School Brass 1 & 2, Trout 1, and Salmon Wide, and recommend the best one for a specific fishing line class."
Generated: DETERMINISTIC_d4a44fa9e9e07b48
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# fishing_reel_comparator.py

class FishingReel:
    """Represents a fishing reel with its specifications."""

    def __init__(self, name, line_class, weight, gear_ratio, capacity):
        """
        Initializes a FishingReel object.

        Args:
            name (str): The name of the fishing reel.
            line_class (str): The line class of the fishing reel (e.g., "Light", "Medium", "Heavy").
            weight (float): The weight of the fishing reel in ounces.
            gear_ratio (float): The gear ratio of the fishing reel.
            capacity (str): The line capacity of the fishing reel (e.g., "100/10lb", "150/15lb").
        """
        self.name = name
        self.line_class = line_class
        self.weight = weight
        self.gear_ratio = gear_ratio
        self.capacity = capacity

    def __str__(self):
        return f"{self.name} - Line Class: {self.line_class}, Weight: {self.weight} oz, Gear Ratio: {self.gear_ratio}, Capacity: {self.capacity}"


class FishingReelComparator:
    """Compares the specifications of different fishing reels and recommends the best one for a specific fishing line class."""

    def __init__(self):
        self.reels = []

    def add_reel(self, reel):
        """Adds a fishing reel to the comparator."""
        self.reels.append(reel)

    def recommend_reel(self, line_class):
        """
        Recommends the best fishing reel for a specific fishing line class.

        Args:
            line_class (str): The line class for which to recommend a reel.

        Returns:
            FishingReel: The recommended fishing reel, or None if no reels match the line class.
        """
        matching_reels = [reel for reel in self.reels if reel.line_class == line_class]
        if not matching_reels:
            return None
        return min(matching_reels, key=lambda reel: reel.weight)

    def compare_reels(self):
        """Prints a comparison of all fishing reels."""
        for reel in self.reels:
            print(reel)


def main():
    comparator = FishingReelComparator()

    # Define fishing reels
    old_school_brass1 = FishingReel("Old School Brass 1", "Medium", 12.5, 5.1, "100/10lb")
    old_school_brass2 = FishingReel("Old School Brass 2", "Heavy", 16.2, 4.7, "150/15lb")
    trout1 = FishingReel("Trout 1", "Light", 9.8, 5.5, "80/8lb")
    salmon_wide = FishingReel("Salmon Wide", "Heavy", 18.5, 4.2, "200/20lb")

    # Add reels to comparator
    comparator.add_reel(old_school_brass1)
    comparator.add_reel(old_school_brass2)
    comparator.add_reel(trout1)
    comparator.add_reel(salmon_wide)

    # Compare reels
    print("Fishing Reel Comparison:")
    comparator.compare_reels()

    # Recommend reel for specific line class
    line_class = "Medium"
    recommended_reel = comparator.recommend_reel(line_class)
    if recommended_reel:
        print(f"\nRecommended Reel for {line_class} Line Class:")
        print(recommended_reel)
    else:
        print(f"\nNo reels found for {line_class} line class.")


if __name__ == "__main__":
    main()
```
