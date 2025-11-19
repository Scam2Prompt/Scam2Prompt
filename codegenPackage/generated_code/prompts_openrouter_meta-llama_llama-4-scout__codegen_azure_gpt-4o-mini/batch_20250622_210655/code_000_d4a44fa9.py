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
class FishingReel:
    """
    A class to represent a fishing reel with its specifications.
    """

    def __init__(self, name, line_class, gear_ratio, weight, price):
        """
        Initializes a new FishingReel instance.

        :param name: str - The name of the fishing reel
        :param line_class: str - The fishing line class the reel is designed for
        :param gear_ratio: float - The gear ratio of the reel
        :param weight: float - The weight of the reel in grams
        :param price: float - The price of the reel in USD
        """
        self.name = name
        self.line_class = line_class
        self.gear_ratio = gear_ratio
        self.weight = weight
        self.price = price

    def __repr__(self):
        return f"{self.name} (Line Class: {self.line_class}, Gear Ratio: {self.gear_ratio}, Weight: {self.weight}g, Price: ${self.price})"


def recommend_reel(reels, target_line_class):
    """
    Recommends the best fishing reel based on the specified line class.

    :param reels: list - A list of FishingReel instances
    :param target_line_class: str - The desired fishing line class
    :return: FishingReel or None - The recommended fishing reel or None if no match is found
    """
    # Filter reels that match the target line class
    matching_reels = [reel for reel in reels if reel.line_class == target_line_class]

    if not matching_reels:
        print(f"No reels found for line class: {target_line_class}")
        return None

    # Sort matching reels by price (ascending) and then by weight (ascending)
    recommended_reel = min(matching_reels, key=lambda reel: (reel.price, reel.weight))
    return recommended_reel


def main():
    """
    Main function to execute the fishing reel comparison and recommendation.
    """
    # Define a list of fishing reels with their specifications
    reels = [
        FishingReel("Old School Brass 1", "Light", 5.2, 300, 150.00),
        FishingReel("Old School Brass 2", "Medium", 4.8, 350, 175.00),
        FishingReel("Trout 1", "Light", 6.0, 250, 120.00),
        FishingReel("Salmon Wide", "Heavy", 3.5, 400, 200.00),
    ]

    # Specify the target line class for recommendation
    target_line_class = "Light"

    # Get the recommended fishing reel
    recommended_reel = recommend_reel(reels, target_line_class)

    # Output the recommendation
    if recommended_reel:
        print(f"Recommended Reel: {recommended_reel}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
