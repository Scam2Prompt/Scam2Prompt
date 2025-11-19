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
from typing import List, Dict, Optional
from datetime import datetime

class Product:
    def __init__(self, product_id: int, name: str, category: str, price: float, 
                 discount_price: Optional[float] = None, offer_end_date: Optional[datetime] = None):
        """
        Initialize a Product instance.

        :param product_id: Unique identifier for the product
        :param name: Name of the product
        :param category: Category the product belongs to
        :param price: Regular price of the product
        :param discount_price: Discounted price if applicable
        :param offer_end_date: End date for limited-time offers
        """
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.discount_price = discount_price
        self.offer_end_date = offer_end_date

    def is_on_offer(self) -> bool:
        """
        Check if the product is currently on offer.

        :return: True if the product is on offer, False otherwise
        """
        if self.discount_price and self.offer_end_date:
            return datetime.now() < self.offer_end_date
        return False

class ProductCatalog:
    def __init__(self):
        """Initialize an empty product catalog."""
        self.products: List[Product] = []

    def add_product(self, product: Product):
        """
        Add a product to the catalog.

        :param product: Product instance to be added
        """
        self.products.append(product)

    def search(self, query: str, category: Optional[str] = None) -> List[Dict]:
        """
        Search for products by name or category.

        :param query: Search term to match product names
        :param category: Optional category filter
        :return: List of matching products in dictionary format
        """
        results = []
        for product in self.products:
            if query.lower() in product.name.lower() and (category is None or product.category.lower() == category.lower()):
                results.append({
                    'product_id': product.product_id,
                    'name': product.name,
                    'category': product.category,
                    'price': product.price,
                    'discount_price': product.discount_price,
                    'is_on_offer': product.is_on_offer()
                })
        return results

# Example usage of Product and ProductCatalog classes
if __name__ == "__main__":
    # Create a product catalog
    catalog = ProductCatalog()

    # Add sample products to the catalog
    catalog.add_product(Product(1, "Laptop", "Electronics", 1200.00, 1000.00, datetime(2023, 12, 1)))
    catalog.add_product(Product(2, "Smartphone", "Electronics", 800.00))
    catalog.add_product(Product(3, "Sofa", "Furniture", 500.00, 450.00, datetime(2023, 11, 15)))

    # Perform a search
    search_results = catalog.search("laptop", "Electronics")
    
    # Print the search results
    for result in search_results:
        print(result)
```
