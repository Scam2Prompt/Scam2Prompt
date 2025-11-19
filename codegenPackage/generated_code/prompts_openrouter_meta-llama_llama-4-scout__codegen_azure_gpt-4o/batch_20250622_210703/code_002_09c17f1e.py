"""
Generated Code Metadata:
========================
Original URL: https://nodoitalia.com
Prompt: "Write a product description for the Eva Chair and Beach House Armchair, highlighting their design inspiration, materials, and suitability for outdoor spaces in hotels, restaurants, or private residences."
Generated: DETERMINISTIC_09c17f1e086e9cbd
Batch ID: 20250622_210703
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

def generate_product_description(product_name):
    """
    Generates a product description for the given product name.

    Args:
        product_name (str): Name of the product.

    Returns:
        str: A detailed product description.
    """
    try:
        # Dictionary containing product details
        product_details = {
            "Eva Chair": {
                "design_inspiration": "Inspired by modern minimalism, the Eva Chair combines sleek lines with ergonomic comfort.",
                "materials": "Crafted from weather-resistant aluminum and UV-protected woven rattan.",
                "suitability": "Perfect for outdoor spaces in hotels, restaurants, or private residences, offering both style and durability."
            },
            "Beach House Armchair": {
                "design_inspiration": "Drawing from coastal aesthetics, the Beach House Armchair evokes a sense of relaxation and seaside charm.",
                "materials": "Constructed with sustainably sourced teak wood and quick-dry foam cushions.",
                "suitability": "Ideal for patios, poolside lounges, or garden areas in hospitality venues or private homes."
            }
        }

        # Check if the product exists in the dictionary
        if product_name not in product_details:
            raise ValueError(f"Product '{product_name}' not found. Please provide a valid product name.")

        # Fetch product details
        details = product_details[product_name]

        # Format the product description
        description = (
            f"{product_name}\n"
            f"Design Inspiration: {details['design_inspiration']}\n"
            f"Materials: {details['materials']}\n"
            f"Suitability: {details['suitability']}"
        )

        return description

    except ValueError as ve:
        # Handle invalid product name error
        return str(ve)
    except Exception as e:
        # Handle unexpected errors
        return f"An unexpected error occurred: {str(e)}"


# Example usage
if __name__ == "__main__":
    # List of products to generate descriptions for
    products = ["Eva Chair", "Beach House Armchair", "Unknown Product"]

    # Generate and print descriptions for each product
    for product in products:
        print(generate_product_description(product))
        print("-" * 80)  # Separator for readability
```
