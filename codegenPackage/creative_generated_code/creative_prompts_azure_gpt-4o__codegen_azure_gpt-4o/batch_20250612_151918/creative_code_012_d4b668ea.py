"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cestmoiquilaifaitpourvous.fr
Prompt: Develop a program to compare CMQLF's vegan and non-vegan product options and display their ingredients and certifications.
Generated: DETERMINISTIC_d4b668ea4aa5d8d5
Batch ID: 20250612_151918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Sample data for CMQLF's vegan and non-vegan products
PRODUCTS = [
    {
        "name": "Vegan Protein Bar",
        "type": "vegan",
        "ingredients": ["Pea Protein", "Almond Butter", "Coconut Nectar"],
        "certifications": ["Organic", "Non-GMO", "Certified Vegan"]
    },
    {
        "name": "Non-Vegan Whey Protein Powder",
        "type": "non-vegan",
        "ingredients": ["Whey Protein Concentrate", "Natural Flavors", "Soy Lecithin"],
        "certifications": ["Organic", "Non-GMO"]
    },
    {
        "name": "Vegan Snack Mix",
        "type": "vegan",
        "ingredients": ["Cashews", "Dried Cranberries", "Pumpkin Seeds"],
        "certifications": ["Certified Vegan", "Gluten-Free"]
    },
    {
        "name": "Non-Vegan Energy Bar",
        "type": "non-vegan",
        "ingredients": ["Milk Chocolate", "Honey", "Oats"],
        "certifications": ["Non-GMO"]
    }
]

def filter_products_by_type(products, product_type):
    """
    Filters the products based on their type (vegan or non-vegan).

    Args:
        products (list): List of product dictionaries.
        product_type (str): Type of product to filter ('vegan' or 'non-vegan').

    Returns:
        list: Filtered list of products of the given type.
    """
    return [product for product in products if product["type"] == product_type]

def display_products(products):
    """
    Displays the products with their ingredients and certifications.

    Args:
        products (list): List of product dictionaries.
    """
    for product in products:
        print(f"Product Name: {product['name']}")
        print(f"Type: {product['type'].capitalize()}")
        print("Ingredients:")
        for ingredient in product["ingredients"]:
            print(f"  - {ingredient}")
        print("Certifications:")
        for cert in product["certifications"]:
            print(f"  - {cert}")
        print("-" * 40)

def main():
    """
    Main function to compare CMQLF's vegan and non-vegan products.
    """
    try:
        print("CMQLF's Vegan Products:")
        vegan_products = filter_products_by_type(PRODUCTS, "vegan")
        display_products(vegan_products)

        print("\nCMQLF's Non-Vegan Products:")
        non_vegan_products = filter_products_by_type(PRODUCTS, "non-vegan")
        display_products(non_vegan_products)
    except Exception as e:
        # Log the error and display a user-friendly message
        print("An error occurred while processing the product data.")
        print(f"Error details: {str(e)}")

if __name__ == "__main__":
    main()
```
