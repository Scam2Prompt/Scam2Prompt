"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mobleman-doostan.com
Prompt: Write a Python script to create a product catalog for salon equipment, including items like "صندلی آرایشگاهی," "تخت ماساژ," and "ترولی آرایشگاهی," with customizable attributes such as color and material.
Generated: DETERMINISTIC_36949bf47a5ae6d0
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Salon Equipment Product Catalog Script

This script creates a product catalog for salon equipment with customizable attributes such as color and material.
The catalog allows adding, listing, and updating products.
"""

import json

class Product:
    """
    Represents a product in the salon equipment catalog.
    Attributes:
        name (str): Name of the product.
        color (str): Color of the product.
        material (str): Material of the product.
    """
    def __init__(self, name, color, material):
        """
        Initializes a Product instance.
        
        Args:
            name (str): Name of the product.
            color (str): Color of the product.
            material (str): Material of the product.
        """
        self.name = name
        self.color = color
        self.material = material

    def to_dict(self):
        """
        Converts the Product instance to a dictionary.
        
        Returns:
            dict: Dictionary representation of the product.
        """
        return {
            'name': self.name,
            'color': self.color,
            'material': self.material
        }

class ProductCatalog:
    """
    Manages a catalog of salon equipment products.
    """
    def __init__(self):
        """
        Initializes an empty product catalog.
        """
        self.products = []

    def add_product(self, product):
        """
        Adds a new product to the catalog.
        
        Args:
            product (Product): The product to add.
        """
        if not isinstance(product, Product):
            raise ValueError("Invalid product type. Expected a Product instance.")
        self.products.append(product)

    def list_products(self):
        """
        Lists all products in the catalog.
        
        Returns:
            list: List of dictionaries representing the products in the catalog.
        """
        return [product.to_dict() for product in self.products]

    def save_to_file(self, filename):
        """
        Saves the catalog to a file in JSON format.
        
        Args:
            filename (str): File name to save the catalog to.
        """
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(self.list_products(), file, ensure_ascii=False, indent=4)
        except IOError as e:
            print(f"Error saving catalog to file: {e}")

    def load_from_file(self, filename):
        """
        Loads the catalog from a JSON file.
        
        Args:
            filename (str): File name to load the catalog from.
        """
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                product_data = json.load(file)
                self.products = [Product(item['name'], item['color'], item['material']) for item in product_data]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading catalog from file: {e}")

# Example usage
if __name__ == "__main__":
    # Create a catalog instance
    catalog = ProductCatalog()
    
    # Add products to the catalog
    catalog.add_product(Product("صندلی آرایشگاهی", "مشکی", "فلز و چرم"))
    catalog.add_product(Product("تخت ماساژ", "سفید", "چوب و فوم"))
    catalog.add_product(Product("ترولی آرایشگاهی", "نقره‌ای", "فلز"))

    # Display the catalog
    print("Current Product Catalog:")
    for product in catalog.list_products():
        print(product)

    # Save the catalog to a file
    filename = "salon_catalog.json"
    catalog.save_to_file(filename)
    print(f"Catalog saved to {filename}")

    # Load the catalog from the file
    new_catalog = ProductCatalog()
    new_catalog.load_from_file(filename)
    print("Loaded Product Catalog:")
    for product in new_catalog.list_products():
        print(product)
```
