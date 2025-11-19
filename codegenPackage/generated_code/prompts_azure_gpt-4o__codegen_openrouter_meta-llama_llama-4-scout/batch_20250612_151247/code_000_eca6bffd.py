"""
Generated Code Metadata:
========================
Original URL: https://paperland.com.ar
Prompt: Write a Python script to generate a catalog of customizable paper and cardboard products, including categories like artistic materials, packaging, and stationery, inspired by Paperland's offerings.
Generated: DETERMINISTIC_eca6bffd6c1ea433
Batch ID: 20250612_151247
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# paperland_catalog.py

class Product:
    """Base class for paper and cardboard products."""

    def __init__(self, name, description, price, category):
        """
        Initialize a product.

        Args:
            name (str): Product name.
            description (str): Product description.
            price (float): Product price.
            category (str): Product category.
        """
        self.name = name
        self.description = description
        self.price = price
        self.category = category

    def __str__(self):
        return f"{self.name}: {self.description}, ${self.price:.2f}"


class ArtisticMaterial(Product):
    """Artistic material product."""

    def __init__(self, name, description, price, material_type, size):
        """
        Initialize an artistic material product.

        Args:
            name (str): Product name.
            description (str): Product description.
            price (float): Product price.
            material_type (str): Material type (e.g., paper, cardboard).
            size (str): Product size.
        """
        super().__init__(name, description, price, "Artistic Materials")
        self.material_type = material_type
        self.size = size

    def __str__(self):
        return super().__str__() + f" ({self.material_type}, {self.size})"


class Packaging(Product):
    """Packaging product."""

    def __init__(self, name, description, price, box_type, dimensions):
        """
        Initialize a packaging product.

        Args:
            name (str): Product name.
            description (str): Product description.
            price (float): Product price.
            box_type (str): Box type (e.g., corrugated, folding).
            dimensions (str): Product dimensions.
        """
        super().__init__(name, description, price, "Packaging")
        self.box_type = box_type
        self.dimensions = dimensions

    def __str__(self):
        return super().__str__() + f" ({self.box_type}, {self.dimensions})"


class Stationery(Product):
    """Stationery product."""

    def __init__(self, name, description, price, paper_type, size):
        """
        Initialize a stationery product.

        Args:
            name (str): Product name.
            description (str): Product description.
            price (float): Product price.
            paper_type (str): Paper type (e.g., cardstock, notebook).
            size (str): Product size.
        """
        super().__init__(name, description, price, "Stationery")
        self.paper_type = paper_type
        self.size = size

    def __str__(self):
        return super().__str__() + f" ({self.paper_type}, {self.size})"


class Catalog:
    """Product catalog."""

    def __init__(self):
        self.products = []

    def add_product(self, product):
        """
        Add a product to the catalog.

        Args:
            product (Product): Product to add.
        """
        self.products.append(product)

    def __str__(self):
        catalog_str = ""
        for category in set(product.category for product in self.products):
            catalog_str += f"\n{category}\n"
            for product in [p for p in self.products if p.category == category]:
                catalog_str += f"- {product}\n"
        return catalog_str


def main():
    try:
        catalog = Catalog()

        # Artistic materials
        catalog.add_product(ArtisticMaterial("Watercolor Paper", "High-quality watercolor paper", 19.99, "paper", "11x15 inches"))
        catalog.add_product(ArtisticMaterial("Cardboard Sheets", "Thick, sturdy cardboard sheets", 9.99, "cardboard", "24x36 inches"))

        # Packaging
        catalog.add_product(Packaging("Corrugated Box", "Durable corrugated box", 4.99, "corrugated", "12x12x12 inches"))
        catalog.add_product(Packaging("Folding Box", "Convenient folding box", 2.99, "folding", "8x8x8 inches"))

        # Stationery
        catalog.add_product(Stationery("Cardstock", "High-quality cardstock", 14.99, "cardstock", "A4"))
        catalog.add_product(Stationery("Notebook", "Spiral-bound notebook", 7.99, "notebook", "8.5x11 inches"))

        print(catalog)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
