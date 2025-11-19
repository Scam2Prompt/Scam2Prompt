"""
Generated Code Metadata:
========================
Original URL: https://ethn.cc
Prompt: Write a product description for the CST Overton gravel tires, highlighting their features and benefits for gravel cycling.
Generated: DETERMINISTIC_3fca5332a2d991f1
Batch ID: 20250622_211520
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

def generate_product_description(product_name, features, benefits):
    """
    Generates a product description for a given product, highlighting its features and benefits.

    Args:
        product_name (str): Name of the product.
        features (list): List of features of the product.
        benefits (list): List of benefits of the product.

    Returns:
        str: A formatted product description.
    """
    try:
        # Validate input types
        if not isinstance(product_name, str):
            raise ValueError("Product name must be a string.")
        if not isinstance(features, list) or not all(isinstance(f, str) for f in features):
            raise ValueError("Features must be a list of strings.")
        if not isinstance(benefits, list) or not all(isinstance(b, str) for b in benefits):
            raise ValueError("Benefits must be a list of strings.")

        # Generate the product description
        description = f"{product_name}\n\n"
        description += "Features:\n"
        for feature in features:
            description += f"- {feature}\n"
        description += "\nBenefits:\n"
        for benefit in benefits:
            description += f"- {benefit}\n"

        return description
    except Exception as e:
        # Handle errors gracefully
        return f"Error generating product description: {str(e)}"


# Product details
product_name = "CST Overton Gravel Tires"
features = [
    "Durable construction for long-lasting performance",
    "Optimized tread pattern for superior grip on gravel roads",
    "Lightweight design for enhanced speed and efficiency",
    "Tubeless-ready compatibility for improved puncture resistance"
]
benefits = [
    "Provides excellent traction and stability on uneven terrain",
    "Ensures a smooth and comfortable ride during gravel cycling",
    "Reduces the risk of flats, allowing for worry-free adventures",
    "Ideal for both competitive and recreational gravel cyclists"
]

# Generate and print the product description
product_description = generate_product_description(product_name, features, benefits)
print(product_description)

# Optionally, save the description to a JSON file for further use
output_file = "product_description.json"
try:
    with open(output_file, "w") as file:
        json.dump({"product_name": product_name, "description": product_description}, file, indent=4)
    print(f"Product description saved to {output_file}")
except IOError as io_error:
    print(f"Error saving product description to file: {str(io_error)}")
```
