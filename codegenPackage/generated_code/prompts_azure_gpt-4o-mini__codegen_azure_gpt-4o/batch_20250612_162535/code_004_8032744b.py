"""
Generated Code Metadata:
========================
Original URL: https://stellarcropgame.fun
Prompt: Write a function that calculates the optimal crop selection based on environmental conditions, similar to the gameplay mechanics in Stellar Crop's live ecosystem system.
Generated: DETERMINISTIC_8032744b57957cbb
Batch ID: 20250612_162535
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_optimal_crop(environmental_conditions):
    """
    Calculate the optimal crop selection based on environmental conditions.

    Parameters:
        environmental_conditions (dict): A dictionary containing environmental data.
            Example:
            {
                "temperature": float,  # Average temperature in Celsius
                "humidity": float,     # Humidity percentage (0-100)
                "soil_quality": float, # Soil quality score (0-10)
                "rainfall": float,     # Average rainfall in mm
                "sunlight_hours": float # Average daily sunlight hours
            }

    Returns:
        str: The name of the optimal crop to plant.
    """
    # Define crop suitability thresholds
    crop_data = [
        {
            "name": "Wheat",
            "temperature_range": (10, 25),
            "humidity_range": (40, 60),
            "soil_quality_min": 5,
            "rainfall_range": (300, 600),
            "sunlight_hours_min": 6
        },
        {
            "name": "Corn",
            "temperature_range": (15, 30),
            "humidity_range": (50, 70),
            "soil_quality_min": 6,
            "rainfall_range": (400, 800),
            "sunlight_hours_min": 8
        },
        {
            "name": "Rice",
            "temperature_range": (20, 35),
            "humidity_range": (70, 90),
            "soil_quality_min": 4,
            "rainfall_range": (1000, 2000),
            "sunlight_hours_min": 4
        },
        {
            "name": "Potatoes",
            "temperature_range": (5, 20),
            "humidity_range": (30, 50),
            "soil_quality_min": 7,
            "rainfall_range": (200, 500),
            "sunlight_hours_min": 5
        }
    ]

    # Extract environmental conditions
    try:
        temperature = environmental_conditions["temperature"]
        humidity = environmental_conditions["humidity"]
        soil_quality = environmental_conditions["soil_quality"]
        rainfall = environmental_conditions["rainfall"]
        sunlight_hours = environmental_conditions["sunlight_hours"]
    except KeyError as e:
        raise ValueError(f"Missing environmental condition: {e}")

    # Validate environmental conditions
    if not (0 <= humidity <= 100):
        raise ValueError("Humidity must be between 0 and 100.")
    if not (0 <= soil_quality <= 10):
        raise ValueError("Soil quality must be between 0 and 10.")
    if temperature < -50 or temperature > 50:
        raise ValueError("Temperature must be within a realistic range (-50 to 50 Celsius).")

    # Determine the optimal crop
    optimal_crop = None
    highest_score = -math.inf

    for crop in crop_data:
        # Check if environmental conditions match crop requirements
        if (crop["temperature_range"][0] <= temperature <= crop["temperature_range"][1] and
            crop["humidity_range"][0] <= humidity <= crop["humidity_range"][1] and
            soil_quality >= crop["soil_quality_min"] and
            crop["rainfall_range"][0] <= rainfall <= crop["rainfall_range"][1] and
            sunlight_hours >= crop["sunlight_hours_min"]):
            
            # Calculate a suitability score (example: weighted sum of conditions)
            score = (
                (temperature - crop["temperature_range"][0]) / (crop["temperature_range"][1] - crop["temperature_range"][0]) +
                (humidity - crop["humidity_range"][0]) / (crop["humidity_range"][1] - crop["humidity_range"][0]) +
                soil_quality / 10 +
                (rainfall - crop["rainfall_range"][0]) / (crop["rainfall_range"][1] - crop["rainfall_range"][0]) +
                sunlight_hours / 12
            )

            # Update optimal crop if this crop has a higher score
            if score > highest_score:
                highest_score = score
                optimal_crop = crop["name"]

    if optimal_crop is None:
        raise ValueError("No suitable crop found for the given environmental conditions.")

    return optimal_crop


# Example usage:
if __name__ == "__main__":
    # Example environmental conditions
    conditions = {
        "temperature": 22,
        "humidity": 65,
        "soil_quality": 6,
        "rainfall": 500,
        "sunlight_hours": 7
    }

    try:
        crop = calculate_optimal_crop(conditions)
        print(f"The optimal crop to plant is: {crop}")
    except ValueError as e:
        print(f"Error: {e}")
```
