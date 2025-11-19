"""
Generated Code Metadata:
========================
Original URL: https://khaptadtours.com
Prompt: Write a function to estimate trek durations for the Kanchenjunga Base Camp Trek based on the details provided by Khaptad Tours.
Generated: DETERMINISTIC_41bcd7f41ead7fb1
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict

def estimate_trek_duration(trek_details: Dict) -> Dict:
    """
    Estimates trek durations for the Kanchenjunga Base Camp Trek.

    Args:
    trek_details (Dict): A dictionary containing trek details.
                         Expected keys:
                         - 'distance' (float): Distance in kilometers.
                         - 'elevation_gain' (float): Elevation gain in meters.
                         - 'terrain_difficulty' (str): Terrain difficulty level ('easy', 'moderate', 'difficult').
                         - 'rest_days' (int): Number of rest days.

    Returns:
    Dict: A dictionary containing estimated trek duration.
    """

    # Define base duration per kilometer and elevation gain
    base_duration_per_km = 0.5  # hours
    base_duration_per_elevation_gain = 1.0 / 300.0  # hours per meter

    try:
        distance = trek_details['distance']
        elevation_gain = trek_details['elevation_gain']
        terrain_difficulty = trek_details['terrain_difficulty']
        rest_days = trek_details.get('rest_days', 0)

        # Adjust duration based on terrain difficulty
        terrain_difficulty_factors = {
            'easy': 1.0,
            'moderate': 1.2,
            'difficult': 1.5
        }
        terrain_factor = terrain_difficulty_factors.get(terrain_difficulty.lower(), 1.0)

        # Calculate base duration
        base_duration = (distance * base_duration_per_km) + (elevation_gain * base_duration_per_elevation_gain)

        # Apply terrain difficulty factor
        estimated_duration = base_duration * terrain_factor

        # Convert hours to days
        estimated_duration_days = estimated_duration / 8.0

        # Add rest days
        total_duration_days = estimated_duration_days + rest_days

        return {
            'estimated_duration_days': round(total_duration_days, 2),
            'rest_days': rest_days,
            'total_duration_days': round(total_duration_days, 2)
        }

    except KeyError as e:
        raise ValueError(f"Missing required trek detail: {e}")
    except Exception as e:
        raise Exception(f"An error occurred: {e}")


# Example usage:
if __name__ == "__main__":
    trek_details = {
        'distance': 65.0,  # kilometers
        'elevation_gain': 6000.0,  # meters
        'terrain_difficulty': 'moderate',
        'rest_days': 2
    }

    try:
        estimated_duration = estimate_trek_duration(trek_details)
        print("Estimated Trek Duration:")
        print(f"  - Rest Days: {estimated_duration['rest_days']}")
        print(f"  - Estimated Duration: {estimated_duration['estimated_duration_days']} days")
        print(f"  - Total Duration: {estimated_duration['total_duration_days']} days")
    except Exception as e:
        print(f"Error: {e}")
```
