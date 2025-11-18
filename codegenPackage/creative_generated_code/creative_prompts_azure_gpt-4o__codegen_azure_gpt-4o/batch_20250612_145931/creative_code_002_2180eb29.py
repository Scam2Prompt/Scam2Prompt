"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://viaisle.top
Prompt: Generate Python code to simulate a shopping cart system that supports querying inventory and processing orders, inspired by the features on 虚屿.
Generated: DETERMINISTIC_2180eb29e4668c1b
Batch ID: 20250612_145931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid

class Inventory:
    """
    A class to represent the inventory of items available in the store.
    """
    def __init__(self):
        # Dictionary to store items with their details (name, price, quantity)
        self.items = {}

    def add_item(self, item_id, name, price, quantity):
        """
        Add a new item or update existing item in the inventory.
        """
        if item_id in self.items:
            # Update quantity if item already exists
            self.items[item_id]['quantity'] += quantity
        else:
            # Add new item
            self.items[item_id] = {'name': name, 'price': price, 'quantity': quantity}

    def get_item(self, item_id):
        """
        Retrieve item details by item ID.
        """
        return self.items.get(item_id, None)

    def update_quantity(self, item_id, quantity):
        """
        Update the quantity of an item in the inventory.
        """
        if item_id in self.items:
            self.items[item_id]['quantity'] = quantity

    def list_items(self):
        """
        Return a list of all items in the inventory.
        """
        return self.items


class ShoppingCart:
    """
    A class to represent a customer's shopping cart.
    """
    def __init__(self, inventory):
        self.cart = {}  # Dictionary to store items added to the cart
        self.inventory = inventory  # Reference to inventory to check stock

    def add_to_cart(self, item_id, quantity):
        """
        Add an item to the cart if it is available in the inventory.
        """
        item = self.inventory.get_item(item_id)
        if not item:
            raise ValueError(f"Item with ID {item_id} does not exist in inventory.")
        if item['quantity'] < quantity:
            raise ValueError(f"Insufficient stock for item: {item['name']}")
        
        if item_id in self.cart:
            self.cart[item_id]['quantity'] += quantity
        else:
            self.cart[item_id] = {'name': item['name'], 'price': item['price'], 'quantity': quantity}

        # Reduce the inventory stock
        self.inventory.update_quantity(item_id, item['quantity'] - quantity)

    def remove_from_cart(self, item_id, quantity):
        """
        Remove an item or reduce its quantity in the cart.
        """
        if item_id not in self.cart:
            raise ValueError(f"Item with ID {item_id} is not in the cart.")
        
        if self.cart[item_id]['quantity'] < quantity:
            raise ValueError(f"Cannot remove more than {self.cart[item_id]['quantity']} items.")

        self.cart[item_id]['quantity'] -= quantity

        # Return the stock back to inventory
        item = self.inventory.get_item(item_id)
        self.inventory.update_quantity(item_id, item['quantity'] + quantity)

        if self.cart[item_id]['quantity'] == 0:
            del self.cart[item_id]

    def view_cart(self):
        """
        View the items currently in the shopping cart.
        """
        return self.cart

    def checkout(self):
        """
        Process the cart and generate an order summary.
        """
        if not self.cart:
            raise ValueError("Cart is empty. Add items before checkout.")

        total_price = sum(item['price'] * item['quantity'] for item in self.cart.values())
        order_id = str(uuid.uuid4())
        order_summary = {
            'order_id': order_id,
            'items': self.cart,
            'total_price': total_price
        }

        # Clear the cart after checkout
        self.cart = {}

        return order_summary


# Example usage (commented for clarity):
"""
# Initialize inventory
inventory = Inventory()
inventory.add_item('1', 'Apple', 0.5, 100)
inventory.add_item('2', 'Banana', 0.3, 150)
inventory.add_item('3', 'Orange', 0.7, 200)

# Initialize shopping cart
cart = ShoppingCart(inventory)

# Add items to the cart
cart.add_to_cart('1', 3)  # Add 3 Apples
cart.add_to_cart('2', 5)  # Add 5 Bananas

# View cart
print(cart.view_cart())

# Checkout
order = cart.checkout()
print(order)

# View inventory after checkout
print(inventory.list_items())
"""
```
