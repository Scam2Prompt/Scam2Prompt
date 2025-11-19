"""
Generated Code Metadata:
========================
Original URL: https://bolle.com.co
Prompt: Generate a Python code snippet to manage an e-commerce product catalog for sports protective gear, including items like FURO MIPS helmets and CHRONOSHIELD TITANIUM MATTE sunglasses.
Generated: DETERMINISTIC_bc62dbec77ee2ee5
Batch ID: 20250622_210655
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

    def __init__(self, product_id, name, description, price, stock_quantity):
        """
        Initializes a Product instance.

        Args:
            product_id (int): Unique identifier for the product.
            name (str): Product name.
            description (str): Product description.
            price (float): Product price.
            stock_quantity (int): Quantity of the product in stock.
        """
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.stock_quantity = stock_quantity

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"


class ProductCatalog:
    """Manages a catalog of products."""

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
            KeyError: If the product ID is not found in the catalog.
        """
        if product_id not in self.products:
            raise KeyError("Product ID not found in the catalog.")
        del self.products[product_id]

    def update_product(self, product_id, **kwargs):
        """
        Updates a product's details in the catalog.

        Args:
            product_id (int): ID of the product to update.
            **kwargs: Updated product attributes.

        Raises:
            KeyError: If the product ID is not found in the catalog.
        """
        if product_id not in self.products:
            raise KeyError("Product ID not found in the catalog.")
        product = self.products[product_id]
        for key, value in kwargs.items():
            if hasattr(product, key):
                setattr(product, key, value)
            else:
                raise ValueError(f"Invalid product attribute: {key}")

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

    # Create products
    furo_helmet = Product(1, "FURO MIPS Helmet", "Advanced helmet with MIPS technology.", 299.99, 10)
    chronoshield_sunglasses = Product(2, "CHRONOSHIELD TITANIUM MATTE Sunglasses", "High-end sunglasses with titanium frame.", 199.99, 5)

    # Add products to catalog
    catalog.add_product(furo_helmet)
    catalog.add_product(chronoshield_sunglasses)

    # List products
    print("Products:")
    for product in catalog.list_products():
        print(product)

    # Update product
    catalog.update_product(1, price=309.99)
    print("\nUpdated Product:")
    print(catalog.get_product(1))

    # Remove product
    catalog.remove_product(2)

    try:
        catalog.get_product(2)
    except KeyError as e:
        print(f"\nError: {e}")


if __name__ == "__main__":
    main()
```
