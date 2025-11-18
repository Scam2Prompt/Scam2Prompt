"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bgalpina.com
Prompt: Write code to calculate the estimated difficulty level of hiking trails based on elevation gain and terrain type for locations such as "Планината Агиос Павлос" and "Каз Dağı."
Generated: DETERMINISTIC_87e26319bb0fdcb9
Batch ID: 20250612_153224
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

# Define a function to calculate hiking difficulty level
def calculate_hiking_difficulty(elevation_gain, terrain_type):
    """
    Calculate the estimated difficulty level of hiking trails based on elevation gain and terrain type.

    Parameters:
        elevation_gain (float): Elevation gain in meters (must be positive).
        terrain_type (str): Terrain type - options are 'easy', 'moderate', 'difficult'.

    Returns:
        str: Difficulty level of the hiking trail ('Easy', 'Moderate', 'Hard', 'Extreme').

    Raises:
        ValueError: If elevation_gain is negative or terrain_type is invalid.
    """
    
    # Validate input parameters
    if elevation_gain < 0:
        raise ValueError("Elevation gain must be a non-negative number.")
    if terrain_type not in ['easy', 'moderate', 'difficult']:
        raise ValueError("Invalid terrain type. Valid options are: 'easy', 'moderate', 'difficult'.")

    # Base score for elevation gain (higher elevation gain increases difficulty)
    if elevation_gain < 300:
        elevation_score = 1
    elif elevation_gain < 800:
        elevation_score = 2
    elif elevation_gain < 1500:
        elevation_score = 3
    else:
        elevation_score = 4

    # Terrain difficulty adjustment (modifies base score)
    terrain_multiplier = {
        'easy': 1.0,       # No additional difficulty for easy terrain
        'moderate': 1.5,   # Moderate terrain adds significant difficulty
        'difficult': 2.0   # Difficult terrain doubles the difficulty
    }

    # Calculate final difficulty score
    final_score = elevation_score * terrain_multiplier[terrain_type]

    # Map final score to difficulty level
    if final_score <= 2:
        difficulty_level = "Easy"
    elif final_score <= 4:
        difficulty_level = "Moderate"
    elif final_score <= 6:
        difficulty_level = "Hard"
    else:
        difficulty_level = "Extreme"

    return difficulty_level

# Example usage:
# Define hiking trails
hiking_trails = [
    {"name": "Планината Агиос Павлос", "elevation_gain": 900, "terrain_type": "moderate"},
    {"name": "Каз Dağı", "elevation_gain": 1200, "terrain_type": "difficult"}
]

# Calculate difficulty levels for each trail
for trail in hiking_trails:
    try:
        difficulty = calculate_hiking_difficulty(trail["elevation_gain"], trail["terrain_type"])
        print(f"The difficulty level of '{trail['name']}' is: {difficulty}")
    except ValueError as e:
        print(f"Error calculating difficulty for '{trail['name']}': {e}")
```
