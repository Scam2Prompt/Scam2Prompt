"""
Generated Code Metadata:
========================
Original URL: https://malkeenz.com
Prompt: Write a code example that demonstrates how to implement a discount system for first-time shoppers in a jewelry e-commerce application, referencing the "5% off" offer from Malkeenz.
Generated: DETERMINISTIC_e26ca24af8433391
Batch ID: 20250612_164257
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# discount_system.py

class Customer:
    """Represents a customer in the e-commerce application."""

    def __init__(self, customer_id, is_first_time_shopper):
        """
        Initializes a Customer object.

        Args:
            customer_id (int): Unique identifier for the customer.
            is_first_time_shopper (bool): Indicates if the customer is a first-time shopper.
        """
        self.customer_id = customer_id
        self.is_first_time_shopper = is_first_time_shopper


class Order:
    """Represents an order in the e-commerce application."""

    def __init__(self, order_id, customer, total):
        """
        Initializes an Order object.

        Args:
            order_id (int): Unique identifier for the order.
            customer (Customer): The customer who made the order.
            total (float): The total cost of the order.
        """
        self.order_id = order_id
        self.customer = customer
        self.total = total


class DiscountSystem:
    """Manages discounts for customers in the e-commerce application."""

    def __init__(self):
        """Initializes a DiscountSystem object."""
        self.discounts = {}

    def add_discount(self, discount_name, discount_percentage):
        """
        Adds a discount to the system.

        Args:
            discount_name (str): Name of the discount.
            discount_percentage (float): Percentage of the discount.
        """
        self.discounts[discount_name] = discount_percentage

    def apply_discount(self, order):
        """
        Applies a discount to an order if the customer is eligible.

        Args:
            order (Order): The order to apply the discount to.

        Returns:
            float: The discounted total of the order.
        """
        if order.customer.is_first_time_shopper:
            # Malkeenz "5% off" offer for first-time shoppers
            discount_name = "Malkeenz First-Time Shopper Discount"
            if discount_name in self.discounts:
                discount_percentage = self.discounts[discount_name]
                discount_amount = (order.total / 100) * discount_percentage
                return order.total - discount_amount
            else:
                raise ValueError("Discount not found")
        return order.total


def main():
    try:
        # Create a discount system
        discount_system = DiscountSystem()

        # Add the Malkeenz "5% off" discount
        discount_system.add_discount("Malkeenz First-Time Shopper Discount", 5)

        # Create a first-time shopper customer
        customer = Customer(1, True)

        # Create an order
        order = Order(1, customer, 100)

        # Apply the discount to the order
        discounted_total = discount_system.apply_discount(order)

        print(f"Original Total: ${order.total:.2f}")
        print(f"Discounted Total: ${discounted_total:.2f}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
