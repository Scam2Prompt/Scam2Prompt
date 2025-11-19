"""
Generated Code Metadata:
========================
Original URL: https://tamnhuavietkhanh.com
Prompt: "Recommend a suitable plastic product for a home office, considering the use of Tấm ốp phẳng Casary and Tấm ốp đa năng CASARY."
Generated: DETERMINISTIC_6ac2db3e1d3a7fe8
Batch ID: 20250622_210655
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

# Define a function to recommend a suitable plastic product for a home office
def recommend_plastic_product(product_options, use_case):
    """
    Recommend a suitable plastic product based on the use case.

    Args:
        product_options (list): A list of available plastic products with their details.
        use_case (str): The intended use case for the product.

    Returns:
        dict: Recommended product details or a message if no suitable product is found.
    """
    try:
        # Validate input
        if not isinstance(product_options, list) or not isinstance(use_case, str):
            raise ValueError("Invalid input: product_options must be a list and use_case must be a string.")

        # Filter products based on the use case
        recommended_products = [
            product for product in product_options
            if use_case.lower() in product.get("use_cases", [])
        ]

        # Return the first suitable product or a message if none are found
        if recommended_products:
            return recommended_products[0]
        else:
            return {"message": "No suitable product found for the specified use case."}

    except Exception as e:
        # Handle unexpected errors
        return {"error": str(e)}

# Define available plastic products
plastic_products = [
    {
        "name": "Tấm ốp phẳng Casary",
        "description": "Flat panel suitable for modern home office designs.",
        "use_cases": ["home office", "wall paneling", "decorative"],
        "material": "High-quality plastic",
    },
    {
        "name": "Tấm ốp đa năng CASARY",
        "description": "Versatile panel for various applications.",
        "use_cases": ["home office", "multi-purpose", "furniture"],
        "material": "Durable plastic",
    },
]

# Define the use case
use_case = "home office"

# Get the recommendation
recommendation = recommend_plastic_product(plastic_products, use_case)

# Print the recommendation in a readable format
print(json.dumps(recommendation, indent=4, ensure_ascii=False))
```
