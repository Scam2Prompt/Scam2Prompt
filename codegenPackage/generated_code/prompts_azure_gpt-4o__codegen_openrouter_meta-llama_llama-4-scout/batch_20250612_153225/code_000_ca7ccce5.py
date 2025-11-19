"""
Generated Code Metadata:
========================
Original URL: https://padmavatienterprise.org
Prompt: Write a Python script to generate a product catalog for a B2B industrial goods provider, including categories like "IT Materials," "Office Stationery," "Signage Materials," and "Packing Materials," with options for adding descriptions and prices.
Generated: DETERMINISTIC_ca7ccce560c3b42b
Batch ID: 20250612_153225
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

    def __init__(self, name, description="", price=0.0):
        """
        Initializes a Product.

        Args:
            name (str): Product name.
            description (str, optional): Product description. Defaults to "".
            price (float, optional): Product price. Defaults to 0.0.
        """
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"{self.name}: ${self.price:.2f}\n  - {self.description}"


class Category:
    """Represents a category in the product catalog."""

    def __init__(self, name):
        """
        Initializes a Category.

        Args:
            name (str): Category name.
        """
        self.name = name
        self.products = []

    def add_product(self, product):
        """
        Adds a product to the category.

        Args:
            product (Product): Product to add.
        """
        self.products.append(product)

    def __str__(self):
        category_str = f"**{self.name}**\n"
        for product in self.products:
            category_str += f"  {product}\n"
        return category_str


class ProductCatalog:
    """Represents a product catalog."""

    def __init__(self):
        self.categories = []

    def add_category(self, category):
        """
        Adds a category to the catalog.

        Args:
            category (Category): Category to add.
        """
        self.categories.append(category)

    def __str__(self):
        catalog_str = ""
        for category in self.categories:
            catalog_str += str(category) + "\n"
        return catalog_str


def main():
    try:
        catalog = ProductCatalog()

        # Create categories
        it_materials = Category("IT Materials")
        office_stationery = Category("Office Stationery")
        signage_materials = Category("Signage Materials")
        packing_materials = Category("Packing Materials")

        # Add products to categories
        it_materials.add_product(Product("Laptop", "High-performance laptop", 999.99))
        it_materials.add_product(Product("Mouse", "Wireless mouse", 19.99))

        office_stationery.add_product(Product("Pen", "Ballpoint pen", 0.99))
        office_stationery.add_product(Product("Paper", "A4 paper pack", 4.99))

        signage_materials.add_product(Product("Banner", "Vinyl banner", 29.99))
        signage_materials.add_product(Product("Sticker", "Vinyl sticker", 9.99))

        packing_materials.add_product(Product("Box", "Cardboard box", 1.99))
        packing_materials.add_product(Product("Tape", "Packing tape", 2.99))

        # Add categories to catalog
        catalog.add_category(it_materials)
        catalog.add_category(office_stationery)
        catalog.add_category(signage_materials)
        catalog.add_category(packing_materials)

        # Print catalog
        print(catalog)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
