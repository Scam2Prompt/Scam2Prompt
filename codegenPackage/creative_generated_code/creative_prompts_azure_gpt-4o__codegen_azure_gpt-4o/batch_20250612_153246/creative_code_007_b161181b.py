"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kadma-wine.co.il
Prompt: Recommend a library for creating an interactive map showing the location of Kadma Winery and nearby parks for picnic basket use.
Generated: DETERMINISTIC_b161181b530a140a
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import folium  # For creating interactive maps
from folium.plugins import MarkerCluster  # For clustering markers

# Define locations: Kadma Winery and nearby parks
locations = {
    "Kadma Winery": {"latitude": 31.7079, "longitude": 34.9531},  # Example coordinates for Kadma Winery
    "Park 1": {"latitude": 31.7100, "longitude": 34.9500},  # Example coordinates for nearby park
    "Park 2": {"latitude": 31.7050, "longitude": 34.9600},  # Example coordinates for nearby park
    "Park 3": {"latitude": 31.7150, "longitude": 34.9520},  # Example coordinates for nearby park
}

# Create a base map centered around Kadma Winery
base_map = folium.Map(
    location=[locations["Kadma Winery"]["latitude"], locations["Kadma Winery"]["longitude"]],
    zoom_start=14,  # Initial zoom level
    tiles="OpenStreetMap",  # Map style
)

# Create a marker cluster for better visualization of multiple nearby parks
marker_cluster = MarkerCluster()

# Add markers to the map
for name, coords in locations.items():
    marker = folium.Marker(
        location=[coords["latitude"], coords["longitude"]],
        popup=f"<strong>{name}</strong>",  # Popup text when marker is clicked
        icon=folium.Icon(color="blue" if name == "Kadma Winery" else "green"),  # Icon color based on location type
    )
    marker_cluster.add_child(marker)

# Add the marker cluster to the base map
base_map.add_child(marker_cluster)

# Save the map as an HTML file
map_file = "interactive_map.html"
base_map.save(map_file)

print(f"Interactive map has been successfully created and saved to '{map_file}'.")
```
