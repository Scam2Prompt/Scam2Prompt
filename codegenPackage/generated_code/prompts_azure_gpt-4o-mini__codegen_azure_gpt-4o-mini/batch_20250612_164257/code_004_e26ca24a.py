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
class ShoppingCart:
    def __init__(self):
        """Initialize an empty shopping cart."""
        self.items = []
        self.is_first_time_shopper = True  # Flag to check if the shopper is a first-time customer
        self.discount_rate = 0.05  # 5% discount for first-time shoppers

    def add_item(self, item_name, item_price):
        """Add an item to the shopping cart.

        Args:
            item_name (str): The name of the item to add.
            item_price (float): The price of the item to add.
        """
        if item_price < 0:
            raise ValueError("Item price cannot be negative.")
        self.items.append({'name': item_name, 'price': item_price})

    def calculate_total(self):
        """Calculate the total price of items in the cart, applying discounts if applicable.

        Returns:
            float: The total price after applying any discounts.
        """
        total = sum(item['price'] for item in self.items)
        if self.is_first_time_shopper:
            discount = total * self.discount_rate
            total -= discount
            self.is_first_time_shopper = False  # Set flag to false after first purchase
        return total

    def checkout(self):
        """Process the checkout for the shopping cart.

        Returns:
            str: A summary of the checkout process including total price.
        """
        if not self.items:
            return "Your cart is empty. Please add items before checking out."
        
        total_price = self.calculate_total()
        return f"Checkout successful! Your total is: ${total_price:.2f}"

# Example usage
if __name__ == "__main__":
    try:
        cart = ShoppingCart()
        cart.add_item("Diamond Ring", 500.00)
        cart.add_item("Gold Necklace", 300.00)
        print(cart.checkout())  # First-time shopper discount applied
        print(cart.checkout())  # No discount for subsequent purchases
    except ValueError as e:
        print(f"Error: {e}")
```
