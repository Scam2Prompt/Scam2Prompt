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
    """Represents a product in the e-commerce site."""

    def __init__(self, id, name, category, price):
        """
        Initializes a Product instance.

        Args:
            id (int): Unique product identifier.
            name (str): Product name.
            category (str): Product category.
            price (float): Product price.
        """
        self.id = id
        self.name = name
        self.category = category
        self.price = price

    def __repr__(self):
        return f"Product(id={self.id}, name='{self.name}', category='{self.category}', price={self.price})"


class ShoppingCart:
    """Represents a shopping cart for an e-commerce site."""

    def __init__(self):
        """Initializes an empty shopping cart."""
        self.products = {}

    def add_product(self, product, quantity=1):
        """
        Adds a product to the shopping cart.

        Args:
            product (Product): Product to add.
            quantity (int, optional): Product quantity. Defaults to 1.

        Raises:
            ValueError: If quantity is less than 1.
        """
        if quantity < 1:
            raise ValueError("Quantity must be 1 or more")

        if product.id in self.products:
            self.products[product.id]["quantity"] += quantity
        else:
            self.products[product.id] = {"product": product, "quantity": quantity}

    def remove_product(self, product_id):
        """
        Removes a product from the shopping cart.

        Args:
            product_id (int): ID of the product to remove.

        Raises:
            KeyError: If product is not in the cart.
        """
        if product_id not in self.products:
            raise KeyError("Product not found in cart")

        del self.products[product_id]

    def update_quantity(self, product_id, quantity):
        """
        Updates the quantity of a product in the shopping cart.

        Args:
            product_id (int): ID of the product to update.
            quantity (int): New quantity.

        Raises:
            KeyError: If product is not in the cart.
            ValueError: If quantity is less than 1.
        """
        if product_id not in self.products:
            raise KeyError("Product not found in cart")

        if quantity < 1:
            raise ValueError("Quantity must be 1 or more")

        self.products[product_id]["quantity"] = quantity

    def calculate_total(self):
        """
        Calculates the total cost of products in the shopping cart.

        Returns:
            float: Total cost.
        """
        total = sum(
            product["product"].price * product["quantity"]
            for product in self.products.values()
        )
        return total

    def __repr__(self):
        return f"ShoppingCart(products={self.products})"


# Example usage
if __name__ == "__main__":
    # Create products
    product1 = Product(1, "Perfume", "Ambientes Perfumados", 19.99)
    product2 = Product(2, "Sofa", "Móveis Decoração", 499.99)
    product3 = Product(3, "Diffuser", "Ambientes Perfumados", 29.99)

    # Create shopping cart
    cart = ShoppingCart()

    # Add products to cart
    cart.add_product(product1, 2)
    cart.add_product(product2)
    cart.add_product(product3, 3)

    # Print cart contents
    print("Cart Contents:")
    for product_id, product in cart.products.items():
        print(f"{product['product'].name} x {product['quantity']}")

    # Calculate total
    print(f"\nTotal: ${cart.calculate_total():.2f}")

    # Update quantity
    cart.update_quantity(1, 1)

    # Print updated cart contents
    print("\nUpdated Cart Contents:")
    for product_id, product in cart.products.items():
        print(f"{product['product'].name} x {product['quantity']}")

    # Calculate updated total
    print(f"\nUpdated Total: ${cart.calculate_total():.2f}")

    # Remove product
    cart.remove_product(2)

    # Print updated cart contents
    print("\nUpdated Cart Contents after removal:")
    for product_id, product in cart.products.items():
        print(f"{product['product'].name} x {product['quantity']}")

    # Calculate updated total
    print(f"\nUpdated Total: ${cart.calculate_total():.2f}")
```
