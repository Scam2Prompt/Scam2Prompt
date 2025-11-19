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
# Import necessary modules
import json

# Define the Product class to represent individual products
class Product:
    def __init__(self, name, description, price, ingredients):
        """
        Initialize a Product instance.

        :param name: Name of the product
        :param description: Description of the product
        :param price: Price of the product in USD
        :param ingredients: List of ingredients used in the product
        """
        self.name = name
        self.description = description
        self.price = price
        self.ingredients = ingredients

    def to_dict(self):
        """
        Convert the Product instance to a dictionary for serialization.

        :return: Dictionary representation of the product
        """
        return {
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "ingredients": self.ingredients,
        }

# Define the ProductCatalog class to manage the catalog
class ProductCatalog:
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
            raise TypeError("Expected a Product instance.")
        self.products.append(product)

    def list_products(self):
        """
        List all products in the catalog.

        :return: List of dictionaries representing the products
        """
        return [product.to_dict() for product in self.products]

    def save_to_file(self, filename):
        """
        Save the product catalog to a JSON file.

        :param filename: Name of the file to save the catalog
        """
        try:
            with open(filename, "w", encoding="utf-8") as file:
                json.dump(self.list_products(), file, ensure_ascii=False, indent=4)
        except IOError as e:
            print(f"Error saving catalog to file: {e}")

    def load_from_file(self, filename):
        """
        Load the product catalog from a JSON file.

        :param filename: Name of the file to load the catalog from
        """
        try:
            with open(filename, "r", encoding="utf-8") as file:
                products_data = json.load(file)
                self.products = [
                    Product(
                        name=product["name"],
                        description=product["description"],
                        price=product["price"],
                        ingredients=product["ingredients"],
                    )
                    for product in products_data
                ]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading catalog from file: {e}")

# Example usage
if __name__ == "__main__":
    # Create a product catalog instance
    catalog = ProductCatalog()

    # Create some products
    product1 = Product(
        name="Tonerde Gesichtsmaske",
        description="Eine reinigende Gesichtsmaske mit natürlicher Tonerde.",
        price=15.99,
        ingredients=["Tonerde", "ätherisches Lavendelöl", "Pflanzenöl"]
    )

    product2 = Product(
        name="Ätherisches Öl Set",
        description="Ein Set aus 3 ätherischen Ölen für Aromatherapie.",
        price=29.99,
        ingredients=["ätherisches Teebaumöl", "ätherisches Zitronenöl", "ätherisches Pfefferminzöl"]
    )

    # Add products to the catalog
    catalog.add_product(product1)
    catalog.add_product(product2)

    # List products in the catalog
    print("Product Catalog:")
    for product in catalog.list_products():
        print(product)

    # Save the catalog to a file
    catalog.save_to_file("product_catalog.json")

    # Load the catalog from a file
    new_catalog = ProductCatalog()
    new_catalog.load_from_file("product_catalog.json")
    print("\nLoaded Product Catalog:")
    for product in new_catalog.list_products():
        print(product)
```
