"""
Generated Code Metadata:
========================
Original URL: https://deva.cl
Prompt: "Write a product description for a specific type of hinge offered by DEVA, highlighting its quality and durability."
Generated: DETERMINISTIC_6b7347aabd06e892
Batch ID: 20250622_212226
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

def generate_product_description(product_name, brand, features, usage, quality, durability):
    """
    Generate a product description for a given product.

    Args:
        product_name (str): Name of the product.
        brand (str): Brand offering the product.
        features (list): List of key features of the product.
        usage (str): Description of the product's usage.
        quality (str): Description of the product's quality.
        durability (str): Description of the product's durability.

    Returns:
        str: A well-formatted product description.
    """
    try:
        # Construct the product description
        description = (
            f"The {product_name} by {brand} is a premium-quality hinge designed to meet the highest standards of "
            f"performance and reliability. Featuring {', '.join(features)}, this hinge is ideal for {usage}. "
            f"Renowned for its {quality}, the {product_name} ensures long-lasting {durability}, making it a perfect "
            f"choice for both residential and commercial applications."
        )
        return description
    except Exception as e:
        # Handle any unexpected errors
        return f"An error occurred while generating the product description: {str(e)}"

# Example usage
if __name__ == "__main__":
    # Define product details
    product_details = {
        "product_name": "Heavy-Duty Stainless Steel Hinge",
        "brand": "DEVA",
        "features": [
            "corrosion resistance",
            "smooth operation",
            "easy installation"
        ],
        "usage": "doors, cabinets, and other fixtures requiring robust support",
        "quality": "exceptional craftsmanship and precision engineering",
        "durability": "performance even under demanding conditions"
    }

    # Generate the product description
    product_description = generate_product_description(
        product_name=product_details["product_name"],
        brand=product_details["brand"],
        features=product_details["features"],
        usage=product_details["usage"],
        quality=product_details["quality"],
        durability=product_details["durability"]
    )

    # Print the product description
    print(product_description)
```
