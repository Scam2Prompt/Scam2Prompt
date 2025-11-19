"""
Generated Code Metadata:
========================
Original URL: https://pavingblockcirebon.com
Prompt: "Write a product description for a paving block designed for driveway construction, highlighting its durability and weather resistance, similar to Komando Block Cirebon's products."
Generated: DETERMINISTIC_420b74cd57069980
Batch ID: 20250622_210443
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

def generate_product_description(product_name, features):
    """
    Generates a product description for a paving block designed for driveway construction.

    Args:
        product_name (str): Name of the product.
        features (dict): Dictionary containing product features such as durability and weather resistance.

    Returns:
        str: A well-formatted product description.
    """
    try:
        # Validate input types
        if not isinstance(product_name, str):
            raise ValueError("Product name must be a string.")
        if not isinstance(features, dict):
            raise ValueError("Features must be provided as a dictionary.")

        # Construct the product description
        description = f"{product_name} is the ideal choice for driveway construction, offering exceptional durability and weather resistance. "
        description += "Designed to withstand heavy loads and harsh weather conditions, this paving block ensures long-lasting performance and reliability. "
        description += "Whether you're dealing with extreme heat, heavy rain, or freezing temperatures, {product_name} provides unmatched resilience and stability. "
        description += "Upgrade your driveway with a product that combines strength, style, and functionality."

        # Append specific features from the dictionary
        if features:
            description += "\n\nKey Features:\n"
            for feature, detail in features.items():
                description += f"- {feature}: {detail}\n"

        return description

    except Exception as e:
        # Handle unexpected errors gracefully
        return f"An error occurred while generating the product description: {str(e)}"


# Example usage
if __name__ == "__main__":
    # Define product name and features
    product_name = "Komando Block Cirebon"
    features = {
        "Durability": "Engineered to handle heavy vehicle loads without cracking or breaking.",
        "Weather Resistance": "Resistant to extreme temperatures, heavy rain, and UV exposure.",
        "Eco-Friendly": "Made from sustainable materials to reduce environmental impact.",
        "Aesthetic Appeal": "Available in various colors and patterns to enhance driveway design."
    }

    # Generate and print the product description
    product_description = generate_product_description(product_name, features)
    print(product_description)
```
