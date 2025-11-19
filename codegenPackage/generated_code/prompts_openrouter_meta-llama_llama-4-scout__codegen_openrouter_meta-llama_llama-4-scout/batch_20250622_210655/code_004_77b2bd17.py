"""
Generated Code Metadata:
========================
Original URL: https://wouo.com.br
Prompt: Write a code to calculate the total cost of a shopping cart containing items like syringes, nebulizer kits, and inhaler accessories, considering discounts and shipping costs.
Generated: DETERMINISTIC_77b2bd174d10e0e6
Batch ID: 20250622_210655
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

    def __init__(self, name, price, quantity):
        """
        Initializes a ShoppingCartItem.

        Args:
            name (str): The name of the item.
            price (float): The price of the item.
            quantity (int): The quantity of the item.
        """
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_subtotal(self):
        """Calculates the subtotal for the item."""
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

    def calculate_subtotal(self):
        """Calculates the subtotal for all items in the cart."""
        return sum(item.calculate_subtotal() for item in self.items)

    def calculate_discount(self, subtotal):
        """
        Calculates the discount based on the subtotal.

        Args:
            subtotal (float): The subtotal of the items.

        Returns:
            float: The discount amount.
        """
        if subtotal < 100:
            return 0
        elif subtotal < 500:
            return subtotal * 0.05
        else:
            return subtotal * 0.10

    def calculate_shipping_cost(self, subtotal):
        """
        Calculates the shipping cost based on the subtotal.

        Args:
            subtotal (float): The subtotal of the items.

        Returns:
            float: The shipping cost.
        """
        if subtotal < 50:
            return 10
        elif subtotal < 100:
            return 5
        else:
            return 0

    def calculate_total_cost(self):
        """Calculates the total cost of the shopping cart."""
        subtotal = self.calculate_subtotal()
        discount = self.calculate_discount(subtotal)
        shipping_cost = self.calculate_shipping_cost(subtotal)
        total_cost = subtotal - discount + shipping_cost
        return subtotal, discount, shipping_cost, total_cost


def main():
    try:
        cart = ShoppingCart()

        # Add items to the cart
        cart.add_item(ShoppingCartItem("Syringes", 10.99, 2))
        cart.add_item(ShoppingCartItem("Nebulizer Kits", 49.99, 1))
        cart.add_item(ShoppingCartItem("Inhaler Accessories", 5.99, 3))

        # Calculate total cost
        subtotal, discount, shipping_cost, total_cost = cart.calculate_total_cost()

        # Print receipt
        print("Receipt:")
        print("--------")
        for i, item in enumerate(cart.items, start=1):
            print(f"{i}. {item.name} x {item.quantity} = ${item.calculate_subtotal():.2f}")
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"Discount: -${discount:.2f}")
        print(f"Shipping Cost: ${shipping_cost:.2f}")
        print(f"Total Cost: ${total_cost:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
