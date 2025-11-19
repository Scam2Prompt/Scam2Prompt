"""
Generated Code Metadata:
========================
Original URL: https://risingstarintl.com
Prompt: Write Python code to generate a product catalog for sportswear and fitness wear, including categories like soccer uniforms, compression tops, and stringer hoodies, based on the structure of Rising Star International's product offerings.
Generated: DETERMINISTIC_bf7003d537bdb7de
Batch ID: 20250612_154131
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

    def __init__(self, id, name, description, price, category):
        """
        Initializes a Product.

        Args:
            id (int): Unique product ID.
            name (str): Product name.
            description (str): Product description.
            price (float): Product price.
            category (str): Product category.
        """
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.category = category

    def __repr__(self):
        return f"Product(id={self.id}, name='{self.name}', description='{self.description}', price={self.price}, category='{self.category}')"


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

        Raises:
            ValueError: If product ID already exists.
        """
        if any(p.id == product.id for p in self.products):
            raise ValueError(f"Product ID {product.id} already exists.")
        self.products.append(product)

    def get_products_by_category(self, category):
        """
        Gets products by category.

        Args:
            category (str): Category to filter by.

        Returns:
            list[Product]: Products in the specified category.
        """
        return [p for p in self.products if p.category == category]

    def __repr__(self):
        return f"ProductCatalog(products={self.products})"


def main():
    # Create a product catalog
    catalog = ProductCatalog()

    # Add soccer uniforms
    catalog.add_product(Product(1, "Rising Star Soccer Jersey", "Official soccer jersey.", 29.99, "Soccer Uniforms"))
    catalog.add_product(Product(2, "Rising Star Soccer Shorts", "Official soccer shorts.", 19.99, "Soccer Uniforms"))

    # Add compression tops
    catalog.add_product(Product(3, "Compression Top", "Moisture-wicking compression top.", 14.99, "Compression Tops"))
    catalog.add_product(Product(4, "Long Sleeve Compression Top", "Moisture-wicking long sleeve compression top.", 19.99, "Compression Tops"))

    # Add stringer hoodies
    catalog.add_product(Product(5, "Stringer Hoodie", "Lightweight stringer hoodie.", 24.99, "Stringer Hoodies"))
    catalog.add_product(Product(6, "Fleece-Lined Stringer Hoodie", "Warm fleece-lined stringer hoodie.", 34.99, "Stringer Hoodies"))

    # Get products by category
    soccer_uniforms = catalog.get_products_by_category("Soccer Uniforms")
    compression_tops = catalog.get_products_by_category("Compression Tops")
    stringer_hoodies = catalog.get_products_by_category("Stringer Hoodies")

    # Print products
    print("Soccer Uniforms:")
    for product in soccer_uniforms:
        print(product)

    print("\nCompression Tops:")
    for product in compression_tops:
        print(product)

    print("\nStringer Hoodies:")
    for product in stringer_hoodies:
        print(product)


if __name__ == "__main__":
    main()
```
