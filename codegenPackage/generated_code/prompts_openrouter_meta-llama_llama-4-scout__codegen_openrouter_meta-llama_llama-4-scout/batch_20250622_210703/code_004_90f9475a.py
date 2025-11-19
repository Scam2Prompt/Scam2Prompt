"""
Generated Code Metadata:
========================
Original URL: https://www.houseofolsha.com
Prompt: Create a product catalog for House of Olsha's latest Baju Kurung collections, including KAMELIA and KHYRA, with details on fabrics, designs, and sizes.
Generated: DETERMINISTIC_90f9475ae1b68a55
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
    def __init__(self, name, fabric, design, sizes):
        """
        Initialize a Product object.

        Args:
            name (str): Product name.
            fabric (str): Product fabric.
            design (str): Product design.
            sizes (list): List of available sizes.
        """
        self.name = name
        self.fabric = fabric
        self.design = design
        self.sizes = sizes

    def __str__(self):
        return f"{self.name} - {self.fabric}, {self.design}"


class ProductCatalog:
    def __init__(self):
        """
        Initialize a ProductCatalog object.
        """
        self.products = []

    def add_product(self, product):
        """
        Add a product to the catalog.

        Args:
            product (Product): Product object to add.
        """
        self.products.append(product)

    def display_catalog(self):
        """
        Display the product catalog.
        """
        for product in self.products:
            print(product)
            print(f"Sizes: {', '.join(product.sizes)}")
            print("------------------------")


def main():
    try:
        # Create products
        kamelia = Product(
            "KAMELIA",
            "Premium Satin",
            "Intricate Floral Embroidery",
            ["XS", "S", "M", "L", "XL"]
        )
        khyra = Product(
            "KHYRA",
            "Luxury Silk",
            "Modern Geometric Pattern",
            ["S", "M", "L", "XL", "XXL"]
        )

        # Create product catalog
        catalog = ProductCatalog()
        catalog.add_product(kamelia)
        catalog.add_product(khyra)

        # Display product catalog
        print("House of Olsha's Latest Baju Kurung Collections:")
        catalog.display_catalog()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
