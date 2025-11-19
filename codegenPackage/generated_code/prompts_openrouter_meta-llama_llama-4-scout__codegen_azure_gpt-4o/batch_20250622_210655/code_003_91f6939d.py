"""
Generated Code Metadata:
========================
Original URL: https://dombrinde.com.br
Prompt: "Create a product catalog for a company that offers customized promotional products, including canetas personalizadas, sacolas personalizadas, and garrafas personalizadas, with descriptions and pricing."
Generated: DETERMINISTIC_91f6939d3a34df12
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# product_catalog.py

# Import necessary modules
import json

class ProductCatalog:
    """
    A class to represent a product catalog for customized promotional products.
    """

    def __init__(self):
        """
        Initialize the product catalog with predefined products.
        """
        self.products = [
            {
                "id": 1,
                "name": "Canetas Personalizadas",
                "description": "Stylish and customizable pens for promotional use.",
                "price": 2.50  # Price per unit in USD
            },
            {
                "id": 2,
                "name": "Sacolas Personalizadas",
                "description": "Durable and eco-friendly customizable bags.",
                "price": 5.00  # Price per unit in USD
            },
            {
                "id": 3,
                "name": "Garrafas Personalizadas",
                "description": "High-quality customizable bottles for everyday use.",
                "price": 8.75  # Price per unit in USD
            }
        ]

    def list_products(self):
        """
        List all products in the catalog.
        :return: List of products.
        """
        return self.products

    def get_product_by_id(self, product_id):
        """
        Retrieve a product by its ID.
        :param product_id: ID of the product to retrieve.
        :return: Product details if found, else None.
        """
        for product in self.products:
            if product["id"] == product_id:
                return product
        return None

    def add_product(self, name, description, price):
        """
        Add a new product to the catalog.
        :param name: Name of the product.
        :param description: Description of the product.
        :param price: Price of the product.
        :return: Newly added product.
        """
        if not name or not description or price <= 0:
            raise ValueError("Invalid product details provided.")

        new_product = {
            "id": len(self.products) + 1,
            "name": name,
            "description": description,
            "price": price
        }
        self.products.append(new_product)
        return new_product

    def save_catalog_to_file(self, file_path):
        """
        Save the product catalog to a JSON file.
        :param file_path: Path to the file where the catalog will be saved.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.products, file, indent=4)
        except IOError as e:
            print(f"Error saving catalog to file: {e}")

    def load_catalog_from_file(self, file_path):
        """
        Load the product catalog from a JSON file.
        :param file_path: Path to the file to load the catalog from.
        """
        try:
            with open(file_path, 'r') as file:
                self.products = json.load(file)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading catalog from file: {e}")


# Example usage
if __name__ == "__main__":
    catalog = ProductCatalog()

    # List all products
    print("Product Catalog:")
    for product in catalog.list_products():
        print(product)

    # Add a new product
    try:
        new_product = catalog.add_product(
            name="Cadernos Personalizados",
            description="Customizable notebooks for promotional use.",
            price=3.50
        )
        print("\nNew Product Added:")
        print(new_product)
    except ValueError as e:
        print(f"Error adding product: {e}")

    # Save catalog to file
    catalog.save_catalog_to_file("product_catalog.json")

    # Load catalog from file
    catalog.load_catalog_from_file("product_catalog.json")
    print("\nCatalog Loaded from File:")
    for product in catalog.list_products():
        print(product)
```
