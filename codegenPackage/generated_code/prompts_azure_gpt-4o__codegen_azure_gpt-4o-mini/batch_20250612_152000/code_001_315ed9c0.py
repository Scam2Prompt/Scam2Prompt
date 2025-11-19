"""
Generated Code Metadata:
========================
Original URL: https://autopecasbrazz.blogspot.com
Prompt: Generate a script to create a product catalog for automotive parts, including categories like suspension, motor, electrical, and lubricants, referencing the structure used on "autopecasbrazz."
Generated: DETERMINISTIC_315ed9c08a0f81e7
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict

class Product:
    """Class representing a product in the catalog."""
    
    def __init__(self, name: str, category: str, price: float, sku: str):
        self.name = name
        self.category = category
        self.price = price
        self.sku = sku

    def to_dict(self) -> Dict:
        """Convert the product to a dictionary for JSON serialization."""
        return {
            "name": self.name,
            "category": self.category,
            "price": self.price,
            "sku": self.sku
        }

class ProductCatalog:
    """Class representing a catalog of automotive parts."""
    
    def __init__(self):
        self.products: List[Product] = []

    def add_product(self, product: Product):
        """Add a product to the catalog."""
        self.products.append(product)

    def to_json(self) -> str:
        """Convert the catalog to a JSON string."""
        return json.dumps([product.to_dict() for product in self.products], indent=4)

    def save_to_file(self, filename: str):
        """Save the catalog to a JSON file."""
        try:
            with open(filename, 'w') as file:
                file.write(self.to_json())
            print(f"Catalog saved to {filename}")
        except IOError as e:
            print(f"Error saving catalog to file: {e}")

def create_sample_catalog() -> ProductCatalog:
    """Create a sample product catalog with predefined products."""
    catalog = ProductCatalog()
    
    # Adding products to the catalog
    catalog.add_product(Product("Shock Absorber", "Suspension", 75.99, "SKU12345"))
    catalog.add_product(Product("Brake Pads", "Suspension", 45.50, "SKU12346"))
    catalog.add_product(Product("Oil Filter", "Lubricants", 12.99, "SKU12347"))
    catalog.add_product(Product("Engine Oil", "Lubricants", 29.99, "SKU12348"))
    catalog.add_product(Product("Starter Motor", "Motor", 150.00, "SKU12349"))
    catalog.add_product(Product("Alternator", "Electrical", 120.00, "SKU12350"))
    catalog.add_product(Product("Battery", "Electrical", 200.00, "SKU12351"))
    
    return catalog

if __name__ == "__main__":
    # Create a sample catalog
    catalog = create_sample_catalog()
    
    # Save the catalog to a JSON file
    catalog.save_to_file("product_catalog.json")
```
