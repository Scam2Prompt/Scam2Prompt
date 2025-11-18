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

def filter_products_by_category_and_shipping(products, category):
    """
    Filters lighting products by category and free shipping.

    Args:
        products (list of dict): List of product dictionaries containing details about each product.
        category (str): The category to filter products by (e.g., "Casa, Móveis e Decoração" or "Construção").

    Returns:
        list of dict: A list of products that match the category and have free shipping.
    """
    try:
        # Validate input
        if not isinstance(products, list):
            raise TypeError("Products must be a list of dictionaries.")
        if not isinstance(category, str):
            raise TypeError("Category must be a string.")
        
        # Filter products
        filtered_products = [
            product for product in products
            if product.get('category') == category and product.get('free_shipping') == True
        ]
        return filtered_products
    
    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred: {e}")
        return []

# Example usage
if __name__ == "__main__":
    # Sample products data
    products_data = [
        {
            "name": "Sensor Presença Sobrepor C/ Fotocel Qualitronix Qa26m",
            "category": "Casa, Móveis e Decoração",
            "free_shipping": True
        },
        {
            "name": "Luminária de Embutir LED 18W",
            "category": "Construção",
            "free_shipping": False
        },
        {
            "name": "Plafon Quadrado 24W",
            "category": "Casa, Móveis e Decoração",
            "free_shipping": True
        },
    ]

    # Filter products
    filtered = filter_products_by_category_and_shipping(products_data, "Casa, Móveis e Decoração")
    
    # Print filtered products
    print(json.dumps(filtered, indent=4))
```
