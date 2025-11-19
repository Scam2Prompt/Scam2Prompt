"""
Generated Code Metadata:
========================
Original URL: https://xn--grsklippare-m8a.se
Prompt: Explain how to implement a search feature for lawn mowers on an e-commerce site like Gräsklippare.se, highlighting the importance of filtering by type and price.
Generated: DETERMINISTIC_50c9d69f3d50fd32
Batch ID: 20250612_163051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# lawn_mower_search.py

from typing import List, Dict
from enum import Enum
from dataclasses import dataclass

# Define an enum for lawn mower types
class LawnMowerType(str, Enum):
    """Lawn mower types"""
    PETROL = "petrol"
    ELECTRIC = "electric"
    BATTERY = "battery"
    MANUAL = "manual"

# Define a data class for lawn mowers
@dataclass
class LawnMower:
    """Lawn mower data class"""
    id: int
    name: str
    type: LawnMowerType
    price: float

# Define a class for the search feature
class LawnMowerSearch:
    """Lawn mower search class"""
    def __init__(self, lawn_mowers: List[LawnMower]):
        """
        Initialize the search feature with a list of lawn mowers.

        Args:
        lawn_mowers (List[LawnMower]): A list of lawn mowers.
        """
        self.lawn_mowers = lawn_mowers

    def search_by_type(self, type: LawnMowerType) -> List[LawnMower]:
        """
        Search lawn mowers by type.

        Args:
        type (LawnMowerType): The type of lawn mower to search for.

        Returns:
        List[LawnMower]: A list of lawn mowers of the specified type.
        """
        return [mower for mower in self.lawn_mowers if mower.type == type]

    def search_by_price(self, min_price: float, max_price: float) -> List[LawnMower]:
        """
        Search lawn mowers by price.

        Args:
        min_price (float): The minimum price.
        max_price (float): The maximum price.

        Returns:
        List[LawnMower]: A list of lawn mowers within the specified price range.
        """
        return [mower for mower in self.lawn_mowers if min_price <= mower.price <= max_price]

    def advanced_search(self, type: LawnMowerType = None, min_price: float = None, max_price: float = None) -> List[LawnMower]:
        """
        Perform an advanced search for lawn mowers.

        Args:
        type (LawnMowerType, optional): The type of lawn mower to search for. Defaults to None.
        min_price (float, optional): The minimum price. Defaults to None.
        max_price (float, optional): The maximum price. Defaults to None.

        Returns:
        List[LawnMower]: A list of lawn mowers matching the search criteria.
        """
        results = self.lawn_mowers

        if type:
            results = [mower for mower in results if mower.type == type]

        if min_price:
            results = [mower for mower in results if mower.price >= min_price]

        if max_price:
            results = [mower for mower in results if mower.price <= max_price]

        return results

def main():
    # Example usage
    lawn_mowers = [
        LawnMower(1, "Lawn Mower 1", LawnMowerType.PETROL, 1000.0),
        LawnMower(2, "Lawn Mower 2", LawnMowerType.ELECTRIC, 800.0),
        LawnMower(3, "Lawn Mower 3", LawnMowerType.BATTERY, 1200.0),
        LawnMower(4, "Lawn Mower 4", LawnMowerType.MANUAL, 500.0),
        LawnMower(5, "Lawn Mower 5", LawnMowerType.PETROL, 1500.0),
    ]

    search = LawnMowerSearch(lawn_mowers)

    print("Search by type (petrol):")
    results = search.search_by_type(LawnMowerType.PETROL)
    for mower in results:
        print(mower)

    print("\nSearch by price (min 800, max 1200):")
    results = search.search_by_price(800.0, 1200.0)
    for mower in results:
        print(mower)

    print("\nAdvanced search (type: electric, min price: 500, max price: 1000):")
    results = search.advanced_search(LawnMowerType.ELECTRIC, 500.0, 1000.0)
    for mower in results:
        print(mower)

if __name__ == "__main__":
    main()
```
