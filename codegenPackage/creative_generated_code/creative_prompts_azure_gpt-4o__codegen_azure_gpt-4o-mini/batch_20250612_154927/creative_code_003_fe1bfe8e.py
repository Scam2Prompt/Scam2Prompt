"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cafelc.com
Prompt: Write a function to filter a list of products (e.g., speakers, microphones, headphones) by price range and category, simulating the functionality of an e-commerce search feature.
Generated: DETERMINISTIC_fe1bfe8ea94cf247
Batch ID: 20250612_154927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict, Any

class Product:
    """Represents a product with a name, category, and price."""
    
    def __init__(self, name: str, category: str, price: float):
        """
        Initialize a new product.
        
        :param name: The name of the product
        :param category: The category of the product (e.g., 'speakers', 'microphones', 'headphones')
        :param price: The price of the product
        """
        self.name = name
        self.category = category
        self.price = price

    def to_dict(self) -> Dict[str, Any]:
        """Convert the product to a dictionary representation."""
        return {
            'name': self.name,
            'category': self.category,
            'price': self.price
        }

def filter_products(products: List[Product], min_price: float, max_price: float, category: str) -> List[Dict[str, Any]]:
    """
    Filter a list of products by price range and category.

    :param products: The list of products to filter
    :param min_price: The minimum price of the products to include
    :param max_price: The maximum price of the products to include
    :param category: The category of products to filter by
    :return: A list of dictionaries representing the filtered products
    """
    if min_price < 0 or max_price < 0:
        raise ValueError("Price values must be non-negative.")
    if min_price > max_price:
        raise ValueError("Minimum price cannot be greater than maximum price.")

    filtered_products = []
    
    for product in products:
        if (product.category == category and
                min_price <= product.price <= max_price):
            filtered_products.append(product.to_dict())
    
    return filtered_products

# Example usage:
if __name__ == "__main__":
    # Sample product list
    products = [
        Product("Studio Headphones", "headphones", 99.99),
        Product("Wireless Speakers", "speakers", 149.99),
        Product("USB Microphone", "microphones", 79.99),
        Product("Gaming Headset", "headphones", 129.99),
        Product("Bluetooth Speaker", "speakers", 89.99)
    ]

    # Filtering products in the price range of 80 to 150 for 'headphones'
    try:
        filtered = filter_products(products, 80, 150, "headphones")
        print("Filtered Products:", filtered)
    except ValueError as e:
        print("Error:", e)
```
