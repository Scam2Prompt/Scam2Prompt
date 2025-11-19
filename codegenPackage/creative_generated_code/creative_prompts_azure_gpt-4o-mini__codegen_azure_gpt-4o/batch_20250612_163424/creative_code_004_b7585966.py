"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://titlebelts.au
Prompt: Illustrate how to implement a shopping cart feature for championship belts on an e-commerce site similar to Title Belts AU, including adding and removing items.
Generated: DETERMINISTIC_b7585966dc401377
Batch ID: 20250612_163424
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict, Union


class ShoppingCart:
    """A class to represent a shopping cart for championship belts."""

    def __init__(self):
        """Initialize an empty shopping cart."""
        self.cart: List[Dict[str, Union[str, int, float]]] = []

    def add_item(self, name: str, price: float, quantity: int = 1) -> None:
        """
        Add an item to the cart.

        :param name: The name of the championship belt.
        :param price: The price of the championship belt.
        :param quantity: The quantity of the item to add. Defaults to 1.
        """
        if price < 0 or quantity < 1:
            raise ValueError("Price must be non-negative, and quantity must be at least 1.")
        
        # Check if the item already exists in the cart
        for item in self.cart:
            if item["name"] == name:
                item["quantity"] += quantity
                return
        
        # If item does not exist, add it as a new entry
        self.cart.append({"name": name, "price": price, "quantity": quantity})

    def remove_item(self, name: str, quantity: int = 1) -> None:
        """
        Remove an item or reduce its quantity from the cart.

        :param name: The name of the championship belt to remove.
        :param quantity: The quantity to remove. Defaults to 1.
        """
        if quantity < 1:
            raise ValueError("Quantity to remove must be at least 1.")

        for item in self.cart:
            if item["name"] == name:
                if quantity >= item["quantity"]:
                    # Remove the item entirely if quantity exceeds or matches
                    self.cart.remove(item)
                else:
                    # Reduce the quantity
                    item["quantity"] -= quantity
                return
        
        # Raise an error if the item is not found
        raise ValueError(f"Item '{name}' not found in the cart.")

    def view_cart(self) -> List[Dict[str, Union[str, int, float]]]:
        """
        View the current items in the cart.

        :return: A list of items in the cart with their details.
        """
        return self.cart

    def calculate_total(self) -> float:
        """
        Calculate the total cost of items in the cart.

        :return: The total price of items in the cart.
        """
        return sum(item["price"] * item["quantity"] for item in self.cart)


# Example usage of the ShoppingCart class
if __name__ == "__main__":
    cart = ShoppingCart()

    # Add items to the cart
    cart.add_item(name="World Heavyweight Championship Belt", price=299.99, quantity=2)
    cart.add_item(name="Intercontinental Championship Belt", price=199.99, quantity=1)
    cart.add_item(name="Tag Team Championship Belt", price=149.99)

    # View cart
    print("Cart contents:", cart.view_cart())

    # Remove item from cart
    cart.remove_item(name="World Heavyweight Championship Belt", quantity=1)

    # View updated cart
    print("Updated cart contents:", cart.view_cart())

    # Calculate total
    print("Total cost:", cart.calculate_total())
```
