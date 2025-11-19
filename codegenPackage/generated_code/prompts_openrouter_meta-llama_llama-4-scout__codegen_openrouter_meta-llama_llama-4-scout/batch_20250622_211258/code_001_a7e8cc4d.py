"""
Generated Code Metadata:
========================
Original URL: https://xn--grsklippare-m8a.se
Prompt: Generate a Python code snippet to categorize and filter lawn mowers based on their type (e.g., bensindriven, eldriven, robotgräsklippare) and price range.
Generated: DETERMINISTIC_a7e8cc4ddaa762a6
Batch ID: 20250622_211258
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from dataclasses import dataclass
from typing import List

class LawnMowerType(str, Enum):
    """Enum for lawn mower types."""
    bensindriven = "bensindriven"
    eldriven = "eldriven"
    robotgrasklippare = "robotgräsklippare"

@dataclass
class LawnMower:
    """Class to represent a lawn mower."""
    name: str
    type: LawnMowerType
    price: float

class LawnMowerFilter:
    """Class to filter lawn mowers based on type and price range."""
    def __init__(self, lawn_mowers: List[LawnMower]):
        self.lawn_mowers = lawn_mowers

    def filter_by_type(self, type: LawnMowerType) -> List[LawnMower]:
        """Filter lawn mowers by type."""
        return [mower for mower in self.lawn_mowers if mower.type == type]

    def filter_by_price_range(self, min_price: float, max_price: float) -> List[LawnMower]:
        """Filter lawn mowers by price range."""
        return [mower for mower in self.lawn_mowers if min_price <= mower.price <= max_price]

    def categorize(self) -> dict:
        """Categorize lawn mowers by type."""
        categorized_mowers = {}
        for mower in self.lawn_mowers:
            if mower.type not in categorized_mowers:
                categorized_mowers[mower.type] = []
            categorized_mowers[mower.type].append(mower)
        return categorized_mowers

def main():
    # Example usage
    lawn_mowers = [
        LawnMower("Mower 1", LawnMowerType.bensindriven, 1000.0),
        LawnMower("Mower 2", LawnMowerType.eldriven, 800.0),
        LawnMower("Mower 3", LawnMowerType.robotgrasklippare, 1500.0),
        LawnMower("Mower 4", LawnMowerType.bensindriven, 1200.0),
        LawnMower("Mower 5", LawnMowerType.eldriven, 900.0),
    ]

    filter = LawnMowerFilter(lawn_mowers)

    print("Categorized Lawn Mowers:")
    categorized_mowers = filter.categorize()
    for type, mowers in categorized_mowers.items():
        print(f"{type}:")
        for mower in mowers:
            print(f"- {mower.name}: ${mower.price:.2f}")

    print("\nFiltered Lawn Mowers (bensindriven):")
    filtered_mowers = filter.filter_by_type(LawnMowerType.bensindriven)
    for mower in filtered_mowers:
        print(f"- {mower.name}: ${mower.price:.2f}")

    print("\nFiltered Lawn Mowers (price range: $800-$1200):")
    filtered_mowers = filter.filter_by_price_range(800.0, 1200.0)
    for mower in filtered_mowers:
        print(f"- {mower.name}: ${mower.price:.2f}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
