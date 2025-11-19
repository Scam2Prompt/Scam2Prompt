"""
Generated Code Metadata:
========================
Original URL: https://craftimus.com
Prompt: Illustrate how to implement a shopping cart feature for Himalayan salt products, referencing the diverse range available at Craftimus Industries, such as salt shot glasses and detox lamps.
Generated: DETERMINISTIC_c3a87cce1e8a703d
Batch ID: 20250612_161700
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
        :param quantity: int - The quantity of the product
        """
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        """Calculate the total price for the product based on quantity."""
        return self.price * self.quantity


class ShoppingCart:
    """Class to represent a shopping cart."""
    
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

    def list_items(self):
        """List all items in the shopping cart."""
        return [(item.name, item.price, item.quantity) for item in self.items]

    def clear_cart(self):
        """Clear all items from the shopping cart."""
        self.items.clear()


# Example usage
if __name__ == "__main__":
    try:
        # Create a shopping cart instance
        cart = ShoppingCart()

        # Create some Himalayan salt products
        salt_shot_glass = Product("Himalayan Salt Shot Glass", 15.99, 2)
        detox_lamp = Product("Himalayan Detox Lamp", 29.99, 1)

        # Add products to the cart
        cart.add_product(salt_shot_glass)
        cart.add_product(detox_lamp)

        # List items in the cart
        print("Items in cart:", cart.list_items())

        # Calculate total price
        total = cart.calculate_total()
        print(f"Total price: ${total:.2f}")

        # Remove a product
        cart.remove_product("Himalayan Salt Shot Glass")
        print("Items in cart after removal:", cart.list_items())

        # Clear the cart
        cart.clear_cart()
        print("Items in cart after clearing:", cart.list_items())

    except ValueError as e:
        print(f"Error: {e}")
```
