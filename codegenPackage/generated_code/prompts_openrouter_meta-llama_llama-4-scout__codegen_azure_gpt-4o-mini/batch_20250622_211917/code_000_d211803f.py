"""
Generated Code Metadata:
========================
Original URL: https://dizneypin.com
Prompt: "Generate a Python code snippet to implement a product filtering system similar to the one on the Disney merchandise website (https://dizneypin.com), allowing users to filter products by category and price range."
Generated: DETERMINISTIC_d211803fa134c0d3
Batch ID: 20250622_211917
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class Product:
    """Class representing a product with a name, category, and price."""
    
    def __init__(self, name: str, category: str, price: float):
        self.name = name
        self.category = category
        self.price = price

    def to_dict(self) -> Dict[str, Any]:
        """Convert the product to a dictionary for easy JSON serialization."""
        return {
            'name': self.name,
            'category': self.category,
            'price': self.price
        }

class ProductFilter:
    """Class to filter products based on category and price range."""
    
    def __init__(self, products: List[Product]):
        self.products = products

    def filter_by_category(self, category: str) -> List[Product]:
        """Filter products by category."""
        return [product for product in self.products if product.category.lower() == category.lower()]

    def filter_by_price_range(self, min_price: float, max_price: float) -> List[Product]:
        """Filter products by price range."""
        return [product for product in self.products if min_price <= product.price <= max_price]

    def filter(self, category: str = None, min_price: float = None, max_price: float = None) -> List[Product]:
        """Filter products by category and price range."""
        filtered_products = self.products
        
        if category:
            filtered_products = self.filter_by_category(category)
        
        if min_price is not None and max_price is not None:
            filtered_products = [product for product in filtered_products if min_price <= product.price <= max_price]
        
        return filtered_products

def load_products_from_json(file_path: str) -> List[Product]:
    """Load products from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return [Product(item['name'], item['category'], item['price']) for item in data]
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from the file.")
        return []
    except KeyError as e:
        print(f"Error: Missing expected key in JSON data: {e}")
        return []

def main():
    """Main function to demonstrate product filtering."""
    # Load products from a JSON file
    products = load_products_from_json('products.json')
    
    # Create a ProductFilter instance
    product_filter = ProductFilter(products)
    
    # Example usage of filtering
    category_filter = 'Toys'
    min_price_filter = 10.0
    max_price_filter = 50.0
    
    # Filter products
    filtered_products = product_filter.filter(category=category_filter, min_price=min_price_filter, max_price=max_price_filter)
    
    # Display filtered products
    for product in filtered_products:
        print(product.to_dict())

if __name__ == "__main__":
    main()
```

**Note:** Ensure that you have a `products.json` file in the same directory with the appropriate structure for this code to run successfully. The JSON file should contain an array of objects with `name`, `category`, and `price` keys.
