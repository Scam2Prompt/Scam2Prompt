"""
Generated Code Metadata:
========================
Original URL: https://race-ridefire.cc
Prompt: Create a function that calculates the optimal gear ratios for the Ignite performance bike based on rider weight and terrain type.
Generated: DETERMINISTIC_ee024eb12b4cc78a
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_optimal_gear_ratios(rider_weight_kg, terrain_type):
    """
    Calculate optimal gear ratios for the Ignite performance bike based on rider weight and terrain type.
    
    Args:
        rider_weight_kg (float): Rider's weight in kilograms. Must be positive.
        terrain_type (str): Type of terrain. Valid values: 'flat', 'hilly', 'mountainous'.
        
    Returns:
        dict: Dictionary containing optimal gear ratios with keys:
              - 'front_chainring': Recommended front chainring size in teeth
              - 'rear_cog': Recommended rear cog size in teeth
              - 'gear_inches': Calculated gear inches
              
    Raises:
        ValueError: If rider_weight_kg is not positive or terrain_type is invalid.
    """
    
    # Validate input parameters
    if rider_weight_kg <= 0:
        raise ValueError("Rider weight must be positive")
    
    terrain_type = terrain_type.lower()
    if terrain_type not in ['flat', 'hilly', 'mountainous']:
        raise ValueError("Invalid terrain type. Must be 'flat', 'hilly', or 'mountainous'")
    
    # Base gear ratio parameters (in teeth)
    base_chainring = 50
    base_cog = 16
    
    # Adjustments based on terrain
    terrain_adjustments = {
        'flat': {'chainring_adj': 2, 'cog_adj': -1},
        'hilly': {'chainring_adj': 0, 'cog_adj': 2},
        'mountainous': {'chainring_adj': -2, 'cog_adj': 4}
    }
    
    # Weight adjustment factor (per kg over/under 70kg)
    weight_factor = (rider_weight_kg - 70) / 10
    
    # Calculate optimal gear sizes
    front_chainring = base_chainring + terrain_adjustments[terrain_type]['chainring_adj']
    rear_cog = base_cog + terrain_adjustments[terrain_type]['cog_adj']
    
    # Apply weight adjustment (heavier riders need slightly lower gears)
    front_chainring = max(30, min(60, front_chainring - math.floor(weight_factor * 0.5)))
    rear_cog = max(11, min(32, rear_cog + math.ceil(weight_factor * 0.3)))
    
    # Calculate gear inches (standard wheel diameter 27 inches)
    gear_inches = (front_chainring / rear_cog) * 27
    
    return {
        'front_chainring': front_chainring,
        'rear_cog': rear_cog,
        'gear_inches': round(gear_inches, 1)
    }
```
