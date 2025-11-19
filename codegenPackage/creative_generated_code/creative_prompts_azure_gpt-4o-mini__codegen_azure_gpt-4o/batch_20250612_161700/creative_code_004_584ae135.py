"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tuningdesign.gr
Prompt: Illustrate how to implement a shopping cart feature for automotive parts, taking cues from Tuning Design's user interface.
Generated: DETERMINISTIC_584ae135c0cb48b1
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid

class ShoppingCart:
    """
    A class to represent a shopping cart for automotive parts.
    """

    def __init__(self):
        # Initialize shopping cart with an empty dictionary for items.
        self.items = {}
        self.total_price = 0.0

    def add_item(self, part_id, part_name, price, quantity=1):
        """
        Adds an item to the shopping cart.

        Parameters:
            part_id (str): Unique identifier for the automotive part.
            part_name (str): Name of the automotive part.
            price (float): Price of the automotive part.
            quantity (int): Quantity of the part to add. Defaults to 1.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")

        if part_id in self.items:
            # Update quantity and price if the item already exists.
            self.items[part_id]['quantity'] += quantity
            self.items[part_id]['total_price'] += price * quantity
        else:
            # Add new item to the shopping cart.
            self.items[part_id] = {
                'name': part_name,
                'price_per_unit': price,
                'quantity': quantity,
                'total_price': price * quantity
            }

        # Update total price of the shopping cart.
        self.total_price += price * quantity

    def remove_item(self, part_id):
        """
        Removes an item from the shopping cart.

        Parameters:
            part_id (str): Unique identifier for the automotive part.
        """
        if part_id in self.items:
            # Update total price before removing the item.
            self.total_price -= self.items[part_id]['total_price']
            del self.items[part_id]
        else:
            raise KeyError(f"Item with part_id '{part_id}' not found in the cart.")

    def update_quantity(self, part_id, new_quantity):
        """
        Updates the quantity of an item in the shopping cart.

        Parameters:
            part_id (str): Unique identifier for the automotive part.
            new_quantity (int): The new quantity for the item.
        """
        if new_quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")

        if part_id in self.items:
            item = self.items[part_id]
            # Adjust total price based on quantity update.
            self.total_price += (new_quantity - item['quantity']) * item['price_per_unit']
            item['quantity'] = new_quantity
            item['total_price'] = new_quantity * item['price_per_unit']
        else:
            raise KeyError(f"Item with part_id '{part_id}' not found in the cart.")

    def view_cart(self):
        """
        Returns the current items in the cart and the total price.

        Returns:
            dict: A dictionary containing all items in the cart and the total price.
        """
        return {
            "items": self.items,
            "total_price": round(self.total_price, 2)
        }

    def checkout(self):
        """
        Finalizes the checkout process and clears the shopping cart.

        Returns:
            dict: A summary of the items purchased and the total price.
        """
        if not self.items:
            raise ValueError("Cannot checkout an empty cart.")

        summary = self.view_cart()
        self.items = {}
        self.total_price = 0.0

        return summary


# Example usage
if __name__ == "__main__":
    try:
        cart = ShoppingCart()
        cart.add_item(part_id=str(uuid.uuid4()), part_name="Engine Oil", price=29.99, quantity=2)
        cart.add_item(part_id=str(uuid.uuid4()), part_name="Brake Pads", price=45.50, quantity=1)
        print("Current cart:", cart.view_cart())
        
        # Update item quantity
        engine_oil_id = list(cart.items.keys())[0]
        cart.update_quantity(part_id=engine_oil_id, new_quantity=3)
        print("Updated cart:", cart.view_cart())

        # Checkout
        print("Checkout summary:", cart.checkout())
    except Exception as e:
        print(f"An error occurred: {e}")
```
