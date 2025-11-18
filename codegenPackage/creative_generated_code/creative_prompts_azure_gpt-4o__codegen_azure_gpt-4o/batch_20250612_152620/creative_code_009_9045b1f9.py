"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kossto.com
Prompt: Write a function to compare Kossto's "Postpartum Belly Band" with similar products, highlighting features like 3-in-1 design and postnatal shapewear benefits.
Generated: DETERMINISTIC_9045b1f90a17b5d4
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python script to compare Kossto's "Postpartum Belly Band" with similar products
# highlighting features like 3-in-1 design and postnatal shapewear benefits.

def compare_products(kossto_product, similar_products):
    """
    Compares Kossto's "Postpartum Belly Band" with similar products.

    Parameters:
        kossto_product (dict): A dictionary containing details about Kossto's product.
        similar_products (list of dict): A list of dictionaries containing details about similar products.

    Returns:
        dict: A comparison summary highlighting the differences and benefits.
    """

    try:
        # Ensure input data is valid
        if not isinstance(kossto_product, dict):
            raise ValueError("kossto_product must be a dictionary.")
        if not isinstance(similar_products, list) or not all(isinstance(p, dict) for p in similar_products):
            raise ValueError("similar_products must be a list of dictionaries.")
        
        # Extract Kossto's product features
        kossto_features = kossto_product.get("features", [])
        if not kossto_features:
            raise ValueError("kossto_product must have a 'features' key with a list of features.")

        # Prepare comparison summary
        comparison_summary = {
            "kossto_features": kossto_features,
            "unique_features": [],
            "shared_features": [],
        }

        # Compare features with other products
        for product in similar_products:
            product_features = product.get("features", [])
            comparison_summary["shared_features"].extend(
                set(kossto_features).intersection(product_features)
            )
            comparison_summary["unique_features"].extend(
                set(kossto_features).difference(product_features)
            )

        # Deduplicate shared and unique features
        comparison_summary["shared_features"] = list(set(comparison_summary["shared_features"]))
        comparison_summary["unique_features"] = list(set(comparison_summary["unique_features"]))

        return comparison_summary

    except Exception as e:
        # Handle unexpected errors gracefully
        return {"error": str(e)}


# Example usage
if __name__ == "__main__":
    # Kossto's product definition
    kossto_product = {
        "name": "Kossto Postpartum Belly Band",
        "features": [
            "3-in-1 design",
            "Postnatal shapewear benefits",
            "Adjustable straps",
            "Breathable material",
            "Provides back support",
        ],
    }

    # Similar products definition
    similar_products = [
        {
            "name": "Brand A Belly Band",
            "features": ["Postnatal shapewear benefits", "Breathable material", "Lightweight design"],
        },
        {
            "name": "Brand B Belly Band",
            "features": ["Adjustable straps", "Provides back support", "4-in-1 design"],
        },
    ]

    # Compare products
    result = compare_products(kossto_product, similar_products)

    # Print the comparison summary
    print("Comparison Summary:")
    print(result)
```
