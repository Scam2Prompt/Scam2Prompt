"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://codes-bigtime.pages.dev
Prompt: Generate a function that simulates opening Mystery Boxes and retrieving collectibles in the Big Time game.
Generated: DETERMINISTIC_65022c21f17caa95
Batch ID: 20250612_163338
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import List, Dict, Any

class MysteryBox:
    def __init__(self, name: str, collectibles: List[str], probabilities: List[float]):
        """
        Initialize a MysteryBox instance.

        :param name: The name of the Mystery Box.
        :param collectibles: A list of collectible items in the box.
        :param probabilities: A list of probabilities corresponding to each collectible.
        """
        if len(collectibles) != len(probabilities):
            raise ValueError("The length of collectibles and probabilities must be the same.")
        if any(p < 0 for p in probabilities) or sum(probabilities) != 1:
            raise ValueError("Probabilities must be non-negative and sum to 1.")
        
        self.name = name
        self.collectibles = collectibles
        self.probabilities = probabilities

    def open(self) -> str:
        """
        Simulate opening the Mystery Box and retrieving a collectible.

        :return: The name of the collectible item retrieved.
        """
        # Generate a random number between 0 and 1
        random_number = random.random()
        cumulative_probability = 0.0
        
        # Determine which collectible was obtained
        for collectible, probability in zip(self.collectibles, self.probabilities):
            cumulative_probability += probability
            if random_number <= cumulative_probability:
                return collectible
        return None  # This should not happen if probabilities sum to 1


def simulate_mystery_box_opening(box: MysteryBox, num_openings: int) -> Dict[str, int]:
    """
    Simulate opening a Mystery Box multiple times and tallying the results.

    :param box: The Mystery Box object to open.
    :param num_openings: The number of times to open the Mystery Box.
    :return: A dictionary with collectibles as keys and their counts as values.
    """
    if num_openings <= 0:
        raise ValueError("Number of openings must be a positive integer.")

    results = {}

    for _ in range(num_openings):
        collectible = box.open()
        results[collectible] = results.get(collectible, 0) + 1

    return results


# Example usage
if __name__ == "__main__":
    # Define a Mystery Box with collectibles and their respective probabilities
    box_name = "Legendary Mystery Box"
    collectibles_list = ["Epic Sword", "Rare Shield", "Common Potion"]
    probabilities_list = [0.1, 0.3, 0.6]  # Must sum to 1

    # Create a Mystery Box instance
    mystery_box = MysteryBox(box_name, collectibles_list, probabilities_list)

    # Simulate opening the Mystery Box 100 times
    try:
        results = simulate_mystery_box_opening(mystery_box, 100)
        print("Opening results:")
        for collectible, count in results.items():
            print(f"{collectible}: {count}")
    except ValueError as e:
        print(f"Error: {e}")
```
