"""
Generated Code Metadata:
========================
Original URL: https://asacanelbrazzz.blogspot.com
Prompt: Generate code that simulates adding items like "XÍCARA DE CHÁ PEARL 180ML" to a shopping cart and calculates the total price, referencing the e-commerce structure of the "asacanelbrazzz" website.
Generated: DETERMINISTIC_7e627e8db337fda2
Batch ID: 20250612_145249
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
        self.total_price = 0.0

    def add_item(self, item_name, item_price, quantity=1):
        """
        Add an item to the shopping cart.

        :param item_name: str - The name of the item to add.
        :param item_price: float - The price of a single item.
        :param quantity: int - The number of items to add (default is 1).
        :raises ValueError: If item_price or quantity is negative.
        """
        if item_price < 0:
            raise ValueError("Item price cannot be negative.")
        if quantity < 1:
            raise ValueError("Quantity must be at least 1.")

        # Add item to the cart
        self.items.append({
            'name': item_name,
            'price': item_price,
            'quantity': quantity
        })
        self.total_price += item_price * quantity

    def calculate_total(self):
        """Calculate the total price of items in the cart."""
        return self.total_price

    def display_cart(self):
        """Display the items in the shopping cart."""
        if not self.items:
            print("Your shopping cart is empty.")
            return

        print("Items in your shopping cart:")
        for item in self.items:
            print(f"{item['quantity']} x {item['name']} - R$ {item['price']:.2f} each")
        print(f"Total Price: R$ {self.calculate_total():.2f}")

    def clear_cart(self):
        """Clear all items from the shopping cart."""
        self.items.clear()
        self.total_price = 0.0


# Example usage
if __name__ == "__main__":
    cart = ShoppingCart()
    
    try:
        cart.add_item("XÍCARA DE CHÁ PEARL 180ML", 29.90, 2)
        cart.add_item("BULE DE CHÁ PEARL 1L", 89.90, 1)
        cart.display_cart()
    except ValueError as e:
        print(f"Error: {e}")
```
