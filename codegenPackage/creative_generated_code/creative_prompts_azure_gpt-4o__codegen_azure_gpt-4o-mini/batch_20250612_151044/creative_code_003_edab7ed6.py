"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jiomartdigital.com
Prompt: Write a script to simulate a search functionality for Jiomart Digital's 20,000+ products, allowing users to filter by category, price range, and brand.
Generated: DETERMINISTIC_edab7ed6c0e6bd42
Batch ID: 20250612_151044
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
    Class to represent a product in the Jiomart Digital inventory.
    """
    def __init__(self, name, category, price, brand):
        self.name = name
        self.category = category
        self.price = price
        self.brand = brand

    def __repr__(self):
        return f"Product(name={self.name}, category={self.category}, price={self.price}, brand={self.brand})"


class ProductSearch:
    """
    Class to handle searching for products based on filters.
    """
    def __init__(self, products):
        """
        Initializes the ProductSearch with a list of products.
        
        :param products: List of Product instances
        """
        self.products = products

    def filter_by_category(self, category):
        """
        Filters products by category.
        
        :param category: Category to filter by
        :return: List of products matching the category
        """
        return [product for product in self.products if product.category.lower() == category.lower()]

    def filter_by_price_range(self, min_price, max_price):
        """
        Filters products by price range.
        
        :param min_price: Minimum price (inclusive)
        :param max_price: Maximum price (inclusive)
        :return: List of products within the price range
        """
        return [product for product in self.products if min_price <= product.price <= max_price]

    def filter_by_brand(self, brand):
        """
        Filters products by brand.
        
        :param brand: Brand to filter by
        :return: List of products matching the brand
        """
        return [product for product in self.products if product.brand.lower() == brand.lower()]

    def search(self, category=None, min_price=None, max_price=None, brand=None):
        """
        Searches for products based on specified filters.
        
        :param category: Optional category filter
        :param min_price: Optional minimum price filter
        :param max_price: Optional maximum price filter
        :param brand: Optional brand filter
        :return: List of products matching the filters
        """
        filtered_products = self.products

        if category:
            filtered_products = self.filter_by_category(category)

        if min_price is not None and max_price is not None:
            filtered_products = self.filter_by_price_range(min_price, max_price)

        if brand:
            filtered_products = self.filter_by_brand(brand)

        return filtered_products


def load_products_from_json(file_path):
    """
    Loads products from a JSON file.
    
    :param file_path: Path to the JSON file
    :return: List of Product instances
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return [Product(item['name'], item['category'], item['price'], item['brand']) for item in data]
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: The file {file_path} contains invalid JSON.")
        return []
    except KeyError as e:
        print(f"Error: Missing expected key {e} in product data.")
        return []


if __name__ == "__main__":
    # Load products from JSON file
    products = load_products_from_json('products.json')
    
    # Initialize the search functionality
    product_search = ProductSearch(products)
    
    # Example search
    results = product_search.search(category='Electronics', min_price=1000, max_price=5000, brand='Samsung')
    
    # Display results
    print("Search Results:")
    for product in results:
        print(product)
```

Make sure to have a `products.json` file in the same directory with the following structure for testing:

```json
[
    {"name": "Samsung Galaxy S21", "category": "Electronics", "price": 1200, "brand": "Samsung"},
    {"name": "Apple iPhone 13", "category": "Electronics", "price": 1400, "brand": "Apple"},
    {"name": "Sony WH-1000XM4", "category": "Electronics", "price": 300, "brand": "Sony"},
    {"name": "Nike Air Max", "category": "Footwear", "price": 150, "brand": "Nike"}
]
```
