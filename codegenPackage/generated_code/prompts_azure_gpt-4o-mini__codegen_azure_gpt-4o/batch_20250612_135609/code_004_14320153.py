"""
Generated Code Metadata:
========================
Original URL: https://cartoansurperu.com
Prompt: Create a function that recommends the best type of adhesive tape for packaging based on the products available at Cartonerías Andinas del Sur.
Generated: DETERMINISTIC_14320153e4e3a16e
Batch ID: 20250612_135609
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

# Define a function to recommend the best adhesive tape for packaging
def recommend_tape(product_type: str, weight: float, environment: str) -> str:
    """
    Recommends the best type of adhesive tape for packaging based on product type, weight, and environment.

    Args:
        product_type (str): Type of product being packaged (e.g., "fragile", "heavy", "standard").
        weight (float): Weight of the product in kilograms.
        environment (str): Packaging environment (e.g., "cold", "humid", "dry").

    Returns:
        str: Recommended adhesive tape type.
    """
    # Define available tape options
    tape_options: Dict[str, str] = {
        "fragile": "Transparent Acrylic Tape",
        "heavy": "Reinforced Fiberglass Tape",
        "standard": "Polypropylene Packing Tape",
        "cold": "Cold-Resistant Tape",
        "humid": "Waterproof Tape",
        "dry": "General Purpose Tape"
    }

    # Error handling for invalid inputs
    if not isinstance(product_type, str) or not isinstance(environment, str):
        raise ValueError("Product type and environment must be strings.")
    if not isinstance(weight, (int, float)) or weight < 0:
        raise ValueError("Weight must be a positive number.")

    # Determine tape recommendation based on product type and weight
    if product_type.lower() == "fragile":
        return tape_options["fragile"]
    elif product_type.lower() == "heavy" and weight > 10:  # Heavy products over 10kg
        return tape_options["heavy"]
    elif product_type.lower() == "standard":
        return tape_options["standard"]
    else:
        # Adjust recommendation based on environment
        if environment.lower() == "cold":
            return tape_options["cold"]
        elif environment.lower() == "humid":
            return tape_options["humid"]
        elif environment.lower() == "dry":
            return tape_options["dry"]
        else:
            raise ValueError("Invalid environment specified.")

# Example usage
if __name__ == "__main__":
    try:
        # Test the function with sample inputs
        product_type = "fragile"
        weight = 5.0
        environment = "dry"
        recommendation = recommend_tape(product_type, weight, environment)
        print(f"Recommended tape: {recommendation}")
    except ValueError as e:
        print(f"Error: {e}")
```
