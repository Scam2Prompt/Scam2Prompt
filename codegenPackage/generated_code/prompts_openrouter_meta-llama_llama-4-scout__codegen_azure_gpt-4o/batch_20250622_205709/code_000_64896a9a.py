"""
Generated Code Metadata:
========================
Original URL: https://ccjourney.co
Prompt: Write a product description for a casual bra top from the Enchanted Forest collection on the Capsule Cosmic Journey online store.
Generated: DETERMINISTIC_64896a9a7524cafb
Batch ID: 20250622_205709
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

def generate_product_description(product_name, collection_name, store_name):
    """
    Generates a product description for a given product in a specific collection and store.

    Args:
        product_name (str): Name of the product.
        collection_name (str): Name of the collection the product belongs to.
        store_name (str): Name of the online store.

    Returns:
        str: A well-crafted product description.
    """
    try:
        # Validate input parameters
        if not all(isinstance(arg, str) for arg in [product_name, collection_name, store_name]):
            raise ValueError("All arguments must be strings.")

        # Generate the product description
        description = (
            f"Introducing the {product_name}, a perfect blend of comfort and style from the {collection_name} collection. "
            f"Designed for the modern adventurer, this casual bra top offers unparalleled ease and versatility, "
            f"making it an essential addition to your wardrobe. Whether you're exploring the great outdoors or relaxing at home, "
            f"the {product_name} ensures you stay effortlessly chic. Available exclusively at {store_name}, "
            f"where every piece is crafted to inspire your cosmic journey."
        )
        return description

    except ValueError as ve:
        # Handle invalid input errors
        return f"Error: {str(ve)}"

    except Exception as e:
        # Handle unexpected errors
        return f"An unexpected error occurred: {str(e)}"


# Example usage
if __name__ == "__main__":
    # Define product details
    product_name = "Casual Bra Top"
    collection_name = "Enchanted Forest"
    store_name = "Capsule Cosmic Journey"

    # Generate and print the product description
    product_description = generate_product_description(product_name, collection_name, store_name)
    print(product_description)
```
