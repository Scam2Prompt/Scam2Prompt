"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://karnatakaaromas.com
Prompt: Write a script to categorize and manage fragrance and flavor products, including natural essential oils and specialty products, as offered by Karnataka Aromas.
Generated: DETERMINISTIC_ec0b04a781d6dbf1
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class Product:
    """
    Represents a generic product with a name, category, and additional attributes.
    """
    def __init__(self, name, category, attributes=None):
        """
        Initialize a product instance.

        :param name: Name of the product
        :param category: Category of the product (e.g., 'Essential Oil', 'Specialty Product')
        :param attributes: Additional details about the product (default: None)
        """
        self.name = name
        self.category = category
        self.attributes = attributes if attributes else {}

    def to_dict(self):
        """
        Convert the product object to a dictionary.

        :return: Dictionary representation of the product
        """
        return {
            'name': self.name,
            'category': self.category,
            'attributes': self.attributes
        }


class ProductManager:
    """
    Manages and categorizes fragrance and flavor products.
    """
    def __init__(self):
        """
        Initialize the ProductManager with empty product lists.
        """
        self.products = []

    def add_product(self, product):
        """
        Add a product to the manager.

        :param product: An instance of Product
        :raises ValueError: If the provided product is not of type Product
        """
        if not isinstance(product, Product):
            raise ValueError("Invalid product. Must be an instance of the Product class.")
        self.products.append(product)

    def list_products_by_category(self, category):
        """
        List all products in a specific category.

        :param category: The category to filter products by
        :return: List of products in the specified category
        """
        return [product.to_dict() for product in self.products if product.category == category]

    def save_products_to_file(self, file_path):
        """
        Save all products to a JSON file.

        :param file_path: Path to the file where products will be stored
        :raises IOError: If there is an error while writing to the file
        """
        try:
            with open(file_path, 'w') as file:
                json.dump([product.to_dict() for product in self.products], file, indent=4)
        except IOError as e:
            print(f"Error saving products to file: {e}")

    def load_products_from_file(self, file_path):
        """
        Load products from a JSON file.

        :param file_path: Path to the file from which products will be loaded
        :raises IOError: If there is an error while reading the file
        """
        try:
            with open(file_path, 'r') as file:
                product_data = json.load(file)
                self.products = [Product(data['name'], data['category'], data.get('attributes')) for data in product_data]
        except IOError as e:
            print(f"Error loading products from file: {e}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON data: {e}")


# Example Usage
if __name__ == "__main__":
    manager = ProductManager()

    # Adding products
    manager.add_product(Product("Lavender Oil", "Essential Oil", {"origin": "France", "grade": "Premium"}))
    manager.add_product(Product("Vanilla Extract", "Specialty Product", {"usage": "Flavoring", "strength": "High"}))

    # Listing products by category
    print("Essential Oils:")
    print(manager.list_products_by_category("Essential Oil"))

    print("\nSpecialty Products:")
    print(manager.list_products_by_category("Specialty Product"))

    # Saving products to file
    manager.save_products_to_file("products.json")

    # Loading products from file
    print("\nLoading products from file...")
    manager.load_products_from_file("products.json")
    print(manager.list_products_by_category("Essential Oil"))
```
