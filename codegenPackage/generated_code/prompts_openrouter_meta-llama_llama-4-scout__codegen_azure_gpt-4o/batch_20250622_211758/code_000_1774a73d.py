"""
Generated Code Metadata:
========================
Original URL: https://zerion.shop
Prompt: Write a product description for a Snow Jacket Fatbike, similar to the one found on Zerion's website.
Generated: DETERMINISTIC_1774a73d6737f73d
Batch ID: 20250622_211758
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

def generate_product_description(product_name, features, target_audience, use_case):
    """
    Generates a product description for a given product.

    Args:
        product_name (str): Name of the product.
        features (list): List of features of the product.
        target_audience (str): Description of the target audience.
        use_case (str): Description of the primary use case.

    Returns:
        str: A well-formatted product description.
    """
    try:
        # Validate inputs
        if not product_name or not isinstance(product_name, str):
            raise ValueError("Product name must be a non-empty string.")
        if not features or not isinstance(features, list):
            raise ValueError("Features must be a non-empty list.")
        if not target_audience or not isinstance(target_audience, str):
            raise ValueError("Target audience must be a non-empty string.")
        if not use_case or not isinstance(use_case, str):
            raise ValueError("Use case must be a non-empty string.")

        # Generate the product description
        description = f"{product_name}\n\n"
        description += "Features:\n"
        for feature in features:
            description += f"- {feature}\n"
        description += f"\nDesigned for: {target_audience}\n"
        description += f"Perfect for: {use_case}\n"

        return description
    except Exception as e:
        # Handle errors gracefully
        return f"Error generating product description: {str(e)}"


# Example usage
if __name__ == "__main__":
    # Define product details
    product_name = "Snow Jacket Fatbike"
    features = [
        "Durable aluminum frame for extreme conditions",
        "Wide, grippy tires for superior traction on snow and ice",
        "High-performance disc brakes for reliable stopping power",
        "Ergonomic design for comfort during long rides",
        "Lightweight construction for easy maneuverability"
    ]
    target_audience = "Outdoor enthusiasts and adventure seekers"
    use_case = "Exploring snowy trails and icy terrains"

    # Generate and print the product description
    product_description = generate_product_description(product_name, features, target_audience, use_case)
    print(product_description)
```
