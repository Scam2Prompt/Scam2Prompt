"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://isoplas.com
Prompt: Write a function to filter and display food packaging products like microwavable containers and dessert containers from a product catalog, inspired by Isoplas Corporation's portfolio.
Generated: DETERMINISTIC_b52b86b4a21c4136
Batch ID: 20250612_150018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python 3 Code

# Import necessary libraries
from typing import List, Dict

def filter_food_packaging_products(product_catalog: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """
    Filters food packaging products from a product catalog.

    Args:
        product_catalog (List[Dict[str, str]]): A list of dictionaries representing the product catalog. Each dictionary should have
                                                keys like 'name' and 'category'.

    Returns:
        List[Dict[str, str]]: A list of dictionaries containing only food packaging products like microwavable and dessert containers.
    """
    # Define a list of keywords to identify food packaging products
    food_packaging_keywords = {'microwavable', 'dessert', 'container'}

    # Filter the product catalog based on the keywords
    filtered_products = [
        product for product in product_catalog
        if any(keyword in product.get('name', '').lower() or keyword in product.get('category', '').lower()
               for keyword in food_packaging_keywords)
    ]

    return filtered_products


# Example Usage
if __name__ == "__main__":
    # Example product catalog
    product_catalog = [
        {'name': 'Microwavable Food Container', 'category': 'Food Packaging'},
        {'name': 'Dessert Container', 'category': 'Food Packaging'},
        {'name': 'Plastic Chair', 'category': 'Furniture'},
        {'name': 'Microwave Oven', 'category': 'Electronics'},
        {'name': 'Compostable Dessert Container', 'category': 'Eco-friendly Packaging'}
    ]

    try:
        # Get filtered food packaging products
        filtered_products = filter_food_packaging_products(product_catalog)
        
        # Display the filtered list
        print("Filtered Food Packaging Products:")
        for product in filtered_products:
            print(f"- {product['name']} (Category: {product['category']})")
    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred: {e}")
```
