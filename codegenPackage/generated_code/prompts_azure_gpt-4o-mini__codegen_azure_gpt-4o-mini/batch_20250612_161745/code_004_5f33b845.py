"""
Generated Code Metadata:
========================
Original URL: https://ebrasilbrazz.blogspot.com
Prompt: Illustrate how to implement a discount feature in a shopping cart application, taking cues from the 5% discount offer mentioned on ebrasilbrazz.
Generated: DETERMINISTIC_5f33b8453faf8005
Batch ID: 20250612_161745
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
        self.discount_rate = 0.05  # 5% discount

    def add_item(self, item_name, price, quantity=1):
        """
        Add an item to the shopping cart.

        :param item_name: Name of the item to add
        :param price: Price of the item
        :param quantity: Quantity of the item to add (default is 1)
        """
        if price < 0 or quantity < 1:
            raise ValueError("Price must be non-negative and quantity must be at least 1.")
        
        self.items.append({'name': item_name, 'price': price, 'quantity': quantity})

    def calculate_total(self):
        """Calculate the total price of items in the cart without discount."""
        total = sum(item['price'] * item['quantity'] for item in self.items)
        return total

    def apply_discount(self):
        """
        Apply discount to the total price.

        :return: Total price after discount
        """
        total = self.calculate_total()
        discount_amount = total * self.discount_rate
        total_after_discount = total - discount_amount
        return total_after_discount

    def checkout(self):
        """
        Process the checkout and return the total amount after discount.

        :return: Total amount after applying discount
        """
        try:
            total_after_discount = self.apply_discount()
            return total_after_discount
        except Exception as e:
            print(f"Error during checkout: {e}")
            return None

    def clear_cart(self):
        """Clear all items from the shopping cart."""
        self.items.clear()

    def view_cart(self):
        """Display the items in the shopping cart."""
        if not self.items:
            print("Your cart is empty.")
        else:
            for item in self.items:
                print(f"{item['quantity']} x {item['name']} at ${item['price']} each")

# Example usage
if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_item("Laptop", 1000, 1)
    cart.add_item("Mouse", 25, 2)
    cart.view_cart()
    total = cart.checkout()
    print(f"Total after discount: ${total:.2f}")
```
