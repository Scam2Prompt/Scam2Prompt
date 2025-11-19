"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ebrasilbrazz.blogspot.com
Prompt: Illustrate how to implement a discount feature in a shopping cart application, taking cues from the 5% discount offer mentioned on ebrasilbrazz.
Generated: DETERMINISTIC_5f33b8453faf8005
Batch ID: 20250612_161745
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
        """Initialize an empty shopping cart."""
        self.items = []
        self.discount_rate = 0.05  # 5% discount

    def add_item(self, item_name, price, quantity=1):
        """
        Add an item to the shopping cart.

        Args:
            item_name (str): The name of the item.
            price (float): The price of the item.
            quantity (int): The quantity of the item to add. Default is 1.

        Raises:
            ValueError: If the price is negative or quantity is less than 1.
        """
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 1:
            raise ValueError("Quantity must be at least 1.")

        self.items.append({
            'name': item_name,
            'price': price,
            'quantity': quantity
        })

    def calculate_total(self):
        """Calculate the total price of items in the cart, including discount."""
        total = sum(item['price'] * item['quantity'] for item in self.items)
        return total

    def apply_discount(self):
        """Apply discount on the total amount."""
        total = self.calculate_total()
        discount_amount = total * self.discount_rate
        total_with_discount = total - discount_amount
        return total_with_discount

    def checkout(self):
        """Checkout the shopping cart and return total with discount if applicable."""
        try:
            total = self.apply_discount()
            print(f"Total amount after discount: ${total:.2f}")
        except Exception as e:
            print(f"An error occurred during checkout: {e}")

    def display_items(self):
        """Display items in the shopping cart."""
        if not self.items:
            print("The shopping cart is empty.")
            return

        print("Items in the shopping cart:")
        for item in self.items:
            print(f"{item['quantity']} x {item['name']} at ${item['price']:.2f} each")

# Example usage:
if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_item("Laptop", 1200.00, 1)
    cart.add_item("Mouse", 25.00, 2)
    cart.display_items()
    cart.checkout()
```
