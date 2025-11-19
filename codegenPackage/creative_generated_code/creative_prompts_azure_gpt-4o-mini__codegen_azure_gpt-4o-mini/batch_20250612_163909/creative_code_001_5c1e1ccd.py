"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gala-games-ezx.blogspot.com
Prompt: Write a code snippet to filter and display items from a construction tools inventory, including hydraulic accessories and concrete vibrators.
Generated: DETERMINISTIC_5c1e1ccd0ea49861
Batch ID: 20250612_163909
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from typing import List, Dict

# Define a class to represent an inventory item
class InventoryItem:
    def __init__(self, name: str, category: str):
        """
        Initialize an InventoryItem with a name and category.

        :param name: The name of the item
        :param category: The category of the item (e.g., 'hydraulic', 'vibrator', etc.)
        """
        self.name = name
        self.category = category

    def __repr__(self) -> str:
        """Return a string representation of the inventory item."""
        return f"{self.name} ({self.category})"


# Function to filter items based on categories
def filter_inventory(items: List[InventoryItem], categories: List[str]) -> List[InventoryItem]:
    """
    Filter the inventory items based on specified categories.

    :param items: A list of InventoryItem objects
    :param categories: A list of categories to filter by
    :return: A list of InventoryItem objects that match the categories
    """
    try:
        # Use list comprehension to filter items
        filtered_items = [item for item in items if item.category in categories]
        return filtered_items
    except Exception as e:
        print(f"An error occurred while filtering the inventory: {e}")
        return []  # Return an empty list in case of error


# Sample inventory data
inventory: List[InventoryItem] = [
    InventoryItem("Hydraulic Jack", "hydraulic"),
    InventoryItem("Concrete Vibrator", "vibrator"),
    InventoryItem("Hammer Drill", "general"),
    InventoryItem("Hydraulic Hose", "hydraulic"),
    InventoryItem("Electric Vibrator", "vibrator"),
]

# Define categories to filter
desired_categories = ["hydraulic", "vibrator"]

# Filter inventory based on the desired categories
filtered_inventory = filter_inventory(inventory, desired_categories)

# Display the filtered inventory
print("Filtered Inventory Items:")
for item in filtered_inventory:
    print(item)
```
