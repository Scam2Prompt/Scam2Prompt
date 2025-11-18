"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nmkt.net
Prompt: Develop a script to track and visualize the distribution network growth for a marketing campaign targeting agricultural businesses, using geographic data and mapping libraries like Folium or GeoPandas.
Generated: DETERMINISTIC_4d501161db8cfaff
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import geopandas as gpd
from folium import Map, Marker, GeoJson
from folium.plugins import MarkerCluster
import os

# Define the file paths (update these paths accordingly)
data_file = "distribution_network.csv"  # CSV file containing distribution points
output_map = "distribution_network_map.html"

# Ensure input file exists
if not os.path.exists(data_file):
    raise FileNotFoundError(f"Data file '{data_file}' not found.")

# Load geographic data for distribution network
try:
    # The CSV file should contain columns: "name", "latitude", "longitude", and optionally "region"
    data = pd.read_csv(data_file)
    if not {"name", "latitude", "longitude"}.issubset(data.columns):
        raise ValueError("CSV file must contain 'name', 'latitude', and 'longitude' columns.")
except Exception as e:
    raise RuntimeError(f"Error loading data file: {e}")

# Convert the DataFrame to a GeoDataFrame for spatial operations
try:
    gdf = gpd.GeoDataFrame(
        data,
        geometry=gpd.points_from_xy(data.longitude, data.latitude),
        crs="EPSG:4326",  # WGS84 coordinate system
    )
except Exception as e:
    raise RuntimeError(f"Error converting DataFrame to GeoDataFrame: {e}")

# Create a base map centered at the mean latitude and longitude of the network points
mean_latitude = gdf.geometry.y.mean()
mean_longitude = gdf.geometry.x.mean()
map_base = Map(location=[mean_latitude, mean_longitude], zoom_start=5)

# Add markers for each distribution point
marker_cluster = MarkerCluster()
for _, row in gdf.iterrows():
    Marker(
        location=(row.geometry.y, row.geometry.x),
        popup=f"Name: {row['name']}\nLatitude: {row.geometry.y}\nLongitude: {row.geometry.x}",
    ).add_to(marker_cluster)
marker_cluster.add_to(map_base)

# Optionally add GeoJSON overlays if regional data is available
if 'region' in gdf.columns:
    # Group points by region and create GeoJSON objects for visualization
    regions = gdf.dissolve(by='region')
    for _, region in regions.iterrows():
        GeoJson(region.geometry, name=region.name).add_to(map_base)

# Save the map to an HTML file
try:
    map_base.save(output_map)
    print(f"Map successfully saved to '{output_map}'")
except Exception as e:
    raise RuntimeError(f"Error saving map: {e}")
```
