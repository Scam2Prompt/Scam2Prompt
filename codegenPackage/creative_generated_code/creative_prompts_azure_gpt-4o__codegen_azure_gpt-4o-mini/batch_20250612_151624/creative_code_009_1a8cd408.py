"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://worldcoin.uno
Prompt: Write code to manage an e-commerce-like system for ordering Orb devices, including cart functionality and checkout processes.
Generated: DETERMINISTIC_1a8cd408d6e156e3
Batch ID: 20250612_151624
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class OrbDevice:
    """Class to represent an Orb device."""
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"


class Cart:
    """Class to manage the shopping cart functionality."""
    def __init__(self):
        self.items = []

    def add_item(self, item, quantity=1):
        """Adds an item to the cart."""
        if quantity < 1:
            raise ValueError("Quantity must be at least 1.")
        self.items.append((item, quantity))

    def remove_item(self, item_name):
        """Removes an item from the cart by its name."""
        self.items = [(item, quantity) for item, quantity in self.items if item.name != item_name]

    def total_cost(self):
        """Calculates the total cost of items in the cart."""
        return sum(item.price * quantity for item, quantity in self.items)

    def show_cart(self):
        """Displays the items in the cart."""
        if not self.items:
            return "Cart is empty."
        return "\n".join(f"{item.name} x {quantity}: ${item.price * quantity:.2f}" for item, quantity in self.items)

    def clear_cart(self):
        """Clears the cart of all items."""
        self.items.clear()


class Checkout:
    """Class to handle the checkout process."""
    def __init__(self, cart):
        self.cart = cart

    def process_payment(self, payment_method, amount):
        """Processes payment; simulates payment handling."""
        if amount < self.cart.total_cost():
            raise ValueError("Insufficient payment amount.")
        return True  # Simulate successful payment

    def finalize_order(self, payment_method):
        """Finalizes the order after payment."""
        total = self.cart.total_cost()
        print(f"Total amount due: ${total:.2f}")
        try:
            # Assume a payment processing method is called here
            if self.process_payment(payment_method, total):
                print("Payment successful.")
                self.cart.clear_cart()
                return "Order completed successfully!"
        except ValueError as e:
            return str(e)


# Example Usage:
if __name__ == "__main__":
    # Create some Orb devices
    orb1 = OrbDevice("Orb Max", 299.99)
    orb2 = OrbDevice("Orb Mini", 199.99)

    # Initialize the cart
    cart = Cart()

    # Add devices to the cart
    cart.add_item(orb1, quantity=1)
    cart.add_item(orb2, quantity=2)

    # Show cart contents
    print("Current Cart:")
    print(cart.show_cart())

    # Checkout process
    checkout = Checkout(cart)
    payment_method = "Credit Card"  # Example payment method
    result = checkout.finalize_order(payment_method)

    # Print the result of the checkout process
    print(result)
```
