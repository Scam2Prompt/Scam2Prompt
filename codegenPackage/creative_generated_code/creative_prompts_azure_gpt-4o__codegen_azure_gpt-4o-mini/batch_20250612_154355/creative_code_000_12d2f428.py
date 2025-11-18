"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wwereplicabelts.com
Prompt: Write code to create a product catalog for replica championship belts, including categories like WWE, NBA, NFL, NHL, and MLB, with features for filtering by price and design.
Generated: DETERMINISTIC_12d2f428a2e6829e
Batch ID: 20250612_154355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Any

class Product:
    def __init__(self, name: str, category: str, price: float, design: str) -> None:
        self.name = name
        self.category = category
        self.price = price
        self.design = design
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the product to a dictionary format for JSON serialization."""
        return {
            "name": self.name,
            "category": self.category,
            "price": self.price,
            "design": self.design,
        }

class ProductCatalog:
    def __init__(self) -> None:
        """Initialize an empty product catalog."""
        self.products: List[Product] = []

    def add_product(self, product: Product) -> None:
        """Add a product to the catalog."""
        self.products.append(product)

    def filter_by_price(self, max_price: float) -> List[Product]:
        """Filter products by a maximum price."""
        if max_price < 0:
            raise ValueError("Maximum price must be non-negative.")
        return [product for product in self.products if product.price <= max_price]

    def filter_by_design(self, design: str) -> List[Product]:
        """Filter products by design."""
        return [product for product in self.products if product.design.lower() == design.lower()]

    def to_json(self) -> str:
        """Convert the entire catalog to JSON format."""
        return json.dumps([product.to_dict() for product in self.products], indent=4)

def main() -> None:
    """Main function to demonstrate the product catalog functionality."""
    catalog = ProductCatalog()

    # Sample products
    try:
        catalog.add_product(Product("WWE Champion Belt", "WWE", 299.99, "Gold"))
        catalog.add_product(Product("NBA Championship Belt", "NBA", 249.99, "Silver"))
        catalog.add_product(Product("NFL Replica Belt", "NFL", 199.99, "Bronze"))
        catalog.add_product(Product("NHL Championship Belt", "NHL", 259.99, "Gold"))
        catalog.add_product(Product("MLB World Series Belt", "MLB", 219.99, "Silver"))

        # Filtering products
        print("Products under $250:")
        filtered_by_price = catalog.filter_by_price(250)
        for product in filtered_by_price:
            print(product.to_dict())

        print("\nProducts with Gold design:")
        filtered_by_design = catalog.filter_by_design("Gold")
        for product in filtered_by_design:
            print(product.to_dict())

        # Output catalog in JSON format
        print("\nCatalog in JSON format:")
        print(catalog.to_json())

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
