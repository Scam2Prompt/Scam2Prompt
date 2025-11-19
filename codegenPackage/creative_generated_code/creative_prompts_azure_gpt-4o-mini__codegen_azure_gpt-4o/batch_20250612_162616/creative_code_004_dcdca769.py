"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zellerscanada.ca
Prompt: Illustrate how to implement a search functionality for an e-commerce platform that categorizes products like Zellers does, including features for limited-time offers.
Generated: DETERMINISTIC_dcdca769c26c74fc
Batch ID: 20250612_162616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta

class Product:
    """
    Represents a product in the e-commerce platform.
    """
    def __init__(self, id, name, category, price, is_limited_offer=False, offer_end_time=None):
        self.id = id
        self.name = name
        self.category = category
        self.price = price
        self.is_limited_offer = is_limited_offer
        self.offer_end_time = offer_end_time

    def is_offer_active(self):
        """
        Checks if the limited-time offer is still active.
        """
        if self.is_limited_offer and self.offer_end_time:
            return datetime.now() < self.offer_end_time
        return False


class EcommercePlatform:
    """
    Represents the e-commerce platform with search functionality.
    """
    def __init__(self):
        self.products = []

    def add_product(self, product):
        """
        Adds a product to the platform.
        """
        if not isinstance(product, Product):
            raise TypeError("Expected a Product instance")
        self.products.append(product)

    def search_products(self, query, category=None, include_limited_offers=False):
        """
        Searches for products based on query, category, and limited-time offer filters.

        Parameters:
            query (str): The search query to match product names.
            category (str, optional): Filter products by category.
            include_limited_offers (bool, optional): Include active limited-time offers in the search results.

        Returns:
            list: List of matching Product objects.
        """
        results = []
        for product in self.products:
            if query.lower() in product.name.lower():
                if category and product.category.lower() != category.lower():
                    continue
                if include_limited_offers and product.is_limited_offer:
                    if not product.is_offer_active():
                        continue
                results.append(product)
        return results


# Example usage
if __name__ == "__main__":
    # Initialize the platform
    platform = EcommercePlatform()

    # Add products to the platform
    platform.add_product(Product(1, "Laptop", "Electronics", 1200.00))
    platform.add_product(Product(2, "Smartphone", "Electronics", 800.00, True,
                                 datetime.now() + timedelta(days=1)))
    platform.add_product(Product(3, "Winter Coat", "Apparel", 150.00))
    platform.add_product(Product(4, "Running Shoes", "Footwear", 80.00))

    # Search for products
    print("Search results for 'Laptop':")
    for product in platform.search_products("Laptop"):
        print(f"Product ID: {product.id}, Name: {product.name}, Category: {product.category}, Price: ${product.price}")

    print("\nSearch results for 'Smartphone' including limited-time offers:")
    for product in platform.search_products("Smartphone", include_limited_offers=True):
        print(f"Product ID: {product.id}, Name: {product.name}, Category: {product.category}, Price: ${product.price}, Offer Active: {product.is_offer_active()}")
```
