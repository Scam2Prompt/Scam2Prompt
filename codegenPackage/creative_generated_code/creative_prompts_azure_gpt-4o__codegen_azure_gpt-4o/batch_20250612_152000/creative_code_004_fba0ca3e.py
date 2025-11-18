"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://autopecasbrazz.blogspot.com
Prompt: Write code to generate a shopping cart system for automotive parts, including support for unitary and set pricing, as seen on "autopecasbrazz."
Generated: DETERMINISTIC_fba0ca3ef55f8b39
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Shopping Cart System for Automotive Parts
Author: Expert Programmer
Description: This script implements a shopping cart system that supports both unitary and set pricing for automotive parts.
"""

from typing import List


class Item:
    """
    Represents an item in the store.
    Attributes:
        name (str): The name of the item.
        unit_price (float): The price of a single unit of the item.
        set_price (float): The price of a predefined set of items (optional).
        set_quantity (int): The quantity of items that constitute a set for set pricing (optional).
    """

    def __init__(self, name: str, unit_price: float, set_price: float = None, set_quantity: int = None):
        if unit_price <= 0:
            raise ValueError("Unit price must be positive.")
        if set_price and set_price <= 0:
            raise ValueError("Set price must be positive if provided.")
        if set_quantity and set_quantity <= 0:
            raise ValueError("Set quantity must be positive if provided.")

        self.name = name
        self.unit_price = unit_price
        self.set_price = set_price
        self.set_quantity = set_quantity


class ShoppingCart:
    """
    Represents a shopping cart.
    Attributes:
        items (List[dict]): A list that keeps track of items added to the cart.
    """

    def __init__(self):
        self.items = []

    def add_item(self, item: Item, quantity: int):
        """
        Adds an item to the shopping cart.

        Args:
            item (Item): The item to be added.
            quantity (int): The quantity of the item to be added.

        Raises:
            ValueError: If the quantity is not positive.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")

        self.items.append({"item": item, "quantity": quantity})

    def calculate_total(self) -> float:
        """
        Calculates the total price of items in the shopping cart.

        Returns:
            float: The total price of all items in the cart.
        """
        total = 0.0

        for entry in self.items:
            item = entry["item"]
            quantity = entry["quantity"]

            if item.set_price and item.set_quantity:
                sets = quantity // item.set_quantity
                remaining_units = quantity % item.set_quantity
                total += sets * item.set_price + remaining_units * item.unit_price
            else:
                total += quantity * item.unit_price

        return total

    def display_cart(self):
        """
        Displays the contents of the shopping cart.
        """
        print("Shopping Cart:")
        for entry in self.items:
            item = entry["item"]
            quantity = entry["quantity"]
            print(f"{item.name}: Quantity={quantity}, Unit Price={item.unit_price:.2f}")
            if item.set_price and item.set_quantity:
                print(f"  Set Pricing: {item.set_quantity} for {item.set_price:.2f}")
        print(f"Total Price: {self.calculate_total():.2f}")


# Example usage
if __name__ == "__main__":
    try:
        # Create items
        spark_plug = Item(name="Spark Plug", unit_price=15.99, set_price=60.00, set_quantity=5)
        oil_filter = Item(name="Oil Filter", unit_price=9.99)

        # Create shopping cart
        cart = ShoppingCart()

        # Add items to cart
        cart.add_item(spark_plug, quantity=10)
        cart.add_item(oil_filter, quantity=3)

        # Display cart and total
        cart.display_cart()
    except Exception as e:
        print(f"Error: {e}")
```
