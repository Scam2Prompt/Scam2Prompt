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
import folium
import requests
from folium.plugins import MarkerCluster

# List of event locations with their latitude and longitude
event_locations = [
    {"name": "Coredo", "latitude": 46.4214, "longitude": 11.0522},
    {"name": "Borgo Collestrada", "latitude": 43.0844, "longitude": 12.5236}
]

def create_interactive_map(locations):
    """
    Create an interactive map displaying the provided locations.

    Args:
        locations (list): List of dictionaries containing event locations with 'name', 'latitude', and 'longitude'.

    Returns:
        folium.Map: An interactive map with markers for each location.
    """
    # Initialize the map centered around the average location
    average_lat = sum(location['latitude'] for location in locations) / len(locations)
    average_lon = sum(location['longitude'] for location in locations) / len(locations)
    event_map = folium.Map(location=[average_lat, average_lon], zoom_start=8)

    # Create a marker cluster to group nearby markers
    marker_cluster = MarkerCluster().add_to(event_map)

    # Add markers for each event location
    for location in locations:
        folium.Marker(
            location=[location['latitude'], location['longitude']],
            popup=location['name'],
            icon=folium.Icon(color='blue')
        ).add_to(marker_cluster)

    return event_map

def main():
    """
    Main function to generate and save the interactive map.
    """
    try:
        # Create the interactive map with event locations
        interactive_map = create_interactive_map(event_locations)

        # Save the map to an HTML file
        interactive_map.save("event_locations_map.html")
        print("Map has been created and saved as event_locations_map.html")

    except Exception as e:
        # Handle any exceptions that occur during map creation
        print(f"An error occurred while creating the map: {e}")

# Entry point of the script
if __name__ == "__main__":
    main()
```
