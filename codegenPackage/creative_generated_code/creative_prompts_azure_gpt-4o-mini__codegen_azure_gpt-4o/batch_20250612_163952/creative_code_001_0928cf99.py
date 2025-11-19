"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eagle-tex.cn
Prompt: Write a Python function that calculates the optimal fabric type for sportswear based on user-defined parameters like stretchability and weight.
Generated: DETERMINISTIC_0928cf991b9f2750
Batch ID: 20250612_163952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary module for handling potential exceptions
from typing import Dict, Optional

def optimal_fabric_type(stretchability: float, weight: float) -> Optional[str]:
    """
    Determines the optimal fabric type for sportswear based on stretchability and weight.

    Parameters:
        stretchability (float): A value between 0 and 1 representing the fabric's stretchability.
                                Higher values indicate more stretch.
        weight (float): The fabric weight in grams per square meter (gsm).

    Returns:
        str: The recommended fabric type for sportswear.
             Returns None if values are out of range or a fabric cannot be determined.

    Raises:
        ValueError: If stretchability is not between 0 and 1, or if weight is negative.
    """
    # Validate input parameters
    if not (0 <= stretchability <= 1):
        raise ValueError("Stretchability must be between 0 and 1.")
    if weight < 0:
        raise ValueError("Weight must be a non-negative value.")

    # Define fabric types with their corresponding attributes
    # Key: Fabric type, Value: Dictionary of fabric attributes
    fabric_types = {
        "Polyester-Spandex Blend": {"stretchability": 0.8, "weight_range": (150, 250)},
        "Nylon": {"stretchability": 0.6, "weight_range": (100, 200)},
        "Cotton": {"stretchability": 0.4, "weight_range": (200, 300)},
        "Bamboo": {"stretchability": 0.5, "weight_range": (150, 250)},
    }

    # Iterate through the fabric types to find the optimal match
    for fabric, attributes in fabric_types.items():
        fabric_stretchability = attributes["stretchability"]
        min_weight, max_weight = attributes["weight_range"]

        # Check if the fabric matches the user-defined parameters
        if stretchability >= fabric_stretchability and min_weight <= weight <= max_weight:
            return fabric

    # Return None if no suitable fabric type is found
    return None

# Example usage:
try:
    # User-defined parameters
    result = optimal_fabric_type(stretchability=0.7, weight=180)
    print(f"Optimal Fabric Type: {result if result else 'No suitable fabric found.'}")
except ValueError as e:
    print(f"Error: {e}")
```
