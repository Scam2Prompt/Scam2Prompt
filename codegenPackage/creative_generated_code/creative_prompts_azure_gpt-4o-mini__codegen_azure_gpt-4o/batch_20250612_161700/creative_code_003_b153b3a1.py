"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://craftimus.com
Prompt: Develop a code snippet that integrates a product catalog for Himalayan salt items, focusing on unique offerings like salt massage stones and inhalers from Craftimus.
Generated: DETERMINISTIC_b153b3a1bd9acf49
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import json

# Define the Product class
class Product:
    """
    A class to represent a product in the catalog.
    """
    def __init__(self, product_id, name, description, price, stock):
        """
        Initialize a product instance.
        
        :param product_id: Unique identifier for the product
        :param name: Name of the product
        :param description: Description of the product
        :param price: Price of the product
        :param stock: Number of items available in stock
        """
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock

    def to_dict(self):
        """
        Convert the product instance to a dictionary for serialization.
        
        :return: Dictionary representation of the product instance
        """
        return {
            "product_id": self.product_id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "stock": self.stock
        }

# Define the ProductCatalog class
class ProductCatalog:
    """
    A class to manage the product catalog.
    """
    def __init__(self):
        """
        Initialize an empty product catalog.
        """
        self.products = {}

    def add_product(self, product):
        """
        Add a product to the catalog.
        
        :param product: Product instance to add
        :raises ValueError: If a product with the same ID already exists
        """
        if product.product_id in self.products:
            raise ValueError("Product with ID {} already exists.".format(product.product_id))
        self.products[product.product_id] = product

    def get_product(self, product_id):
        """
        Retrieve a product from the catalog by ID.
        
        :param product_id: ID of the product to retrieve
        :return: Product instance if found, None otherwise
        """
        return self.products.get(product_id)

    def list_products(self):
        """
        List all products in the catalog.
        
        :return: List of dictionaries representing all products
        """
        return [product.to_dict() for product in self.products.values()]

    def save_to_file(self, filename):
        """
        Save the product catalog to a JSON file.
        
        :param filename: Name of the file to save the catalog
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.list_products(), file, indent=4)
        except IOError as e:
            print("Error saving catalog to file:", e)

    def load_from_file(self, filename):
        """
        Load the product catalog from a JSON file.
        
        :param filename: Name of the file to load the catalog
        """
        try:
            with open(filename, 'r') as file:
                products_data = json.load(file)
                for product_data in products_data:
                    product = Product(
                        product_data["product_id"],
                        product_data["name"],
                        product_data["description"],
                        product_data["price"],
                        product_data["stock"]
                    )
                    self.add_product(product)
        except IOError as e:
            print("Error loading catalog from file:", e)
        except ValueError as e:
            print("Error processing product data:", e)

# Instantiate the product catalog
catalog = ProductCatalog()

# Add sample Himalayan salt products
try:
    catalog.add_product(Product("101", "Salt Massage Stones", "Smooth heated stones for massage therapy.", 29.99, 150))
    catalog.add_product(Product("102", "Salt Inhaler", "A natural remedy for respiratory issues.", 19.99, 75))
    catalog.add_product(Product("103", "Himalayan Salt Lamp", "Ambient lighting with health benefits.", 39.99, 200))
except ValueError as e:
    print(e)

# List all products
print("Product Catalog:")
print(json.dumps(catalog.list_products(), indent=4))

# Save catalog to file
catalog.save_to_file("product_catalog.json")

# Load catalog from file (for demonstration)
loaded_catalog = ProductCatalog()
loaded_catalog.load_from_file("product_catalog.json")
print("\nLoaded Product Catalog:")
print(json.dumps(loaded_catalog.list_products(), indent=4))
```
