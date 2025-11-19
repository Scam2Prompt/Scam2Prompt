"""
Generated Code Metadata:
========================
Original URL: https://titlebelts.au
Prompt: Illustrate how to implement a shopping cart feature for championship belts on an e-commerce site similar to Title Belts AU, including adding and removing items.
Generated: DETERMINISTIC_b7585966dc401377
Batch ID: 20250612_163424
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# shopping_cart.py

class ShoppingCart:
    """
    A class to represent a shopping cart for an e-commerce site.
    Allows adding, removing, and viewing items in the cart.
    """

    def __init__(self):
        """
        Initialize an empty shopping cart.
        """
        self.cart = {}

    def add_item(self, item_id, item_name, price, quantity=1):
        """
        Add an item to the shopping cart.

        :param item_id: Unique identifier for the item
        :param item_name: Name of the item
        :param price: Price of the item
        :param quantity: Quantity of the item to add (default is 1)
        """
        if item_id in self.cart:
            # If the item already exists, update the quantity
            self.cart[item_id]['quantity'] += quantity
        else:
            # Add a new item to the cart
            self.cart[item_id] = {
                'item_name': item_name,
                'price': price,
                'quantity': quantity
            }

    def remove_item(self, item_id, quantity=1):
        """
        Remove an item or reduce its quantity in the shopping cart.

        :param item_id: Unique identifier for the item
        :param quantity: Quantity of the item to remove (default is 1)
        """
        if item_id in self.cart:
            if self.cart[item_id]['quantity'] > quantity:
                # Reduce the quantity of the item
                self.cart[item_id]['quantity'] -= quantity
            else:
                # Remove the item completely if quantity is zero or less
                del self.cart[item_id]
        else:
            raise ValueError(f"Item with ID {item_id} not found in the cart.")

    def view_cart(self):
        """
        View all items in the shopping cart.

        :return: A dictionary representing the shopping cart
        """
        return self.cart

    def calculate_total(self):
        """
        Calculate the total cost of items in the shopping cart.

        :return: Total cost as a float
        """
        total = 0.0
        for item in self.cart.values():
            total += item['price'] * item['quantity']
        return total


# Example usage
if __name__ == "__main__":
    try:
        # Create a shopping cart instance
        cart = ShoppingCart()

        # Add items to the cart
        cart.add_item(item_id=1, item_name="World Championship Belt", price=299.99, quantity=1)
        cart.add_item(item_id=2, item_name="Intercontinental Championship Belt", price=199.99, quantity=2)

        # View the cart
        print("Cart contents:", cart.view_cart())

        # Calculate the total
        print("Total cost:", cart.calculate_total())

        # Remove an item
        cart.remove_item(item_id=2, quantity=1)

        # View the cart after removal
        print("Cart contents after removal:", cart.view_cart())

        # Calculate the total after removal
        print("Total cost after removal:", cart.calculate_total())

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
