"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://icestyle.pl
Prompt: Create a function that calculates the total cost of a shopping cart containing figure skating gear, including custom costumes, as described on IceStyle.pl.
Generated: DETERMINISTIC_8fe1b5ea19133b51
Batch ID: 20250612_162228
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

    def add_item(self, item_name, price, quantity=1):
        """
        Add an item to the shopping cart.

        :param item_name: Name of the item to add.
        :param price: Price of the item.
        :param quantity: Quantity of the item to add, defaults to 1.
        """
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 1:
            raise ValueError("Quantity must be at least 1.")

        self.items.append({"name": item_name, "price": price, "quantity": quantity})

    def calculate_total(self):
        """
        Calculate the total cost of the items in the shopping cart.

        :return: Total cost as a float.
        """
        total_cost = 0.0
        for item in self.items:
            total_cost += item["price"] * item["quantity"]

        return round(total_cost, 2)  # Round to two decimal places for currency

    def clear_cart(self):
        """Clear all items from the shopping cart."""
        self.items.clear()

# Example usage
if __name__ == "__main__":
    cart = ShoppingCart()
    try:
        cart.add_item("Custom Costume", 150.00, quantity=1)
        cart.add_item("Skates", 200.00, quantity=2)
        cart.add_item("Protective Gear", 75.50)

        total = cart.calculate_total()
        print(f"Total cost of the shopping cart: ${total}")

    except ValueError as e:
        print(f"Error: {e}")
```
