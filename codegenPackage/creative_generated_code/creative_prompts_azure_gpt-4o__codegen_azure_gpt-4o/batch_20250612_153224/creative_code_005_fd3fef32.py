"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.aidasdb.org
Prompt: Provide code to create an interactive map displaying the locations of community empowerment projects, such as those conducted by AIDA in Nagaland and Arunachal Pradesh.
Generated: DETERMINISTIC_fd3fef32cd4a458c
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the Python code to create an interactive map using the `folium` library. You can replace the placeholder data with actual project coordinates and details.

```python
import folium
from folium.plugins import MarkerCluster

# List of community empowerment project locations (latitude, longitude, and description)
project_locations = [
    {"name": "Project A", "latitude": 26.1584, "longitude": 94.5624, "description": "Empowerment project in Nagaland."},
    {"name": "Project B", "latitude": 27.1000, "longitude": 93.6166, "description": "Empowerment project in Arunachal Pradesh."},
    {"name": "Project C", "latitude": 26.2678, "longitude": 94.1115, "description": "Another project in Nagaland."},
    {"name": "Project D", "latitude": 27.0984, "longitude": 93.6344, "description": "Additional project in Arunachal Pradesh."}
]

# Initialize the map centered in Northeast India
# Setting a zoom level to ensure the map displays relevant locations
map_center = [26.5, 94.0]  # Adjust based on approximate mid-point of the locations
interactive_map = folium.Map(location=map_center, zoom_start=7, tiles="OpenStreetMap")

# Create a MarkerCluster to group nearby locations
marker_cluster = MarkerCluster().add_to(interactive_map)

# Add markers for each project to the map
for project in project_locations:
    try:
        folium.Marker(
            location=[project["latitude"], project["longitude"]],
            popup=folium.Popup(
                f"<strong>{project['name']}</strong><br>{project['description']}",
                max_width=200
            ),
            tooltip=project["name"]
        ).add_to(marker_cluster)
    except KeyError as e:
        print(f"Error adding marker for project: {e}")

# Save the map to an HTML file
output_file = "community_projects_map.html"
interactive_map.save(output_file)

print(f"Map generated successfully. Open '{output_file}' to view the interactive map.")
```

### Key Points:
1. Install required dependencies:
   ```bash
   pip install folium
   ```

2. Replace the placeholder `project_locations` list with actual data, including latitude, longitude, and project descriptions.

3. Open the `community_projects_map.html` file in a browser to view the interactive map.

4. This code uses `MarkerCluster` to improve visualization when locations are close together.
