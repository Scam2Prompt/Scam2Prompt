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
import folium
from folium.plugins import MarkerCluster

# Define the locations to be highlighted on the map
locations = {
    "Valbonne Village": (43.6102, 6.9352),
    "Opio": (43.6342, 6.9350),
    "Gourdon": (43.6500, 6.6880)
}

# Create a base map centered around the average location
map_center = (43.6315, 6.8524)  # Average coordinates of the locations
map_zoom_start = 12  # Initial zoom level
interactive_map = folium.Map(location=map_center, zoom_start=map_zoom_start)

# Create a marker cluster to group nearby markers
marker_cluster = MarkerCluster().add_to(interactive_map)

# Add locations to the map with markers
for location_name, coordinates in locations.items():
    try:
        folium.Marker(
            location=coordinates,
            popup=folium.Popup(location_name, parse_html=True),
            icon=folium.Icon(color='blue', icon='info-sign')
        ).add_to(marker_cluster)
    except Exception as e:
        print(f"Error adding marker for {location_name}: {e}")

# Save the map to an HTML file
output_file = 'sophia_loisirs_vie_map.html'
try:
    interactive_map.save(output_file)
    print(f"Map has been successfully created and saved to {output_file}")
except Exception as e:
    print(f"Error saving the map: {e}")
```
