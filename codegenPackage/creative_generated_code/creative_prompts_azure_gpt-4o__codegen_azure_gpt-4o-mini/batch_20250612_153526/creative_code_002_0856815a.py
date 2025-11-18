"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://khaptadtours.com
Prompt: Generate code to display a map of the Upper Mustang Trek route, incorporating cultural landmarks highlighted on the Khaptad Tours webpage.
Generated: DETERMINISTIC_0856815a4c9d8619
Batch ID: 20250612_153526
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

# Define a function to create a map of the Upper Mustang Trek
def create_upper_mustang_map():
    """
    Creates an interactive map displaying the Upper Mustang Trek route along with cultural landmarks.

    Returns:
        folium.Map: An interactive map object centered around Upper Mustang.
    """
    # Initialize the map centered at Upper Mustang
    upper_mustang_map = folium.Map(location=[29.3296, 82.7032], zoom_start=10)

    # Create a marker cluster to group landmarks
    marker_cluster = MarkerCluster().add_to(upper_mustang_map)

    # List of cultural landmarks with their names and coordinates
    cultural_landmarks = [
        {
            "name": "Lo Manthang",
            "location": [29.2618, 83.8327],
            "description": "The ancient capital of the Kingdom of Lo, rich in history and culture."
        },
        {
            "name": "Tsarang Monastery",
            "location": [29.2676, 83.8445],
            "description": "A historic monastery with stunning architecture and a serene atmosphere."
        },
        {
            "name": "Choser Cave",
            "location": [29.2878, 83.8741],
            "description": "An ancient cave system known for its historical significance and beautiful views."
        },
        {
            "name": "Ghar Gompa",
            "location": [29.2175, 83.8553],
            "description": "One of the oldest monasteries in the region, offering insights into local Buddhist culture."
        },
        {
            "name": "Dhi Village",
            "location": [29.1945, 83.8315],
            "description": "A picturesque village showcasing traditional architecture and daily life."
        }
    ]

    # Add each landmark to the map
    for landmark in cultural_landmarks:
        try:
            folium.Marker(
                location=landmark["location"],
                popup=f"<strong>{landmark['name']}</strong><br>{landmark['description']}",
                icon=folium.Icon(color='blue', icon='info-sign')
            ).add_to(marker_cluster)
        except KeyError as e:
            print(f"KeyError: Missing {e} in landmark data: {landmark}")
        except Exception as e:
            print(f"An error occurred while adding landmark '{landmark['name']}': {e}")

    # Save the map to an HTML file
    try:
        upper_mustang_map.save('upper_mustang_trek_map.html')
        print("Map has been successfully created and saved as 'upper_mustang_trek_map.html'.")
    except IOError as e:
        print(f"IOError: Failed to save the map due to: {e}")

if __name__ == "__main__":
    create_upper_mustang_map()
```
