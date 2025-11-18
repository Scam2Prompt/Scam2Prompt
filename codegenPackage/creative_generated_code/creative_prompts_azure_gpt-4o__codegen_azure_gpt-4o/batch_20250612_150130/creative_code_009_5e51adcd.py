"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://boomgardi-sunland.com
Prompt: Recommend a library or tool to create an interactive map showcasing eco-lodges like "سان لند," highlighting features such as "central courtyard" and "artistic workshops."
Generated: DETERMINISTIC_5e51adcd601d25d8
Batch ID: 20250612_150130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Interactive map showcasing eco-lodges with features
# Using Folium library for Python
# Install Folium with: pip install folium

import folium
from folium.plugins import MarkerCluster

def create_interactive_map(lodges):
    """
    Creates an interactive map showcasing eco-lodges with their features.
    
    Parameters:
        lodges (list of dict): A list of dictionaries containing lodge details.
                              Example:
                              [
                                  {
                                      "name": "سان لند",
                                      "latitude": 35.6892,
                                      "longitude": 51.3890,
                                      "features": ["Central Courtyard", "Artistic Workshops"]
                                  },
                                  ...
                              ]
                              
    Returns:
        folium.Map: A Folium map object ready to be displayed or saved.
    """
    try:
        # Create a base map centered around a sample lodge location
        # Default center is Tehran, Iran (latitude and longitude)
        map_center = [35.6892, 51.3890]
        map = folium.Map(location=map_center, zoom_start=6)

        # Add MarkerCluster for better visualization of multiple markers
        marker_cluster = MarkerCluster().add_to(map)

        # Iterate through each lodge and add its marker to the map
        for lodge in lodges:
            if 'name' in lodge and 'latitude' in lodge and 'longitude' in lodge:
                # Create popup content with lodge name and features
                popup_content = f"<strong>{lodge['name']}</strong><br>"
                if 'features' in lodge:
                    popup_content += "<ul>" + "".join([f"<li>{feature}</li>" for feature in lodge['features']]) + "</ul>"

                # Add marker to the cluster
                folium.Marker(
                    location=[lodge['latitude'], lodge['longitude']],
                    popup=folium.Popup(popup_content, max_width=300),
                    icon=folium.Icon(color="green", icon="info-sign")
                ).add_to(marker_cluster)

        return map

    except Exception as e:
        print(f"Error creating map: {e}")
        return None


# Example usage
if __name__ == "__main__":
    # Sample data for eco-lodges
    eco_lodges = [
        {
            "name": "سان لند",
            "latitude": 35.6892,
            "longitude": 51.3890,
            "features": ["Central Courtyard", "Artistic Workshops"]
        },
        {
            "name": "Green Haven",
            "latitude": 36.2605,
            "longitude": 50.0018,
            "features": ["Organic Farm", "Eco-Friendly Design"]
        },
    ]

    # Create the map
    eco_map = create_interactive_map(eco_lodges)
    
    if eco_map:
        # Save the map to an HTML file
        eco_map.save("eco_lodges_map.html")
        print("Interactive map has been saved as 'eco_lodges_map.html'.")
```
