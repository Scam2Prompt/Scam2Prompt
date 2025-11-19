"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hoorainz.com
Prompt: Generate a Python script that creates a shopping cart for natural stone bracelets, similar to those offered by Hoorainz, including features for adding and removing items.
Generated: DETERMINISTIC_42a65858160653c8
Batch ID: 20250612_164310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Bracelet:
    """
    Represents a natural stone bracelet with a name and price.
    """
    def __init__(self, name: str, price: float):
        if price < 0:
            raise ValueError("Price cannot be negative.")
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"


class ShoppingCart:
    """
    Manages a shopping cart for natural stone bracelets.
    """
    def __init__(self):
        self.items = []

    def add_item(self, bracelet: Bracelet):
        """
        Adds a bracelet to the shopping cart.

        :param bracelet: An instance of Bracelet to add.
        """
        if not isinstance(bracelet, Bracelet):
            raise TypeError("Expected an instance of Bracelet.")
        self.items.append(bracelet)
        print(f"Added {bracelet} to the cart.")

    def remove_item(self, bracelet: Bracelet):
        """
        Removes a bracelet from the shopping cart.

        :param bracelet: An instance of Bracelet to remove.
        """
        try:
            self.items.remove(bracelet)
            print(f"Removed {bracelet} from the cart.")
        except ValueError:
            print(f"Bracelet {bracelet} not found in the cart.")

    def view_cart(self):
        """
        Displays the current items in the shopping cart.
        """
        if not self.items:
            print("Your cart is empty.")
            return

        print("Your Shopping Cart:")
        for bracelet in self.items:
            print(bracelet)
        total = self.calculate_total()
        print(f"Total: ${total:.2f}")

    def calculate_total(self) -> float:
        """
        Calculates the total price of items in the cart.

        :return: Total price as a float.
        """
        return sum(bracelet.price for bracelet in self.items)


if __name__ == "__main__":
    # Example usage
    cart = ShoppingCart()

    # Creating some bracelets
    bracelet1 = Bracelet("Amethyst Bracelet", 25.99)
    bracelet2 = Bracelet("Rose Quartz Bracelet", 19.99)

    # Adding items to the cart
    cart.add_item(bracelet1)
    cart.add_item(bracelet2)

    # Viewing the cart
    cart.view_cart()

    # Removing an item
    cart.remove_item(bracelet1)

    # Viewing the cart again
    cart.view_cart()

    # Attempting to remove an item that is not in the cart
    cart.remove_item(bracelet1)
```
