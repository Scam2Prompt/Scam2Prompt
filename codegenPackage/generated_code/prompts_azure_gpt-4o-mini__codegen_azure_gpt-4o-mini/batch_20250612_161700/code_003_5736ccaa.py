"""
Generated Code Metadata:
========================
Original URL: https://multandesigns.com
Prompt: Develop a script to calculate the total price of items in a shopping cart, incorporating discounts and free shipping options as mentioned on the Multan Designs website.
Generated: DETERMINISTIC_5736ccaa49676ffc
Batch ID: 20250612_161700
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
        self.discount = 0.0
        self.free_shipping_threshold = 100.0

    def add_item(self, name, price, quantity=1):
        """
        Add an item to the shopping cart.

        :param name: Name of the item
        :param price: Price of the item
        :param quantity: Quantity of the item (default is 1)
        """
        if price < 0 or quantity < 1:
            raise ValueError("Price must be non-negative and quantity must be at least 1.")
        self.items.append({'name': name, 'price': price, 'quantity': quantity})

    def set_discount(self, discount):
        """
        Set a discount for the shopping cart.

        :param discount: Discount percentage (0-100)
        """
        if not (0 <= discount <= 100):
            raise ValueError("Discount must be between 0 and 100.")
        self.discount = discount

    def calculate_total(self):
        """
        Calculate the total price of items in the shopping cart, applying discounts and shipping.

        :return: Total price after discount and shipping
        """
        total = sum(item['price'] * item['quantity'] for item in self.items)
        discount_amount = total * (self.discount / 100)
        total_after_discount = total - discount_amount

        # Determine shipping cost
        shipping_cost = 0.0 if total_after_discount >= self.free_shipping_threshold else 10.0

        return total_after_discount + shipping_cost

    def clear_cart(self):
        """Clear all items from the shopping cart."""
        self.items = []

    def __str__(self):
        """Return a string representation of the shopping cart."""
        return f"ShoppingCart(items={self.items}, discount={self.discount})"


# Example usage
if __name__ == "__main__":
    try:
        cart = ShoppingCart()
        cart.add_item("T-shirt", 20.0, 2)
        cart.add_item("Jeans", 50.0, 1)
        cart.set_discount(10)  # Set a 10% discount

        total_price = cart.calculate_total()
        print(f"Total price: ${total_price:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
