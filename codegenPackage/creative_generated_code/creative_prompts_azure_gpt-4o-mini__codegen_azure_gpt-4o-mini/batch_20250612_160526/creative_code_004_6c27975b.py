"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zentocosmetic.com
Prompt: Develop a function that calculates the optimal hair care routine using Zento's products for damaged hair, incorporating their unique features like exotic oils and botanical extracts.
Generated: DETERMINISTIC_6c27975b13c99bb2
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class HairCareProduct:
    """Represents a hair care product."""

    def __init__(self, name, type_of_product, features):
        """
        Initialize a new HairCareProduct.

        Args:
            name (str): The name of the product.
            type_of_product (str): The type of product (e.g., shampoo, conditioner).
            features (list): Unique features of the hair care product.
        """
        self.name = name
        self.type_of_product = type_of_product
        self.features = features

    def __repr__(self):
        return f"{self.name} ({self.type_of_product})"


def calculate_optimal_routine(damaged_hair_products):
    """
    Calculate the optimal hair care routine for damaged hair.

    Args:
        damaged_hair_products (list): A list of HairCareProduct instances.

    Returns:
        list: A recommended routine in the order of application.

    Raises:
        ValueError: If the input list is empty or contains non-HairCareProduct instances.
    """
    if not damaged_hair_products:
        raise ValueError("The product list cannot be empty.")

    if not all(isinstance(product, HairCareProduct) for product in damaged_hair_products):
        raise ValueError("All items in the product list must be instances of HairCareProduct.")

    routine = []

    # Prioritize products with exotic oils and botanical extracts
    for product in damaged_hair_products:
        if 'exotic oils' in product.features or 'botanical extracts' in product.features:
            routine.append(product)

    # Sort products to create a recommended routine
    routine.sort(key=lambda x: x.type_of_product)

    # Ensure the routine covers all necessary steps
    if not routine:
        raise ValueError("No suitable products found for the optimal routine.")

    return routine


if __name__ == "__main__":
    # Example usage
    try:
        products = [
            HairCareProduct("Moisturizing Shampoo", "shampoo", ["exotic oils"]),
            HairCareProduct("Deep Conditioner", "conditioner", ["botanical extracts"]),
            HairCareProduct("Leave-in Treatment", "treatment", ["exotic oils", "botanical extracts"]),
            HairCareProduct("Hair Serum", "serum", [])
        ]

        optimal_routine = calculate_optimal_routine(products)

        print("Optimal Hair Care Routine:")
        for product in optimal_routine:
            print(product)

    except ValueError as e:
        print(f"Error: {e}")
```
