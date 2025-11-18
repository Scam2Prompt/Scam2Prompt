"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aprisacv.com.mx
Prompt: Create a Python function that selects the most suitable Aprisacv refractory product (e.g., Ancla Cerámica Aprick) for a furnace wall based on its alumina content and intended use.
Generated: DETERMINISTIC_ea6e1953039d4392
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import List, Dict, Optional


# Define a class to represent a refractory product
class RefractoryProduct:
    def __init__(self, name: str, alumina_content: float, suitable_uses: List[str]):
        """Initialize a refractory product with its attributes."""
        self.name = name
        self.alumina_content = alumina_content
        self.suitable_uses = suitable_uses


# Define the function to select the most suitable refractory product
def select_refractory_product(
    alumina_content: float, intended_use: str, products: List[RefractoryProduct]
) -> Optional[Dict[str, str]]:
    """
    Select the most suitable refractory product based on alumina content and intended use.

    :param alumina_content: The required alumina content for the furnace wall (percentage).
    :param intended_use: The intended use of the refractory product (e.g., 'high-temperature').
    :param products: A list of available refractory products.
    :return: A dictionary with product details if a suitable product is found, else None.
    """
    try:
        # Filter products based on alumina content and intended use
        suitable_products = [
            product
            for product in products
            if product.alumina_content >= alumina_content
            and intended_use.lower() in map(str.lower, product.suitable_uses)
        ]

        # If no suitable product is found, return None
        if not suitable_products:
            return None

        # Select the product with the closest alumina content to the requirement
        selected_product = min(
            suitable_products, key=lambda p: abs(p.alumina_content - alumina_content)
        )

        # Return the selected product details as a dictionary
        return {
            "name": selected_product.name,
            "alumina_content": f"{selected_product.alumina_content}%",
            "suitable_uses": ", ".join(selected_product.suitable_uses),
        }

    except Exception as e:
        # Handle any unexpected errors gracefully
        print(f"An error occurred: {e}")
        return None


# Example usage
if __name__ == "__main__":
    # Define some example refractory products
    product_list = [
        RefractoryProduct("Ancla Cerámica Aprick", 85.0, ["high-temperature", "abrasion"]),
        RefractoryProduct("Aprisacv ProMax", 70.0, ["medium-temperature", "corrosion"]),
        RefractoryProduct("Aprisacv UltraShield", 92.0, ["high-temperature", "thermal-shock"]),
    ]

    # Example inputs
    required_alumina_content = 80.0
    intended_furnace_use = "high-temperature"

    # Find the most suitable product
    result = select_refractory_product(required_alumina_content, intended_furnace_use, product_list)

    # Print the result
    if result:
        print("Selected Product Details:")
        for key, value in result.items():
            print(f"{key.capitalize()}: {value}")
    else:
        print("No suitable product found.")
```
