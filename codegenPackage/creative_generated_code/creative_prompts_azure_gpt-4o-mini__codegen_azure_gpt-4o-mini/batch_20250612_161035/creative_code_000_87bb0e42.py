"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://novavault.shop
Prompt: Generate a code snippet for an e-commerce checkout process that includes a discount feature similar to the 40% off promotion on Novavault.
Generated: DETERMINISTIC_87bb0e4210feba4a
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ShoppingCart:
    def __init__(self):
        """Initialize an empty cart."""
        self.items = []
        self.discount_rate = 0.0

    def add_item(self, item, price):
        """Add an item to the shopping cart.

        Args:
            item (str): The name of the item.
            price (float): The price of the item.

        Raises:
            ValueError: If the price is negative.
        """
        if price < 0:
            raise ValueError("Price cannot be negative.")
        self.items.append((item, price))

    def set_discount(self, discount_percent):
        """Set the discount rate for the cart.

        Args:
            discount_percent (float): The discount percentage (0 to 100).

        Raises:
            ValueError: If the discount is not in the range 0 to 100.
        """
        if not (0 <= discount_percent <= 100):
            raise ValueError("Discount percentage must be between 0 and 100.")
        self.discount_rate = discount_percent / 100.0

    def calculate_total(self):
        """Calculate the total price of items in the cart after applying the discount.

        Returns:
            float: The total price after discount.
        """
        total = sum(price for _, price in self.items)
        discount_amount = total * self.discount_rate
        return total - discount_amount

    def checkout(self):
        """Finalize the checkout process and return the total amount.

        Returns:
            float: The total amount due after discounts.
        """
        if not self.items:
            raise ValueError("The shopping cart is empty. Please add items before checkout.")
        total_amount = self.calculate_total()
        # Here we would normally process the payment.
        return total_amount


# Example usage
if __name__ == "__main__":
    try:
        cart = ShoppingCart()
        cart.add_item("Laptop", 1000.00)
        cart.add_item("Mouse", 50.00)
        
        # Set a 40% discount
        cart.set_discount(40)

        # Calculate and print the total amount due
        total_amount_due = cart.checkout()
        print(f"Total amount due: ${total_amount_due:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
