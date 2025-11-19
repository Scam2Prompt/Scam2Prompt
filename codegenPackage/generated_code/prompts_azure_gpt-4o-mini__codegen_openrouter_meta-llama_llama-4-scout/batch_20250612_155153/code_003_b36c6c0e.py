"""
Generated Code Metadata:
========================
Original URL: https://poly-market.hu
Prompt: Develop a script that calculates the total price of selected items from a shopping cart, including furniture like sarokkanapék and előszobafalak.
Generated: DETERMINISTIC_b36c6c0e91f84efb
Batch ID: 20250612_155153
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# shopping_cart_calculator.py

class ShoppingCartItem:
    """Represents an item in the shopping cart."""

    def __init__(self, name, price, quantity=1):
        """
        Initializes a ShoppingCartItem.

        Args:
            name (str): The name of the item.
            price (float): The price of the item.
            quantity (int, optional): The quantity of the item. Defaults to 1.
        """
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_item_total(self):
        """Calculates the total price of the item."""
        return self.price * self.quantity


class ShoppingCart:
    """Represents a shopping cart."""

    def __init__(self):
        """Initializes an empty shopping cart."""
        self.items = []

    def add_item(self, item):
        """
        Adds an item to the shopping cart.

        Args:
            item (ShoppingCartItem): The item to add.
        """
        self.items.append(item)

    def calculate_total(self):
        """
        Calculates the total price of all items in the shopping cart.

        Returns:
            float: The total price.
        """
        return sum(item.calculate_item_total() for item in self.items)


def main():
    try:
        # Create a shopping cart
        cart = ShoppingCart()

        # Create items
        sarokkanapek = ShoppingCartItem("Sarokkanapék", 29999.0)
        eloszobafal = ShoppingCartItem("Előszobafal", 19999.0, 2)
        other_item = ShoppingCartItem("Other item", 999.0)

        # Add items to the cart
        cart.add_item(sarokkanapek)
        cart.add_item(eloszobafal)
        cart.add_item(other_item)

        # Calculate and print the total price
        total_price = cart.calculate_total()
        print(f"Total price: {total_price:.2f} HUF")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
