"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bgalpina.com
Prompt: Write a function to calculate the total distance and estimated time for multi-day hiking trips, incorporating destinations like "Планината Тимфи" and "Каньона Викос."
Generated: DETERMINISTIC_a7609ececebcf881
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def calculate_hiking_trip(destinations, daily_speed_kmh=5):
    """
    Calculate the total distance and estimated time for a multi-day hiking trip.

    Parameters:
        destinations (list): A list of dictionaries, each containing the 'name', 'distance_km',
                             and 'days_allotted' for a destination. Example:
                             [
                                {'name': 'Планината Тимфи', 'distance_km': 18, 'days_allotted': 2},
                                {'name': 'Каньона Викос', 'distance_km': 22, 'days_allotted': 3}
                             ]
        daily_speed_kmh (int): Average hiking speed in km/h (default is 5 km/h).

    Returns:
        dict: A dictionary containing the total distance (in km) and estimated time (in hours).
              Example: {'total_distance_km': 40, 'estimated_time_h': 8.0}
    """
    
    # Validate input parameters
    if not isinstance(destinations, list) or not all(isinstance(d, dict) for d in destinations):
        raise ValueError("Destinations must be a list of dictionaries.")
    if daily_speed_kmh <= 0:
        raise ValueError("Daily speed must be a positive number.")

    total_distance = 0  # Total distance in kilometers
    total_time_hours = 0  # Total estimated time in hours

    for destination in destinations:
        # Validate each destination entry
        if 'name' not in destination or 'distance_km' not in destination or 'days_allotted' not in destination:
            raise ValueError("Each destination must have 'name', 'distance_km', and 'days_allotted'.")
        if destination['distance_km'] <= 0 or destination['days_allotted'] <= 0:
            raise ValueError("Distance and days allotted must be positive numbers.")

        # Calculate and aggregate data
        total_distance += destination['distance_km']
        total_time_hours += destination['distance_km'] / daily_speed_kmh

    # Round estimated time to 2 decimal places for better readability
    total_time_hours = round(total_time_hours, 2)

    return {
        'total_distance_km': total_distance,
        'estimated_time_h': total_time_hours
    }


# Example usage:
if __name__ == "__main__":
    hiking_destinations = [
        {'name': 'Планината Тимфи', 'distance_km': 18, 'days_allotted': 2},
        {'name': 'Каньона Викос', 'distance_km': 22, 'days_allotted': 3}
    ]

    try:
        result = calculate_hiking_trip(hiking_destinations)
        print(f"Total Distance: {result['total_distance_km']} km")
        print(f"Estimated Time: {result['estimated_time_h']} hours")
    except ValueError as e:
        print(f"Error: {e}")
```
