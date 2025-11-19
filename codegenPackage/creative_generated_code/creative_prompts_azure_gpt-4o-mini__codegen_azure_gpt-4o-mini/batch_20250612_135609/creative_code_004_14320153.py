"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cartoansurperu.com
Prompt: Create a function that recommends the best type of adhesive tape for packaging based on the products available at Cartonerías Andinas del Sur.
Generated: DETERMINISTIC_14320153e4e3a16e
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TapeRecommendationError(Exception):
    """Custom exception for tape recommendation errors."""
    pass

def recommend_tape(product_type: str, weight: float, fragility: bool) -> str:
    """
    Recommend the best type of adhesive tape for packaging.

    Parameters:
    - product_type (str): The type of product being packaged (e.g., 'light', 'medium', 'heavy').
    - weight (float): The weight of the product in kilograms.
    - fragility (bool): Indicates whether the product is fragile.

    Returns:
    - str: Recommended type of tape.

    Raises:
    - TapeRecommendationError: If the input parameters are invalid.
    """
    
    # Validate input parameters
    if not isinstance(product_type, str) or not product_type:
        raise TapeRecommendationError("Invalid product type. Must be a non-empty string.")
    if not isinstance(weight, (int, float)) or weight <= 0:
        raise TapeRecommendationError("Invalid weight. Must be a positive number.")
    if not isinstance(fragility, bool):
        raise TapeRecommendationError("Fragility must be a boolean value.")

    # Recommendation logic based on product type and characteristics
    if weight <= 1.0:
        tape_type = "Light-duty tape"
    elif weight <= 5.0:
        tape_type = "Medium-duty tape"
    else:
        tape_type = "Heavy-duty tape"

    if fragility:
        tape_type += " with cushioning properties"

    # Final recommendation
    return f"For a {product_type} package weighing {weight}kg that is {'fragile' if fragility else 'not fragile'}, we recommend using {tape_type}."

# Example usage
if __name__ == "__main__":
    try:
        recommendation = recommend_tape("box", 2.5, True)
        print(recommendation)
    except TapeRecommendationError as e:
        print(f"Error: {e}")
```
