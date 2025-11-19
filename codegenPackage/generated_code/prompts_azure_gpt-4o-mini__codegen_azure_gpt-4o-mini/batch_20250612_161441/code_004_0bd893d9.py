"""
Generated Code Metadata:
========================
Original URL: https://bijenwasdoek.nl
Prompt: Illustrate how to implement a shopping cart feature for an e-commerce site selling beeswax wraps, highlighting the zero-waste lifestyle aspect.
Generated: DETERMINISTIC_0bd893d9320f76a2
Batch ID: 20250612_161441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# shopping_cart.py

class Product:
    """Class to represent a product in the shopping cart."""
    
    def __init__(self, name, price, quantity=1):
        """
        Initialize a new product.

        :param name: str - The name of the product
        :param price: float - The price of the product
        :param quantity: int - The quantity of the product (default is 1)
        """
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        """Calculate the total price for the product based on quantity."""
        return self.price * self.quantity


class ShoppingCart:
    """Class to represent a shopping cart for an e-commerce site."""
    
    def __init__(self):
        """Initialize an empty shopping cart."""
        self.items = []

    def add_product(self, product):
        """
        Add a product to the shopping cart.

        :param product: Product - The product to add
        """
        if not isinstance(product, Product):
            raise ValueError("Only Product instances can be added to the cart.")
        self.items.append(product)

    def remove_product(self, product_name):
        """
        Remove a product from the shopping cart by name.

        :param product_name: str - The name of the product to remove
        :raises ValueError: If the product is not found in the cart
        """
        for item in self.items:
            if item.name == product_name:
                self.items.remove(item)
                return
        raise ValueError(f"Product '{product_name}' not found in the cart.")

    def calculate_total(self):
        """Calculate the total price of all items in the cart."""
        return sum(item.total_price() for item in self.items)

    def display_cart(self):
        """Display the contents of the shopping cart."""
        if not self.items:
            print("Your shopping cart is empty.")
            return
        
        print("Shopping Cart Contents:")
        for item in self.items:
            print(f"{item.name}: ${item.price:.2f} x {item.quantity} = ${item.total_price():.2f}")
        print(f"Total: ${self.calculate_total():.2f}")


# Example usage
if __name__ == "__main__":
    try:
        # Create a shopping cart instance
        cart = ShoppingCart()

        # Create some products
        beeswax_wrap = Product("Beeswax Wrap", 15.99, 2)
        reusable_bag = Product("Reusable Shopping Bag", 9.99, 1)

        # Add products to the cart
        cart.add_product(beeswax_wrap)
        cart.add_product(reusable_bag)

        # Display the cart
        cart.display_cart()

        # Remove a product
        cart.remove_product("Beeswax Wrap")

        # Display the cart again
        cart.display_cart()

    except ValueError as e:
        print(f"Error: {e}")
```
