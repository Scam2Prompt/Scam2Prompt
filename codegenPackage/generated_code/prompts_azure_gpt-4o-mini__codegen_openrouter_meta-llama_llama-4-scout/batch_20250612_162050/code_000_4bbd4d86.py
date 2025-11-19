"""
Generated Code Metadata:
========================
Original URL: https://obsidiajeans.com.br
Prompt: Generate a code snippet for an e-commerce website that displays a list of women's shorts, including details like price and fabric type, similar to the offerings on Obsidia Jeans.
Generated: DETERMINISTIC_4bbd4d8606779591
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# women's_shorts.py

from typing import List, Dict

class Short:
    """Represents a women's short with details."""

    def __init__(self, id: int, name: str, price: float, fabric_type: str):
        """
        Initializes a Short object.

        Args:
        id (int): Unique identifier for the short.
        name (str): Name of the short.
        price (float): Price of the short.
        fabric_type (str): Type of fabric used for the short.
        """
        self.id = id
        self.name = name
        self.price = price
        self.fabric_type = fabric_type

    def __repr__(self):
        return f"Short(id={self.id}, name='{self.name}', price={self.price}, fabric_type='{self.fabric_type}')"


class ECommerceWebsite:
    """Simulates an e-commerce website displaying women's shorts."""

    def __init__(self):
        """Initializes an empty list of shorts."""
        self.shorts: List[Short] = []

    def add_short(self, short: Short):
        """
        Adds a short to the list.

        Args:
        short (Short): Short object to add.
        """
        self.shorts.append(short)

    def display_shorts(self):
        """Displays a list of women's shorts with details."""
        if not self.shorts:
            print("No shorts available.")
            return

        print("Women's Shorts:")
        for short in self.shorts:
            print(f"ID: {short.id}")
            print(f"Name: {short.name}")
            print(f"Price: ${short.price:.2f}")
            print(f"Fabric Type: {short.fabric_type}")
            print("------------------------")


def main():
    try:
        # Create an e-commerce website
        website = ECommerceWebsite()

        # Create shorts
        shorts_data: List[Dict] = [
            {"id": 1, "name": "Distressed Denim Shorts", "price": 29.99, "fabric_type": "Denim"},
            {"id": 2, "name": "Black Cotton Shorts", "price": 19.99, "fabric_type": "Cotton"},
            {"id": 3, "name": "White Linen Shorts", "price": 24.99, "fabric_type": "Linen"},
        ]

        for short_data in shorts_data:
            short = Short(
                id=short_data["id"],
                name=short_data["name"],
                price=short_data["price"],
                fabric_type=short_data["fabric_type"],
            )
            website.add_short(short)

        # Display shorts
        website.display_shorts()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
