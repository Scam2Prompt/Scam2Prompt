"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ajp.cl
Prompt: Suggest a library for creating interactive maps that visualize rural water supply projects, inspired by the project designs from AJP Ingenieros.
Generated: DETERMINISTIC_a5c2078813bbda29
Batch ID: 20250612_155840
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is Python code using the `folium` library to create an interactive map for visualizing rural water supply projects.

```python
"""
Interactive map visualization for rural water supply projects.
Inspired by project designs from AJP Ingenieros.

This script uses the `folium` library to create customizable maps.
Install the required library with `pip install folium` before running.
"""

import folium
from folium.plugins import MarkerCluster


def create_interactive_map(projects, center_lat=0, center_lon=0, zoom_start=2, output_file="water_supply_map.html"):
    """
    Creates an interactive map to visualize rural water supply projects.

    Args:
        projects (list of dict): A list of dictionaries containing project data.
                                 Each dictionary must have 'name', 'latitude', 'longitude', and 'description' keys.
        center_lat (float): The latitude to center the map on.
        center_lon (float): The longitude to center the map on.
        zoom_start (int): Initial zoom level for the map.
        output_file (str): Name of the output HTML file for the map.

    Returns:
        None. Saves the map as an HTML file.
    """

    try:
        # Create the map object centered on the given coordinates
        project_map = folium.Map(location=[center_lat, center_lon], zoom_start=zoom_start)

        # Add a marker cluster layer for grouping markers
        marker_cluster = MarkerCluster().add_to(project_map)

        # Add markers for each project
        for project in projects:
            # Extract project data
            name = project.get('name', 'Unknown Project')
            lat = project.get('latitude')
            lon = project.get('longitude')
            description = project.get('description', 'No description available.')

            # Validate latitude and longitude
            if lat is None or lon is None:
                print(f"Skipping project '{name}' due to missing coordinates.")
                continue

            # Create marker with a popup containing project details
            popup_content = f"<b>{name}</b><br>{description}"
            folium.Marker(location=[lat, lon], popup=popup_content).add_to(marker_cluster)

        # Save the map to an HTML file
        project_map.save(output_file)
        print(f"Interactive map created successfully: {output_file}")

    except Exception as e:
        print(f"An error occurred while creating the map: {e}")


# Example usage:
if __name__ == "__main__":
    # Define sample project data (replace with real data)
    example_projects = [
        {
            "name": "Water Supply Project 1",
            "latitude": 37.7749,
            "longitude": -122.4194,
            "description": "Providing clean water to rural communities near San Francisco.",
        },
        {
            "name": "Water Supply Project 2",
            "latitude": 40.7128,
            "longitude": -74.0060,
            "description": "Upgrading old water supply systems in New York City outskirts.",
        },
        {
            "name": "Water Supply Project 3",
            "latitude": -1.2921,
            "longitude": 36.8219,
            "description": "Installing new water tanks in Nairobi, Kenya.",
        },
    ]

    # Create the map
    create_interactive_map(
        projects=example_projects,
        center_lat=0,  # Global map centered at latitude 0
        center_lon=0,  # Global map centered at longitude 0
        zoom_start=2,  # Initial zoom level
        output_file="water_supply_map.html",  # Output file name
    )
```

**How to run:**
1. Install the required library: `pip install folium`.
2. Run the script. It will generate an interactive map saved as `water_supply_map.html`.
3. Open the HTML file in a browser to explore the map.
