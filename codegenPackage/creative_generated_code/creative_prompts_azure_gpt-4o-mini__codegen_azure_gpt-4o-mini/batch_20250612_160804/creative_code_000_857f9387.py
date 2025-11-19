"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meatmaster.pe
Prompt: Generate a code snippet for a product catalog that includes various sizes and types of "Cajas Chinas" and "Cilindros" as described on the Meat Master website.
Generated: DETERMINISTIC_857f93878a20e6eb
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# product_catalog.py

class Product:
    """Class to represent a product in the catalog."""

    def __init__(self, name, category, sizes, price):
        """
        Initialize a product with a name, category, available sizes, and price.

        :param name: str - Name of the product
        :param category: str - Category of the product (e.g., Cajas Chinas, Cilindros)
        :param sizes: list - List of available sizes for the product
        :param price: float - Price of the product
        """
        self.name = name
        self.category = category
        self.sizes = sizes
        self.price = price

    def __str__(self):
        """Return a string representation of the product."""
        return f"{self.name} ({self.category}): Sizes: {', '.join(self.sizes)} - Price: ${self.price:.2f}"


class ProductCatalog:
    """Class to manage a product catalog."""

    def __init__(self):
        """Initialize an empty product catalog."""
        self.products = []

    def add_product(self, product):
        """
        Add a product to the catalog.

        :param product: Product - an instance of Product to add to the catalog
        """
        if not isinstance(product, Product):
            raise ValueError("The product must be an instance of the Product class.")
        self.products.append(product)

    def list_products(self):
        """Return a list of all products in the catalog."""
        return [str(product) for product in self.products]

    def find_product_by_category(self, category):
        """
        Find products by category.

        :param category: str - The category to search for
        :return: list - List of products in the specified category
        """
        return [product for product in self.products if product.category.lower() == category.lower()]


def main():
    """Main function to demonstrate the product catalog."""
    try:
        # Create an instance of the product catalog
        catalog = ProductCatalog()

        # Define products
        caja_china_small = Product("Caja China Small", "Cajas Chinas", ["Small"], 299.99)
        caja_china_large = Product("Caja China Large", "Cajas Chinas", ["Large"], 499.99)
        cilindro_mediano = Product("Cilindro Mediano", "Cilindros", ["Medium"], 199.99)
        cilindro_grande = Product("Cilindro Grande", "Cilindros", ["Large"], 249.99)

        # Add products to the catalog
        catalog.add_product(caja_china_small)
        catalog.add_product(caja_china_large)
        catalog.add_product(cilindro_mediano)
        catalog.add_product(cilindro_grande)

        # List all products
        print("Product Catalog:")
        for product in catalog.list_products():
            print(product)

        # Find products by category
        print("\nCajas Chinas:")
        for product in catalog.find_product_by_category("Cajas Chinas"):
            print(product)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
