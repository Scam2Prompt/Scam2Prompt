"""
Generated Code Metadata:
========================
Original URL: https://semillasplantae.com
Prompt: "Generate a list of product categories and subcategories for an online store selling organic seeds, using Semillas Plantae as a reference."
Generated: DETERMINISTIC_17bad5053acb0cf5
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
import json

# Define a function to generate product categories and subcategories
def generate_product_categories():
    """
    Generates a list of product categories and subcategories for an online store selling organic seeds.
    Returns:
        dict: A dictionary containing categories and their respective subcategories.
    """
    try:
        # Define the categories and subcategories
        categories = {
            "Vegetables": [
                "Leafy Greens",
                "Root Vegetables",
                "Fruiting Vegetables",
                "Herbs"
            ],
            "Fruits": [
                "Berries",
                "Citrus Fruits",
                "Stone Fruits",
                "Tropical Fruits"
            ],
            "Flowers": [
                "Annual Flowers",
                "Perennial Flowers",
                "Edible Flowers",
                "Wildflowers"
            ],
            "Grains & Legumes": [
                "Cereal Grains",
                "Pulses",
                "Ancient Grains"
            ],
            "Specialty Seeds": [
                "Medicinal Plants",
                "Rare Varieties",
                "Cover Crops"
            ]
        }

        # Return the categories as a dictionary
        return categories

    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred while generating product categories: {e}")
        return {}

# Main execution block
if __name__ == "__main__":
    # Generate the product categories
    product_categories = generate_product_categories()

    # Convert the categories to a JSON string for better readability
    categories_json = json.dumps(product_categories, indent=4)

    # Print the categories
    print("Product Categories and Subcategories:")
    print(categories_json)
```
