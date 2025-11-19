"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zkoutdoor.pk
Prompt: Generate a code snippet to create a shopping cart feature for an online furniture store like Tahirbrosfurniture, including functionalities for adding items, removing items, and calculating total price.
Generated: DETERMINISTIC_d875732b5e9472b9
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
        """Initializes a new shopping cart with an empty list."""
        self.items = []  # List to hold items in the cart

    def add_item(self, item_name, price, quantity=1):
        """
        Adds an item to the shopping cart.

        :param item_name: Name of the item to be added
        :param price: Price of the item
        :param quantity: Number of items to be added (default is 1)
        """
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 1:
            raise ValueError("Quantity must be at least 1.")

        # Check if item already exists in the cart and update quantity if it does
        for item in self.items:
            if item['name'] == item_name:
                item['quantity'] += quantity
                return
        
        # If item does not exist, add a new entry
        self.items.append({'name': item_name, 'price': price, 'quantity': quantity})

    def remove_item(self, item_name, quantity=1):
        """
        Removes an item from the shopping cart.

        :param item_name: Name of the item to be removed
        :param quantity: Number of items to be removed (default is 1)
        """
        if quantity < 1:
            raise ValueError("Quantity must be at least 1.")
        
        for item in self.items:
            if item['name'] == item_name:
                if item['quantity'] < quantity:
                    raise ValueError("Cannot remove more items than are in the cart.")
                item['quantity'] -= quantity
                # Remove item if quantity reaches zero
                if item['quantity'] == 0:
                    self.items.remove(item)
                return
        raise ValueError(f"Item '{item_name}' not found in the cart.")

    def calculate_total(self):
        """
        Calculates the total price of items in the shopping cart.

        :return: Total price of items in the cart
        """
        total = sum(item['price'] * item['quantity'] for item in self.items)
        return total

    def view_cart(self):
        """
        Returns a detailed view of items in the cart.

        :return: List of items in the cart with their details
        """
        return self.items

# Example usage
if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_item("Sofa", 299.99, 1)
    cart.add_item("Coffee Table", 89.99, 2)
    print("Current Cart:", cart.view_cart())
    print("Total Price:", cart.calculate_total())

    cart.remove_item("Coffee Table", 1)
    print("Cart after removing one Coffee Table:", cart.view_cart())
    print("Total Price:", cart.calculate_total())
```
