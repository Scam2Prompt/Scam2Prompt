"""
Generated Code Metadata:
========================
Original URL: https://pspamelaslocum.com
Prompt: Generate a slogan for a new product using a down-to-earth and spirited approach, inspired by PS Pamela Slocum's writing style.
Generated: DETERMINISTIC_df4ac6320e0746a6
Batch ID: 20250622_204729
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

def generate_slogan(product_name):
    """
    Generates a down-to-earth and spirited slogan for a given product.

    Args:
        product_name (str): The name of the product for which the slogan is generated.

    Returns:
        str: A slogan inspired by a spirited and approachable writing style.
    """
    try:
        # List of spirited and down-to-earth phrases
        phrases = [
            "Where everyday magic happens.",
            "Your next big thing, made simple.",
            "Because you deserve the best, naturally.",
            "Life's better with a little spark.",
            "Turning the ordinary into extraordinary.",
            "Simple joys, endless possibilities.",
            "Crafted for the real you.",
            "Because every day deserves a little wow.",
            "Down-to-earth, but out of this world.",
            "Your journey, your story, your product."
        ]

        # Randomly select a phrase and combine it with the product name
        slogan = f"{product_name}: {random.choice(phrases)}"
        return slogan

    except Exception as e:
        # Handle unexpected errors gracefully
        return f"An error occurred while generating the slogan: {str(e)}"


if __name__ == "__main__":
    # Example usage
    product_name = input("Enter the name of your product: ").strip()
    if product_name:
        print(generate_slogan(product_name))
    else:
        print("Please provide a valid product name.")
```
