"""
Generated Code Metadata:
========================
Original URL: https://milarbrazw.blogspot.com
Prompt: Write a function to filter lighting products by category (e.g., "Casa, Móveis e Decoração" or "Construção") and display only those with free shipping, such as "Sensor Presença Sobrepor C/ Fotocel Qualitronix Qa26m."
Generated: DETERMINISTIC_be91379f6621021a
Batch ID: 20250612_151438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict

def filter_lighting_products(products: List[Dict], category: str) -> List[Dict]:
    """
    Filters lighting products by category and checks for free shipping.

    Args:
        products (List[Dict]): A list of product dictionaries containing product details.
        category (str): The category to filter products by.

    Returns:
        List[Dict]: A list of filtered products that belong to the specified category and have free shipping.
    """
    filtered_products = []

    for product in products:
        try:
            # Check if the product belongs to the specified category and has free shipping
            if product.get('category') == category and product.get('free_shipping', False):
                filtered_products.append(product)
        except KeyError as e:
            # Log the error for missing expected keys in the product dictionary
            print(f"KeyError: {e} in product: {product}")
        except Exception as e:
            # Catch any other exceptions and log them
            print(f"An error occurred: {e} in product: {product}")

    return filtered_products

# Example usage
if __name__ == "__main__":
    # Sample product data
    products_data = [
        {"name": "Sensor Presença Sobrepor C/ Fotocel Qualitronix Qa26m", "category": "Casa, Móveis e Decoração", "free_shipping": True},
        {"name": "Lâmpada LED 9W", "category": "Construção", "free_shipping": False},
        {"name": "Abajur Moderno", "category": "Casa, Móveis e Decoração", "free_shipping": True},
        {"name": "Fita LED 5m", "category": "Iluminação", "free_shipping": True},
    ]

    # Filter products by category "Casa, Móveis e Decoração"
    filtered = filter_lighting_products(products_data, "Casa, Móveis e Decoração")
    
    # Display the filtered products
    print(json.dumps(filtered, indent=4, ensure_ascii=False))
```
