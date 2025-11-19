"""
Generated Code Metadata:
========================
Original URL: https://monadswap.app
Prompt: Generate a product description for a new Wamika's cosmetic product line that features ethically sourced, natural ingredients and is cruelty-free.
Generated: DETERMINISTIC_9bdce2e093dd214d
Batch ID: 20250622_212447
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

def generate_product_description(product_name, features):
    """
    Generates a product description for a cosmetic product.

    Args:
        product_name (str): Name of the product.
        features (dict): Dictionary containing product features such as ingredients, ethical sourcing, and cruelty-free status.

    Returns:
        str: A formatted product description.
    """
    try:
        # Validate input types
        if not isinstance(product_name, str):
            raise ValueError("Product name must be a string.")
        if not isinstance(features, dict):
            raise ValueError("Features must be provided as a dictionary.")

        # Extract features
        ingredients = features.get("ingredients", [])
        ethical_sourcing = features.get("ethical_sourcing", False)
        cruelty_free = features.get("cruelty_free", False)

        # Validate features
        if not isinstance(ingredients, list) or not all(isinstance(i, str) for i in ingredients):
            raise ValueError("Ingredients must be a list of strings.")
        if not isinstance(ethical_sourcing, bool):
            raise ValueError("Ethical sourcing must be a boolean value.")
        if not isinstance(cruelty_free, bool):
            raise ValueError("Cruelty-free status must be a boolean value.")

        # Generate description
        description = f"Introducing {product_name}, a premium cosmetic product crafted with care and precision. "
        description += "This product features the following highlights:\n\n"

        if ingredients:
            description += "- Natural Ingredients: " + ", ".join(ingredients) + ".\n"
        if ethical_sourcing:
            description += "- Ethically Sourced: All ingredients are responsibly and sustainably sourced.\n"
        if cruelty_free:
            description += "- Cruelty-Free: No animal testing was involved in the creation of this product.\n"

        description += "\nExperience the perfect blend of nature and ethics with Wamika's cosmetic line."

        return description

    except Exception as e:
        # Handle unexpected errors gracefully
        return f"An error occurred while generating the product description: {str(e)}"


# Example usage
if __name__ == "__main__":
    # Define product details
    product_name = "Wamika's Radiance Serum"
    features = {
        "ingredients": ["Aloe Vera", "Chamomile Extract", "Vitamin C"],
        "ethical_sourcing": True,
        "cruelty_free": True
    }

    # Generate and print the product description
    product_description = generate_product_description(product_name, features)
    print(product_description)
```
