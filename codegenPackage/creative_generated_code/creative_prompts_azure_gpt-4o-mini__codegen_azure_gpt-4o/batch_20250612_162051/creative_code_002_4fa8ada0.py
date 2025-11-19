"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vaperiyadh2.com
Prompt: Create a function that calculates the discounted price for products on Vape Riyadh 2, such as the Juul Pods and ELF BAR devices.
Generated: DETERMINISTIC_4fa8ada06e335eab
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required modules
from typing import List, Dict

def calculate_discounted_prices(products: List[Dict[str, any]], discount_percentage: float) -> List[Dict[str, any]]:
    """
    Calculate the discounted price for a list of products.

    Args:
        products (List[Dict[str, any]]): A list of products, each represented as a dictionary containing:
            - 'name': str -> The name of the product.
            - 'price': float -> The original price of the product.
        discount_percentage (float): The discount percentage to apply (e.g., 20 for 20% discount).

    Returns:
        List[Dict[str, any]]: A list of products with updated dictionary, including the discounted price:
            - 'name': str -> The name of the product.
            - 'original_price': float -> The original price of the product.
            - 'discounted_price': float -> The price after applying the discount.
    """
    # Validate input
    if not products or not isinstance(products, list):
        raise ValueError("Products must be a list of dictionaries.")
    if not isinstance(discount_percentage, (int, float)) or discount_percentage < 0 or discount_percentage > 100:
        raise ValueError("Discount percentage must be a number between 0 and 100.")
    
    discounted_products = []
    
    for product in products:
        # Validate product data structure
        if not isinstance(product, dict) or 'name' not in product or 'price' not in product:
            raise ValueError("Each product must be a dictionary with 'name' and 'price' keys.")
        if not isinstance(product['name'], str) or not isinstance(product['price'], (int, float)):
            raise ValueError("'name' must be a string and 'price' must be a number.")
        
        # Calculate discounted price
        discounted_price = product['price'] * (1 - discount_percentage / 100)
        
        # Append result to the list with original and discounted prices
        discounted_products.append({
            'name': product['name'],
            'original_price': product['price'],
            'discounted_price': round(discounted_price, 2)  # Round to 2 decimal places for currency
        })
    
    return discounted_products

# Example usage:
if __name__ == "__main__":
    products_list = [
        {"name": "Juul Pods", "price": 50.0},
        {"name": "ELF BAR Device", "price": 30.0}
    ]
    discount = 15  # 15% discount
    try:
        result = calculate_discounted_prices(products_list, discount)
        for product in result:
            print(f"Product: {product['name']}, Original Price: {product['original_price']}, Discounted Price: {product['discounted_price']}")
    except ValueError as e:
        print(f"Error: {e}")
```
