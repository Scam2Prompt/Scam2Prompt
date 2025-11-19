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
class Item:
    """Represents an item in the shopping cart or wishlist."""
    
    def __init__(self, item_id, name, price):
        self.item_id = item_id
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Item(id={self.item_id}, name={self.name}, price={self.price})"


class ShoppingCart:
    """Manages the shopping cart functionality."""
    
    def __init__(self):
        self.cart_items = []

    def add_item(self, item):
        """Adds an item to the shopping cart."""
        if isinstance(item, Item):
            self.cart_items.append(item)
            print(f"Added to cart: {item}")
        else:
            raise ValueError("Item must be an instance of Item.")

    def remove_item(self, item_id):
        """Removes an item from the shopping cart by item ID."""
        for item in self.cart_items:
            if item.item_id == item_id:
                self.cart_items.remove(item)
                print(f"Removed from cart: {item}")
                return
        raise ValueError("Item not found in cart.")

    def view_cart(self):
        """Returns a list of items currently in the shopping cart."""
        return self.cart_items

    def total_price(self):
        """Calculates the total price of the items in the cart."""
        return sum(item.price for item in self.cart_items)


class Wishlist:
    """Manages the wishlist functionality."""
    
    def __init__(self):
        self.wishlist_items = []

    def add_to_wishlist(self, item):
        """Adds an item to the wishlist."""
        if isinstance(item, Item):
            self.wishlist_items.append(item)
            print(f"Added to wishlist: {item}")
        else:
            raise ValueError("Item must be an instance of Item.")

    def remove_from_wishlist(self, item_id):
        """Removes an item from the wishlist by item ID."""
        for item in self.wishlist_items:
            if item.item_id == item_id:
                self.wishlist_items.remove(item)
                print(f"Removed from wishlist: {item}")
                return
        raise ValueError("Item not found in wishlist.")

    def view_wishlist(self):
        """Returns a list of items currently in the wishlist."""
        return self.wishlist_items


# Example usage
if __name__ == "__main__":
    cart = ShoppingCart()
    wishlist = Wishlist()

    # Create some items
    item1 = Item(item_id=1, name="Laptop", price=999.99)
    item2 = Item(item_id=2, name="Smartphone", price=499.99)

    # Adding items to the cart
    try:
        cart.add_item(item1)
        cart.add_item(item2)
        print("Current cart:", cart.view_cart())
        print("Total price:", cart.total_price())
        
        # Removing an item from the cart
        cart.remove_item(item_id=1)
        print("Current cart after removal:", cart.view_cart())
        
    except ValueError as e:
        print(f"Error: {e}")

    # Adding items to the wishlist
    try:
        wishlist.add_to_wishlist(item1)
        wishlist.add_to_wishlist(item2)
        print("Current wishlist:", wishlist.view_wishlist())
        
        # Removing an item from the wishlist
        wishlist.remove_from_wishlist(item_id=2)
        print("Current wishlist after removal:", wishlist.view_wishlist())
        
    except ValueError as e:
        print(f"Error: {e}")
```
