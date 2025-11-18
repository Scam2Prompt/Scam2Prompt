"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chile-horseriding.com
Prompt: Suggest a mapping API to visualize the Melado Valley and Andes Mountains, highlighting tour routes like the "Rari Day Ride" and "Laguna del Maule" crossings.
Generated: DETERMINISTIC_7267cc2f507636da
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
from folium.plugins import MarkerCluster

# Define a function to create a map of the Melado Valley and Andes Mountains
def create_tour_map():
    # Initialize the map centered around Melado Valley with a specific zoom level
    try:
        map_center = [-35.505, -70.187]  # Latitude and longitude for Melado Valley
        tour_map = folium.Map(location=map_center, zoom_start=10)

        # Create a marker cluster to group markers for better visualization
        marker_cluster = MarkerCluster().add_to(tour_map)

        # Define tour routes with their locations, names, and descriptions
        tours = [
            {
                "name": "Rari Day Ride",
                "location": [-35.511, -70.165],
                "description": "A scenic ride through the beautiful landscapes of the Rari area."
            },
            {
                "name": "Laguna del Maule Crossing",
                "location": [-35.575, -70.187],
                "description": "A breathtaking route that offers views of Laguna del Maule."
            }
        ]

        # Add tour markers to the map
        for tour in tours:
            folium.Marker(
                location=tour["location"],
                popup=folium.Popup(f"<strong>{tour['name']}</strong><br>{tour['description']}", parse_html=True),
                icon=folium.Icon(color="blue", icon="info-sign")
            ).add_to(marker_cluster)

        # Save the map to an HTML file
        tour_map.save("melado_valley_tour_map.html")
        print("Tour map created successfully! Open 'melado_valley_tour_map.html' to view it.")
    
    except Exception as e:
        print(f"Error creating the tour map: {e}")

# Call the function to create the map
if __name__ == "__main__":
    create_tour_map()
```
