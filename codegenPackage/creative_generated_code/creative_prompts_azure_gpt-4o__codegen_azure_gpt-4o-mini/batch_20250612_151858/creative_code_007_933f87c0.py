"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marchigue.cl
Prompt: Recommend a mapping API to create an interactive map showcasing locations like "Viña Polkura," "Vivero las Vertientes," and "IIVO" as featured on the Turismo Marchigüe website.
Generated: DETERMINISTIC_933f87c0dcd74d2c
Batch ID: 20250612_151858
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

# Define a list of locations with their names and coordinates
locations = [
    {"name": "Viña Polkura", "coordinates": (-34.5199, -71.5694)},
    {"name": "Vivero las Vertientes", "coordinates": (-34.5330, -71.5475)},
    {"name": "IIVO", "coordinates": (-34.5100, -71.5650)}
]

def create_interactive_map(locations):
    """
    Create an interactive map showcasing the specified locations.

    Parameters:
    locations (list): A list of dictionaries with location names and coordinates.

    Returns:
    folium.Map: An interactive map object with plotted locations.
    """
    # Initialize the map centered at the average location
    map_center = [sum(location["coordinates"][0] for location in locations) / len(locations),
                  sum(location["coordinates"][1] for location in locations) / len(locations)]
    
    interactive_map = folium.Map(location=map_center, zoom_start=13)

    # Initialize a marker cluster for better visualization
    marker_cluster = MarkerCluster().add_to(interactive_map)

    # Add locations to the map with markers
    for location in locations:
        folium.Marker(
            location=location["coordinates"],
            popup=location["name"],
            icon=folium.Icon(color="blue")
        ).add_to(marker_cluster)

    return interactive_map

# Main execution block
if __name__ == "__main__":
    try:
        # Create the map with locations
        map_object = create_interactive_map(locations)

        # Save the map to an HTML file
        map_object.save("interactive_map.html")
        print("Map has been created and saved as 'interactive_map.html'.")
    
    except Exception as e:
        print(f"An error occurred while creating the map: {e}")
```
