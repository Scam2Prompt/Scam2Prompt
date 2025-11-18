"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://medebooks.shop
Prompt: Write a script to manage and display discounted prices for products, ensuring discounts are applied dynamically based on the original price, as seen on medebooks.shop.
Generated: DETERMINISTIC_fcb1bff9494a9ddd
Batch ID: 20250612_153947
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
    """Class to represent a product with a name, original price, and discount."""

    def __init__(self, name: str, original_price: float, discount_percentage: float = 0.0):
        """Initialize the product with name, original price, and optional discount."""
        self.name = name
        self.original_price = original_price
        self.discount_percentage = discount_percentage

    def apply_discount(self):
        """Calculate the discounted price based on the original price and discount percentage."""
        if self.discount_percentage < 0 or self.discount_percentage > 100:
            raise ValueError("Discount percentage must be between 0 and 100.")
        discount_amount = (self.discount_percentage / 100) * self.original_price
        return self.original_price - discount_amount

    def __str__(self):
        """Return a string representation of the product."""
        discounted_price = self.apply_discount()
        return f"{self.name}: Original Price = ${self.original_price:.2f}, " \
               f"Discounted Price = ${discounted_price:.2f} (Discount: {self.discount_percentage}%)"


def load_products_from_json(file_path: str) -> List[Product]:
    """Load products from a JSON file and return a list of Product instances."""
    try:
        with open(file_path, 'r') as file:
            products_data = json.load(file)
            products = [
                Product(name=item['name'], original_price=item['original_price'], discount_percentage=item.get('discount_percentage', 0))
                for item in products_data
            ]
            return products
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from the file.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []


def display_products(products: List[Product]):
    """Display the list of products with their discounted prices."""
    if not products:
        print("No products to display.")
        return
    
    print("Product List:")
    for product in products:
        print(product)


def main():
    """Main function to load products and display them."""
    file_path = 'products.json'  # Specify the path to the JSON file containing product data
    products = load_products_from_json(file_path)
    display_products(products)


if __name__ == "__main__":
    main()
```

### Example JSON file (`products.json`):
```json
[
    {
        "name": "Product A",
        "original_price": 100.0,
        "discount_percentage": 20
    },
    {
        "name": "Product B",
        "original_price": 200.0,
        "discount_percentage": 15
    },
    {
        "name": "Product C",
        "original_price": 150.0
    }
]
```
