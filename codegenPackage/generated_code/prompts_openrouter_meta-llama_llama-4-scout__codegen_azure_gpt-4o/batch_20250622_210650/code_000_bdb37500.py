"""
Generated Code Metadata:
========================
Original URL: https://morevacare.com
Prompt: "Write a product description for a natural soap made with lavender oil and tonerde, using a tone that emphasizes sustainability and natural beauty."
Generated: DETERMINISTIC_bdb3750048c7f816
Batch ID: 20250622_210650
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

def generate_product_description(product_name, ingredients, tone):
    """
    Generates a product description for a given product.

    Args:
        product_name (str): Name of the product.
        ingredients (list): List of key ingredients in the product.
        tone (str): Desired tone for the description.

    Returns:
        str: A well-crafted product description.
    """
    try:
        # Validate inputs
        if not product_name or not isinstance(product_name, str):
            raise ValueError("Product name must be a non-empty string.")
        if not ingredients or not all(isinstance(i, str) for i in ingredients):
            raise ValueError("Ingredients must be a list of non-empty strings.")
        if not tone or not isinstance(tone, str):
            raise ValueError("Tone must be a non-empty string.")

        # Generate description
        description = (
            f"Introducing {product_name}, a luxurious natural soap crafted with care to "
            f"celebrate sustainability and the beauty of nature. Infused with the calming essence "
            f"of {ingredients[0]} and enriched with the purifying properties of {ingredients[1]}, "
            f"this soap is a perfect harmony of gentle care and eco-conscious living. "
            f"Experience the soothing touch of nature with every use, knowing that {product_name} "
            f"is thoughtfully made to support a greener, more beautiful world."
        )

        return description

    except Exception as e:
        # Handle errors gracefully
        return f"An error occurred while generating the product description: {str(e)}"


# Example usage
if __name__ == "__main__":
    # Define product details
    product_name = "Lavender & Tonerde Natural Soap"
    ingredients = ["lavender oil", "tonerde"]
    tone = "sustainability and natural beauty"

    # Generate and print the product description
    product_description = generate_product_description(product_name, ingredients, tone)
    print(product_description)

    # Optionally, save the description to a JSON file
    try:
        with open("product_description.json", "w") as file:
            json.dump({"product_name": product_name, "description": product_description}, file, indent=4)
    except IOError as io_error:
        print(f"Failed to save the product description to a file: {str(io_error)}")
```
