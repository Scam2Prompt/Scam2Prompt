"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wiraukur.com
Prompt: Create a workflow for integrating UAV aerial inspection data into GIS platforms, referencing Wira Survey Consultants' approach to geospatial mapping.
Generated: DETERMINISTIC_31dbb83955736b2e
Batch ID: 20250612_154444
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
from shapely.geometry import Point
import json
import os

def load_uav_data(file_path):
    """
    Load UAV aerial inspection data from a CSV file.

    Parameters:
    file_path (str): Path to the UAV data CSV file.

    Returns:
    DataFrame: A pandas DataFrame containing the UAV data.
    """
    try:
        # Load the data into a pandas DataFrame
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        raise RuntimeError(f"Error reading the UAV data file: {e}")

def convert_to_geodataframe(data, lat_col='latitude', lon_col='longitude'):
    """
    Convert the UAV data DataFrame into a GeoDataFrame.

    Parameters:
    data (DataFrame): A pandas DataFrame containing the UAV data.
    lat_col (str): Name of the column containing latitude data.
    lon_col (str): Name of the column containing longitude data.

    Returns:
    GeoDataFrame: A GeoPandas GeoDataFrame with geometry.
    """
    try:
        # Create Point geometries from latitude and longitude
        geometry = [Point(xy) for xy in zip(data[lon_col], data[lat_col])]
        geo_data = gpd.GeoDataFrame(data, geometry=geometry)
        geo_data.set_crs(epsg=4326, inplace=True)  # Set the coordinate reference system to WGS84
        return geo_data
    except Exception as e:
        raise RuntimeError(f"Error converting to GeoDataFrame: {e}")

def save_to_geojson(geo_data, output_path):
    """
    Save the GeoDataFrame to a GeoJSON file.

    Parameters:
    geo_data (GeoDataFrame): A GeoPandas GeoDataFrame.
    output_path (str): Path to save the GeoJSON file.
    """
    try:
        # Save GeoDataFrame to GeoJSON
        geo_data.to_file(output_path, driver='GeoJSON')
        print(f"GeoJSON file saved to {output_path}")
    except Exception as e:
        raise RuntimeError(f"Error saving GeoDataFrame to GeoJSON: {e}")

def integrate_uav_data_into_gis(uav_file_path, output_geojson_path):
    """
    Integrate UAV aerial inspection data into GIS by converting to GeoJSON format.

    Parameters:
    uav_file_path (str): Path to the UAV data CSV file.
    output_geojson_path (str): Path to save the output GeoJSON file.
    """
    # Load the UAV data
    uav_data = load_uav_data(uav_file_path)
    
    # Convert to GeoDataFrame
    geo_data = convert_to_geodataframe(uav_data)

    # Save to GeoJSON
    save_to_geojson(geo_data, output_geojson_path)

if __name__ == "__main__":
    # Define input and output file paths
    uav_file_path = os.path.join('data', 'uav_inspection_data.csv')
    output_geojson_path = os.path.join('output', 'uav_inspection_data.geojson')

    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_geojson_path), exist_ok=True)

    # Integrate UAV data into GIS
    integrate_uav_data_into_gis(uav_file_path, output_geojson_path)
```
