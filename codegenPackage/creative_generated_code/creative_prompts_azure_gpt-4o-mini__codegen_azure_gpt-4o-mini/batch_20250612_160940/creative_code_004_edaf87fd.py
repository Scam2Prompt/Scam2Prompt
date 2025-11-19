"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://portal-bigtime.pages.dev
Prompt: Create a code snippet that integrates a Mystery Box opening mechanic into a game, inspired by the features described on the Big Time website.
Generated: DETERMINISTIC_edaf87fdfc141ab1
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import time

class MysteryBox:
    def __init__(self, box_id, items):
        """
        Initializes a MysteryBox instance.

        :param box_id: Unique identifier for the Mystery Box
        :param items: List of items that can be contained in the box
        """
        self.box_id = box_id
        self.items = items

    def open_box(self):
        """
        Simulates opening the mystery box and returns a random item.

        :return: Randomly selected item from the box's items
        """
        if not self.items:
            raise ValueError("The mystery box is empty.")
        
        # Simulate a slight delay for dramatic effect
        time.sleep(1)  # Represents the mystery box opening
        selected_item = random.choice(self.items)
        
        print(f"You've opened the Mystery Box {self.box_id} and received: {selected_item}")
        return selected_item

def main():
    """
    Main function to demonstrate the Mystery Box mechanic.
    """
    # Define some items for the mystery box
    box_items = [
        "Rare Sword",
        "Legendary Shield",
        "Potion of Healing",
        "Ancient Artifact",
        "Gold Coins"
    ]

    # Create an instance of MysteryBox
    mystery_box = MysteryBox(box_id=1, items=box_items)

    try:
        # Open the mystery box
        mystery_box.open_box()
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
