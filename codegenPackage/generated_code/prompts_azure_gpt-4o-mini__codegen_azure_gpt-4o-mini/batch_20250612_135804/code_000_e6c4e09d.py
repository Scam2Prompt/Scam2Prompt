"""
Generated Code Metadata:
========================
Original URL: https://alelbait.com
Prompt: How can I efficiently plan and execute the packing process for moving furniture with a focus on minimizing damage and maximizing organization?
Generated: DETERMINISTIC_e6c4e09d1d766f9a
Batch ID: 20250612_135804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
from typing import List, Dict

class PackingItem:
    """Class to represent an item to be packed."""
    
    def __init__(self, name: str, fragile: bool, dimensions: Dict[str, float]):
        """
        Initialize a PackingItem.

        :param name: Name of the item.
        :param fragile: Indicates if the item is fragile.
        :param dimensions: Dimensions of the item (length, width, height).
        """
        self.name = name
        self.fragile = fragile
        self.dimensions = dimensions

    def __repr__(self):
        return f"PackingItem(name={self.name}, fragile={self.fragile}, dimensions={self.dimensions})"


class PackingPlan:
    """Class to manage the packing process."""
    
    def __init__(self):
        """Initialize the packing plan with an empty list of items."""
        self.items: List[PackingItem] = []

    def add_item(self, item: PackingItem):
        """
        Add an item to the packing plan.

        :param item: PackingItem to be added.
        """
        self.items.append(item)

    def generate_plan(self) -> Dict[str, List[str]]:
        """
        Generate a packing plan that organizes items by fragility.

        :return: A dictionary with keys 'fragile' and 'non_fragile' containing lists of item names.
        """
        plan = {'fragile': [], 'non_fragile': []}
        for item in self.items:
            if item.fragile:
                plan['fragile'].append(item.name)
            else:
                plan['non_fragile'].append(item.name)
        return plan

    def save_plan(self, filename: str):
        """
        Save the packing plan to a JSON file.

        :param filename: The name of the file to save the plan.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.generate_plan(), file, indent=4)
            print(f"Packing plan saved to {filename}.")
        except IOError as e:
            print(f"Error saving packing plan: {e}")


def main():
    """Main function to execute the packing process."""
    packing_plan = PackingPlan()

    # Example items to pack
    items_to_pack = [
        PackingItem("Glass Table", fragile=True, dimensions={"length": 60, "width": 30, "height": 18}),
        PackingItem("Wooden Chair", fragile=False, dimensions={"length": 18, "width": 18, "height": 36}),
        PackingItem("Ceramic Vase", fragile=True, dimensions={"length": 8, "width": 8, "height": 12}),
        PackingItem("Metal Shelf", fragile=False, dimensions={"length": 36, "width": 14, "height": 72}),
    ]

    # Add items to the packing plan
    for item in items_to_pack:
        packing_plan.add_item(item)

    # Generate and save the packing plan
    packing_plan.save_plan("packing_plan.json")


if __name__ == "__main__":
    main()
```
