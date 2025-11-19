"""
Generated Code Metadata:
========================
Original URL: https://khalom.in
Prompt: Generate a code snippet to create a shopping cart feature for an online clothing store, similar to the one described on Khalomclothing, including functions for adding items, viewing the cart, and checking out.
Generated: DETERMINISTIC_f0e0cef4231590dd
Batch ID: 20250612_160720
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
    A class to represent a shopping cart for an online clothing store.
    """

    def __init__(self):
        """
        Initializes an empty shopping cart.
        """
        self.cart = []  # List to store items in the cart
        self.total_price = 0.0  # Total price of items in the cart

    def add_item(self, item_name, price, quantity=1):
        """
        Adds an item to the shopping cart.

        :param item_name: Name of the item to add
        :param price: Price of the item
        :param quantity: Quantity of the item (default is 1)
        """
        if price < 0 or quantity < 1:
            raise ValueError("Price must be non-negative and quantity must be at least 1.")
        
        # Add item to the cart
        self.cart.append({
            "item_name": item_name,
            "price": price,
            "quantity": quantity
        })
        self.total_price += price * quantity
        print(f"Added {quantity} x {item_name} to the cart.")

    def view_cart(self):
        """
        Displays the contents of the shopping cart.
        """
        if not self.cart:
            print("Your cart is empty.")
            return
        
        print("Shopping Cart:")
        for index, item in enumerate(self.cart, start=1):
            print(f"{index}. {item['item_name']} - ${item['price']:.2f} x {item['quantity']}")
        print(f"Total Price: ${self.total_price:.2f}")

    def checkout(self):
        """
        Proceeds to checkout and clears the cart.
        """
        if not self.cart:
            print("Your cart is empty. Add items before checking out.")
            return
        
        print("Proceeding to checkout...")
        print("Order Summary:")
        self.view_cart()
        print("Thank you for your purchase!")
        
        # Clear the cart after checkout
        self.cart.clear()
        self.total_price = 0.0


# Example usage
if __name__ == "__main__":
    try:
        # Create a shopping cart instance
        cart = ShoppingCart()

        # Add items to the cart
        cart.add_item("T-Shirt", 19.99, 2)
        cart.add_item("Jeans", 49.99, 1)
        cart.add_item("Jacket", 89.99, 1)

        # View the cart
        cart.view_cart()

        # Checkout
        cart.checkout()

        # View the cart after checkout
        cart.view_cart()
    except Exception as e:
        print(f"An error occurred: {e}")
```
