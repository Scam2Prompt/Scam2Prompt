"""
Generated Code Metadata:
========================
Original URL: https://jiomartdigital.com
Prompt: Write a script to simulate a search functionality for Jiomart Digital's 20,000+ products, allowing users to filter by category, price range, and brand.
Generated: DETERMINISTIC_edab7ed6c0e6bd42
Batch ID: 20250612_151044
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
    """Class to represent a product in the Jiomart Digital catalog."""
    
    def __init__(self, name: str, category: str, price: float, brand: str):
        self.name = name
        self.category = category
        self.price = price
        self.brand = brand

    def to_dict(self) -> Dict[str, Any]:
        """Convert the product to a dictionary for easy JSON serialization."""
        return {
            "name": self.name,
            "category": self.category,
            "price": self.price,
            "brand": self.brand
        }

class ProductCatalog:
    """Class to manage a collection of products and provide search functionality."""
    
    def __init__(self, products: List[Product]):
        self.products = products

    def search(self, category: str = None, price_range: tuple = None, brand: str = None) -> List[Dict[str, Any]]:
        """Search for products based on category, price range, and brand.

        Args:
            category (str): The category to filter by.
            price_range (tuple): A tuple containing the min and max price.
            brand (str): The brand to filter by.

        Returns:
            List[Dict[str, Any]]: A list of products matching the search criteria.
        """
        filtered_products = self.products
        
        if category:
            filtered_products = [p for p in filtered_products if p.category.lower() == category.lower()]
        
        if price_range:
            min_price, max_price = price_range
            filtered_products = [p for p in filtered_products if min_price <= p.price <= max_price]
        
        if brand:
            filtered_products = [p for p in filtered_products if p.brand.lower() == brand.lower()]
        
        return [product.to_dict() for product in filtered_products]

def load_products_from_json(file_path: str) -> List[Product]:
    """Load products from a JSON file.

    Args:
        file_path (str): The path to the JSON file containing product data.

    Returns:
        List[Product]: A list of Product objects.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        json.JSONDecodeError: If the file contains invalid JSON.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return [Product(**item) for item in data]
    except FileNotFoundError as e:
        print(f"Error: The file {file_path} was not found.")
        raise e
    except json.JSONDecodeError as e:
        print("Error: Failed to decode JSON from the file.")
        raise e

def main():
    """Main function to run the product search simulation."""
    # Load products from a JSON file
    try:
        products = load_products_from_json('products.json')
    except Exception as e:
        print("Exiting due to error in loading products.")
        return

    catalog = ProductCatalog(products)

    # Example search criteria
    search_results = catalog.search(category='Electronics', price_range=(1000, 5000), brand='Samsung')
    
    # Print search results
    print(json.dumps(search_results, indent=4))

if __name__ == "__main__":
    main()
```

**Note:** Ensure that you have a `products.json` file in the same directory with the appropriate structure to test this code. The JSON file should contain an array of objects with keys: `name`, `category`, `price`, and `brand`.
