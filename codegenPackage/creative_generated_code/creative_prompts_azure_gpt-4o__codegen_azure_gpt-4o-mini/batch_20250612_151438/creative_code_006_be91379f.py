"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://milarbrazw.blogspot.com
Prompt: Write a function to filter lighting products by category (e.g., "Casa, Móveis e Decoração" or "Construção") and display only those with free shipping, such as "Sensor Presença Sobrepor C/ Fotocel Qualitronix Qa26m."
Generated: DETERMINISTIC_be91379f6621021a
Batch ID: 20250612_151438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict

# Define a custom exception for handling product filtering errors
class ProductFilterError(Exception):
    pass

def filter_lighting_products(products: List[Dict], category: str) -> List[Dict]:
    """
    Filters the lighting products by category and free shipping status.

    Args:
        products (List[Dict]): A list of product dictionaries to filter.
        category (str): The category to filter products by.

    Returns:
        List[Dict]: A list of products that match the specified category 
                     and have free shipping.

    Raises:
        ProductFilterError: If products list is empty or category is invalid.
    """
    if not products:
        raise ProductFilterError("The product list cannot be empty.")
    
    if not category:
        raise ProductFilterError("The category must be specified.")

    # Filter products based on category and free shipping
    filtered_products = [
        product for product in products
        if product.get('category') == category and product.get('free_shipping', False)
    ]
    
    return filtered_products

def main():
    # Sample data of lighting products
    products_data = '''
    [
        {"name": "Sensor Presença Sobrepor C/ Fotocel Qualitronix Qa26m", "category": "Casa, Móveis e Decoração", "free_shipping": true},
        {"name": "Lâmpada LED 9W", "category": "Construção", "free_shipping": false},
        {"name": "Lustre de Cristal", "category": "Casa, Móveis e Decoração", "free_shipping": true},
        {"name": "Fita LED", "category": "Iluminação", "free_shipping": true}
    ]
    '''
    
    # Load the products from JSON data
    try:
        products = json.loads(products_data)
    except json.JSONDecodeError as e:
        print("Error loading products data:", e)
        return

    # Specify the category to filter by
    category_to_filter = "Casa, Móveis e Decoração"

    # Filter the products and display them
    try:
        filtered_products = filter_lighting_products(products, category_to_filter)
        print("Filtered products with free shipping:")
        for product in filtered_products:
            print(f" - {product['name']}")
    except ProductFilterError as e:
        print("Filtering error:", e)

if __name__ == "__main__":
    main()
```
