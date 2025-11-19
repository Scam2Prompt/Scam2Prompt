"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://brandsoutlet.qa
Prompt: Illustrate how to implement a shopping cart feature for an e-commerce site that mimics the functionality seen on Brands Outlet, including adding items to a wishlist.
Generated: DETERMINISTIC_f5372de6f6405eff
Batch ID: 20250612_155250
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid

class Item:
    """
    Represents an item in the e-commerce store.
    """
    def __init__(self, name, price):
        self.id = str(uuid.uuid4())  # Generate unique ID for the item
        self.name = name  # Name of the item
        self.price = price  # Price of the item

    def __repr__(self):
        return f"Item(name={self.name}, price={self.price})"


class ShoppingCart:
    """
    Represents a shopping cart for an e-commerce site.
    """
    def __init__(self):
        self.cart_items = []  # Stores items added to the cart
        self.wishlist_items = []  # Stores items added to the wishlist

    def add_to_cart(self, item):
        """
        Adds an item to the shopping cart.
        :param item: An instance of the Item class.
        """
        if not isinstance(item, Item):
            raise TypeError("Invalid item type. Must be an instance of Item.")
        self.cart_items.append(item)
        print(f"{item.name} added to cart.")

    def remove_from_cart(self, item_id):
        """
        Removes an item from the shopping cart by its ID.
        :param item_id: The unique ID of the item to remove.
        """
        for item in self.cart_items:
            if item.id == item_id:
                self.cart_items.remove(item)
                print(f"{item.name} removed from cart.")
                return
        print("Item not found in cart.")

    def add_to_wishlist(self, item):
        """
        Adds an item to the wishlist.
        :param item: An instance of the Item class.
        """
        if not isinstance(item, Item):
            raise TypeError("Invalid item type. Must be an instance of Item.")
        self.wishlist_items.append(item)
        print(f"{item.name} added to wishlist.")

    def remove_from_wishlist(self, item_id):
        """
        Removes an item from the wishlist by its ID.
        :param item_id: The unique ID of the item to remove.
        """
        for item in self.wishlist_items:
            if item.id == item_id:
                self.wishlist_items.remove(item)
                print(f"{item.name} removed from wishlist.")
                return
        print("Item not found in wishlist.")

    def view_cart(self):
        """
        Displays all items in the shopping cart.
        """
        if not self.cart_items:
            print("Your cart is empty.")
        else:
            print("Items in your cart:")
            for item in self.cart_items:
                print(f"- {item.name} (${item.price:.2f})")

    def view_wishlist(self):
        """
        Displays all items in the wishlist.
        """
        if not self.wishlist_items:
            print("Your wishlist is empty.")
        else:
            print("Items in your wishlist:")
            for item in self.wishlist_items:
                print(f"- {item.name} (${item.price:.2f})")


# Example usage:
if __name__ == "__main__":
    # Create some items
    item1 = Item(name="T-shirt", price=19.99)
    item2 = Item(name="Jeans", price=39.99)
    item3 = Item(name="Sneakers", price=59.99)

    # Initialize shopping cart
    cart = ShoppingCart()

    # Add items to cart and wishlist
    cart.add_to_cart(item1)
    cart.add_to_cart(item2)
    cart.view_cart()

    cart.add_to_wishlist(item3)
    cart.view_wishlist()

    # Remove an item from cart
    cart.remove_from_cart(item1.id)
    cart.view_cart()

    # Remove an item from wishlist
    cart.remove_from_wishlist(item3.id)
    cart.view_wishlist()
```
