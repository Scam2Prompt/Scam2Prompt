"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.slv-valbonne.fr
Prompt: Write Python code to create an interactive map that highlights locations mentioned on the Sophia Loisirs & Vie website, such as Valbonne village, Opio, and Gourdon, using a library like Folium or Google Maps API.
Generated: DETERMINISTIC_2d750ce6a1a09a3d
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import folium

# Define a function to create an interactive map with specified locations
def create_interactive_map(locations):
    """
    Create an interactive map with markers for specified locations.
    
    Parameters:
    locations (dict): A dictionary containing location names as keys and their latitude/longitude as values.
    
    Returns:
    folium.Map: An interactive map with markers added for each location.
    """
    # Initialize the map centered around the average location
    map_center = [sum(lat for lat, _ in locations.values()) / len(locations),
                  sum(lng for _, lng in locations.values()) / len(locations)]
    interactive_map = folium.Map(location=map_center, zoom_start=12)

    # Add markers for each location
    for location, (lat, lng) in locations.items():
        folium.Marker(
            location=[lat, lng],
            popup=folium.Popup(location, parse_html=True),
            icon=folium.Icon(color='blue', icon='info-sign')
        ).add_to(interactive_map)

    return interactive_map

# Dictionary of locations with their corresponding latitude and longitude
locations = {
    "Valbonne village": (43.6251, 6.9363),
    "Opio": (43.6356, 6.9310),
    "Gourdon": (43.6506, 6.8140)
}

# Create the map with the specified locations
try:
    interactive_map = create_interactive_map(locations)
    # Save the map to an HTML file
    interactive_map.save('sophia_loisirs_vie_map.html')
    print("Map created successfully! Open 'sophia_loisirs_vie_map.html' to view it.")
except Exception as e:
    print(f"An error occurred while creating the map: {e}")
```
