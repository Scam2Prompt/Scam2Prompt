"""
Generated Code Metadata:
========================
Original URL: https://loli.bg
Prompt: Generate a list of product categories and subcategories for a children's clothing online store, inspired by the categories found on loli.bg.
Generated: DETERMINISTIC_a1c0a24256a2c14e
Batch ID: 20250622_205955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from typing import List, Dict

def generate_product_categories() -> List[Dict[str, List[str]]]:
    """
    Generate a list of product categories and their corresponding subcategories
    for a children's clothing online store.

    Returns:
        List[Dict[str, List[str]]]: A list of dictionaries where each dictionary
        contains a category and its subcategories.
    """
    try:
        # Define the product categories and their subcategories
        categories = [
            {
                "category": "Boys",
                "subcategories": [
                    "T-Shirts",
                    "Pants",
                    "Shorts",
                    "Jackets",
                    "Sweaters",
                    "Suits",
                    "Activewear"
                ]
            },
            {
                "category": "Girls",
                "subcategories": [
                    "Dresses",
                    "Tops",
                    "Skirts",
                    "Pants",
                    "Shorts",
                    "Jackets",
                    "Activewear"
                ]
            },
            {
                "category": "Infants",
                "subcategories": [
                    "Bodysuits",
                    "Sleepers",
                    "Outfits",
                    "Hats",
                    "Socks",
                    "Outerwear"
                ]
            },
            {
                "category": "Accessories",
                "subcategories": [
                    "Hats",
                    "Bags",
                    "Belts",
                    "Socks",
                    "Shoes",
                    "Jewelry"
                ]
            },
            {
                "category": "Footwear",
                "subcategories": [
                    "Sneakers",
                    "Sandals",
                    "Boots",
                    "Dress Shoes",
                    "Slippers"
                ]
            }
        ]
        
        return categories

    except Exception as e:
        # Log the error and raise an exception
        print(f"An error occurred while generating categories: {e}")
        raise

# Example usage
if __name__ == "__main__":
    try:
        product_categories = generate_product_categories()
        for category in product_categories:
            print(f"Category: {category['category']}")
            print("Subcategories:", ", ".join(category['subcategories']))
            print()
    except Exception as e:
        print(f"Failed to retrieve product categories: {e}")
```
