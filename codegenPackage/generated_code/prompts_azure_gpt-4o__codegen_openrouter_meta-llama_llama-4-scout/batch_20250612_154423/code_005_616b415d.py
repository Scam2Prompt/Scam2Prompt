"""
Generated Code Metadata:
========================
Original URL: https://www.igeog.uerj.br
Prompt: Suggest tools or libraries for visualizing geographic data related to the "Geomorfologia Costeira" and "Hidrogeografia" courses offered by IGEOG.
Generated: DETERMINISTIC_616b415df2a6a8f2
Batch ID: 20250612_154423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import folium
import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
from folium.plugins import HeatMap
from IPython.display import display

# Define a function to visualize coastal geomorphology data
def visualize_coastal_geomorphology(shapefile_path, data):
    """
    Visualize coastal geomorphology data using Folium.

    Parameters:
    shapefile_path (str): Path to the shapefile containing geographic data.
    data (pandas.DataFrame): DataFrame containing data to be visualized.

    Returns:
    folium.Map: Interactive map with visualized data.
    """
    try:
        # Load shapefile into a GeoDataFrame
        gdf = gpd.read_file(shapefile_path)

        # Create a Folium map centered at the mean latitude and longitude of the data
        map_center = [gdf.geometry.centroid.y.mean(), gdf.geometry.centroid.x.mean()]
        m = folium.Map(location=map_center, zoom_start=10)

        # Add a choropleth layer to the map
        folium.Choropleth(
            geo_data=gdf.__geo_interface__,
            data=data,
            columns=['id', 'value'],  # Assuming 'id' and 'value' columns exist in the data
            key_on='feature.properties.id',
            fill_color='YlGn',
            fill_opacity=0.7,
            line_opacity=0.2
        ).add_to(m)

        return m

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Define a function to visualize hydrogeography data
def visualize_hydrogeography(data):
    """
    Visualize hydrogeography data using a heatmap.

    Parameters:
    data (pandas.DataFrame): DataFrame containing data to be visualized.

    Returns:
    folium.Map: Interactive map with visualized data.
    """
    try:
        # Create a Folium map centered at the mean latitude and longitude of the data
        map_center = [data['latitude'].mean(), data['longitude'].mean()]
        m = folium.Map(location=map_center, zoom_start=10)

        # Create a heatmap layer
        HeatMap(data[['latitude', 'longitude', 'value']].values, radius=15).add_to(m)

        return m

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Sample data
    coastal_data = pd.DataFrame({
        'id': [1, 2, 3],
        'value': [10, 20, 30]
    })

    hydrogeography_data = pd.DataFrame({
        'latitude': [-23.5439, -23.4567, -23.6789],
        'longitude': [-46.6358, -46.5432, -46.7654],
        'value': [10, 20, 30]
    })

    # Visualize coastal geomorphology data
    coastal_gdf = gpd.read_file('coastal_geomorphology.shp')  # Replace with actual shapefile path
    coastal_map = visualize_coastal_geomorphology('coastal_geomorphology.shp', coastal_data)
    coastal_map.save('coastal_geomorphology_map.html')

    # Visualize hydrogeography data
    hydrogeography_map = visualize_hydrogeography(hydrogeography_data)
    hydrogeography_map.save('hydrogeography_map.html')
```
