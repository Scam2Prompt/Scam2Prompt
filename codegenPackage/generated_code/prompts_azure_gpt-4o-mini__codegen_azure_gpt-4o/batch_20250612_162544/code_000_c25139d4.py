"""
Generated Code Metadata:
========================
Original URL: https://asacanelbrazzz.blogspot.com
Prompt: Generate a code snippet to create a shopping cart functionality for an e-commerce site that includes categories like "Ambientes Perfumados" and "Móveis Decoração."
Generated: DETERMINISTIC_c25139d4a984b2b9
Batch ID: 20250612_162544
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
    """
    Represents a product in the shopping cart.
    """
    def __init__(self, name, category, price, quantity=1):
        """
        Initialize a product with name, category, price, and quantity.
        :param name: str - Name of the product
        :param category: str - Category of the product (e.g., "Ambientes Perfumados", "Móveis Decoração")
        :param price: float - Price of the product
        :param quantity: int - Quantity of the product (default is 1)
        """
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def __str__(self):
        """
        String representation of the product.
        """
        return f"{self.name} ({self.category}) - ${self.price:.2f} x {self.quantity}"


class ShoppingCart:
    """
    Represents a shopping cart for an e-commerce site.
    """
    def __init__(self):
        """
        Initialize an empty shopping cart.
        """
        self.items = []

    def add_product(self, product):
        """
        Add a product to the shopping cart.
        :param product: Product - The product to add
        """
        if not isinstance(product, Product):
            raise TypeError("Expected a Product instance.")
        self.items.append(product)

    def remove_product(self, product_name):
        """
        Remove a product from the shopping cart by name.
        :param product_name: str - Name of the product to remove
        """
        for item in self.items:
            if item.name == product_name:
                self.items.remove(item)
                return
        raise ValueError(f"Product '{product_name}' not found in the cart.")

    def calculate_total(self):
        """
        Calculate the total cost of all items in the shopping cart.
        :return: float - Total cost
        """
        return sum(item.price * item.quantity for item in self.items)

    def list_items(self):
        """
        List all items in the shopping cart.
        :return: list - List of product strings
        """
        return [str(item) for item in self.items]

    def clear_cart(self):
        """
        Clear all items from the shopping cart.
        """
        self.items = []


# Example usage
if __name__ == "__main__":
    try:
        # Create products
        product1 = Product(name="Lavender Diffuser", category="Ambientes Perfumados", price=25.99, quantity=2)
        product2 = Product(name="Wooden Coffee Table", category="Móveis Decoração", price=120.00, quantity=1)

        # Create shopping cart
        cart = ShoppingCart()

        # Add products to the cart
        cart.add_product(product1)
        cart.add_product(product2)

        # List items in the cart
        print("Items in the cart:")
        for item in cart.list_items():
            print(item)

        # Calculate total
        print(f"Total cost: ${cart.calculate_total():.2f}")

        # Remove a product
        cart.remove_product("Lavender Diffuser")
        print("Items after removal:")
        for item in cart.list_items():
            print(item)

        # Clear the cart
        cart.clear_cart()
        print("Cart cleared.")
        print(f"Items in the cart: {cart.list_items()}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
