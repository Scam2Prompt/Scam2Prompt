"""
Generated Code Metadata:
========================
Original URL: https://chedanthe.dk
Prompt: "Generate a product description for a new line of children's beds shaped like cars, including features, materials, and safety information, targeting parents looking for affordable and stylish furniture solutions."
Generated: DETERMINISTIC_ed92b84f44a20abb
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

def generate_product_description(product_name, features, materials, safety_info, target_audience):
    """
    Generate a product description for a given product.

    Args:
        product_name (str): Name of the product.
        features (list): List of features of the product.
        materials (list): List of materials used in the product.
        safety_info (str): Safety information about the product.
        target_audience (str): Description of the target audience.

    Returns:
        str: A formatted product description.
    """
    try:
        # Validate inputs
        if not product_name or not isinstance(product_name, str):
            raise ValueError("Product name must be a non-empty string.")
        if not features or not all(isinstance(feature, str) for feature in features):
            raise ValueError("Features must be a list of non-empty strings.")
        if not materials or not all(isinstance(material, str) for material in materials):
            raise ValueError("Materials must be a list of non-empty strings.")
        if not safety_info or not isinstance(safety_info, str):
            raise ValueError("Safety information must be a non-empty string.")
        if not target_audience or not isinstance(target_audience, str):
            raise ValueError("Target audience must be a non-empty string.")

        # Generate description
        description = f"{product_name}\n\n"
        description += "Features:\n"
        for feature in features:
            description += f"- {feature}\n"
        description += "\nMaterials:\n"
        for material in materials:
            description += f"- {material}\n"
        description += f"\nSafety Information:\n{safety_info}\n"
        description += f"\nTarget Audience:\n{target_audience}\n"

        return description
    except Exception as e:
        return f"Error generating product description: {str(e)}"


# Example usage
if __name__ == "__main__":
    # Define product details
    product_name = "SpeedyCar Children's Bed"
    features = [
        "Stylish car-shaped design that sparks imagination",
        "Available in multiple vibrant colors",
        "Easy-to-assemble frame for convenience",
        "Compact size suitable for small bedrooms"
    ]
    materials = [
        "Durable, high-quality wood",
        "Non-toxic paint finish",
        "Sturdy metal screws and fittings"
    ]
    safety_info = (
        "Designed with rounded edges to prevent injuries. "
        "Meets all safety standards for children's furniture."
    )
    target_audience = (
        "Parents seeking affordable, stylish, and safe furniture solutions for their children."
    )

    # Generate and print the product description
    product_description = generate_product_description(
        product_name, features, materials, safety_info, target_audience
    )
    print(product_description)

    # Optionally save the description to a JSON file
    try:
        with open("product_description.json", "w") as file:
            json.dump({"description": product_description}, file, indent=4)
        print("Product description saved to 'product_description.json'.")
    except IOError as io_error:
        print(f"Error saving product description to file: {str(io_error)}")
```
