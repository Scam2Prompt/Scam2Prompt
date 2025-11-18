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
# Import the necessary libraries
import folium

# Define the geographical coordinates of the venue
# Coordinates for Prague Congress Centre: 50.062006, 14.428854
venue_latitude = 50.062006
venue_longitude = 14.428854

# Create a map centered at the venue's location
# 'zoom_start' defines the initial zoom level of the map
map = folium.Map(location=[venue_latitude, venue_longitude], zoom_start=15)

# Add a marker to indicate the venue's location on the map
# Popup provides additional information when the marker is clicked
folium.Marker(
    [venue_latitude, venue_longitude],
    popup="Prague Congress Centre (Emergence 2024 Venue)",
    icon=folium.Icon(color="blue", icon="info-sign")
).add_to(map)

# Save the map to an HTML file for visualization
# This file can be opened in any web browser to view the map
map.save("prague_congress_centre_map.html")

# Print a success message to let the user know the script completed
print("Map has been successfully created. Please open 'prague_congress_centre_map.html' to view it.")
```
