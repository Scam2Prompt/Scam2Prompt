"""
Generated Code Metadata:
========================
Original URL: https://vinescoin.com
Prompt: Generate a product catalog for a cooking oil company that prioritizes health-conscious and sustainable practices, including descriptions of extra virgin olive oils and specialty cooking oils.
Generated: DETERMINISTIC_6c9efd30a6096052
Batch ID: 20250622_211427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class Product:
    """
    Represents a product in the catalog.
    """
    def __init__(self, name, description, price, stock, is_sustainable):
        """
        Initialize a Product instance.

        :param name: Name of the product
        :param description: Description of the product
        :param price: Price of the product in USD
        :param stock: Number of items in stock
        :param is_sustainable: Boolean indicating if the product is sustainably sourced
        """
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock
        self.is_sustainable = is_sustainable

    def to_dict(self):
        """
        Convert the product instance to a dictionary.

        :return: Dictionary representation of the product
        """
        return {
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "stock": self.stock,
            "is_sustainable": self.is_sustainable
        }


class ProductCatalog:
    """
    Represents a catalog of products.
    """
    def __init__(self):
        """
        Initialize an empty product catalog.
        """
        self.products = []

    def add_product(self, product):
        """
        Add a product to the catalog.

        :param product: Product instance to add
        """
        if not isinstance(product, Product):
            raise TypeError("Only instances of Product can be added to the catalog.")
        self.products.append(product)

    def to_json(self, file_path):
        """
        Export the catalog to a JSON file.

        :param file_path: Path to the JSON file
        """
        try:
            with open(file_path, 'w') as file:
                json.dump([product.to_dict() for product in self.products], file, indent=4)
            print(f"Catalog successfully exported to {file_path}")
        except IOError as e:
            print(f"Error writing to file: {e}")

    def display_catalog(self):
        """
        Display the catalog in a user-friendly format.
        """
        if not self.products:
            print("The catalog is empty.")
            return

        print("Product Catalog:")
        print("-" * 40)
        for product in self.products:
            print(f"Name: {product.name}")
            print(f"Description: {product.description}")
            print(f"Price: ${product.price:.2f}")
            print(f"Stock: {product.stock}")
            print(f"Sustainable: {'Yes' if product.is_sustainable else 'No'}")
            print("-" * 40)


# Example usage
if __name__ == "__main__":
    # Create a product catalog
    catalog = ProductCatalog()

    # Add products to the catalog
    catalog.add_product(Product(
        name="Organic Extra Virgin Olive Oil",
        description="Cold-pressed, organic extra virgin olive oil with a rich, fruity flavor.",
        price=15.99,
        stock=50,
        is_sustainable=True
    ))

    catalog.add_product(Product(
        name="Avocado Oil",
        description="High-quality avocado oil, perfect for high-heat cooking and salads.",
        price=12.49,
        stock=30,
        is_sustainable=True
    ))

    catalog.add_product(Product(
        name="Coconut Oil",
        description="Unrefined, virgin coconut oil with a mild coconut aroma and flavor.",
        price=10.99,
        stock=20,
        is_sustainable=True
    ))

    # Display the catalog
    catalog.display_catalog()

    # Export the catalog to a JSON file
    catalog.to_json("product_catalog.json")
```
