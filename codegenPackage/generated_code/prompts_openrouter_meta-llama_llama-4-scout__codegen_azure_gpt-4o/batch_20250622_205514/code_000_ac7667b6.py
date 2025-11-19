"""
Generated Code Metadata:
========================
Original URL: https://zentocosmetic.com
Prompt: Write a product description for a hair volume shampoo that contains natural oil complex and provides a protective layer for hair, similar to ZENTO VOLUME ŞAMPUAN.
Generated: DETERMINISTIC_ac7667b62f7bdf5b
Batch ID: 20250622_205514
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

def generate_product_description(product_name, key_features, benefits):
    """
    Generates a product description for a given product.

    Args:
        product_name (str): Name of the product.
        key_features (list): List of key features of the product.
        benefits (list): List of benefits provided by the product.

    Returns:
        str: A well-formatted product description.
    """
    try:
        # Validate input types
        if not isinstance(product_name, str):
            raise ValueError("Product name must be a string.")
        if not isinstance(key_features, list) or not all(isinstance(feature, str) for feature in key_features):
            raise ValueError("Key features must be a list of strings.")
        if not isinstance(benefits, list) or not all(isinstance(benefit, str) for benefit in benefits):
            raise ValueError("Benefits must be a list of strings.")

        # Generate description
        description = f"{product_name} is designed to elevate your hair care routine. "
        description += "Infused with a natural oil complex, this shampoo provides a protective layer for your hair, "
        description += "ensuring long-lasting volume and vitality. Key features include:\n\n"

        # Add key features
        for feature in key_features:
            description += f"- {feature}\n"

        description += "\nBenefits:\n\n"

        # Add benefits
        for benefit in benefits:
            description += f"- {benefit}\n"

        return description

    except Exception as e:
        # Handle errors gracefully
        return f"An error occurred while generating the product description: {str(e)}"


# Example usage
if __name__ == "__main__":
    # Define product details
    product_name = "ZENTO VOLUME ŞAMPUAN"
    key_features = [
        "Contains a natural oil complex",
        "Provides a protective layer for hair",
        "Enhances hair volume and vitality"
    ]
    benefits = [
        "Long-lasting volume",
        "Improved hair texture",
        "Protection against environmental damage"
    ]

    # Generate and print the product description
    product_description = generate_product_description(product_name, key_features, benefits)
    print(product_description)
```
