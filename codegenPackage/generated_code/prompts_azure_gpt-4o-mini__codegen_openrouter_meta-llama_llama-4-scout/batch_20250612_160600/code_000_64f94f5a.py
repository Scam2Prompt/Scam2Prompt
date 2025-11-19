"""
Generated Code Metadata:
========================
Original URL: https://livivid.com
Prompt: How can I generate code to create a shopping cart feature for a website selling handmade Tibetan clothing, similar to the offerings on livivid.com?
Generated: DETERMINISTIC_64f94f5abb8b7b41
Batch ID: 20250612_160600
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
    """Represents a handmade Tibetan clothing product."""

    def __init__(self, product_id, name, description, price):
        """
        Initializes a Product instance.

        Args:
            product_id (int): Unique product identifier.
            name (str): Product name.
            description (str): Product description.
            price (float): Product price.
        """
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price

class ShoppingCart:
    """Represents a shopping cart for a customer."""

    def __init__(self):
        """Initializes an empty shopping cart."""
        self.cart = {}

    def add_product(self, product, quantity=1):
        """
        Adds a product to the shopping cart.

        Args:
            product (Product): Product to add.
            quantity (int, optional): Quantity of the product. Defaults to 1.

        Raises:
            ValueError: If quantity is less than 1.
        """
        if quantity < 1:
            raise ValueError("Quantity must be 1 or more")

        if product.product_id in self.cart:
            self.cart[product.product_id]["quantity"] += quantity
        else:
            self.cart[product.product_id] = {"product": product, "quantity": quantity}

    def remove_product(self, product_id):
        """
        Removes a product from the shopping cart.

        Args:
            product_id (int): ID of the product to remove.

        Raises:
            KeyError: If the product is not in the cart.
        """
        if product_id not in self.cart:
            raise KeyError("Product not found in cart")

        del self.cart[product_id]

    def update_quantity(self, product_id, quantity):
        """
        Updates the quantity of a product in the shopping cart.

        Args:
            product_id (int): ID of the product to update.
            quantity (int): New quantity.

        Raises:
            KeyError: If the product is not in the cart.
            ValueError: If quantity is less than 1.
        """
        if product_id not in self.cart:
            raise KeyError("Product not found in cart")

        if quantity < 1:
            raise ValueError("Quantity must be 1 or more")

        self.cart[product_id]["quantity"] = quantity

    def calculate_total(self):
        """
        Calculates the total cost of the products in the shopping cart.

        Returns:
            float: Total cost.
        """
        total = sum(
            product["product"].price * product["quantity"]
            for product in self.cart.values()
        )
        return total

    def view_cart(self):
        """Prints the contents of the shopping cart."""
        print("Shopping Cart:")
        for product in self.cart.values():
            print(
                f"{product['product'].name} x {product['quantity']} = ${product['product'].price * product['quantity']:.2f}"
            )
        print(f"Total: ${self.calculate_total():.2f}")


# Example usage:
if __name__ == "__main__":
    # Create products
    product1 = Product(1, "Tibetan Robe", "Traditional Tibetan robe.", 99.99)
    product2 = Product(2, "Tibetan Scarf", "Handmade Tibetan scarf.", 19.99)

    # Create shopping cart
    cart = ShoppingCart()

    # Add products to cart
    cart.add_product(product1, 2)
    cart.add_product(product2)

    # View cart
    cart.view_cart()

    # Update quantity
    cart.update_quantity(1, 1)

    # View cart again
    cart.view_cart()

    # Remove product
    cart.remove_product(2)

    # View cart again
    cart.view_cart()
```
