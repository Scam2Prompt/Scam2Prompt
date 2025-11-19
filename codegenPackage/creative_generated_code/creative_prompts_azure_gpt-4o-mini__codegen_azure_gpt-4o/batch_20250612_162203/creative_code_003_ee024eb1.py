"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://race-ridefire.cc
Prompt: Create a function that calculates the optimal gear ratios for the Ignite performance bike based on rider weight and terrain type.
Generated: DETERMINISTIC_ee024eb12b4cc78a
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def calculate_optimal_gear_ratios(rider_weight, terrain_type):
    """
    Calculate the optimal gear ratios for the Ignite performance bike based on rider weight and terrain type.

    Args:
        rider_weight (float): Weight of the rider in kilograms.
        terrain_type (str): Type of terrain. Accepted values: 'flat', 'hill', 'mountain'.

    Returns:
        dict: Dictionary containing recommended gear ratios for the bike.
    """
    
    # Validate input parameters
    if not isinstance(rider_weight, (int, float)) or rider_weight <= 0:
        raise ValueError("Rider weight must be a positive number.")
    if terrain_type not in ['flat', 'hill', 'mountain']:
        raise ValueError("Terrain type must be one of: 'flat', 'hill', 'mountain'.")

    # Gear ratio ranges
    gear_ratios = {
        'flat': (2.5, 3.5),  # High gear ratios for speed
        'hill': (1.8, 2.5),  # Medium gear ratios for moderate climbs
        'mountain': (1.2, 1.8)  # Low gear ratios for steep inclines
    }

    # Adjust gear ratios based on rider weight
    base_ratio_min, base_ratio_max = gear_ratios[terrain_type]
    weight_factor = math.log1p(rider_weight) / 10  # Logarithmic adjustment for rider weight

    adjusted_min_ratio = round(base_ratio_min + weight_factor, 2)
    adjusted_max_ratio = round(base_ratio_max + weight_factor, 2)

    # Ensure ratios stay within reasonable bounds
    adjusted_min_ratio = max(adjusted_min_ratio, 0.5)  # Minimum gear ratio
    adjusted_max_ratio = min(adjusted_max_ratio, 5.0)  # Maximum gear ratio

    return {
        'terrain': terrain_type,
        'adjusted_min_ratio': adjusted_min_ratio,
        'adjusted_max_ratio': adjusted_max_ratio
    }

# Example usage (uncomment to test):
# try:
#     print(calculate_optimal_gear_ratios(rider_weight=75, terrain_type='hill'))
# except ValueError as e:
#     print(f"Error: {e}")
```
