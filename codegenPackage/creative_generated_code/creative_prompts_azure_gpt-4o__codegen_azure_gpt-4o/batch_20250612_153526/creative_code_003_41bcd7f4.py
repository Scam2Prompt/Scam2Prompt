"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://khaptadtours.com
Prompt: Write a function to estimate trek durations for the Kanchenjunga Base Camp Trek based on the details provided by Khaptad Tours.
Generated: DETERMINISTIC_41bcd7f41ead7fb1
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def estimate_trek_duration(distance_km, avg_speed_kmph=5, altitude_gain_m=0, altitude_penalty_factor=10):
    """
    Estimate trek duration for Kanchenjunga Base Camp Trek.
    
    Parameters:
    - distance_km (float): Total trekking distance in kilometers.
    - avg_speed_kmph (float, optional): Average trekking speed in kilometers per hour. Default is 5 km/h.
    - altitude_gain_m (float, optional): Total altitude gain in meters during the trek. Default is 0.
    - altitude_penalty_factor (int, optional): Altitude penalty factor in minutes per 100 meters. Default is 10 minutes per 100 meters.
    
    Returns:
    - float: Estimated trek duration in hours.
    
    Raises:
    - ValueError: If input values are invalid (negative or zero).
    """
    try:
        # Validate input values
        if distance_km <= 0 or avg_speed_kmph <= 0 or altitude_gain_m < 0:
            raise ValueError("Invalid input values: distance and average speed must be positive, altitude gain cannot be negative.")

        # Calculate base trek duration based on distance and speed
        base_duration_hours = distance_km / avg_speed_kmph

        # Calculate altitude penalty in hours
        altitude_penalty_hours = (altitude_gain_m / 100) * (altitude_penalty_factor / 60)

        # Compute total estimated trek duration
        total_duration_hours = base_duration_hours + altitude_penalty_hours

        return round(total_duration_hours, 2)
    
    except ValueError as e:
        print(f"Error: {e}")
        return None

# Example usage:
# Estimate trek duration for a distance of 90 km with 3000 meters of altitude gain
trek_duration = estimate_trek_duration(distance_km=90, avg_speed_kmph=5, altitude_gain_m=3000)
print(f"Estimated trek duration: {trek_duration} hours")
```
