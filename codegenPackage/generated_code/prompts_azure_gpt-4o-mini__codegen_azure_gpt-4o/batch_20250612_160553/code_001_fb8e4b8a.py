"""
Generated Code Metadata:
========================
Original URL: https://logingalagames-io.blogspot.com
Prompt: How can I implement a filtering system for furniture products based on price and relevance, as seen on the Móveis Campo Largo site?
Generated: DETERMINISTIC_fb8e4b8a25b4a871
Batch ID: 20250612_160553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# furniture_filtering_system.py

from typing import List, Dict

class FurnitureItem:
    """
    Represents a furniture item with attributes for filtering.
    """
    def __init__(self, name: str, price: float, relevance: int):
        """
        Initialize a furniture item.

        :param name: Name of the furniture item.
        :param price: Price of the furniture item.
        :param relevance: Relevance score of the furniture item (higher is more relevant).
        """
        self.name = name
        self.price = price
        self.relevance = relevance

    def __repr__(self):
        """
        String representation of the furniture item.
        """
        return f"FurnitureItem(name={self.name}, price={self.price}, relevance={self.relevance})"


def filter_furniture(items: List[FurnitureItem], max_price: float = None, sort_by: str = "relevance") -> List[FurnitureItem]:
    """
    Filters and sorts furniture items based on price and relevance.

    :param items: List of furniture items to filter and sort.
    :param max_price: Maximum price for filtering items. If None, no price filtering is applied.
    :param sort_by: Sorting criteria - "price" or "relevance". Defaults to "relevance".
    :return: Filtered and sorted list of furniture items.
    """
    # Validate sorting criteria
    if sort_by not in ["price", "relevance"]:
        raise ValueError("Invalid sort_by value. Must be 'price' or 'relevance'.")

    # Filter items based on max_price
    if max_price is not None:
        items = [item for item in items if item.price <= max_price]

    # Sort items based on the specified criteria
    if sort_by == "price":
        items.sort(key=lambda x: x.price)  # Sort by price (ascending)
    elif sort_by == "relevance":
        items.sort(key=lambda x: x.relevance, reverse=True)  # Sort by relevance (descending)

    return items


# Example usage
if __name__ == "__main__":
    # Sample furniture items
    furniture_items = [
        FurnitureItem(name="Sofa", price=500.0, relevance=90),
        FurnitureItem(name="Dining Table", price=300.0, relevance=80),
        FurnitureItem(name="Chair", price=100.0, relevance=70),
        FurnitureItem(name="Bed", price=700.0, relevance=95),
    ]

    # Filter and sort furniture items
    try:
        filtered_items = filter_furniture(furniture_items, max_price=500.0, sort_by="relevance")
        print("Filtered and sorted furniture items:")
        for item in filtered_items:
            print(item)
    except ValueError as e:
        print(f"Error: {e}")
```
