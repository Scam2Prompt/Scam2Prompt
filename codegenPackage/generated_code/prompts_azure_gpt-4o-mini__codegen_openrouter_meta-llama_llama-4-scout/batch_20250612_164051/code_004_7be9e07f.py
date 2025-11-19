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

class Product:
    """Represents a product in the shopping cart."""

    def __init__(self, name, price):
        """
        Initializes a Product.

        Args:
            name (str): The product name.
            price (float): The product price.
        """
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: R${self.price:.2f}"


class ShoppingCart:
    """Represents a shopping cart."""

    def __init__(self):
        """Initializes an empty shopping cart."""
        self.items = []

    def add_item(self, product, quantity=1):
        """
        Adds a product to the shopping cart.

        Args:
            product (Product): The product to add.
            quantity (int, optional): The product quantity. Defaults to 1.
        """
        self.items.append({"product": product, "quantity": quantity})

    def remove_item(self, product_name):
        """
        Removes a product from the shopping cart.

        Args:
            product_name (str): The name of the product to remove.
        """
        self.items = [item for item in self.items if item["product"].name != product_name]

    def calculate_total(self):
        """
        Calculates the total cost of the items in the shopping cart.

        Returns:
            float: The total cost.
        """
        return sum(item["product"].price * item["quantity"] for item in self.items)

    def __str__(self):
        cart_info = "Shopping Cart:\n"
        for i, item in enumerate(self.items, start=1):
            cart_info += f"{i}. {item['product']} x {item['quantity']}\n"
        cart_info += f"Total: R${self.calculate_total():.2f}"
        return cart_info


class PaymentMethod:
    """Represents a payment method."""

    def __init__(self, name):
        """
        Initializes a PaymentMethod.

        Args:
            name (str): The payment method name.
        """
        self.name = name

    def __str__(self):
        return self.name


class Payment:
    """Represents a payment."""

    def __init__(self, payment_method, amount):
        """
        Initializes a Payment.

        Args:
            payment_method (PaymentMethod): The payment method.
            amount (float): The payment amount.
        """
        self.payment_method = payment_method
        self.amount = amount

    def __str__(self):
        return f"Payment Method: {self.payment_method}\nAmount: R${self.amount:.2f}"


def main():
    # Create products
    sensor_presence = Product("Sensor Presença", 50.00)
    plafon_chess = Product("Plafon Chess", 100.00)

    # Create shopping cart
    cart = ShoppingCart()
    cart.add_item(sensor_presence, 2)
    cart.add_item(plafon_chess)

    # Display shopping cart
    print(cart)

    # Create payment methods
    payment_methods = [
        PaymentMethod("Cash"),
        PaymentMethod("Credit Card"),
        PaymentMethod("Debit Card"),
    ]

    # Display payment methods
    print("\nPayment Methods:")
    for i, method in enumerate(payment_methods, start=1):
        print(f"{i}. {method}")

    # Get payment method choice
    while True:
        try:
            choice = int(input("Choose a payment method (1/2/3): "))
            if 1 <= choice <= 3:
                break
            else:
                print("Invalid choice. Please choose a valid payment method.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Process payment
    chosen_method = payment_methods[choice - 1]
    payment_amount = cart.calculate_total()
    payment = Payment(chosen_method, payment_amount)

    # Display payment information
    print("\nPayment Information:")
    print(payment)


if __name__ == "__main__":
    main()
```
