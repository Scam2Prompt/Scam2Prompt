"""
Generated Code Metadata:
========================
Original URL: https://karlakarita.com.br
Prompt: Generate a code snippet that creates a shopping cart feature for an e-commerce site selling casual clothing, similar to the offerings on karlakarita.com.br.
Generated: DETERMINISTIC_c1b74c08ec907773
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
    """Represents a product in the shopping cart."""
    
    def __init__(self, product_id, name, price, quantity=1):
        """
        Initializes a Product object.

        Args:
            product_id (int): Unique identifier for the product.
            name (str): Name of the product.
            price (float): Price of the product.
            quantity (int, optional): Quantity of the product. Defaults to 1.
        """
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total(self):
        """Calculates the total cost of the product based on quantity."""
        return self.price * self.quantity


class ShoppingCart:
    """Represents a shopping cart for an e-commerce site."""
    
    def __init__(self):
        """Initializes an empty shopping cart."""
        self.products = {}

    def add_product(self, product, quantity=1):
        """
        Adds a product to the shopping cart.

        Args:
            product (Product): Product to add to the cart.
            quantity (int, optional): Quantity of the product. Defaults to 1.

        Raises:
            ValueError: If quantity is less than 1.
        """
        if quantity < 1:
            raise ValueError("Quantity must be 1 or more")

        product.quantity = quantity
        self.products[product.product_id] = product

    def remove_product(self, product_id):
        """
        Removes a product from the shopping cart.

        Args:
            product_id (int): ID of the product to remove.

        Raises:
            KeyError: If product is not found in the cart.
        """
        if product_id not in self.products:
            raise KeyError("Product not found in cart")
        del self.products[product_id]

    def update_quantity(self, product_id, quantity):
        """
        Updates the quantity of a product in the shopping cart.

        Args:
            product_id (int): ID of the product to update.
            quantity (int): New quantity of the product.

        Raises:
            KeyError: If product is not found in the cart.
            ValueError: If quantity is less than 1.
        """
        if product_id not in self.products:
            raise KeyError("Product not found in cart")
        if quantity < 1:
            raise ValueError("Quantity must be 1 or more")
        self.products[product_id].quantity = quantity

    def calculate_cart_total(self):
        """Calculates the total cost of all products in the shopping cart."""
        return sum(product.calculate_total() for product in self.products.values())

    def view_cart(self):
        """Displays the contents of the shopping cart."""
        for product in self.products.values():
            print(f"Product ID: {product.product_id}, Name: {product.name}, Quantity: {product.quantity}, Total: ${product.calculate_total():.2f}")


def main():
    # Example usage:
    cart = ShoppingCart()

    product1 = Product(1, "T-Shirt", 19.99)
    product2 = Product(2, "Jeans", 49.99)

    cart.add_product(product1)
    cart.add_product(product2, 2)

    print("Shopping Cart:")
    cart.view_cart()

    print(f"\nCart Total: ${cart.calculate_cart_total():.2f}")

    cart.update_quantity(1, 2)
    print("\nUpdated Shopping Cart:")
    cart.view_cart()

    print(f"\nUpdated Cart Total: ${cart.calculate_cart_total():.2f}")

    cart.remove_product(2)
    print("\nShopping Cart after removal:")
    cart.view_cart()

    print(f"\nCart Total after removal: ${cart.calculate_cart_total():.2f}")


if __name__ == "__main__":
    main()
```
