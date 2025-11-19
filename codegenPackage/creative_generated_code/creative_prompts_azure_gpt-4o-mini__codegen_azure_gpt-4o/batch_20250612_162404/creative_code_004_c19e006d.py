"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://centraldata-enterpristore.com
Prompt: Illustrate how to implement a shopping cart functionality that allows users to save items for later on an eCommerce platform like Central Data's.
Generated: DETERMINISTIC_c19e006d3ec6efb3
Batch ID: 20250612_162404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Implementation of a shopping cart functionality for an eCommerce platform.
This includes the ability to add items to the cart and save items for later.
"""

from typing import List, Dict

class ShoppingCart:
    def __init__(self):
        """
        Initialize the shopping cart with an empty items list
        and an empty save-for-later list.
        """
        self.cart_items: List[Dict[str, any]] = []  # Items in the cart
        self.saved_for_later_items: List[Dict[str, any]] = []  # Items saved for later

    def add_to_cart(self, item_id: int, name: str, price: float, quantity: int) -> None:
        """
        Add an item to the shopping cart.

        Parameters:
        item_id (int): Unique identifier for the item.
        name (str): Name of the item.
        price (float): Price of the item.
        quantity (int): Quantity of the item being added.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        item = {"item_id": item_id, "name": name, "price": price, "quantity": quantity}
        self.cart_items.append(item)

    def remove_from_cart(self, item_id: int) -> None:
        """
        Remove an item from the shopping cart by its ID.

        Parameters:
        item_id (int): Unique identifier for the item to remove.
        """
        self.cart_items = [item for item in self.cart_items if item["item_id"] != item_id]

    def move_to_save_for_later(self, item_id: int) -> None:
        """
        Move an item from the cart to the Save-for-Later list.

        Parameters:
        item_id (int): Unique identifier for the item to move.
        """
        item_to_move = None
        for item in self.cart_items:
            if item["item_id"] == item_id:
                item_to_move = item
                break
        
        if item_to_move:
            self.cart_items.remove(item_to_move)
            self.saved_for_later_items.append(item_to_move)
        else:
            raise ValueError(f"Item with ID {item_id} not found in cart.")

    def restore_to_cart(self, item_id: int) -> None:
        """
        Restore an item from the Save-for-Later list back to the cart.

        Parameters:
        item_id (int): Unique identifier for the item to restore.
        """
        item_to_restore = None
        for item in self.saved_for_later_items:
            if item["item_id"] == item_id:
                item_to_restore = item
                break
        
        if item_to_restore:
            self.saved_for_later_items.remove(item_to_restore)
            self.cart_items.append(item_to_restore)
        else:
            raise ValueError(f"Item with ID {item_id} not found in Save-for-Later list.")

    def view_cart(self) -> List[Dict[str, any]]:
        """
        View all items currently in the shopping cart.

        Returns:
        List[Dict[str, any]]: List of items in the cart.
        """
        return self.cart_items

    def view_saved_for_later(self) -> List[Dict[str, any]]:
        """
        View all items currently in the Save-for-Later list.

        Returns:
        List[Dict[str, any]]: List of items in the Save-for-Later list.
        """
        return self.saved_for_later_items


# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the shopping cart
        cart = ShoppingCart()

        # Add items to the cart
        cart.add_to_cart(item_id=1, name="Laptop", price=999.99, quantity=1)
        cart.add_to_cart(item_id=2, name="Mouse", price=49.99, quantity=2)

        # View cart items
        print("Cart Items:", cart.view_cart())

        # Move an item to the Save-for-Later list
        cart.move_to_save_for_later(item_id=2)
        print("Cart Items after moving an item to Save-for-Later:", cart.view_cart())
        print("Saved For Later Items:", cart.view_saved_for_later())

        # Restore an item from the Save-for-Later list back to the cart
        cart.restore_to_cart(item_id=2)
        print("Cart Items after restoring an item:", cart.view_cart())
        print("Saved For Later Items after restoring an item:", cart.view_saved_for_later())

    except Exception as e:
        print(f"Error: {e}")
```
