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
# clothing_item.py

class ClothingItem:
    """Represents a clothing item with name, price, and popularity."""

    def __init__(self, name: str, price: float, popularity: int):
        """
        Initializes a ClothingItem.

        Args:
            name (str): The name of the clothing item.
            price (float): The price of the clothing item.
            popularity (int): The popularity of the clothing item.
        """
        self.name = name
        self.price = price
        self.popularity = popularity

    def __repr__(self):
        return f"ClothingItem(name='{self.name}', price={self.price}, popularity={self.popularity})"


def sort_by_popularity(clothing_items: list[ClothingItem]) -> list[ClothingItem]:
    """
    Sorts clothing items by popularity in descending order.

    Args:
        clothing_items (list[ClothingItem]): A list of clothing items.

    Returns:
        list[ClothingItem]: A list of clothing items sorted by popularity.
    """
    return sorted(clothing_items, key=lambda item: item.popularity, reverse=True)


def sort_by_price(clothing_items: list[ClothingItem]) -> list[ClothingItem]:
    """
    Sorts clothing items by price in ascending order.

    Args:
        clothing_items (list[ClothingItem]): A list of clothing items.

    Returns:
        list[ClothingItem]: A list of clothing items sorted by price.
    """
    return sorted(clothing_items, key=lambda item: item.price)


def sort_by_popularity_and_price(clothing_items: list[ClothingItem]) -> list[ClothingItem]:
    """
    Sorts clothing items by popularity in descending order and then by price in ascending order.

    Args:
        clothing_items (list[ClothingItem]): A list of clothing items.

    Returns:
        list[ClothingItem]: A list of clothing items sorted by popularity and price.
    """
    return sorted(clothing_items, key=lambda item: (-item.popularity, item.price))


def main():
    try:
        # Example usage
        clothing_items = [
            ClothingItem("T-Shirt", 19.99, 100),
            ClothingItem("Jeans", 49.99, 50),
            ClothingItem("Dress", 29.99, 200),
            ClothingItem("Jacket", 79.99, 150),
        ]

        print("Sorting by popularity:")
        for item in sort_by_popularity(clothing_items):
            print(item)

        print("\nSorting by price:")
        for item in sort_by_price(clothing_items):
            print(item)

        print("\nSorting by popularity and price:")
        for item in sort_by_popularity_and_price(clothing_items):
            print(item)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
