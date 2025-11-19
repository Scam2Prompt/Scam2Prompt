"""
Generated Code Metadata:
========================
Original URL: https://asacanelbrazzz.blogspot.com
Prompt: Write a Python function that filters products based on price and category, similar to the features on asacanelbrazzz.
Generated: DETERMINISTIC_a35cdbcc087210ee
Batch ID: 20250612_162544
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional, Union

class ProductFilter:
    """
    A class to filter products based on price range and category.
    """
    
    def __init__(self, products: List[Dict[str, Union[str, float]]]):
        """
        Initialize the ProductFilter with a list of products.
        
        Args:
            products: List of product dictionaries, each containing at least
                     'name', 'price', and 'category' keys.
        """
        self.products = products
    
    def filter_by_price_and_category(
        self,
        min_price: Optional[float] = None,
        max_price: Optional[float] = None,
        categories: Optional[List[str]] = None
    ) -> List[Dict[str, Union[str, float]]]:
        """
        Filter products by price range and category.
        
        Args:
            min_price: Minimum price threshold (inclusive). If None, no minimum.
            max_price: Maximum price threshold (inclusive). If None, no maximum.
            categories: List of categories to include. If None, all categories.
            
        Returns:
            List of filtered product dictionaries.
            
        Raises:
            ValueError: If min_price > max_price or if invalid price values are provided.
        """
        # Validate price range
        if min_price is not None and max_price is not None and min_price > max_price:
            raise ValueError("min_price cannot be greater than max_price")
        
        if min_price is not None and min_price < 0:
            raise ValueError("min_price cannot be negative")
            
        if max_price is not None and max_price < 0:
            raise ValueError("max_price cannot be negative")
        
        filtered_products = []
        
        for product in self.products:
            # Validate product structure
            if not all(key in product for key in ['name', 'price', 'category']):
                continue
                
            try:
                price = float(product['price'])
            except (ValueError, TypeError):
                continue
            
            # Apply price filters
            price_condition = True
            if min_price is not None:
                price_condition = price_condition and (price >= min_price)
            if max_price is not None:
                price_condition = price_condition and (price <= max_price)
            
            # Apply category filter
            category_condition = True
            if categories is not None:
                category_condition = product['category'] in categories
            
            if price_condition and category_condition:
                filtered_products.append(product)
        
        return filtered_products

# Example usage
if __name__ == "__main__":
    # Sample product data
    products = [
        {"name": "Product 1", "price": 10.99, "category": "Electronics"},
        {"name": "Product 2", "price": 25.50, "category": "Clothing"},
        {"name": "Product 3", "price": 5.99, "category": "Electronics"},
        {"name": "Product 4", "price": 50.00, "category": "Home"},
        {"name": "Product 5", "price": 15.75, "category": "Electronics"},
    ]
    
    # Initialize filter
    product_filter = ProductFilter(products)
    
    # Filter products
    filtered = product_filter.filter_by_price_and_category(
        min_price=10.0,
        max_price=30.0,
        categories=["Electronics", "Clothing"]
    )
    
    # Print results
    print(json.dumps(filtered, indent=2))
```
