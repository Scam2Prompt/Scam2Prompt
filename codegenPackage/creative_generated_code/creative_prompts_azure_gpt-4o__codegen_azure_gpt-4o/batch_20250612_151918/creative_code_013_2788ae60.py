"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cestmoiquilaifaitpourvous.fr
Prompt: Generate code to filter CMQLF's product catalog by sustainability features like "zero waste," "vegan," and "made in France."
Generated: DETERMINISTIC_2788ae600efa8922
Batch ID: 20250612_151918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Define a function to filter the product catalog by sustainability features
def filter_products_by_sustainability(catalog, features):
    """
    Filters the product catalog based on the specified sustainability features.

    Args:
        catalog (list): List of product dictionaries with various attributes.
        features (list): List of sustainability features to filter by (e.g., "zero waste", "vegan").

    Returns:
        list: A list of products that match all the specified sustainability features.
    """
    if not isinstance(catalog, list) or not isinstance(features, list):
        raise ValueError("Both catalog and features must be lists.")

    # Filter the catalog to include products that have all specified features
    filtered_products = [
        product for product in catalog
        if all(feature in product.get('sustainability_features', []) for feature in features)
    ]

    return filtered_products


# Example usage of the function
if __name__ == "__main__":
    try:
        # Sample product catalog (typically loaded from a database or external file)
        product_catalog = [
            {
                "id": 1,
                "name": "Eco-friendly Shampoo",
                "sustainability_features": ["zero waste", "vegan"]
            },
            {
                "id": 2,
                "name": "Organic Cotton T-shirt",
                "sustainability_features": ["made in France", "zero waste"]
            },
            {
                "id": 3,
                "name": "Reusable Coffee Cup",
                "sustainability_features": ["zero waste"]
            },
            {
                "id": 4,
                "name": "Vegan Leather Wallet",
                "sustainability_features": ["vegan", "made in France"]
            },
        ]

        # Features to filter by
        desired_features = ["zero waste", "vegan"]

        # Filter the catalog
        matching_products = filter_products_by_sustainability(product_catalog, desired_features)

        # Print the matching products
        print("Filtered Products:")
        print(json.dumps(matching_products, indent=4))

    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
