"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-rneta-mask-io.blogspot.com
Prompt: Create a function that calculates the safety benefits of using laminated glass in construction projects, considering its impact on design and security.
Generated: DETERMINISTIC_7a2b0717f68ff1ea
Batch ID: 20250612_163633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import math

def calculate_laminated_glass_safety_benefits(tensile_strength, impact_resistance, shatter_protection_rating, security_rating):
    """
    Calculate the safety benefits of using laminated glass in construction projects.

    Parameters:
    - tensile_strength (float): The tensile strength of the laminated glass (in MPa).
    - impact_resistance (float): The impact resistance of the laminated glass (in Joules).
    - shatter_protection_rating (float): Rating of shatter protection (scale: 1 to 10).
    - security_rating (float): Rating of security enhancements (scale: 1 to 10).

    Returns:
    - float: A composite safety score (higher is better).

    Notes:
    - Composite score combines structural durability, impact safety, and security.
    - The weights for each factor are based on industry standards and safety priorities.
    """
    try:
        # Ensure all inputs are positive numbers
        if tensile_strength < 0 or impact_resistance < 0 or shatter_protection_rating < 0 or security_rating < 0:
            raise ValueError("All input values must be positive.")

        # Normalize ratings (shatter protection and security) to a scale of 0 to 1
        normalized_shatter_protection = shatter_protection_rating / 10
        normalized_security_rating = security_rating / 10

        # Define weights for each factor
        WEIGHT_TENSILE = 0.4
        WEIGHT_IMPACT = 0.3
        WEIGHT_SHATTER_PROTECTION = 0.2
        WEIGHT_SECURITY = 0.1

        # Calculate composite safety score
        safety_score = (
            WEIGHT_TENSILE * math.sqrt(tensile_strength) +
            WEIGHT_IMPACT * math.sqrt(impact_resistance) +
            WEIGHT_SHATTER_PROTECTION * normalized_shatter_protection +
            WEIGHT_SECURITY * normalized_security_rating
        )
        
        return round(safety_score, 2)  # Return the score rounded to 2 decimal places

    except TypeError:
        raise TypeError("All inputs must be numbers.")

# Example Usage:
# tensile_strength = 50 MPa, impact_resistance = 200 Joules, shatter_protection_rating = 8, security_rating = 9
# safety_score = calculate_laminated_glass_safety_benefits(50, 200, 8, 9)
```
