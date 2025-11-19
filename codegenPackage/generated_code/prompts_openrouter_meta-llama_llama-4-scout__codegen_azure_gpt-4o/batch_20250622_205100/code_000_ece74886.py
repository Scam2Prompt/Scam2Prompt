"""
Generated Code Metadata:
========================
Original URL: https://villagepetbrazz.blogspot.com
Prompt: Write a Python code snippet to create an e-commerce product catalog for pet supplies, including items like "Caixa de Transporte" and "Antipulgas e Carrapatos Frontline Plus".
Generated: DETERMINISTIC_ece74886d9abd955
Batch ID: 20250622_205100
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

# Define a class for Product
class Product:
    """
    Represents a product in the catalog.
    """
    def __init__(self, product_id, name, description, price, stock_quantity):
        """
        Initialize a Product instance.

        :param product_id: Unique identifier for the product
        :param name: Name of the product
        :param description: Description of the product
        :param price: Price of the product (float)
        :param stock_quantity: Quantity of the product in stock (int)
        """
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.stock_quantity = stock_quantity

    def to_dict(self):
        """
        Convert the Product instance to a dictionary.

        :return: Dictionary representation of the product
        """
        return {
            "product_id": self.product_id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "stock_quantity": self.stock_quantity,
        }

# Define a class for ProductCatalog
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
            raise TypeError("Expected a Product instance.")
        self.products.append(product)

    def list_products(self):
        """
        List all products in the catalog.

        :return: List of dictionaries representing the products
        """
        return [product.to_dict() for product in self.products]

    def save_to_file(self, file_path):
        """
        Save the product catalog to a JSON file.

        :param file_path: Path to the file where the catalog will be saved
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.list_products(), file, indent=4)
        except IOError as e:
            print(f"Error saving catalog to file: {e}")

    def load_from_file(self, file_path):
        """
        Load the product catalog from a JSON file.

        :param file_path: Path to the file to load the catalog from
        """
        try:
            with open(file_path, 'r') as file:
                products_data = json.load(file)
                self.products = [
                    Product(
                        product_id=product["product_id"],
                        name=product["name"],
                        description=product["description"],
                        price=product["price"],
                        stock_quantity=product["stock_quantity"],
                    )
                    for product in products_data
                ]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading catalog from file: {e}")

# Example usage
if __name__ == "__main__":
    # Create a product catalog
    catalog = ProductCatalog()

    # Add products to the catalog
    catalog.add_product(Product(1, "Caixa de Transporte", "Durable pet transport box", 120.50, 10))
    catalog.add_product(Product(2, "Antipulgas e Carrapatos Frontline Plus", "Effective flea and tick treatment", 89.99, 25))

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
