"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://logingalagames-io.blogspot.com
Prompt: How can I implement a filtering system for furniture products based on price and relevance, as seen on the Móveis Campo Largo site?
Generated: DETERMINISTIC_fb8e4b8a25b4a871
Batch ID: 20250612_160553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict, Any

class Furniture:
    """
    Class to represent a furniture item.

    Attributes:
        id (int): Unique identifier for the furniture item.
        name (str): Name of the furniture item.
        price (float): Price of the furniture item.
        relevance_score (float): Relevance score based on certain criteria.
    """

    def __init__(self, id: int, name: str, price: float, relevance_score: float):
        self.id = id
        self.name = name
        self.price = price
        self.relevance_score = relevance_score

    def __repr__(self) -> str:
        return f"Furniture(id={self.id}, name='{self.name}', price={self.price}, relevance_score={self.relevance_score})"


class FurnitureFilter:
    """
    Class to filter furniture items based on price range and relevance score.

    Attributes:
        furniture_list (List[Furniture]): List of furniture items to filter.
    """

    def __init__(self, furniture_list: List[Furniture]):
        self.furniture_list = furniture_list

    def filter_by_price(self, min_price: float, max_price: float) -> List[Furniture]:
        """
        Filter furniture items by a given price range.

        Args:
            min_price (float): Minimum price for filtering.
            max_price (float): Maximum price for filtering.

        Returns:
            List[Furniture]: Filtered list of furniture items within the specified price range.
        """
        if min_price < 0 or max_price < 0:
            raise ValueError("Price values must be non-negative.")
        if min_price > max_price:
            raise ValueError("Minimum price cannot be greater than maximum price.")

        return [item for item in self.furniture_list if min_price <= item.price <= max_price]

    def filter_by_relevance(self, min_relevance: float) -> List[Furniture]:
        """
        Filter furniture items by a minimum relevance score.

        Args:
            min_relevance (float): Minimum relevance score for filtering.

        Returns:
            List[Furniture]: Filtered list of furniture items with a relevance score above the specified threshold.
        """
        if min_relevance < 0:
            raise ValueError("Relevance score must be non-negative.")

        return [item for item in self.furniture_list if item.relevance_score >= min_relevance]

    def filter_furniture(self, min_price: float, max_price: float, min_relevance: float) -> List[Furniture]:
        """
        Filter furniture items by both price range and relevance score.

        Args:
            min_price (float): Minimum price for filtering.
            max_price (float): Maximum price for filtering.
            min_relevance (float): Minimum relevance score for filtering.

        Returns:
            List[Furniture]: Filtered list of furniture items that satisfy both criteria.
        """
        price_filtered = self.filter_by_price(min_price, max_price)
        return self.filter_by_relevance(min_relevance)


# Example usage:
if __name__ == "__main__":
    # Sample furniture items
    furniture_items = [
        Furniture(1, "Sofa", 299.99, 4.5),
        Furniture(2, "Chair", 99.99, 3.8),
        Furniture(3, "Table", 149.99, 4.0),
        Furniture(4, "Desk", 199.99, 4.8),
        Furniture(5, "Bookshelf", 89.99, 4.0),
    ]

    # Initialize the furniture filter with sample items
    filter_system = FurnitureFilter(furniture_items)

    # Set filtering criteria
    min_price = 100.00
    max_price = 300.00
    min_relevance = 4.0

    # Perform filtering
    try:
        filtered_items = filter_system.filter_furniture(min_price, max_price, min_relevance)
        print("Filtered Furniture Items:")
        for item in filtered_items:
            print(item)
    except ValueError as e:
        print(f"Error: {e}")
```
