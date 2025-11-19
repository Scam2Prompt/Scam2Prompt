"""
Generated Code Metadata:
========================
Original URL: https://www.slv-valbonne.fr
Prompt: Write Python code to create an interactive map that highlights locations mentioned on the Sophia Loisirs & Vie website, such as Valbonne village, Opio, and Gourdon, using a library like Folium or Google Maps API.
Generated: DETERMINISTIC_2d750ce6a1a09a3d
Batch ID: 20250612_153224
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
from folium.plugins import MarkerCluster

def create_interactive_map(locations):
    """
    Create an interactive map with highlighted locations.

    Args:
        locations (dict): Dictionary of locations with their latitude and longitude.

    Returns:
        folium.Map: Interactive map with markers.
    """
    # Create a new map centered at the average latitude and longitude of all locations
    latitudes = [location['lat'] for location in locations.values()]
    longitudes = [location['lng'] for location in locations.values()]
    center_lat = sum(latitudes) / len(latitudes)
    center_lng = sum(longitudes) / len(longitudes)
    map = folium.Map(location=[center_lat, center_lng], zoom_start=10)

    # Add a marker cluster to the map
    marker_cluster = MarkerCluster().add_to(map)

    # Add markers for each location
    for name, location in locations.items():
        folium.Marker(
            [location['lat'], location['lng']],
            popup=name,
            icon=folium.Icon(color='blue')
        ).add_to(marker_cluster)

    return map

def main():
    # Define locations with their latitude and longitude
    locations = {
        'Valbonne village': {'lat': 43.6703, 'lng': 6.9463},
        'Opio': {'lat': 43.6667, 'lng': 6.9333},
        'Gourdon': {'lat': 43.7167, 'lng': 6.9833},
    }

    try:
        # Create the interactive map
        map = create_interactive_map(locations)
        # Save the map as an HTML file
        map.save('sophia_loisirs_map.html')
        print("Map saved as sophia_loisirs_map.html")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
