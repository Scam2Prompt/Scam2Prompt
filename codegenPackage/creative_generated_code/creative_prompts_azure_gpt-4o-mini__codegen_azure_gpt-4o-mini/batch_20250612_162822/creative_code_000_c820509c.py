"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://simplife.life
Prompt: Generate a code snippet for a shopping cart that includes a feature for free shipping on orders over $40, similar to the policy on simplife.life.
Generated: DETERMINISTIC_c820509c24d25cbe
Batch ID: 20250612_162822
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
        self.total_price = 0.0

    def add_item(self, item_name, price, quantity=1):
        """
        Add an item to the shopping cart.

        :param item_name: Name of the item to add
        :param price: Price of the item
        :param quantity: Quantity of the item to add
        """
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 1:
            raise ValueError("Quantity must be at least 1.")

        self.items.append({'name': item_name, 'price': price, 'quantity': quantity})
        self.total_price += price * quantity

    def calculate_shipping(self):
        """
        Calculate shipping cost based on the total price.

        :return: Shipping cost
        """
        if self.total_price > 40:
            return 0.0  # Free shipping for orders over $40
        else:
            return 5.99  # Flat shipping cost for orders $40 or less

    def checkout(self):
        """
        Calculate the total amount due, including shipping.

        :return: Total amount due
        """
        shipping_cost = self.calculate_shipping()
        total_due = self.total_price + shipping_cost
        return total_due

    def display_cart(self):
        """Display the items in the cart and the total price."""
        print("Shopping Cart:")
        for item in self.items:
            print(f"- {item['name']}: ${item['price']} x {item['quantity']}")
        print(f"Total Price: ${self.total_price:.2f}")
        print(f"Shipping Cost: ${self.calculate_shipping():.2f}")
        print(f"Total Amount Due: ${self.checkout():.2f}")


# Example usage
if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_item("Book", 15.99, 2)
    cart.add_item("Headphones", 25.00)
    cart.display_cart()
```
