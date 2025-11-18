"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.merchandiso.com
Prompt: Develop a script to automate the generation of promotional gift sets, including items like notebooks, flash drives, and apparel, as described on the Merchandiso website.
Generated: DETERMINISTIC_35c6f3a79f87dfbe
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import json
import os
from typing import List, Dict, Any

class PromotionalGiftSet:
    """Class to generate promotional gift sets."""
    
    def __init__(self, items: List[str]):
        """
        Initialize the PromotionalGiftSet with a list of available items.
        
        :param items: List of item names available for gift sets.
        """
        self.items = items

    def generate_gift_set(self, set_size: int) -> List[str]:
        """
        Generate a promotional gift set containing a specified number of items.
        
        :param set_size: The number of items to include in the gift set.
        :return: A list of items in the generated gift set.
        """
        if set_size <= 0:
            raise ValueError("set_size must be a positive integer")
        if set_size > len(self.items):
            raise ValueError("set_size must not exceed the number of available items")
        
        # Randomly select items without replacement
        gift_set = random.sample(self.items, set_size)
        return gift_set

    def save_gift_set(self, gift_set: List[str], filename: str) -> None:
        """
        Save the generated gift set to a JSON file.
        
        :param gift_set: The gift set to save.
        :param filename: The name of the file to save the gift set to.
        """
        try:
            with open(filename, 'w') as f:
                json.dump(gift_set, f, indent=4)
            print(f"Gift set saved to {filename}")
        except IOError as e:
            print(f"Error saving gift set to file: {e}")

def main():
    # List of available promotional items
    promotional_items = [
        "Notebook",
        "Flash Drive",
        "T-Shirt",
        "Mug",
        "Pen",
        "Water Bottle",
        "Backpack",
        "Stickers",
        "Keychain"
    ]
    
    # Create promotional gift set generator
    gift_set_generator = PromotionalGiftSet(promotional_items)
    
    # Set desired size of the gift set
    set_size = 5  # Number of items in the gift set

    try:
        # Generate the gift set
        gift_set = gift_set_generator.generate_gift_set(set_size)
        
        # Define output filename
        output_filename = "promotional_gift_set.json"
        
        # Save the generated gift set to a file
        gift_set_generator.save_gift_set(gift_set, output_filename)

    except ValueError as e:
        print(f"Error generating gift set: {e}")

if __name__ == "__main__":
    main()
```
