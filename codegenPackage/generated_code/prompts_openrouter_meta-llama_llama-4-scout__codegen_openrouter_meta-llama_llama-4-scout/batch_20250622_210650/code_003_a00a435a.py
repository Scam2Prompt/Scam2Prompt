"""
Generated Code Metadata:
========================
Original URL: https://morevacare.com
Prompt: "Create a product catalog for a natural cosmetics brand that features handgefertigte products with natural ingredients like Tonerde, ätherischen Öle, and Pflanzenöle."
Generated: DETERMINISTIC_a00a435adac90255
Batch ID: 20250622_210650
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

    def __init__(self, id: int, name: str, ingredients: list[str], price: float, description: str):
        """
        Initializes a Product.

        Args:
            id (int): Unique product ID.
            name (str): Product name.
            ingredients (list[str]): List of ingredients.
            price (float): Product price.
            description (str): Product description.
        """
        self.id = id
        self.name = name
        self.ingredients = ingredients
        self.price = price
        self.description = description

    def __str__(self):
        return f"{self.name} - {', '.join(self.ingredients)}"


class ProductCatalog:
    """Represents a product catalog."""

    def __init__(self):
        """Initializes an empty product catalog."""
        self.products = {}

    def add_product(self, product: Product):
        """
        Adds a product to the catalog.

        Args:
            product (Product): Product to add.

        Raises:
            ValueError: If a product with the same ID already exists.
        """
        if product.id in self.products:
            raise ValueError("Product with this ID already exists")
        self.products[product.id] = product

    def remove_product(self, id: int):
        """
        Removes a product from the catalog.

        Args:
            id (int): ID of the product to remove.

        Raises:
            KeyError: If the product does not exist.
        """
        if id not in self.products:
            raise KeyError("Product does not exist")
        del self.products[id]

    def get_product(self, id: int) -> Product:
        """
        Retrieves a product from the catalog.

        Args:
            id (int): ID of the product to retrieve.

        Returns:
            Product: The product with the given ID.

        Raises:
            KeyError: If the product does not exist.
        """
        return self.products[id]

    def list_products(self) -> list[Product]:
        """Returns a list of all products in the catalog."""
        return list(self.products.values())


def main():
    catalog = ProductCatalog()

    # Create products
    product1 = Product(
        1,
        "Clay Face Mask",
        ["Tonerde", "ätherische Öle"],
        19.99,
        "A soothing face mask made with natural clay and essential oils.",
    )
    product2 = Product(
        2,
        "Nourishing Body Oil",
        ["Pflanzenöle", "ätherische Öle"],
        14.99,
        "A rich and nourishing body oil made with plant oils and essential oils.",
    )

    # Add products to catalog
    catalog.add_product(product1)
    catalog.add_product(product2)

    # List products
    print("Product Catalog:")
    for product in catalog.list_products():
        print(product)

    # Get product
    print("\nGet Product:")
    product = catalog.get_product(1)
    print(product)
    print(product.description)

    # Remove product
    catalog.remove_product(2)

    # Try to get removed product
    try:
        catalog.get_product(2)
    except KeyError as e:
        print(f"\nError: {e}")


if __name__ == "__main__":
    main()
```
