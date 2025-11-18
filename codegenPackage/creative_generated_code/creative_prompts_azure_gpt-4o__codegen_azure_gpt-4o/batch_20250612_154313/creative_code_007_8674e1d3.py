"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://syncconnects.com
Prompt: Write a function to filter and display nearby meetup locations for members of a platform like Sync Connects, using geolocation data.
Generated: DETERMINISTIC_8674e1d3a20f871f
Batch ID: 20250612_154313
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def haversine_distance(lat1, lon1, lat2, lon2):
    """
    Calculate the great-circle distance between two points on the Earth using the Haversine formula.
    
    Parameters:
        lat1 (float): Latitude of the first location.
        lon1 (float): Longitude of the first location.
        lat2 (float): Latitude of the second location.
        lon2 (float): Longitude of the second location.

    Returns:
        float: Distance between the two points in kilometers.
    """
    R = 6371  # Radius of the Earth in kilometers
    # Convert latitude and longitude from degrees to radians
    lat1_rad, lon1_rad, lat2_rad, lon2_rad = map(math.radians, [lat1, lon1, lat2, lon2])
    
    # Haversine formula
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c


def filter_nearby_meetups(user_location, meetups, max_distance_km):
    """
    Filter and display nearby meetup locations based on the user's location and a maximum distance.

    Parameters:
        user_location (dict): A dictionary containing 'latitude' and 'longitude' of the user.
        meetups (list): A list of dictionaries, each containing 'name', 'latitude', and 'longitude' of meetup locations.
        max_distance_km (float): Maximum distance in kilometers to filter meetups.

    Returns:
        list: Filtered meetups within the specified maximum distance.
    """
    try:
        # Validate input data
        if not all(key in user_location for key in ['latitude', 'longitude']):
            raise ValueError("User location must contain 'latitude' and 'longitude'.")
        for meetup in meetups:
            if not all(key in meetup for key in ['name', 'latitude', 'longitude']):
                raise ValueError("Each meetup must contain 'name', 'latitude', and 'longitude'.")
        
        # Calculate the nearby meetups
        nearby_meetups = []
        for meetup in meetups:
            distance = haversine_distance(user_location['latitude'], user_location['longitude'], 
                                          meetup['latitude'], meetup['longitude'])
            if distance <= max_distance_km:
                nearby_meetups.append({
                    'name': meetup['name'],
                    'distance_km': round(distance, 2)  # Round distance for better readability
                })
        
        # Sort meetups by distance (nearest first)
        nearby_meetups.sort(key=lambda x: x['distance_km'])
        return nearby_meetups
    except Exception as e:
        print(f"Error: {e}")
        return []


# Example usage
if __name__ == "__main__":
    # User's location
    user_location = {'latitude': 37.7749, 'longitude': -122.4194}  # San Francisco, CA
    
    # List of meetup locations
    meetups = [
        {'name': 'Tech Enthusiasts Meetup', 'latitude': 37.7749, 'longitude': -122.4312},  # Nearby in SF
        {'name': 'AI Innovators Forum', 'latitude': 37.8044, 'longitude': -122.2711},  # Oakland, CA
        {'name': 'Game Developers Hangout', 'latitude': 34.0522, 'longitude': -118.2437},  # Los Angeles, CA
    ]
    
    # Maximum distance in kilometers
    max_distance_km = 50
    
    # Filter and display nearby meetups
    nearby_meetups = filter_nearby_meetups(user_location, meetups, max_distance_km)
    print("Nearby Meetups:")
    for meetup in nearby_meetups:
        print(f"{meetup['name']} - {meetup['distance_km']} km away")
```
