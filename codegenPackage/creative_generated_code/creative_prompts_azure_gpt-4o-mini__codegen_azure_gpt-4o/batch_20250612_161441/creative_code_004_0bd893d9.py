"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bijenwasdoek.nl
Prompt: Illustrate how to implement a shopping cart feature for an e-commerce site selling beeswax wraps, highlighting the zero-waste lifestyle aspect.
Generated: DETERMINISTIC_0bd893d9320f76a2
Batch ID: 20250612_161441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Shopping Cart Feature for Beeswax Wraps E-Commerce Site
This script implements a shopping cart functionality for an e-commerce platform focused on selling 
zero-waste beeswax wraps. It adheres to clean code principles, includes error handling, 
and highlights the zero-waste lifestyle in some of the messages.
"""

class Product:
    """
    Represents a product in the store.
    Attributes:
        id (int): Unique identifier for the product.
        name (str): Name of the product.
        price (float): Price of the product.
        description (str): A short description of the product.
    """
    def __init__(self, product_id, name, price, description):
        self.id = product_id
        self.name = name
        self.price = price
        self.description = description


class ShoppingCart:
    """
    Represents a shopping cart for the user.
    Attributes:
        items (dict): Dictionary where keys are Product IDs and values are tuples (Product object, quantity).
    """
    def __init__(self):
        self.items = {}

    def add_to_cart(self, product, quantity=1):
        """
        Adds a product to the cart or updates the quantity if it already exists.
        Args:
            product (Product): The product to be added.
            quantity (int): Number of units to add (default: 1).
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0.")
        if product.id in self.items:
            # Update quantity if product is already in the cart
            self.items[product.id] = (product, self.items[product.id][1] + quantity)
        else:
            # Add product to the cart
            self.items[product.id] = (product, quantity)

    def remove_from_cart(self, product_id):
        """
        Removes a product from the cart.
        Args:
            product_id (int): The ID of the product to be removed.
        """
        if product_id not in self.items:
            raise KeyError(f"Product with ID {product_id} not found in the cart.")
        del self.items[product_id]

    def update_quantity(self, product_id, quantity):
        """
        Updates the quantity of a product in the cart.
        Args:
            product_id (int): The ID of the product to be updated.
            quantity (int): New quantity of the product.
        """
        if product_id not in self.items:
            raise KeyError(f"Product with ID {product_id} not found in the cart.")
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0.")
        product = self.items[product_id][0]
        self.items[product_id] = (product, quantity)

    def view_cart(self):
        """
        Displays the contents of the shopping cart in a user-friendly format.
        """
        if not self.items:
            print("Your cart is empty! Embrace zero-waste living by adding beeswax wraps.")
            return
        total = 0
        print("Here are the items in your cart:")
        for product_id, (product, quantity) in self.items.items():
            print(f"- {product.name} (x{quantity}): ${product.price:.2f} each")
            total += product.price * quantity
        print(f"Total: ${total:.2f}")
        print("Thank you for choosing sustainable products!")

    def checkout(self):
        """
        Simulates the checkout process.
        """
        if not self.items:
            print("Your cart is empty! Add some eco-friendly beeswax wraps and promote zero-waste.")
            return
        print("Checking out...")
        self.view_cart()
        print("Order placed successfully! Continue your zero-waste journey!")
        self.items.clear()  # Clear the cart after checkout


# Example Usage:
if __name__ == "__main__":
    # Create some products
    beeswax_wrap_small = Product(1, "Small Beeswax Wrap", 12.99, "Perfect for wrapping snacks and small items.")
    beeswax_wrap_medium = Product(2, "Medium Beeswax Wrap", 15.99, "Ideal for sandwiches and medium dishes.")
    beeswax_wrap_large = Product(3, "Large Beeswax Wrap", 18.99, "Great for covering large bowls and plates.")

    # Initialize shopping cart
    cart = ShoppingCart()

    try:
        # Add products to the cart
        cart.add_to_cart(beeswax_wrap_small, 2)
        cart.add_to_cart(beeswax_wrap_medium)
        cart.add_to_cart(beeswax_wrap_large, 3)

        # View the cart
        cart.view_cart()

        # Update quantity
        cart.update_quantity(3, 2)

        # Remove a product
        cart.remove_from_cart(2)

        # View updated cart
        cart.view_cart()

        # Checkout
        cart.checkout()

    except Exception as e:
        print(f"An error occurred: {e}")
```
