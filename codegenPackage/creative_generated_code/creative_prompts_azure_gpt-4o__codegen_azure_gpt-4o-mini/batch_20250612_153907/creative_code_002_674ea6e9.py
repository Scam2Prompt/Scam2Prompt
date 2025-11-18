"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1iiinch.teachable.com
Prompt: Provide a script to filter and sort products on an online course platform like Teachable, even when no products are currently listed.
Generated: DETERMINISTIC_674ea6e9b1ccb392
Batch ID: 20250612_153907
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
    """
    Class to represent a product with a name and price.
    """
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the Product instance to a dictionary.
        """
        return {
            'name': self.name,
            'price': self.price
        }

class ProductFilter:
    """
    Class to filter and sort products based on given criteria.
    """
    def __init__(self, products: List[Product]):
        self.products = products

    def filter_products(self, min_price: float = 0, max_price: float = float('inf')) -> List[Product]:
        """
        Filter products based on price range.

        :param min_price: Minimum price for filtering.
        :param max_price: Maximum price for filtering.
        :return: List of filtered products.
        """
        return [product for product in self.products if min_price <= product.price <= max_price]

    def sort_products(self, reverse: bool = False) -> List[Product]:
        """
        Sort products by price.

        :param reverse: Flag to sort in descending order.
        :return: List of sorted products.
        """
        return sorted(self.products, key=lambda product: product.price, reverse=reverse)

def main():
    """
    Main function to demonstrate filtering and sorting of products.
    """
    try:
        # Initialize an empty list of products
        products = []

        # Example of loading products (could be from a database or API)
        # Uncomment and modify the following lines as needed to load actual products
        # products = [Product("Course A", 29.99), Product("Course B", 49.99), Product("Course C", 19.99)]

        # Check if products are available
        if not products:
            print("No products available. Please add products to filter and sort.")
            return

        # Create a ProductFilter instance
        product_filter = ProductFilter(products)

        # Set your filter criteria
        min_price = 20
        max_price = 50
        
        # Filter products
        filtered_products = product_filter.filter_products(min_price, max_price)
        
        # Sort products
        sorted_products = product_filter.sort_products()

        # Display filtered products
        print("Filtered Products:")
        for product in filtered_products:
            print(json.dumps(product.to_dict(), indent=4))
        
        # Display sorted products
        print("\nSorted Products:")
        for product in sorted_products:
            print(json.dumps(product.to_dict(), indent=4))
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
