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
# Function to recommend the best type of adhesive tape for packaging
# based on the product characteristics.

def recommend_adhesive_tape(packaging_type, weight, fragility_level):
    """
    Recommend the best type of adhesive tape for packaging based on input criteria.

    Args:
        packaging_type (str): The type of packaging (e.g., "box", "bag", "envelope").
        weight (float): The weight of the package in kilograms.
        fragility_level (str): Level of fragility ("low", "medium", "high").

    Returns:
        str: Recommended adhesive tape type.
    """

    # Validating inputs
    if not isinstance(packaging_type, str):
        raise ValueError("packaging_type must be a string.")
    if not isinstance(weight, (int, float)) or weight < 0:
        raise ValueError("weight must be a positive number.")
    if fragility_level not in ["low", "medium", "high"]:
        raise ValueError("fragility_level must be one of 'low', 'medium', 'high'.")

    # Define tape recommendations based on criteria
    if packaging_type.lower() == "box":
        if fragility_level == "high" or weight > 5:
            return "Heavy-Duty Packing Tape"
        elif fragility_level == "medium" or weight > 2:
            return "Standard Packing Tape"
        else:
            return "Light-Duty Packing Tape"
    elif packaging_type.lower() == "bag":
        if fragility_level == "high":
            return "Reinforced Adhesive Tape"
        else:
            return "General Purpose Tape"
    elif packaging_type.lower() == "envelope":
        if weight > 1 or fragility_level == "high":
            return "Seal-and-Secure Tape"
        else:
            return "Light Adhesive Tape"
    else:
        # Default case if packaging type is unknown
        return "Multipurpose Adhesive Tape"

# Example usage
if __name__ == "__main__":
    try:
        # Inputs for the function
        packaging_type = "box"
        weight = 3.5
        fragility_level = "medium"

        # Call the function and print the result
        recommendation = recommend_adhesive_tape(packaging_type, weight, fragility_level)
        print(f"Recommended tape: {recommendation}")
    except ValueError as e:
        # Handle input validation errors
        print(f"Error: {e}")
```
