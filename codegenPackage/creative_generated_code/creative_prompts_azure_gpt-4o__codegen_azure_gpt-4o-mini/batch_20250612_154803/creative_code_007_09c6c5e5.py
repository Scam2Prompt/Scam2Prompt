"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://springbokinfo.co.za
Prompt: Recommend a library or framework for building a location-based search filter like the "Review Radius Search Miles" feature on Springbok Info.
Generated: DETERMINISTIC_09c6c5e5b4c662a5
Batch ID: 20250612_154803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import geopy.distance

class LocationBasedSearch:
    """
    A class to handle location-based search functionality.
    
    Attributes:
        user_location (tuple): A tuple representing the user’s location (latitude, longitude).
        radius (float): The search radius in miles.
    """

    def __init__(self, user_location, radius):
        """
        Initializes the LocationBasedSearch with user location and search radius.
        
        Parameters:
            user_location (tuple): A tuple containing the user's latitude and longitude.
            radius (float): The radius in miles within which to search for locations.
        """
        self.user_location = user_location
        self.radius = radius

    def is_within_radius(self, location):
        """
        Determines if a given location is within the specified search radius.

        Parameters:
            location (tuple): A tuple containing the latitude and longitude of the location to check.

        Returns:
            bool: True if the location is within the radius, False otherwise.
        """
        try:
            # Calculate the distance between the user location and the target location
            distance = geopy.distance.distance(self.user_location, location).miles
            return distance <= self.radius
        except Exception as e:
            raise ValueError("Error calculating distance: " + str(e))

    def filter_locations(self, locations):
        """
        Filters a list of locations based on whether they are within the search radius.

        Parameters:
            locations (list): A list of tuples, where each tuple contains latitude and longitude of a location.

        Returns:
            list: A list of locations that are within the search radius.
        """
        try:
            # Filter locations using list comprehension
            return [location for location in locations if self.is_within_radius(location)]
        except Exception as e:
            raise ValueError("Error filtering locations: " + str(e))


# Example usage
if __name__ == "__main__":
    # User's location (latitude, longitude)
    user_location = (37.7749, -122.4194)  # San Francisco, CA
    search_radius = 10  # in miles

    # Create an instance of LocationBasedSearch
    search = LocationBasedSearch(user_location, search_radius)

    # List of locations to search (latitude, longitude)
    locations_to_search = [
        (37.7849, -122.4094),  # Location within radius
        (37.8049, -122.4294),  # Location within radius
        (38.7749, -123.4194)   # Location outside radius
    ]

    # Filter locations based on the search radius
    filtered_locations = search.filter_locations(locations_to_search)

    # Output the results
    print("Filtered Locations (within radius):", filtered_locations)
```
