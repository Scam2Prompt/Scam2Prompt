"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oromaticas.com
Prompt: Generate a code snippet for an e-commerce application that allows users to browse and purchase agroecological products like medicinal plants and fresh vegetables from Oromáticas.
Generated: DETERMINISTIC_1e823f060f974968
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: ecommerce_app.py

import uuid
import sys


class Product:
    """
    Represents a product in the e-commerce application.
    """

    def __init__(self, name, description, price, stock):
        """
        Initialize the Product object.
        
        :param name: Name of the product
        :param description: Description of the product
        :param price: Price of the product
        :param stock: Quantity available in stock
        """
        self.id = str(uuid.uuid4())  # Unique identifier for the product
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock


class Cart:
    """
    Represents a shopping cart for a user.
    """

    def __init__(self):
        """
        Initialize the Cart object with an empty list of items.
        """
        self.items = []  # List to store cart items

    def add_item(self, product, quantity):
        """
        Add an item to the cart.

        :param product: The product to add
        :param quantity: Quantity of the product
        :raises ValueError: If the product stock is insufficient
        """
        if product.stock < quantity:
            raise ValueError(f"Insufficient stock for product: {product.name}")
        self.items.append({'product': product, 'quantity': quantity})
        product.stock -= quantity  # Update product stock

    def remove_item(self, product_id):
        """
        Remove an item from the cart.

        :param product_id: ID of the product to remove
        """
        self.items = [item for item in self.items if item['product'].id != product_id]

    def calculate_total(self):
        """
        Calculate the total cost of items in the cart.

        :return: Total cost of items in the cart
        """
        return sum(item['product'].price * item['quantity'] for item in self.items)


class ECommerceApp:
    """
    Represents the main e-commerce application.
    """

    def __init__(self):
        """
        Initialize the ECommerceApp object with products and a shopping cart.
        """
        self.products = []  # List to store available products
        self.cart = Cart()

    def add_product(self, name, description, price, stock):
        """
        Add a new product to the product list.

        :param name: Name of the product
        :param description: Description of the product
        :param price: Price of the product
        :param stock: Quantity available in stock
        """
        product = Product(name, description, price, stock)
        self.products.append(product)

    def list_products(self):
        """
        List all available products.

        :return: List of products
        """
        return self.products

    def purchase(self):
        """
        Complete the purchase of items in the cart.
        
        :return: Confirmation message
        :raises ValueError: If the cart is empty
        """
        if not self.cart.items:
            raise ValueError("Cart is empty")
        total = self.cart.calculate_total()
        self.cart.items = []  # Clear the cart after purchase
        return f"Purchase completed successfully. Total amount: ${total:.2f}"


# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the application
        app = ECommerceApp()

        # Add products to the catalog
        app.add_product("Chamomile", "Medicinal plant for calming", 5.99, 100)
        app.add_product("Fresh Lettuce", "Organic lettuce for salads", 2.49, 50)

        # List available products
        print("Available products:")
        for product in app.list_products():
            print(f"- {product.name}: {product.description} (${product.price}, Stock: {product.stock})")

        # Add items to the cart
        product_to_add = app.products[0]  # Assuming Chamomile is the first product
        app.cart.add_item(product_to_add, 2)

        print("\nCart items:")
        for item in app.cart.items:
            print(f"- {item['product'].name} x {item['quantity']}")

        # Complete the purchase
        print("\nProcessing purchase...")
        confirmation_message = app.purchase()
        print(confirmation_message)

    except ValueError as ve:
        print(f"Error: {ve}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
```
