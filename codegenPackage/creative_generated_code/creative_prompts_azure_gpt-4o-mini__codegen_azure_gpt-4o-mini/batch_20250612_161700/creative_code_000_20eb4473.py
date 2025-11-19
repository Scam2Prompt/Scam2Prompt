"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://utterlybaked.com
Prompt: Generate a code snippet for an online ordering system that offers discounts, similar to the 50% OFF promotion mentioned on utterlybaked.com.
Generated: DETERMINISTIC_20eb447371df3cb8
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Order:
    def __init__(self, items):
        """
        Initializes the Order with a list of items.
        
        :param items: List of tuples, where each tuple contains the item name and its price.
        """
        if not isinstance(items, list):
            raise ValueError("Items must be provided as a list.")
        
        self.items = items

    def calculate_total(self):
        """
        Calculates the total price of the order.
        
        :return: Total price of the items.
        """
        total = sum(price for _, price in self.items)
        return total

    def apply_discount(self, discount_percentage):
        """
        Applies a discount to the total price of the order.

        :param discount_percentage: The discount percentage to apply (0-100).
        :return: The total price after discount.
        """
        if not (0 <= discount_percentage <= 100):
            raise ValueError("Discount percentage must be between 0 and 100.")
        
        total_before_discount = self.calculate_total()
        discount_amount = total_before_discount * (discount_percentage / 100)
        total_after_discount = total_before_discount - discount_amount
        
        return total_after_discount

    def __str__(self):
        """
        Returns a string representation of the order.
        
        :return: A formatted string of the order items and their prices.
        """
        items_str = "\n".join(f"{item}: ${price:.2f}" for item, price in self.items)
        total = self.calculate_total()
        return f"Order Items:\n{items_str}\nTotal: ${total:.2f}"


if __name__ == "__main__":
    # Example usage of the Order class
    try:
        # Define items in the order as (item_name, price)
        items = [
            ("Brownie", 4.00),
            ("Cookie", 2.50),
            ("Cupcake", 3.75)
        ]

        order = Order(items)
        print(order)  # Print the order details

        # Apply a 50% discount
        discount_percentage = 50
        total_after_discount = order.apply_discount(discount_percentage)
        print(f"Total after applying {discount_percentage}% discount: ${total_after_discount:.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
