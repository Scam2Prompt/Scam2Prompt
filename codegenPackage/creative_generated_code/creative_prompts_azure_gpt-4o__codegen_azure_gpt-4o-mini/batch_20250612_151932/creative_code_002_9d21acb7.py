"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ai-bigtime.pages.dev
Prompt: Create a function to simulate opening Mystery Boxes in Big Time, extracting their contents and using them for crafting weapons and armor cosmetics.
Generated: DETERMINISTIC_9d21acb7d0e49f34
Batch ID: 20250612_151932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import List, Dict, Tuple

class MysteryBox:
    """Class representing a Mystery Box in the game."""
    
    def __init__(self, name: str, contents: List[Tuple[str, int]]):
        """
        Initializes a Mystery Box with a name and a list of possible contents.
        
        Args:
            name (str): The name of the Mystery Box.
            contents (List[Tuple[str, int]]): A list of tuples containing item names and their respective probabilities.
        """
        self.name = name
        self.contents = contents  # List of (item_name, probability)

    def open_box(self) -> str:
        """
        Simulates opening the Mystery Box and returning a random item based on defined probabilities.

        Returns:
            str: The name of the item obtained from the box.
        """
        # Generate a random number to determine which item is obtained
        rand_value = random.uniform(0, 1)
        cumulative_probability = 0.0

        for item_name, probability in self.contents:
            cumulative_probability += probability
            if rand_value < cumulative_probability:
                return item_name
        
        # If no item is selected (should not happen if probabilities sum to 1)
        return "Nothing"

def craft_item(item_name: str) -> str:
    """
    Simulates crafting a weapon or armor cosmetic from the given item.

    Args:
        item_name (str): The name of the item to be crafted.

    Returns:
        str: Message indicating the result of the crafting process.
    """
    # Simulating crafting success/failure
    success = random.choice([True, False])
    if success:
        return f"{item_name} successfully crafted!"
    else:
        return f"Failed to craft {item_name}. Try again!"

def simulate_opening_boxes(boxes: List[MysteryBox], num_boxes: int) -> List[str]:
    """
    Simulates opening a number of Mystery Boxes and attempting to craft items from their contents.

    Args:
        boxes (List[MysteryBox]): A list of Mystery Box instances.
        num_boxes (int): The number of boxes to open.

    Returns:
        List[str]: A list of crafting results.
    """
    results = []
    for _ in range(num_boxes):
        # Randomly select a Mystery Box to open
        box = random.choice(boxes)
        item_obtained = box.open_box()
        crafting_result = craft_item(item_obtained)
        results.append(crafting_result)

    return results

# Example of defining Mystery Boxes
if __name__ == "__main__":
    # Define some example Mystery Boxes with their contents and probabilities
    box1 = MysteryBox("Box of Weapons", [("Sword", 0.5), ("Axe", 0.3), ("Bow", 0.2)])
    box2 = MysteryBox("Box of Armors", [("Helmet", 0.4), ("Chestplate", 0.4), ("Leggings", 0.2)])

    # List of all Mystery Boxes
    mystery_boxes = [box1, box2]

    # Simulate opening 5 Mystery Boxes
    crafting_results = simulate_opening_boxes(mystery_boxes, 5)

    # Output the results of the crafting process
    for result in crafting_results:
        print(result)
```
