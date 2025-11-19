"""
Generated Code Metadata:
========================
Original URL: https://acula.com.ua
Prompt: Generate a code snippet for an e-commerce website that allows users to filter diving gear by category, such as wetsuits, fins, and masks, similar to the product categorization found on acula.com.ua.
Generated: DETERMINISTIC_70c1414bdad66f4f
Batch ID: 20250612_163243
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# diving_gear_filter.py

from enum import Enum
from typing import List, Dict

class DivingGearCategory(str, Enum):
    """Enum for diving gear categories."""
    WETSUITS = "wetsuits"
    FINS = "fins"
    MASKS = "masks"
    REGULATORS = "regulators"
    BCDs = "bcds"

class DivingGear:
    """Class representing diving gear."""
    def __init__(self, name: str, category: DivingGearCategory, price: float):
        """
        Initialize diving gear.

        Args:
        - name (str): Name of the gear.
        - category (DivingGearCategory): Category of the gear.
        - price (float): Price of the gear.
        """
        self.name = name
        self.category = category
        self.price = price

class DivingGearFilter:
    """Class for filtering diving gear by category."""
    def __init__(self, gear_list: List[DivingGear]):
        """
        Initialize the filter with a list of diving gear.

        Args:
        - gear_list (List[DivingGear]): List of diving gear.
        """
        self.gear_list = gear_list

    def filter_by_category(self, category: DivingGearCategory) -> List[DivingGear]:
        """
        Filter diving gear by category.

        Args:
        - category (DivingGearCategory): Category to filter by.

        Returns:
        - List[DivingGear]: List of diving gear in the specified category.

        Raises:
        - ValueError: If the category is not a valid DivingGearCategory.
        """
        if not isinstance(category, DivingGearCategory):
            raise ValueError("Invalid category")

        return [gear for gear in self.gear_list if gear.category == category]

    def get_categories(self) -> List[DivingGearCategory]:
        """
        Get all unique categories in the gear list.

        Returns:
        - List[DivingGearCategory]: List of unique categories.
        """
        return list(set(gear.category for gear in self.gear_list))

def main():
    # Example usage
    gear_list = [
        DivingGear("Wetsuit X", DivingGearCategory.WETSUITS, 200.0),
        DivingGear("Fin Y", DivingGearCategory.FINS, 50.0),
        DivingGear("Mask Z", DivingGearCategory.MASKS, 30.0),
        DivingGear("Regulator A", DivingGearCategory.REGULATORS, 300.0),
        DivingGear("BCD B", DivingGearCategory.BCDs, 400.0),
    ]

    filter = DivingGearFilter(gear_list)

    print("Categories:")
    for category in filter.get_categories():
        print(category)

    print("\nWetsuits:")
    for gear in filter.filter_by_category(DivingGearCategory.WETSUITS):
        print(f"- {gear.name}: ${gear.price:.2f}")

if __name__ == "__main__":
    main()
```
