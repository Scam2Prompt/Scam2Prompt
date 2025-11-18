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
import geopy.distance

class MeetupLocation:
    """Class representing a Meetup location with name and coordinates."""
    
    def __init__(self, name, latitude, longitude):
        """
        Initialize a MeetupLocation instance.
        
        :param name: Name of the meetup location
        :param latitude: Latitude of the location
        :param longitude: Longitude of the location
        """
        self.name = name
        self.coordinates = (latitude, longitude)

def filter_nearby_meetups(meetup_locations, user_location, max_distance_km):
    """
    Filter meetup locations that are within a specific distance from the user's location.
    
    :param meetup_locations: List of MeetupLocation instances
    :param user_location: Tuple containing user's latitude and longitude
    :param max_distance_km: Maximum distance in kilometers to filter the meetups
    :return: List of nearby MeetupLocation instances
    """
    nearby_meetups = []
    
    try:
        for meetup in meetup_locations:
            # Calculate the distance from user location to meetup location
            distance = geopy.distance.distance(user_location, meetup.coordinates).kilometers
            
            # Check if the distance is within the allowed maximum distance
            if distance <= max_distance_km:
                nearby_meetups.append(meetup)
    
    except Exception as e:
        # Log the error (in production, replace with proper logging)
        print(f"An error occurred during filtering: {e}")

    return nearby_meetups

def display_meetups(meetups):
    """
    Display the list of meetup locations.
    
    :param meetups: List of MeetupLocation instances to display
    """
    if not meetups:
        print("No nearby meetups found.")
    else:
        print("Nearby Meetups:")
        for meetup in meetups:
            print(f"- {meetup.name} at coordinates {meetup.coordinates}")

# Example usage
if __name__ == "__main__":
    user_location = (40.7128, -74.0060)  # Example: New York City coordinates
    meetup_locations = [
        MeetupLocation("Tech Talk", 40.730610, -73.935242),  # Example location
        MeetupLocation("Art Workshop", 40.650002, -73.949997),  # Example location
        MeetupLocation("Networking Event", 40.7580, -73.9855)  # Example location
    ]
    
    max_distance_km = 10  # Example: 10 km radius
    nearby_meetups = filter_nearby_meetups(meetup_locations, user_location, max_distance_km)
    display_meetups(nearby_meetups)
```
