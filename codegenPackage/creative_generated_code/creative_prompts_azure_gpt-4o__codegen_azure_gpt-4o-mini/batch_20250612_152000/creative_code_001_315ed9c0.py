"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://autopecasbrazz.blogspot.com
Prompt: Generate a script to create a product catalog for automotive parts, including categories like suspension, motor, electrical, and lubricants, referencing the structure used on "autopecasbrazz."
Generated: DETERMINISTIC_315ed9c08a0f81e7
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict

class Product:
    """Class representing a single product in the automotive parts catalog."""
    def __init__(self, name: str, category: str, price: float, sku: str) -> None:
        self.name = name
        self.category = category
        self.price = price
        self.sku = sku

    def to_dict(self) -> Dict[str, str]:
        """Convert product details to a dictionary."""
        return {
            "name": self.name,
            "category": self.category,
            "price": self.price,
            "sku": self.sku
        }


class ProductCatalog:
    """Class representing a catalog of automotive parts."""
    def __init__(self) -> None:
        self.products: List[Product] = []

    def add_product(self, product: Product) -> None:
        """Add a product to the catalog."""
        self.products.append(product)

    def get_products_by_category(self, category: str) -> List[Dict[str, str]]:
        """Retrieve all products in a given category."""
        return [product.to_dict() for product in self.products if product.category == category]

    def save_to_file(self, filename: str) -> None:
        """Save the catalog to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump([product.to_dict() for product in self.products], file, indent=4)
        except IOError as e:
            print(f"Error saving to file {filename}: {e}")


def main() -> None:
    """Main function to create the product catalog and populate it with sample data."""
    catalog = ProductCatalog()

    # Sample product data
    sample_products = [
        Product("Shock Absorber", "Suspension", 75.99, "SA123"),
        Product("Brake Pad Set", "Suspension", 45.00, "BP456"),
        Product("Oil Filter", "Lubricants", 12.50, "OF789"),
        Product("Motor Oil 5W-30", "Lubricants", 25.00, "MO101"),
        Product("Spark Plug", "Electrical", 3.99, "SP202"),
        Product("Starter Motor", "Electrical", 150.00, "SM303"),
        Product("Engine", "Motor", 2000.00, "ENG404"),
        Product("Transmission", "Motor", 1500.00, "TRN505"),
    ]

    # Adding products to the catalog
    for product in sample_products:
        catalog.add_product(product)

    # Output catalog to a JSON file
    catalog.save_to_file("product_catalog.json")

    # Example of retrieving products by category
    suspension_parts = catalog.get_products_by_category("Suspension")
    print("Suspension Parts:", suspension_parts)


if __name__ == "__main__":
    main()
```
