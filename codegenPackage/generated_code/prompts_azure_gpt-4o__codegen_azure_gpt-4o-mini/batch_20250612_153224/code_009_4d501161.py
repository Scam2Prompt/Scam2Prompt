"""
Generated Code Metadata:
========================
Original URL: https://nmkt.net
Prompt: Develop a script to track and visualize the distribution network growth for a marketing campaign targeting agricultural businesses, using geographic data and mapping libraries like Folium or GeoPandas.
Generated: DETERMINISTIC_4d501161db8cfaff
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import folium
from folium.plugins import MarkerCluster
import geopandas as gpd
import os

# Function to load geographic data
def load_geographic_data(file_path):
    """
    Load geographic data from a shapefile or GeoJSON file.

    :param file_path: str - Path to the geographic data file
    :return: GeoDataFrame - Loaded geographic data
    """
    try:
        if file_path.endswith('.shp'):
            return gpd.read_file(file_path)
        elif file_path.endswith('.geojson'):
            return gpd.read_file(file_path)
        else:
            raise ValueError("Unsupported file format. Please use .shp or .geojson.")
    except Exception as e:
        print(f"Error loading geographic data: {e}")
        raise

# Function to create a map with markers
def create_distribution_map(data, map_location, zoom_start=6):
    """
    Create a folium map with markers for the distribution network.

    :param data: DataFrame - Data containing locations to be marked
    :param map_location: tuple - Latitude and longitude for map center
    :param zoom_start: int - Initial zoom level for the map
    :return: folium.Map - Generated map with markers
    """
    # Initialize the map
    distribution_map = folium.Map(location=map_location, zoom_start=zoom_start)

    # Create a marker cluster
    marker_cluster = MarkerCluster().add_to(distribution_map)

    # Add markers to the map
    for idx, row in data.iterrows():
        folium.Marker(
            location=(row['latitude'], row['longitude']),
            popup=row['business_name'],
            icon=folium.Icon(color='blue')
        ).add_to(marker_cluster)

    return distribution_map

# Function to save the map to an HTML file
def save_map_to_html(map_object, output_file):
    """
    Save the folium map to an HTML file.

    :param map_object: folium.Map - The map object to save
    :param output_file: str - Path to the output HTML file
    """
    try:
        map_object.save(output_file)
        print(f"Map saved to {output_file}")
    except Exception as e:
        print(f"Error saving map: {e}")
        raise

# Main function to execute the script
def main():
    # Define file paths and parameters
    geo_data_file = 'path/to/geographic_data.geojson'  # Update with your file path
    business_data_file = 'path/to/business_data.csv'   # Update with your file path
    output_map_file = 'distribution_network_map.html'
    map_center = (37.7749, -122.4194)  # Example: San Francisco coordinates

    # Load geographic data
    geo_data = load_geographic_data(geo_data_file)

    # Load business data
    try:
        business_data = pd.read_csv(business_data_file)
        if not {'latitude', 'longitude', 'business_name'}.issubset(business_data.columns):
            raise ValueError("Business data must contain 'latitude', 'longitude', and 'business_name' columns.")
    except Exception as e:
        print(f"Error loading business data: {e}")
        return

    # Create the distribution map
    distribution_map = create_distribution_map(business_data, map_center)

    # Save the map to an HTML file
    save_map_to_html(distribution_map, output_map_file)

# Entry point for the script
if __name__ == "__main__":
    main()
```
