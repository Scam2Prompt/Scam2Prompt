"""
Generated Code Metadata:
========================
Original URL: https://milarbrazw.blogspot.com
Prompt: Illustrate how to implement a shopping cart feature that includes items like 'Sensor Presença' and 'Plafon Chess' with payment options.
Generated: DETERMINISTIC_7be9e07f80ccc579
Batch ID: 20250612_164051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# shopping_cart.py

import uuid

class Item:
    """
    Represents an item in the shopping cart.
    """
    def __init__(self, name, price):
        self.id = str(uuid.uuid4())  # Unique identifier for the item
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"


class ShoppingCart:
    """
    Represents a shopping cart that can hold items and calculate total cost.
    """
    def __init__(self):
        self.items = []  # List to store items in the cart

    def add_item(self, item):
        """
        Adds an item to the shopping cart.
        :param item: Item object to be added
        """
        if not isinstance(item, Item):
            raise ValueError("Invalid item. Must be an instance of Item.")
        self.items.append(item)

    def remove_item(self, item_id):
        """
        Removes an item from the shopping cart by its ID.
        :param item_id: ID of the item to be removed
        """
        self.items = [item for item in self.items if item.id != item_id]

    def calculate_total(self):
        """
        Calculates the total cost of items in the shopping cart.
        :return: Total cost as a float
        """
        return sum(item.price for item in self.items)

    def list_items(self):
        """
        Lists all items in the shopping cart.
        :return: List of item descriptions
        """
        return [str(item) for item in self.items]


class PaymentProcessor:
    """
    Handles payment processing for the shopping cart.
    """
    def __init__(self):
        self.supported_methods = ["credit_card", "paypal"]

    def process_payment(self, method, amount):
        """
        Processes payment for the given amount using the specified method.
        :param method: Payment method (e.g., 'credit_card', 'paypal')
        :param amount: Amount to be paid
        :return: Confirmation message
        """
        if method not in self.supported_methods:
            raise ValueError(f"Unsupported payment method: {method}")
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        # Simulate payment processing
        return f"Payment of ${amount:.2f} processed successfully using {method}."


# Example usage
if __name__ == "__main__":
    try:
        # Create items
        sensor_presenca = Item("Sensor Presença", 49.99)
        plafon_chess = Item("Plafon Chess", 89.99)

        # Create shopping cart and add items
        cart = ShoppingCart()
        cart.add_item(sensor_presenca)
        cart.add_item(plafon_chess)

        # List items in the cart
        print("Items in cart:")
        for item in cart.list_items():
            print(item)

        # Calculate total
        total = cart.calculate_total()
        print(f"Total: ${total:.2f}")

        # Process payment
        payment_processor = PaymentProcessor()
        confirmation = payment_processor.process_payment("credit_card", total)
        print(confirmation)

    except Exception as e:
        print(f"Error: {e}")
```
