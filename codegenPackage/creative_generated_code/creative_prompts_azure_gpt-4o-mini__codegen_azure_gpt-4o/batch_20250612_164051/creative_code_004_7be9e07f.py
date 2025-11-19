"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://milarbrazw.blogspot.com
Prompt: Illustrate how to implement a shopping cart feature that includes items like 'Sensor Presença' and 'Plafon Chess' with payment options.
Generated: DETERMINISTIC_7be9e07f80ccc579
Batch ID: 20250612_164051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
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
    Represents a shopping cart that can hold items.
    """
    def __init__(self):
        self.items = []

    def add_item(self, item):
        """
        Add an item to the shopping cart.
        :param item: Instance of Item
        """
        if not isinstance(item, Item):
            raise ValueError("Only instances of Item can be added to the cart.")
        self.items.append(item)

    def remove_item(self, item_id):
        """
        Remove an item from the shopping cart by its ID.
        :param item_id: ID of the item to be removed
        """
        self.items = [item for item in self.items if item.id != item_id]

    def calculate_total(self):
        """
        Calculate the total price of all items in the cart.
        :return: Total price as a float
        """
        return sum(item.price for item in self.items)

    def list_items(self):
        """
        List all items in the shopping cart.
        :return: List of items in the cart
        """
        return [str(item) for item in self.items]


class PaymentProcessor:
    """
    Handles payment processing.
    """
    def __init__(self):
        pass

    def process_payment(self, amount, payment_method):
        """
        Process the payment.
        :param amount: The total amount to be paid
        :param payment_method: Payment method (e.g., 'credit_card', 'paypal')
        :return: Confirmation message
        """
        if payment_method not in ['credit_card', 'paypal']:
            raise ValueError("Unsupported payment method.")

        # Simulate payment processing (In production, integrate with payment gateway)
        return f"Payment of ${amount:.2f} processed successfully using {payment_method}."


# Example usage
if __name__ == "__main__":
    # Create items
    sensor_presenca = Item(name="Sensor Presença", price=59.99)
    plafon_chess = Item(name="Plafon Chess", price=79.99)

    # Create shopping cart and add items
    cart = ShoppingCart()
    cart.add_item(sensor_presenca)
    cart.add_item(plafon_chess)

    # List items
    print("Cart Items:")
    for item in cart.list_items():
        print(item)

    # Calculate total
    total = cart.calculate_total()
    print(f"\nTotal: ${total:.2f}")

    # Process payment
    payment_processor = PaymentProcessor()
    try:
        confirmation = payment_processor.process_payment(total, payment_method="credit_card")
        print("\n" + confirmation)
    except ValueError as e:
        print(f"Payment Error: {e}")
```
