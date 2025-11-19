"""
Generated Code Metadata:
========================
Original URL: https://snackpointemmen.nl
Prompt: Generate a code snippet for a restaurant ordering system that includes features for takeaway and contactless payment, similar to Snackpoint Emmen's services.
Generated: DETERMINISTIC_f360a3beb2af621a
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
from datetime import datetime

class Order:
    def __init__(self, customer_name, items, takeaway=False):
        """
        Initialize an order.

        :param customer_name: Name of the customer
        :param items: List of items ordered (list of dicts with 'name' and 'price')
        :param takeaway: Boolean indicating if the order is for takeaway
        """
        self.order_id = str(uuid.uuid4())  # Generate a unique order ID
        self.customer_name = customer_name
        self.items = items
        self.takeaway = takeaway
        self.timestamp = datetime.now()
        self.total_price = self.calculate_total()

    def calculate_total(self):
        """
        Calculate the total price of the order.

        :return: Total price as a float
        """
        return sum(item['price'] for item in self.items)

    def display_order_summary(self):
        """
        Display a summary of the order.
        """
        print(f"Order ID: {self.order_id}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Order Time: {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
        print("Items:")
        for item in self.items:
            print(f"  - {item['name']}: ${item['price']:.2f}")
        print(f"Total Price: ${self.total_price:.2f}")
        print(f"Takeaway: {'Yes' if self.takeaway else 'No'}")

class PaymentProcessor:
    def __init__(self):
        """
        Initialize the payment processor.
        """
        self.supported_methods = ['contactless', 'card', 'cash']

    def process_payment(self, order, payment_method):
        """
        Process payment for an order.

        :param order: Order object
        :param payment_method: Payment method as a string
        :return: Boolean indicating success or failure
        """
        if payment_method not in self.supported_methods:
            print(f"Error: Payment method '{payment_method}' is not supported.")
            return False

        # Simulate payment processing
        print(f"Processing {payment_method} payment for Order ID: {order.order_id}...")
        print(f"Payment of ${order.total_price:.2f} successful!")
        return True

# Example usage
if __name__ == "__main__":
    try:
        # Create an order
        items = [
            {'name': 'Burger', 'price': 8.99},
            {'name': 'Fries', 'price': 3.49},
            {'name': 'Soda', 'price': 1.99}
        ]
        order = Order(customer_name="John Doe", items=items, takeaway=True)

        # Display order summary
        order.display_order_summary()

        # Process payment
        payment_processor = PaymentProcessor()
        payment_method = 'contactless'  # Example payment method
        payment_success = payment_processor.process_payment(order, payment_method)

        if payment_success:
            print("Thank you for your order!")
        else:
            print("Payment failed. Please try again.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
