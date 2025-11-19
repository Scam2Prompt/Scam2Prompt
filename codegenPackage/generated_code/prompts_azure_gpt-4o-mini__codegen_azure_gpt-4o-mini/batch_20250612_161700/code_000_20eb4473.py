"""
Generated Code Metadata:
========================
Original URL: https://utterlybaked.com
Prompt: Generate a code snippet for an online ordering system that offers discounts, similar to the 50% OFF promotion mentioned on utterlybaked.com.
Generated: DETERMINISTIC_20eb447371df3cb8
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Order:
    def __init__(self, items):
        """
        Initialize the Order with a list of items.
        
        :param items: List of tuples where each tuple contains (item_name, price)
        """
        self.items = items
        self.discount = 0.0

    def apply_discount(self, discount_percentage):
        """
        Apply a discount to the order.
        
        :param discount_percentage: The percentage discount to apply (0-100)
        :raises ValueError: If discount_percentage is not between 0 and 100
        """
        if not (0 <= discount_percentage <= 100):
            raise ValueError("Discount percentage must be between 0 and 100.")
        self.discount = discount_percentage

    def calculate_total(self):
        """
        Calculate the total price of the order after applying the discount.
        
        :return: Total price after discount
        """
        total = sum(price for _, price in self.items)
        discount_amount = total * (self.discount / 100)
        return total - discount_amount

    def __str__(self):
        """
        String representation of the order, including items and total price.
        
        :return: String representation of the order
        """
        item_list = ', '.join(f"{name}: ${price:.2f}" for name, price in self.items)
        total_price = self.calculate_total()
        return f"Order items: {item_list}\nTotal after discount: ${total_price:.2f}"


# Example usage
if __name__ == "__main__":
    try:
        # Create an order with some items
        order_items = [("Cookie", 2.50), ("Brownie", 3.00), ("Cake", 5.00)]
        order = Order(order_items)

        # Apply a 50% discount
        order.apply_discount(50)

        # Print the order details
        print(order)

    except ValueError as e:
        print(f"Error: {e}")
```
