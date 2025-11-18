"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bigtimecodes.pages.dev
Prompt: Create a tool that opens Mystery Boxes in Big Time, extracts their contents, and categorizes items for crafting or upgrading.
Generated: DETERMINISTIC_ee2161446df52e7d
Batch ID: 20250612_150316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import random

# Simulated data for Mystery Box contents
MYSTERY_BOX_CONTENTS = [
    {"item_name": "Rare Gem", "type": "crafting"},
    {"item_name": "Ancient Scroll", "type": "upgrading"},
    {"item_name": "Mystic Feather", "type": "crafting"},
    {"item_name": "Enchanted Ink", "type": "upgrading"},
    {"item_name": "Golden Shard", "type": "crafting"},
    {"item_name": "Obsidian Fragment", "type": "upgrading"}
]

class MysteryBoxTool:
    """
    A tool to open Mystery Boxes, extract their contents, and categorize items for crafting or upgrading.
    """

    def __init__(self):
        """
        Initializes the MysteryBoxTool with empty categorized storage.
        """
        self.crafting_items = []
        self.upgrading_items = []

    def open_mystery_box(self):
        """
        Simulates opening a Mystery Box and retrieving its contents.
        
        Returns:
            dict: Randomly selected item from the predefined mystery box contents.
        """
        try:
            return random.choice(MYSTERY_BOX_CONTENTS)
        except Exception as e:
            raise RuntimeError(f"Error opening Mystery Box: {e}")

    def categorize_item(self, item):
        """
        Categorizes the given item into crafting or upgrading based on its type.
        
        Args:
            item (dict): Item to categorize, must include 'item_name' and 'type'.
        """
        try:
            if item["type"] == "crafting":
                self.crafting_items.append(item["item_name"])
            elif item["type"] == "upgrading":
                self.upgrading_items.append(item["item_name"])
            else:
                raise ValueError(f"Unknown item type: {item['type']}")
        except KeyError as e:
            raise KeyError(f"Item data missing required field: {e}")
        except Exception as e:
            raise RuntimeError(f"Error categorizing item: {e}")

    def run(self, num_boxes):
        """
        Opens a specified number of Mystery Boxes and categorizes their contents.
        
        Args:
            num_boxes (int): The number of Mystery Boxes to open.
        """
        try:
            for _ in range(num_boxes):
                item = self.open_mystery_box()
                self.categorize_item(item)
            self.display_results()
        except Exception as e:
            print(f"An error occurred during execution: {e}")

    def display_results(self):
        """
        Displays the categorized items to the user.
        """
        print("\nCategorized Items:")
        print("Crafting Items:")
        for item in self.crafting_items:
            print(f"- {item}")
        print("\nUpgrading Items:")
        for item in self.upgrading_items:
            print(f"- {item}")

if __name__ == "__main__":
    # Number of Mystery Boxes to open
    NUM_BOXES = 5

    # Create an instance of the tool and run it
    tool = MysteryBoxTool()
    tool.run(NUM_BOXES)
```
