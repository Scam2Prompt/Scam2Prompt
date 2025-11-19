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
from typing import List, Dict

class ClothingItem:
    """Class representing a clothing item with attributes for name, popularity, and price."""
    
    def __init__(self, name: str, popularity: int, price: float):
        self.name = name
        self.popularity = popularity
        self.price = price

    def __repr__(self):
        return f"{self.name} (Popularity: {self.popularity}, Price: {self.price})"

def sort_clothing_items(items: List[ClothingItem], sort_by: str = 'popularity', ascending: bool = True) -> List[ClothingItem]:
    """
    Sorts a list of clothing items by the specified attribute.

    Args:
        items (List[ClothingItem]): The list of clothing items to sort.
        sort_by (str): The attribute to sort by ('popularity' or 'price').
        ascending (bool): If True, sort in ascending order; otherwise, sort in descending order.

    Returns:
        List[ClothingItem]: The sorted list of clothing items.

    Raises:
        ValueError: If sort_by is not 'popularity' or 'price'.
    """
    
    # Validate the sort_by parameter
    if sort_by not in ['popularity', 'price']:
        raise ValueError("sort_by must be either 'popularity' or 'price'.")

    # Sort the items based on the specified attribute
    return sorted(items, key=lambda item: getattr(item, sort_by), reverse=not ascending)

# Example usage
if __name__ == "__main__":
    # Create a list of clothing items
    clothing_items = [
        ClothingItem("T-Shirt", popularity=150, price=19.99),
        ClothingItem("Jeans", popularity=200, price=49.99),
        ClothingItem("Jacket", popularity=100, price=89.99),
        ClothingItem("Hat", popularity=250, price=15.99),
    ]

    # Sort by popularity in ascending order
    sorted_by_popularity = sort_clothing_items(clothing_items, sort_by='popularity', ascending=True)
    print("Sorted by popularity (ascending):", sorted_by_popularity)

    # Sort by price in descending order
    sorted_by_price = sort_clothing_items(clothing_items, sort_by='price', ascending=False)
    print("Sorted by price (descending):", sorted_by_price)
```
