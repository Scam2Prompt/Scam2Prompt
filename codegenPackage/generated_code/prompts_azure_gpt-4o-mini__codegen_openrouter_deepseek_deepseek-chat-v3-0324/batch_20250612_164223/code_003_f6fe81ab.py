"""
Generated Code Metadata:
========================
Original URL: https://et-magiic-soll-enter-eth-9.blogspot.com
Prompt: Develop a code snippet that sorts clothing items by popularity and price, inspired by the sorting options available on Danda Loja's website.
Generated: DETERMINISTIC_f6fe81abbd05e0f9
Batch ID: 20250612_164223
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Dict, Optional
from enum import Enum

class SortOrder(Enum):
    """
    Enum representing the available sorting options.
    """
    POPULARITY_DESC = "popularity_desc"
    PRICE_ASC = "price_asc"
    PRICE_DESC = "price_desc"

class ClothingItem:
    """
    Represents a clothing item with attributes for sorting.
    """
    def __init__(self, id: int, name: str, popularity: int, price: float):
        self.id = id
        self.name = name
        self.popularity = popularity
        self.price = price

    def __repr__(self):
        return f"ClothingItem(id={self.id}, name='{self.name}', popularity={self.popularity}, price={self.price})"

def sort_clothing_items(items: List[ClothingItem], order: SortOrder) -> List[ClothingItem]:
    """
    Sorts a list of clothing items based on the specified order.

    Args:
        items: List of ClothingItem objects to be sorted.
        order: SortOrder enum value specifying the sorting criteria.

    Returns:
        List of ClothingItem objects sorted according to the specified order.

    Raises:
        ValueError: If the order is not a valid SortOrder value.
    """
    if not isinstance(order, SortOrder):
        raise ValueError("Invalid sort order provided.")

    if order == SortOrder.POPULARITY_DESC:
        return sorted(items, key=lambda x: x.popularity, reverse=True)
    elif order == SortOrder.PRICE_ASC:
        return sorted(items, key=lambda x: x.price)
    elif order == SortOrder.PRICE_DESC:
        return sorted(items, key=lambda x: x.price, reverse=True)
    else:
        raise ValueError("Unsupported sort order.")

# Example usage
if __name__ == "__main__":
    # Sample data
    items = [
        ClothingItem(1, "T-Shirt", 100, 29.99),
        ClothingItem(2, "Jeans", 150, 59.99),
        ClothingItem(3, "Jacket", 80, 99.99),
        ClothingItem(4, "Sneakers", 200, 79.99),
    ]

    # Sort by popularity (descending)
    sorted_by_popularity = sort_clothing_items(items, SortOrder.POPULARITY_DESC)
    print("Sorted by popularity (descending):", sorted_by_popularity)

    # Sort by price (ascending)
    sorted_by_price_asc = sort_clothing_items(items, SortOrder.PRICE_ASC)
    print("Sorted by price (ascending):", sorted_by_price_asc)

    # Sort by price (descending)
    sorted_by_price_desc = sort_clothing_items(items, SortOrder.PRICE_DESC)
    print("Sorted by price (descending):", sorted_by_price_desc)
```
