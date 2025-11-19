"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://et-magiic-soll-enter-eth-9.blogspot.com
Prompt: Develop a code snippet that sorts clothing items by popularity and price, inspired by the sorting options available on Danda Loja's website.
Generated: DETERMINISTIC_f6fe81abbd05e0f9
Batch ID: 20250612_164223
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict

class ClothingItem:
    """Class representing a clothing item with attributes for name, price, and popularity."""
    
    def __init__(self, name: str, price: float, popularity: int):
        self.name = name
        self.price = price
        self.popularity = popularity

    def __repr__(self):
        return f"{self.name} (Price: {self.price}, Popularity: {self.popularity})"

def sort_clothing_items(items: List[ClothingItem], sort_by: str = 'popularity', reverse: bool = True) -> List[ClothingItem]:
    """
    Sorts a list of clothing items based on the specified attribute.

    Args:
        items (List[ClothingItem]): A list of clothing items to be sorted.
        sort_by (str): The attribute to sort by, either 'popularity' or 'price'.
        reverse (bool): If True, sorts in descending order; otherwise, ascending.

    Returns:
        List[ClothingItem]: The sorted list of clothing items.

    Raises:
        ValueError: If sort_by is not 'popularity' or 'price'.
    """
    
    # Validate the sort_by parameter
    if sort_by not in ['popularity', 'price']:
        raise ValueError("sort_by must be 'popularity' or 'price'")
    
    # Perform sorting based on the selected attribute
    sorted_items = sorted(items, key=lambda item: getattr(item, sort_by), reverse=reverse)
    return sorted_items

# Example usage
if __name__ == "__main__":
    # Create a list of clothing items
    clothing_items = [
        ClothingItem("T-Shirt", 19.99, 150),
        ClothingItem("Jeans", 49.99, 300),
        ClothingItem("Jacket", 89.99, 200),
        ClothingItem("Sneakers", 59.99, 250),
    ]

    # Sort items by popularity
    sorted_by_popularity = sort_clothing_items(clothing_items, sort_by='popularity')
    print("Sorted by popularity:")
    print(sorted_by_popularity)

    # Sort items by price
    sorted_by_price = sort_clothing_items(clothing_items, sort_by='price', reverse=False)
    print("\nSorted by price (ascending):")
    print(sorted_by_price)
```
