"""
Generated Code Metadata:
========================
Original URL: https://mambowood.ir
Prompt: Write a Python code snippet to create an e-commerce website for selling wooden kitchen utensils, including a product catalog with prices and discounts.
Generated: DETERMINISTIC_9502378b34110dfc
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# e-commerce_website.py

class Product:
    """Represents a product in the catalog."""

    def __init__(self, id, name, price, discount=0):
        """
        Initializes a Product.

        Args:
            id (int): Unique product ID.
            name (str): Product name.
            price (float): Product price.
            discount (float, optional): Discount percentage. Defaults to 0.
        """
        self.id = id
        self.name = name
        self.price = price
        self.discount = discount

    def get_discounted_price(self):
        """Calculates the discounted price."""
        return self.price * (1 - self.discount / 100)


class Catalog:
    """Represents a product catalog."""

    def __init__(self):
        """Initializes an empty catalog."""
        self.products = {}

    def add_product(self, product):
        """
        Adds a product to the catalog.

        Args:
            product (Product): Product to add.
        """
        self.products[product.id] = product

    def get_product(self, id):
        """
        Retrieves a product by ID.

        Args:
            id (int): Product ID.

        Returns:
            Product: Product with the given ID, or None if not found.
        """
        return self.products.get(id)

    def list_products(self):
        """Returns a list of all products in the catalog."""
        return list(self.products.values())


class ECommerceWebsite:
    """Represents an e-commerce website."""

    def __init__(self, catalog):
        """
        Initializes an e-commerce website.

        Args:
            catalog (Catalog): Product catalog.
        """
        self.catalog = catalog
        self.cart = {}

    def add_to_cart(self, product_id, quantity):
        """
        Adds a product to the cart.

        Args:
            product_id (int): Product ID.
            quantity (int): Quantity to add.

        Raises:
            ValueError: If product not found or quantity is invalid.
        """
        product = self.catalog.get_product(product_id)
        if product is None:
            raise ValueError("Product not found")
        if quantity <= 0:
            raise ValueError("Invalid quantity")

        if product_id in self.cart:
            self.cart[product_id]["quantity"] += quantity
        else:
            self.cart[product_id] = {"product": product, "quantity": quantity}

    def view_cart(self):
        """Returns a dictionary of products in the cart."""
        return self.cart

    def checkout(self):
        """Calculates the total cost of products in the cart."""
        total = 0
        for item in self.cart.values():
            total += item["product"].get_discounted_price() * item["quantity"]
        return total


def main():
    # Create a product catalog
    catalog = Catalog()

    # Add products to the catalog
    catalog.add_product(Product(1, "Wooden Spoon", 9.99, 10))
    catalog.add_product(Product(2, "Wooden Fork", 8.99, 5))
    catalog.add_product(Product(3, "Wooden Knife", 12.99))

    # Create an e-commerce website
    website = ECommerceWebsite(catalog)

    try:
        # Add products to the cart
        website.add_to_cart(1, 2)
        website.add_to_cart(2, 1)

        # View cart
        cart = website.view_cart()
        print("Cart:")
        for product_id, item in cart.items():
            product = item["product"]
            print(f"{product.name} x {item['quantity']} = ${product.get_discounted_price() * item['quantity']:.2f}")

        # Checkout
        total = website.checkout()
        print(f"Total: ${total:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
