"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://adp-magiceden.lojaintegrada.com.br
Prompt: Implement a feature in an e-commerce platform to display products with the highest discounts, such as "-50% Perfume Al Wataniah Special Oud Eau de Parfum Unissex 100ml."
Generated: DETERMINISTIC_4322153ed23d7d47
Batch ID: 20250612_154946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict
import logging

# Configure logging for error handling
logging.basicConfig(level=logging.INFO)

class Product:
    def __init__(self, name: str, original_price: float, discounted_price: float):
        if original_price <= 0 or discounted_price < 0:
            logging.error("Invalid product prices provided. Prices must be positive.")
            raise ValueError("Original price must be greater than 0 and discounted price must be non-negative.")
        
        self.name = name
        self.original_price = original_price
        self.discounted_price = discounted_price

    def discount_percentage(self) -> float:
        """Calculate the discount percentage of the product."""
        discount = (self.original_price - self.discounted_price) / self.original_price * 100
        return round(discount, 2)

def get_top_discounted_products(products: List[Product], top_n: int) -> List[Dict[str, float]]:
    """
    Retrieve the top N products with the highest discounts.

    Args:
        products (List[Product]): List of products to evaluate.
        top_n (int): Number of top discounted products to return.

    Returns:
        List[Dict[str, float]]: List of dictionaries containing product name and discount percentage.
    """
    if top_n <= 0:
        logging.error("top_n must be a positive integer.")
        raise ValueError("The number of top products must be greater than 0.")
    
    # Sort the products by discount percentage in descending order
    sorted_products = sorted(products, key=lambda p: p.discount_percentage(), reverse=True)
    
    # Prepare the result
    top_products = [
        {
            'name': product.name,
            'discount_percentage': product.discount_percentage()
        }
        for product in sorted_products[:top_n]
    ]
    
    return top_products

# Example usage
if __name__ == "__main__":
    try:
        # Sample product data
        products = [
            Product("Perfume Al Wataniah Special Oud Eau de Parfum Unissex 100ml", 100.0, 50.0),
            Product("Luxury Leather Wallet", 80.0, 40.0),
            Product("Designer Sunglasses", 150.0, 75.0),
            Product("Digital Watch", 200.0, 150.0),
            Product("Sports Shoes", 120.0, 60.0),
        ]

        # Get top 3 products with the highest discounts
        top_discounted_products = get_top_discounted_products(products, 3)
        
        # Display the results
        for product in top_discounted_products:
            print(f"{product['name']} - {product['discount_percentage']}% off")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
