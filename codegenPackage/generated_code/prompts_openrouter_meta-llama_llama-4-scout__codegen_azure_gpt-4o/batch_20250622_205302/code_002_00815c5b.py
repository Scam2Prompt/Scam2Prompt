"""
Generated Code Metadata:
========================
Original URL: https://regency-towel.com
Prompt: Generate a product description for a 100% cotton bath towel,  similar to those produced by Regency Towel, using a formal tone and highlighting its features and benefits.
Generated: DETERMINISTIC_00815c5b0cf86f69
Batch ID: 20250622_205302
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

def generate_product_description(product_name, material, features, benefits):
    """
    Generates a formal product description for a given product.

    Args:
        product_name (str): Name of the product.
        material (str): Material of the product.
        features (list): List of features of the product.
        benefits (list): List of benefits of the product.

    Returns:
        str: A formal product description highlighting features and benefits.
    """
    try:
        # Validate input types
        if not isinstance(product_name, str) or not isinstance(material, str):
            raise ValueError("Product name and material must be strings.")
        if not isinstance(features, list) or not isinstance(benefits, list):
            raise ValueError("Features and benefits must be lists.")

        # Construct the product description
        description = f"{product_name}\n"
        description += f"Crafted from 100% {material}, this premium bath towel offers unparalleled quality and comfort.\n\n"
        description += "Features:\n"
        for feature in features:
            description += f"- {feature}\n"
        description += "\nBenefits:\n"
        for benefit in benefits:
            description += f"- {benefit}\n"

        return description
    except Exception as e:
        # Handle unexpected errors
        return f"An error occurred while generating the product description: {str(e)}"

# Example usage
if __name__ == "__main__":
    # Define product details
    product_name = "Regency Towel - 100% Cotton Bath Towel"
    material = "cotton"
    features = [
        "Luxuriously soft and absorbent",
        "Generously sized for maximum comfort",
        "Durable and long-lasting construction",
        "Elegant design suitable for any bathroom decor"
    ]
    benefits = [
        "Provides a spa-like experience in the comfort of your home",
        "Efficiently dries your skin while remaining gentle",
        "Retains its quality after multiple washes",
        "Enhances the aesthetic appeal of your bathroom"
    ]

    # Generate and print the product description
    product_description = generate_product_description(product_name, material, features, benefits)
    print(product_description)
```
