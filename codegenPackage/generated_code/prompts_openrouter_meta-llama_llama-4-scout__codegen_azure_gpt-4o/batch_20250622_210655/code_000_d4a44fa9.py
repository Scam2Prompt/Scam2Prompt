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

# Import necessary modules
import json

# Define a class to represent a fishing reel
class FishingReel:
    def __init__(self, name, line_class, capacity, material, weight):
        """
        Initialize a FishingReel object.

        :param name: Name of the fishing reel
        :param line_class: Line class supported by the reel (e.g., "Light", "Medium", "Heavy")
        :param capacity: Line capacity in meters
        :param material: Material of the reel (e.g., "Brass", "Aluminum")
        :param weight: Weight of the reel in grams
        """
        self.name = name
        self.line_class = line_class
        self.capacity = capacity
        self.material = material
        self.weight = weight

    def __str__(self):
        """
        String representation of the FishingReel object.
        """
        return f"{self.name} (Line Class: {self.line_class}, Capacity: {self.capacity}m, Material: {self.material}, Weight: {self.weight}g)"


# Function to recommend the best fishing reel for a specific line class
def recommend_fishing_reel(reels, target_line_class):
    """
    Recommend the best fishing reel for a specific line class.

    :param reels: List of FishingReel objects
    :param target_line_class: Desired line class (e.g., "Light", "Medium", "Heavy")
    :return: Recommended FishingReel object or None if no match is found
    """
    # Filter reels that match the target line class
    matching_reels = [reel for reel in reels if reel.line_class.lower() == target_line_class.lower()]

    if not matching_reels:
        print(f"No fishing reels found for line class: {target_line_class}")
        return None

    # Sort matching reels by capacity (descending) and weight (ascending)
    matching_reels.sort(key=lambda reel: (-reel.capacity, reel.weight))

    # Return the best reel (highest capacity, lowest weight)
    return matching_reels[0]


# Main function to demonstrate the functionality
def main():
    """
    Main function to compare fishing reels and recommend the best one.
    """
    # Define fishing reels
    fishing_reels = [
        FishingReel("Old School Brass 1", "Light", 100, "Brass", 500),
        FishingReel("Old School Brass 2", "Medium", 150, "Brass", 600),
        FishingReel("Trout 1", "Light", 120, "Aluminum", 450),
        FishingReel("Salmon Wide", "Heavy", 200, "Aluminum", 700),
    ]

    # Input: Desired line class
    target_line_class = input("Enter the desired line class (Light, Medium, Heavy): ").strip()

    # Recommend the best fishing reel
    best_reel = recommend_fishing_reel(fishing_reels, target_line_class)

    # Display the result
    if best_reel:
        print("\nRecommended Fishing Reel:")
        print(best_reel)


# Entry point for the script
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
