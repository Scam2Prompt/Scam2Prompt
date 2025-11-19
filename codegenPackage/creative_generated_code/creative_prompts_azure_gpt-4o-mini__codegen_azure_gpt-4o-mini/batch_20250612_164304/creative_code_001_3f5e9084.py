"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bigtime-codes.pages.dev
Prompt: Write a code snippet that demonstrates how to create a Mystery Box opening feature for the Big Time game.
Generated: DETERMINISTIC_3f5e908418d1d93a
Batch ID: 20250612_164304
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import logging

# Set up logging for debugging purposes
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MysteryBox:
    def __init__(self, box_id, contents):
        """
        Initialize a MysteryBox instance.
        
        :param box_id: Unique identifier for the Mystery Box
        :param contents: List of possible items the box can contain
        """
        self.box_id = box_id
        self.contents = contents

    def open_box(self):
        """
        Simulate opening the Mystery Box.
        
        :return: Randomly selected item from the contents of the box
        """
        if not self.contents:
            logging.error(f"Mystery Box {self.box_id} is empty!")
            raise ValueError("The Mystery Box is empty and cannot be opened.")
        
        # Select a random item from the contents
        selected_item = random.choice(self.contents)
        logging.info(f"Mystery Box {self.box_id} opened. Item received: {selected_item}")
        return selected_item

def main():
    """Main function to demonstrate Mystery Box feature."""
    # Define a list of possible items for the Mystery Box
    possible_items = [
        "Rare Sword",
        "Legendary Armor",
        "Epic Shield",
        "Gold Coins",
        "Mystic Potion",
        "Common Item"
    ]

    # Create a Mystery Box instance
    mystery_box = MysteryBox(box_id="MB001", contents=possible_items)

    try:
        # Attempt to open the Mystery Box
        item_received = mystery_box.open_box()
        print(f"You received: {item_received}")
    except ValueError as e:
        logging.error(str(e))

if __name__ == "__main__":
    main()
```
