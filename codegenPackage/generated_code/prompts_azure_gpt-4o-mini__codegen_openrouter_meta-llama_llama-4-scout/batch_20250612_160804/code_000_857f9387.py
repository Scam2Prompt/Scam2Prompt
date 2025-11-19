"""
Generated Code Metadata:
========================
Original URL: https://meatmaster.pe
Prompt: Generate a code snippet for a product catalog that includes various sizes and types of "Cajas Chinas" and "Cilindros" as described on the Meat Master website.
Generated: DETERMINISTIC_857f93878a20e6eb
Batch ID: 20250612_160804
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
    def __init__(self, name, description, price):
        """
        Initialize a Product.

        Args:
            name (str): Product name.
            description (str): Product description.
            price (float): Product price.
        """
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.description}, ${self.price:.2f}"


class CajaChina(Product):
    def __init__(self, size, price):
        """
        Initialize a Caja China.

        Args:
            size (str): Caja China size.
            price (float): Caja China price.
        """
        description = f"Caja China {size}"
        super().__init__("Caja China", description, price)
        self.size = size


class Cilindro(Product):
    def __init__(self, size, price):
        """
        Initialize a Cilindro.

        Args:
            size (str): Cilindro size.
            price (float): Cilindro price.
        """
        description = f"Cilindro {size}"
        super().__init__("Cilindro", description, price)
        self.size = size


class ProductCatalog:
    def __init__(self):
        """
        Initialize a Product Catalog.
        """
        self.products = []

    def add_product(self, product):
        """
        Add a product to the catalog.

        Args:
            product (Product): Product to add.
        """
        self.products.append(product)

    def __str__(self):
        catalog_str = "Product Catalog:\n"
        for i, product in enumerate(self.products, start=1):
            catalog_str += f"{i}. {product}\n"
        return catalog_str


def main():
    try:
        catalog = ProductCatalog()

        # Cajas Chinas
        caja_china_sizes = ["Chica", "Mediana", "Grande", "Extra Grande"]
        caja_china_prices = [19.99, 29.99, 39.99, 49.99]
        for size, price in zip(caja_china_sizes, caja_china_prices):
            catalog.add_product(CajaChina(size, price))

        # Cilindros
        cilindro_sizes = ["Pequeño", "Mediano", "Grande"]
        cilindro_prices = [14.99, 24.99, 34.99]
        for size, price in zip(cilindro_sizes, cilindro_prices):
            catalog.add_product(Cilindro(size, price))

        print(catalog)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
