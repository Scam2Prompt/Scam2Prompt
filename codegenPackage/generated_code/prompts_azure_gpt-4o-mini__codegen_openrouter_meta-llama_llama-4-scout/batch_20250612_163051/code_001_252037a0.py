"""
Generated Code Metadata:
========================
Original URL: https://xn--grsklippare-m8a.se
Prompt: Write a code snippet to filter lawn mowers by price and type, similar to the sorting options on Gräsklippare.se.
Generated: DETERMINISTIC_252037a0fb7b8bb6
Batch ID: 20250612_163051
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
    """Lawn mower types"""
    PETROL = "petrol"
    ELECTRIC = "electric"
    BATTERY = "battery"
    MANUAL = "manual"

@dataclass
class LawnMower:
    """Lawn mower data class"""
    name: str
    price: float
    type: LawnMowerType

class LawnMowerFilter:
    """Lawn mower filter class"""
    def __init__(self, lawn_mowers: List[LawnMower]):
        self.lawn_mowers = lawn_mowers

    def filter_by_price(self, min_price: float = None, max_price: float = None) -> List[LawnMower]:
        """Filter lawn mowers by price"""
        if min_price is not None and max_price is not None and min_price > max_price:
            raise ValueError("Min price cannot be greater than max price")

        filtered_mowers = [mower for mower in self.lawn_mowers 
                           if (min_price is None or mower.price >= min_price) 
                           and (max_price is None or mower.price <= max_price)]
        return filtered_mowers

    def filter_by_type(self, mower_type: LawnMowerType) -> List[LawnMower]:
        """Filter lawn mowers by type"""
        if not isinstance(mower_type, LawnMowerType):
            raise TypeError("Invalid lawn mower type")

        filtered_mowers = [mower for mower in self.lawn_mowers if mower.type == mower_type]
        return filtered_mowers

    def filter(self, min_price: float = None, max_price: float = None, mower_type: LawnMowerType = None) -> List[LawnMower]:
        """Filter lawn mowers by price and type"""
        filtered_mowers = self.lawn_mowers

        if min_price is not None or max_price is not None:
            filtered_mowers = self.filter_by_price(min_price, max_price)

        if mower_type is not None:
            filtered_mowers = self.filter_by_type(mower_type)

        return filtered_mowers

def main():
    # Create lawn mowers
    lawn_mowers = [
        LawnMower("Mower 1", 1000.0, LawnMowerType.PETROL),
        LawnMower("Mower 2", 800.0, LawnMowerType.ELECTRIC),
        LawnMower("Mower 3", 1200.0, LawnMowerType.BATTERY),
        LawnMower("Mower 4", 900.0, LawnMowerType.MANUAL),
        LawnMower("Mower 5", 1100.0, LawnMowerType.PETROL),
    ]

    # Create filter
    filter = LawnMowerFilter(lawn_mowers)

    # Filter by price
    print("Filtered by price (min 900, max 1100):")
    for mower in filter.filter_by_price(900.0, 1100.0):
        print(f"{mower.name}: {mower.price}, {mower.type}")

    # Filter by type
    print("\nFiltered by type (PETROL):")
    for mower in filter.filter_by_type(LawnMowerType.PETROL):
        print(f"{mower.name}: {mower.price}, {mower.type}")

    # Filter by price and type
    print("\nFiltered by price (min 800, max 1200) and type (ELECTRIC):")
    for mower in filter.filter(min_price=800.0, max_price=1200.0, mower_type=LawnMowerType.ELECTRIC):
        print(f"{mower.name}: {mower.price}, {mower.type}")

if __name__ == "__main__":
    main()
```
