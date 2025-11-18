"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.predaiaarteenatura.eu
Prompt: Suggest a library for generating interactive maps and write code to display locations of events mentioned on the Predaia Arte e Natura website, such as Coredo and Borgo Collestrada.
Generated: DETERMINISTIC_73dac80299de5494
Batch ID: 20250612_151539
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import folium  # Folium is a Python library for creating interactive maps

# Function to create a map and plot locations
def create_event_map(locations):
    """
    Create an interactive map displaying event locations.

    Parameters:
        locations (list of dicts): A list of dictionaries where each dictionary contains
                                   'name', 'latitude', and 'longitude' of a location.

    Returns:
        folium.Map: A Folium map object with the event locations plotted.
    """
    try:
        # Validate input
        if not isinstance(locations, list):
            raise ValueError("Locations must be a list of dictionaries.")

        if len(locations) == 0:
            raise ValueError("Locations list is empty.")

        # Initialize the map centered around the first location
        initial_coords = [locations[0]['latitude'], locations[0]['longitude']]
        event_map = folium.Map(location=initial_coords, zoom_start=12)

        # Add markers for each location
        for location in locations:
            name = location.get('name')
            lat = location.get('latitude')
            lon = location.get('longitude')

            # Validate latitude and longitude values
            if not isinstance(lat, (int, float)) or not isinstance(lon, (int, float)):
                raise ValueError(f"Invalid latitude/longitude for location: {name}")

            # Add marker to the map
            folium.Marker(
                location=[lat, lon],
                popup=name,
                tooltip=name
            ).add_to(event_map)

        return event_map

    except Exception as e:
        # Handle exceptions and provide error messages
        print(f"Error while creating the map: {e}")
        return None


# List of event locations from Predaia Arte e Natura website
locations = [
    {"name": "Coredo", "latitude": 46.3736, "longitude": 11.0869},
    {"name": "Borgo Collestrada", "latitude": 43.0939, "longitude": 12.4712},
]

# Create the map
event_map = create_event_map(locations)

# Save the map to an HTML file for display
if event_map:
    event_map.save("event_map.html")
    print("Map has been successfully created and saved as 'event_map.html'.")
else:
    print("Failed to create the map.")
```
