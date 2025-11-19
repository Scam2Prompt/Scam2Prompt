"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lowbrowartcompany.com
Prompt: Illustrate how to implement a shopping cart feature for the Black Market Art Company site, focusing on adding and removing items like the "Asian Scorned" T-shirt.
Generated: DETERMINISTIC_15d97a51f9fed392
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Shopping Cart Implementation for Black Market Art Company.
The code allows users to add and remove items (e.g., "Asian Scorned" T-shirt) to/from a shopping cart.
"""

class ShoppingCart:
    def __init__(self):
        """
        Initialize an empty shopping cart.
        """
        self.cart = {}

    def add_item(self, item_name, quantity=1):
        """
        Add an item to the shopping cart.

        Parameters:
            item_name (str): Name of the item to add.
            quantity (int): Number of items to add (default is 1).
        """
        if quantity < 1:
            raise ValueError("Quantity must be at least 1")
        
        if item_name in self.cart:
            self.cart[item_name] += quantity
        else:
            self.cart[item_name] = quantity

        print(f"Added {quantity} x '{item_name}' to the shopping cart.")

    def remove_item(self, item_name, quantity=1):
        """
        Remove an item from the shopping cart.

        Parameters:
            item_name (str): Name of the item to remove.
            quantity (int): Number of items to remove (default is 1).
        """
        if item_name not in self.cart:
            print(f"'{item_name}' is not in the shopping cart.")
            return
        
        if quantity < 1:
            raise ValueError("Quantity must be at least 1")

        if self.cart[item_name] <= quantity:
            del self.cart[item_name]  # Remove the item completely if quantity is less or equal
            print(f"Removed '{item_name}' from the shopping cart.")
        else:
            self.cart[item_name] -= quantity
            print(f"Removed {quantity} x '{item_name}' from the shopping cart.")

    def view_cart(self):
        """
        Display the contents of the shopping cart.
        """
        if not self.cart:
            print("Your shopping cart is empty.")
        else:
            print("Shopping Cart Contents:")
            for item, quantity in self.cart.items():
                print(f" - {item}: {quantity}")

    def clear_cart(self):
        """
        Clear all items from the shopping cart.
        """
        self.cart.clear()
        print("Shopping cart cleared.")

# Example usage
if __name__ == "__main__":
    try:
        # Create a shopping cart instance
        cart = ShoppingCart()

        # Add items to the cart
        cart.add_item("Asian Scorned T-shirt", 2)
        cart.add_item("Black Market Art Poster", 1)

        # View the cart
        cart.view_cart()

        # Remove an item from the cart
        cart.remove_item("Asian Scorned T-shirt", 1)

        # View the cart again
        cart.view_cart()

        # Clear the cart
        cart.clear_cart()
        
        # View the cart to confirm it's empty
        cart.view_cart()
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
