"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://acula.com.ua
Prompt: Write code to generate product listings with detailed descriptions, including items like "гидрокостюм AquaDiscovery VOEVODA" and "сумка Beuchat Voyager XL," as featured on acula.com.ua.
Generated: DETERMINISTIC_2720dd6dd7cce611
Batch ID: 20250612_150927
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
    """Class representing a product with detailed descriptions."""
    
    def __init__(self, name: str, description: str, price: float, stock: int):
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock

    def to_dict(self) -> Dict:
        """Converts the Product instance to a dictionary."""
        return {
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "stock": self.stock
        }

class ProductListing:
    """Class to manage a collection of products."""
    
    def __init__(self):
        self.products: List[Product] = []

    def add_product(self, product: Product):
        """Adds a product to the listing."""
        if not isinstance(product, Product):
            raise TypeError("Expected a Product instance.")
        self.products.append(product)

    def to_json(self) -> str:
        """Converts the product listing to a JSON string."""
        return json.dumps([product.to_dict() for product in self.products], ensure_ascii=False, indent=4)

def main():
    """Main function to create and showcase product listings."""
    try:
        # Create a product listing
        listing = ProductListing()

        # Define products
        wetsuit = Product(
            name="гидрокостюм AquaDiscovery VOEVODA",
            description="Гидрокостюм AquaDiscovery VOEVODA, идеальный для активного отдыха на воде.",
            price=200.0,
            stock=15
        )

        bag = Product(
            name="сумка Beuchat Voyager XL",
            description="Сумка Beuchat Voyager XL, просторное и удобное решение для хранения снаряжения.",
            price=85.0,
            stock=30
        )

        # Add products to the listing
        listing.add_product(wetsuit)
        listing.add_product(bag)

        # Output the product listing as JSON
        print(listing.to_json())

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
