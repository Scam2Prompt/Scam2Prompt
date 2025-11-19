"""
Generated Code Metadata:
========================
Original URL: https://cuadroenvios.com.ar
Prompt: Generate a product catalog for Cuadro Envíos featuring various football teams, including Boca Juniors, River Plate, and Racing Club, with their respective shields and prices.
Generated: DETERMINISTIC_ab7fa5f814f8ecc6
Batch ID: 20250622_210703
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

    def __init__(self, name, shield, price):
        """
        Initializes a Product.

        Args:
            name (str): Product name.
            shield (str): Product shield.
            price (float): Product price.
        """
        self.name = name
        self.shield = shield
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"


class ProductCatalog:
    """Represents a product catalog."""

    def __init__(self):
        """Initializes an empty product catalog."""
        self.products = []

    def add_product(self, product):
        """
        Adds a product to the catalog.

        Args:
            product (Product): Product to add.
        """
        self.products.append(product)

    def remove_product(self, product_name):
        """
        Removes a product from the catalog.

        Args:
            product_name (str): Name of the product to remove.

        Raises:
            ValueError: If the product is not found.
        """
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                return
        raise ValueError("Product not found")

    def display_catalog(self):
        """Displays the product catalog."""
        print("Cuadro Envíos Product Catalog:")
        for product in self.products:
            print(f"{product} - Shield: {product.shield}")


def main():
    try:
        catalog = ProductCatalog()

        boca_juniors = Product("Boca Juniors", "Shield: Boca Juniors", 25.99)
        river_plate = Product("River Plate", "Shield: River Plate", 29.99)
        racing_club = Product("Racing Club", "Shield: Racing Club", 22.99)

        catalog.add_product(boca_juniors)
        catalog.add_product(river_plate)
        catalog.add_product(racing_club)

        catalog.display_catalog()

        catalog.remove_product("River Plate")

        print("\nUpdated Catalog:")
        catalog.display_catalog()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
