"""
Generated Code Metadata:
========================
Original URL: https://spottersbrasil.com.br
Prompt: Suggest tools or libraries for creating interactive maps of Brazilian Air Force bases, referencing the events covered on Spotters Brasil.
Generated: DETERMINISTIC_fe9cc1e1fdfe2e76
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import folium
import pandas as pd
from folium.plugins import MarkerCluster

# Define a function to create an interactive map
def create_interactive_map(base_data, spotter_events):
    """
    Create an interactive map of Brazilian Air Force bases referencing events covered on Spotters Brasil.

    Parameters:
    base_data (list): List of dictionaries containing base information (name, latitude, longitude)
    spotter_events (list): List of dictionaries containing event information (base_name, event_description)

    Returns:
    map (folium.Map): Interactive map with markers and pop-ups
    """

    # Create a new map centered on Brazil
    map = folium.Map(location=[-14.1372, -53.1805], zoom_start=4)

    # Create a marker cluster for bases
    base_cluster = MarkerCluster().add_to(map)

    # Iterate over base data and add markers to the cluster
    for base in base_data:
        try:
            # Create a marker for the base
            folium.Marker(
                location=[base['latitude'], base['longitude']],
                popup=base['name'],
                icon=folium.Icon(color='blue')
            ).add_to(base_cluster)
        except KeyError as e:
            print(f"Error adding base marker: {e}")

    # Iterate over spotter events and add pop-ups to corresponding base markers
    for event in spotter_events:
        try:
            # Find the base marker corresponding to the event
            base_name = event['base_name']
            base_marker = next((base for base in base_data if base['name'] == base_name), None)

            if base_marker:
                # Add a pop-up to the base marker with event description
                folium.Marker(
                    location=[base_marker['latitude'], base_marker['longitude']],
                    popup=f"{base_name}: {event['event_description']}",
                    icon=folium.Icon(color='red')
                ).add_to(base_cluster)
        except KeyError as e:
            print(f"Error adding event pop-up: {e}")

    return map

# Example usage
if __name__ == "__main__":
    # Sample base data
    base_data = [
        {'name': 'Base 1', 'latitude': -12.3456, 'longitude': -45.6789},
        {'name': 'Base 2', 'latitude': -23.4567, 'longitude': -56.7890},
        {'name': 'Base 3', 'latitude': -34.5678, 'longitude': -67.8901}
    ]

    # Sample spotter events
    spotter_events = [
        {'base_name': 'Base 1', 'event_description': 'Event 1 description'},
        {'base_name': 'Base 2', 'event_description': 'Event 2 description'},
        {'base_name': 'Base 3', 'event_description': 'Event 3 description'}
    ]

    # Create and save the interactive map
    map = create_interactive_map(base_data, spotter_events)
    map.save('brazilian_air_force_bases.html')
```
