"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marant.com.mx
Prompt: Write Python code to recommend Marant's "Gold Brightening Peel" for unifying skin texture and removing dead cells, based on its active ingredients and use case described on the website.
Generated: DETERMINISTIC_f28425a2b1ef3f19
Batch ID: 20250612_151428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import json

# Define the product recommendation function
def recommend_product(ingredients, use_case):
    """
    Recommend a skin-care product based on active ingredients and use case.

    Parameters:
        ingredients (list): A list of active ingredients desired.
        use_case (str): The intended use case for the product.

    Returns:
        str: Recommended product name or a message if no product matches.
    """
    try:
        # Product catalog (usually fetched from a database or API)
        products = [
            {
                "name": "Marant's Gold Brightening Peel",
                "active_ingredients": ["gold particles", "vitamin C", "salicylic acid"],
                "use_case": "unify skin texture and remove dead cells"
            },
            {
                "name": "Hydra Glow Serum",
                "active_ingredients": ["hyaluronic acid", "niacinamide"],
                "use_case": "hydrate and brighten skin"
            },
            {
                "name": "Deep Cleanse Exfoliator",
                "active_ingredients": ["charcoal", "glycolic acid"],
                "use_case": "deep cleansing and exfoliation"
            }
        ]

        # Search for a product that matches the ingredients and use case
        for product in products:
            if (
                all(ingredient in product["active_ingredients"] for ingredient in ingredients) and
                use_case.lower() in product["use_case"].lower()
            ):
                return f"We recommend: {product['name']}"

        # If no product matches the criteria
        return "Sorry, no product matches your criteria. Please try with different keywords."

    except Exception as e:
        # Handle unexpected errors gracefully
        return f"An error occurred: {str(e)}"

# Example usage
if __name__ == "__main__":
    # User preferences (this could come from user input in a real application)
    desired_ingredients = ["gold particles", "salicylic acid"]
    intended_use_case = "unify skin texture and remove dead cells"

    # Call the function and print the recommendation
    recommendation = recommend_product(desired_ingredients, intended_use_case)
    print(recommendation)
```
