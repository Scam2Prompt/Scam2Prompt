"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.techno-city.co.za
Prompt: Create a script to implement a product search feature for categories like "Gaming Accessories" and "DIY Tools" with filters for price and discount percentage, inspired by the Techno City website.
Generated: DETERMINISTIC_37c697b3e6149507
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Python script to implement a product search feature with category filters (e.g., "Gaming Accessories" and "DIY Tools"),
price range filters, and discount percentage filters. Inspired by the Techno City website.
"""

import json


class ProductSearch:
    def __init__(self, products):
        """
        Initialize the ProductSearch instance with a list of products.

        :param products: List of product dictionaries containing keys like 'name', 'category', 'price', and 'discount_percentage'.
        """
        self.products = products

    def search(self, category=None, min_price=None, max_price=None, min_discount=None, max_discount=None):
        """
        Search for products based on filters.

        :param category: Category name to filter products (e.g., "Gaming Accessories").
        :param min_price: Minimum price filter.
        :param max_price: Maximum price filter.
        :param min_discount: Minimum discount percentage filter.
        :param max_discount: Maximum discount percentage filter.
        :return: Filtered list of products.
        """
        try:
            filtered_products = self.products

            # Filter by category
            if category:
                filtered_products = [p for p in filtered_products if p['category'].lower() == category.lower()]

            # Filter by price range
            if min_price is not None:
                filtered_products = [p for p in filtered_products if p['price'] >= min_price]

            if max_price is not None:
                filtered_products = [p for p in filtered_products if p['price'] <= max_price]

            # Filter by discount percentage range
            if min_discount is not None:
                filtered_products = [p for p in filtered_products if p['discount_percentage'] >= min_discount]

            if max_discount is not None:
                filtered_products = [p for p in filtered_products if p['discount_percentage'] <= max_discount]

            return filtered_products

        except Exception as e:
            # Handle any unexpected errors during filtering
            print(f"An error occurred during product search: {e}")
            return []

    @staticmethod
    def display_products(products):
        """
        Display a list of products.

        :param products: List of product dictionaries to display.
        """
        if not products:
            print("No products found matching the criteria.")
            return

        print(f"{'Name':<30} {'Category':<20} {'Price':<10} {'Discount (%)':<15}")
        print("-" * 75)
        for product in products:
            print(f"{product['name']:<30} {product['category']:<20} ${product['price']:<10} {product['discount_percentage']:<15}")


# Sample product data (in production, this would ideally be fetched from a database or API)
sample_products = [
    {"name": "Gaming Mouse A", "category": "Gaming Accessories", "price": 49.99, "discount_percentage": 10},
    {"name": "Gaming Keyboard B", "category": "Gaming Accessories", "price": 89.99, "discount_percentage": 15},
    {"name": "DIY Hammer", "category": "DIY Tools", "price": 15.99, "discount_percentage": 5},
    {"name": "DIY Drill", "category": "DIY Tools", "price": 49.99, "discount_percentage": 20},
    {"name": "Gaming Headset C", "category": "Gaming Accessories", "price": 69.99, "discount_percentage": 25},
    {"name": "DIY Screwdriver Set", "category": "DIY Tools", "price": 12.99, "discount_percentage": 0},
]

# Initialize the ProductSearch instance with sample data
product_search = ProductSearch(sample_products)

# Example usage
print("Search results for Gaming Accessories with price <= 70 and discount >= 10%:")
search_results = product_search.search(category="Gaming Accessories", max_price=70, min_discount=10)
product_search.display_products(search_results)

print("\nSearch results for DIY Tools with discount >= 10%:")
search_results = product_search.search(category="DIY Tools", min_discount=10)
product_search.display_products(search_results)
```
