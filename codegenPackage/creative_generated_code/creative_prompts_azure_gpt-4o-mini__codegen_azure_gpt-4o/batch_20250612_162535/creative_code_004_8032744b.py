"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stellarcropgame.fun
Prompt: Write a function that calculates the optimal crop selection based on environmental conditions, similar to the gameplay mechanics in Stellar Crop's live ecosystem system.
Generated: DETERMINISTIC_8032744b57957cbb
Batch ID: 20250612_162535
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for debugging and error reporting
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class CropSelectionError(Exception):
    """Custom exception for errors in crop selection."""
    pass


def calculate_optimal_crop(environment_conditions, crop_data):
    """
    Calculate the optimal crop selection based on environmental conditions.

    Args:
        environment_conditions (dict): A dictionary containing environmental factors such as:
            {
                "temperature": float,   # Average temperature in Celsius
                "rainfall": float,      # Average rainfall in mm
                "soil_type": str,       # Soil type (e.g., 'sandy', 'clay', 'loam')
                "sunlight_hours": int   # Average daily sunlight hours
            }
        crop_data (list): A list of dictionaries containing crop information such as:
            [
                {
                    "name": str,               # Name of the crop
                    "preferred_conditions": { # Preferred environmental conditions
                        "temperature_range": (min_temp, max_temp),  # Temperature range in Celsius
                        "rainfall_range": (min_rainfall, max_rainfall),  # Rainfall range in mm
                        "soil_types": [soil_type1, soil_type2],  # Compatible soil types
                        "sunlight_hours_range": (min_hours, max_hours)   # Sunlight hours range
                    }
                },
                ...
            ]

    Returns:
        str: The name of the optimal crop.

    Raises:
        CropSelectionError: If no suitable crop is found for the given conditions.
    """
    try:
        optimal_crop = None
        highest_match_score = -1

        # Iterate through each crop and evaluate its compatibility with the environment conditions
        for crop in crop_data:
            match_score = 0
            preferences = crop['preferred_conditions']

            # Check temperature compatibility
            if preferences["temperature_range"][0] <= environment_conditions["temperature"] <= preferences["temperature_range"][1]:
                match_score += 1

            # Check rainfall compatibility
            if preferences["rainfall_range"][0] <= environment_conditions["rainfall"] <= preferences["rainfall_range"][1]:
                match_score += 1

            # Check soil type compatibility
            if environment_conditions["soil_type"] in preferences["soil_types"]:
                match_score += 1

            # Check sunlight hours compatibility
            if preferences["sunlight_hours_range"][0] <= environment_conditions["sunlight_hours"] <= preferences["sunlight_hours_range"][1]:
                match_score += 1

            # Update the optimal crop based on match score
            if match_score > highest_match_score:
                highest_match_score = match_score
                optimal_crop = crop['name']

        # Ensure a suitable crop was found
        if optimal_crop is None:
            raise CropSelectionError("No suitable crop found for the given environmental conditions.")

        logging.info(f"Optimal crop selected: {optimal_crop}")
        return optimal_crop

    except Exception as e:
        logging.error(f"Error occurred during crop selection: {e}")
        raise


# Example usage
if __name__ == "__main__":
    # Sample environmental conditions
    environment_conditions = {
        "temperature": 25.5,  # Celsius
        "rainfall": 1200,     # mm
        "soil_type": "loam",  # Soil type
        "sunlight_hours": 8   # Hours
    }

    # Sample crop data
    crop_data = [
        {
            "name": "Wheat",
            "preferred_conditions": {
                "temperature_range": (20, 30),
                "rainfall_range": (1000, 1500),
                "soil_types": ["loam", "clay"],
                "sunlight_hours_range": (6, 10)
            }
        },
        {
            "name": "Corn",
            "preferred_conditions": {
                "temperature_range": (25, 35),
                "rainfall_range": (800, 1200),
                "soil_types": ["sandy", "loam"],
                "sunlight_hours_range": (7, 12)
            }
        },
        {
            "name": "Rice",
            "preferred_conditions": {
                "temperature_range": (22, 32),
                "rainfall_range": (1500, 2000),
                "soil_types": ["clay"],
                "sunlight_hours_range": (5, 8)
            }
        }
    ]

    try:
        optimal_crop = calculate_optimal_crop(environment_conditions, crop_data)
        print(f"The optimal crop for the given conditions is: {optimal_crop}")
    except CropSelectionError as e:
        print(f"Error: {e}")
```
