"""
Generated Code Metadata:
========================
Original URL: https://allsmallshop.com
Prompt: "Write a product description for men's waterproof anti-skid boots and women's lined boots with lace-up side zipper."
Generated: DETERMINISTIC_f842c49a138d61ad
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import json

def generate_product_description(product_type):
    """
    Generates a product description based on the product type.

    Args:
        product_type (str): The type of product ("men's boots" or "women's boots").

    Returns:
        str: A detailed product description.
    """
    try:
        # Dictionary to store product descriptions
        product_descriptions = {
            "men's boots": (
                "Experience unparalleled comfort and durability with our Men's Waterproof Anti-Skid Boots. "
                "Designed to withstand the toughest conditions, these boots feature a waterproof exterior "
                "to keep your feet dry in any weather. The anti-skid sole ensures superior grip and stability, "
                "making them perfect for outdoor adventures or everyday wear. Built for performance and style, "
                "these boots are a must-have for any wardrobe."
            ),
            "women's boots": (
                "Step into elegance and warmth with our Women's Lined Boots featuring a stylish lace-up side zipper. "
                "Crafted for both fashion and functionality, these boots offer a cozy lined interior to keep your feet "
                "comfortable during colder months. The lace-up design combined with a convenient side zipper provides "
                "a secure fit and easy wear. Perfect for pairing with any outfit, these boots are a versatile addition "
                "to your collection."
            )
        }

        # Fetch the product description based on the product type
        description = product_descriptions.get(product_type.lower())
        if not description:
            raise ValueError("Invalid product type. Please choose 'men's boots' or 'women's boots'.")

        return description

    except Exception as e:
        # Handle errors gracefully
        return f"Error generating product description: {str(e)}"


# Example usage
if __name__ == "__main__":
    # Define product types
    product_types = ["men's boots", "women's boots"]

    # Generate descriptions for each product type
    for product in product_types:
        print(f"Product Type: {product}")
        print(generate_product_description(product))
        print("-" * 80)
```
