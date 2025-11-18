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

# Function to create an interactive map with highlighted locations
def create_interactive_map():
    try:
        # Initialize map centered around Valbonne (latitude and longitude for Valbonne village)
        map_center = [43.6419, 6.9984]  # Coordinates for Valbonne
        interactive_map = folium.Map(location=map_center, zoom_start=11)

        # Define locations (latitude, longitude, name)
        locations = [
            {"name": "Valbonne Village", "coordinates": [43.6419, 6.9984]},
            {"name": "Opio", "coordinates": [43.6822, 7.0026]},
            {"name": "Gourdon", "coordinates": [43.7237, 6.9753]},
        ]

        # Add markers for each location
        for location in locations:
            folium.Marker(
                location["coordinates"],
                popup=location["name"],
                icon=folium.Icon(color="blue", icon="info-sign"),  # Styling the marker
            ).add_to(interactive_map)

        # Save the map as an HTML file
        interactive_map.save("sophia_loisirs_map.html")
        print("Map created successfully! Saved as 'sophia_loisirs_map.html'")
    except Exception as e:
        # Error handling
        print(f"An error occurred while creating the map: {e}")

# Execute the function to create the map
if __name__ == "__main__":
    create_interactive_map()
```

This code generates an interactive map using Folium with markers for Valbonne, Opio, and Gourdon, and saves the map as an HTML file ready for use.
