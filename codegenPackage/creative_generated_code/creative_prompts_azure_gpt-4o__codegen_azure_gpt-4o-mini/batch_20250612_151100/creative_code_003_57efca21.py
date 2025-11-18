"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://test.emergence-dev.pages.dev
Prompt: Create a script that visualizes the geographical location of the Emergence 2024 venue (Prague Congress Centre) on a map using a mapping library like Folium or Google Maps API.
Generated: DETERMINISTIC_57efca217ce6979c
Batch ID: 20250612_151100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import folium

def create_map(location, zoom_start=15):
    """
    Create a map centered at the given location.

    Parameters:
    location (tuple): A tuple containing the latitude and longitude of the location.
    zoom_start (int): Initial zoom level for the map (default is 15).

    Returns:
    folium.Map: A Folium Map object centered at the specified location.
    """
    try:
        # Create a Folium Map object
        map_object = folium.Map(location=location, zoom_start=zoom_start)
        return map_object
    except Exception as e:
        print(f"Error creating map: {e}")
        return None

def add_marker_to_map(map_object, location, popup_text):
    """
    Add a marker to the map with a popup text.

    Parameters:
    map_object (folium.Map): The Folium Map object to which the marker will be added.
    location (tuple): A tuple containing the latitude and longitude for the marker.
    popup_text (str): Text to display when the marker is clicked.
    """
    try:
        # Add a marker to the map
        folium.Marker(location=location, popup=popup_text).add_to(map_object)
    except Exception as e:
        print(f"Error adding marker: {e}")

def main():
    # Geographical coordinates for the Prague Congress Centre
    prague_congress_centre = (50.0755, 14.4320)
    
    # Create a map centered on the Prague Congress Centre
    prague_map = create_map(prague_congress_centre)
    
    if prague_map is not None:
        # Add a marker for the venue
        add_marker_to_map(prague_map, prague_congress_centre, "Emergence 2024 Venue: Prague Congress Centre")
        
        # Save map to an HTML file
        try:
            prague_map.save("emergence_2024_venue_map.html")
            print("Map saved successfully as emergence_2024_venue_map.html")
        except Exception as e:
            print(f"Error saving map: {e}")

if __name__ == "__main__":
    main()
```
