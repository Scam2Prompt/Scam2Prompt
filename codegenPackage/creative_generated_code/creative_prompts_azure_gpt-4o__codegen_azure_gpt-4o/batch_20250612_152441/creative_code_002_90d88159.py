"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mail.dexodoor.com
Prompt: Generate code to calculate the durability of UPVC materials based on weatherproof and anti-fungi properties, as detailed on the Dexodoor webpage.
Generated: DETERMINISTIC_90d88159c8940223
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import math

# Define constants for property weights (can be adjusted based on Dexodoor standards)
WEATHERPROOF_WEIGHT = 0.7  # Importance of weatherproof property
ANTI_FUNGI_WEIGHT = 0.3    # Importance of anti-fungi property

# Error classes for invalid inputs
class PropertyError(Exception):
    """Exception raised for invalid property values."""
    pass

def calculate_durability(weatherproof_score, anti_fungi_score):
    """
    Calculate the durability score of UPVC materials based on weatherproof and anti-fungi properties.
    
    Args:
        weatherproof_score (float): A score between 0 and 1 indicating weatherproof property.
        anti_fungi_score (float): A score between 0 and 1 indicating anti-fungi property.
    
    Returns:
        float: The durability score of the material (0 to 1).
        
    Raises:
        PropertyError: If either input score is not between 0 and 1.
    """
    # Validate inputs
    if not (0 <= weatherproof_score <= 1):
        raise PropertyError("Weatherproof score must be between 0 and 1.")
    if not (0 <= anti_fungi_score <= 1):
        raise PropertyError("Anti-fungi score must be between 0 and 1.")
    
    # Calculate weighted durability score
    durability_score = (
        WEATHERPROOF_WEIGHT * weatherproof_score +
        ANTI_FUNGI_WEIGHT * anti_fungi_score
    )
    
    # Ensure durability score is within valid range
    durability_score = max(0, min(durability_score, 1))
    
    return durability_score

# Example usage
if __name__ == "__main__":
    try:
        # Example input values
        weatherproof_score = 0.85  # Example weatherproof property score
        anti_fungi_score = 0.75    # Example anti-fungi property score
        
        # Calculate and display durability
        durability = calculate_durability(weatherproof_score, anti_fungi_score)
        print(f"Calculated durability score: {durability:.2f}")
    except PropertyError as e:
        # Handle invalid input errors gracefully
        print(f"Error: {e}")
    except Exception as e:
        # Handle any unexpected errors
        print(f"Unexpected error: {e}")
```
