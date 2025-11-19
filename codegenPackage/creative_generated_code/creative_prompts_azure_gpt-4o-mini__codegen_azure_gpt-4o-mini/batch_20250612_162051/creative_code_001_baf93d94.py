"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://erismizar.com
Prompt: Write a function that calculates the total price of a shopping cart containing items like the M101 sneakers and maintenance kits from Eris Mizar, considering discounts for bulk purchases.
Generated: DETERMINISTIC_baf93d94aa781d37
Batch ID: 20250612_162051
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

    def add_item(self, item_name, price, quantity):
        """Add an item to the shopping cart.
        
        Args:
            item_name (str): The name of the item.
            price (float): The price of a single item.
            quantity (int): The number of items to add.
        
        Raises:
            ValueError: If price is negative or quantity is not a positive integer.
        """
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")

        self.items.append({"name": item_name, "price": price, "quantity": quantity})

    def calculate_total(self):
        """Calculate the total price of the shopping cart, applying bulk discounts.
        
        Returns:
            float: The total price after discounts.
        """
        total = 0.0

        for item in self.items:
            # Apply bulk discount for M101 sneakers and Eris Mizar maintenance kits
            if item['name'] == "M101 sneakers" and item['quantity'] >= 3:
                discount = 0.1  # 10% discount for buying 3 or more
            elif item['name'] == "Eris Mizar maintenance kit" and item['quantity'] >= 5:
                discount = 0.15  # 15% discount for buying 5 or more
            else:
                discount = 0.0

            # Calculate total for this item
            item_total = item['price'] * item['quantity'] * (1 - discount)
            total += item_total

        return round(total, 2)  # Round to 2 decimal places for currency format

    def clear_cart(self):
        """Clear all items from the shopping cart."""
        self.items.clear()


# Example usage:
if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_item("M101 sneakers", 100.00, 4)  # 4 sneakers
    cart.add_item("Eris Mizar maintenance kit", 25.00, 5)  # 5 kits
    cart.add_item("Basic socks", 5.00, 2)  # 2 pairs of socks

    total_price = cart.calculate_total()
    print(f"Total price of the shopping cart: ${total_price}")
```
