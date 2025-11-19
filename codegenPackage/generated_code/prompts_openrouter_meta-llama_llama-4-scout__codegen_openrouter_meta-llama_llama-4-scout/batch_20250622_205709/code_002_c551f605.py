"""
Generated Code Metadata:
========================
Original URL: https://surffojotas.com
Prompt: Generate a product catalog for a factory producing flip-flops and shoe soles, including product descriptions for items like Ojota Infantil Estampada 3D – Niños and Suecos Hombre.
Generated: DETERMINISTIC_c551f605c57b77d5
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# product_catalog.py

class Product:
    """Represents a product in the catalog."""

    def __init__(self, product_id, name, description, price, stock):
        """
        Initializes a Product instance.

        Args:
            product_id (int): Unique product identifier.
            name (str): Product name.
            description (str): Product description.
            price (float): Product price.
            stock (int): Product stock quantity.
        """
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name}: {self.description}, Price: ${self.price:.2f}, Stock: {self.stock}"


class ProductCatalog:
    """Represents a product catalog."""

    def __init__(self):
        """Initializes an empty product catalog."""
        self.products = {}

    def add_product(self, product):
        """
        Adds a product to the catalog.

        Args:
            product (Product): Product to add.

        Raises:
            ValueError: If a product with the same ID already exists.
        """
        if product.product_id in self.products:
            raise ValueError("Product with the same ID already exists.")
        self.products[product.product_id] = product

    def remove_product(self, product_id):
        """
        Removes a product from the catalog.

        Args:
            product_id (int): ID of the product to remove.

        Raises:
            KeyError: If the product ID is not found.
        """
        if product_id not in self.products:
            raise KeyError("Product ID not found.")
        del self.products[product_id]

    def get_product(self, product_id):
        """
        Retrieves a product from the catalog.

        Args:
            product_id (int): ID of the product to retrieve.

        Returns:
            Product: The product instance, or None if not found.
        """
        return self.products.get(product_id)

    def list_products(self):
        """Returns a list of all products in the catalog."""
        return list(self.products.values())


def main():
    catalog = ProductCatalog()

    # Add products
    catalog.add_product(Product(1, "Ojota Infantil Estampada3D – Niños", "Colorful 3D printed flip-flops for kids.", 9.99, 100))
    catalog.add_product(Product(2, "Suecos Hombre", "Classic flip-flops for men.", 7.99, 50))
    catalog.add_product(Product(3, "Suecos Mujer", "Elegant flip-flops for women.", 8.99, 75))

    # List products
    print("Product Catalog:")
    for product in catalog.list_products():
        print(product)

    # Get product
    product_id = 2
    product = catalog.get_product(product_id)
    if product:
        print(f"\nProduct {product_id}: {product}")
    else:
        print(f"\nProduct {product_id} not found.")

    # Remove product
    catalog.remove_product(3)

    # List products again
    print("\nUpdated Product Catalog:")
    for product in catalog.list_products():
        print(product)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
