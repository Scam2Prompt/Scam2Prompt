"""
Generated Code Metadata:
========================
Original URL: https://zentocosmetic.com
Prompt: Develop a function that calculates the optimal hair care routine using Zento's products for damaged hair, incorporating their unique features like exotic oils and botanical extracts.
Generated: DETERMINISTIC_6c27975b13c99bb2
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
from typing import List, Dict

# Define a function to calculate the optimal hair care routine
def calculate_optimal_hair_care_routine(hair_condition: str, zento_products: List[Dict[str, str]]) -> List[str]:
    """
    Calculate the optimal hair care routine using Zento's products for damaged hair.

    Parameters:
        hair_condition (str): The condition of the hair (e.g., "damaged", "dry", "oily").
        zento_products (List[Dict[str, str]]): A list of Zento's products, where each product is represented
                                               as a dictionary with keys 'name', 'features', and 'usage'.

    Returns:
        List[str]: A list of product names in the recommended order of use for the optimal routine.
    """
    # Validate input
    if not isinstance(hair_condition, str) or not isinstance(zento_products, list):
        raise ValueError("Invalid input: 'hair_condition' must be a string and 'zento_products' must be a list.")

    # Filter products based on hair condition and features
    recommended_products = [
        product for product in zento_products
        if hair_condition.lower() in product['features'].lower()
    ]

    # Sort products based on their recommended usage order
    # Assuming 'usage' contains values like "pre-wash", "shampoo", "conditioner", "leave-in"
    usage_order = ["pre-wash", "shampoo", "conditioner", "leave-in"]
    recommended_products.sort(key=lambda p: usage_order.index(p['usage']))

    # Extract product names in the recommended order
    optimal_routine = [product['name'] for product in recommended_products]

    return optimal_routine


# Example usage
if __name__ == "__main__":
    # Define Zento's product catalog
    zento_products = [
        {"name": "Exotic Oil Pre-Wash", "features": "damaged, exotic oils", "usage": "pre-wash"},
        {"name": "Botanical Repair Shampoo", "features": "damaged, botanical extracts", "usage": "shampoo"},
        {"name": "Deep Conditioning Mask", "features": "damaged, hydration", "usage": "conditioner"},
        {"name": "Leave-In Strengthener", "features": "damaged, strengthening", "usage": "leave-in"},
    ]

    # Calculate the optimal routine for damaged hair
    try:
        routine = calculate_optimal_hair_care_routine("damaged", zento_products)
        print("Optimal Hair Care Routine:", routine)
    except ValueError as e:
        print("Error:", e)
```
