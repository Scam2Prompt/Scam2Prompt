"""
Generated Code Metadata:
========================
Original URL: https://micadbrazzz.blogspot.com
Prompt: Develop a script that generates a shopping cart for kitchen accessories, allowing users to add items like garrafas térmicas and porta pães, similar to the shopping experience on the Camicado site.
Generated: DETERMINISTIC_991c08ccf4e84d1a
Batch ID: 20250612_160633
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

    def add_item(self, item_name, item_price, quantity=1):
        """
        Add an item to the shopping cart.

        :param item_name: Name of the item to add.
        :param item_price: Price of the item.
        :param quantity: Number of items to add (default is 1).
        :raises ValueError: If the item price is negative or quantity is less than 1.
        """
        if item_price < 0:
            raise ValueError("Item price cannot be negative.")
        if quantity < 1:
            raise ValueError("Quantity must be at least 1.")

        item = {
            'name': item_name,
            'price': item_price,
            'quantity': quantity
        }
        self.items.append(item)
        print(f"Added {quantity} x {item_name} at ${item_price:.2f} each to the cart.")

    def remove_item(self, item_name):
        """
        Remove an item from the shopping cart.

        :param item_name: Name of the item to remove.
        :raises ValueError: If the item is not found in the cart.
        """
        for item in self.items:
            if item['name'] == item_name:
                self.items.remove(item)
                print(f"Removed {item_name} from the cart.")
                return
        raise ValueError(f"Item '{item_name}' not found in the cart.")

    def view_cart(self):
        """Display the current items in the shopping cart."""
        if not self.items:
            print("Your shopping cart is empty.")
            return

        print("Shopping Cart:")
        for item in self.items:
            print(f"{item['quantity']} x {item['name']} at ${item['price']:.2f} each")

    def total_price(self):
        """Calculate and return the total price of items in the cart."""
        total = sum(item['price'] * item['quantity'] for item in self.items)
        print(f"Total price: ${total:.2f}")
        return total

def main():
    """Main function to run the shopping cart application."""
    cart = ShoppingCart()

    # Example usage
    try:
        cart.add_item("Garrafas Térmicas", 49.99, 2)
        cart.add_item("Porta Pães", 29.99, 1)
        cart.view_cart()
        cart.total_price()
        cart.remove_item("Porta Pães")
        cart.view_cart()
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
