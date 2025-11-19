"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://emarket.ps
Prompt: How can I implement a shopping cart feature for an online store that includes customizable products such as mugs and notebooks?
Generated: DETERMINISTIC_7dfb9c32bf2be627
Batch ID: 20250612_155356
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
shopping_cart.py

This script implements a shopping cart feature for an online store
with customizable products such as mugs and notebooks. The shopping
cart allows adding items, customizing them, removing items, viewing
the cart, and calculating the total price.
"""

class Product:
    """
    Represents a product in the store.
    Customizable products can have additional attributes like color, size, or text.
    """
    def __init__(self, name, base_price, customizations=None):
        """
        Initialize the product with its name, price, and customizations.

        :param name: Name of the product (e.g., 'Mug').
        :param base_price: Base price of the product.
        :param customizations: Dictionary of customizations (e.g., {'color': 'red', 'text': 'Hello'}).
        """
        self.name = name
        self.base_price = base_price
        self.customizations = customizations if customizations else {}

    def calculate_price(self):
        """
        Calculate the price of the product based on customizations.
        Additional charges for customizations can be added here.

        :return: Final price of the product.
        """
        # Example: Add $2 for each customization
        customization_cost = 2 * len(self.customizations)
        return self.base_price + customization_cost

    def __str__(self):
        """
        String representation of the product.
        """
        customizations = ", ".join(f"{key}: {value}" for key, value in self.customizations.items())
        return f"{self.name} (${self.calculate_price()}) - Customizations: {customizations}"


class ShoppingCart:
    """
    Represents a shopping cart for managing products.
    """
    def __init__(self):
        """
        Initialize an empty shopping cart.
        """
        self.items = []

    def add_product(self, product):
        """
        Add a product to the cart.

        :param product: Instance of Product to add to the cart.
        """
        if not isinstance(product, Product):
            raise ValueError("Invalid product. Must be an instance of Product.")
        self.items.append(product)
        print(f"Added {product.name} to the cart.")

    def remove_product(self, product_name):
        """
        Remove a product from the cart by name.

        :param product_name: Name of the product to remove.
        """
        for product in self.items:
            if product.name == product_name:
                self.items.remove(product)
                print(f"Removed {product.name} from the cart.")
                return
        print(f"Product '{product_name}' not found in the cart.")

    def view_cart(self):
        """
        Display all products in the cart.
        """
        if not self.items:
            print("Your cart is empty.")
        else:
            print("Shopping Cart:")
            for product in self.items:
                print(f" - {product}")

    def calculate_total(self):
        """
        Calculate the total price of all items in the cart.

        :return: Total price of the cart.
        """
        return sum(product.calculate_price() for product in self.items)


# Example usage:

if __name__ == "__main__":
    # Create customizable products
    mug = Product(name="Mug", base_price=10, customizations={"color": "blue", "text": "Best Day Ever"})
    notebook = Product(name="Notebook", base_price=15, customizations={"size": "A5", "text": "Work Hard"})

    # Create a shopping cart
    cart = ShoppingCart()

    # Add products to the cart
    cart.add_product(mug)
    cart.add_product(notebook)

    # View the cart
    cart.view_cart()

    # Calculate total price
    print(f"Total Price: ${cart.calculate_total()}")

    # Remove a product
    cart.remove_product("Mug")

    # View the cart again
    cart.view_cart()

    # Calculate total price again
    print(f"Total Price: ${cart.calculate_total()}")
```
