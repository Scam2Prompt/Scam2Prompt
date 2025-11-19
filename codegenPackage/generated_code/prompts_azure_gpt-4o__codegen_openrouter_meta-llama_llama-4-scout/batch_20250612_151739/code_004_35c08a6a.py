"""
Generated Code Metadata:
========================
Original URL: https://afco-federation.fr
Prompt: Suggest APIs or libraries for building a guide to prevent risks related to unstable terrain, targeting construction and foundation companies, as described on the AFCO site.
Generated: DETERMINISTIC_35c08a6a786808fb
Batch ID: 20250612_151739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'm happy to provide code, but I need to clarify that I'll be providing a Python solution. I'll be using the `Flask` library to create a simple API and `GeoPandas` and `Rasterio` libraries for geospatial operations.

```python
# Import required libraries
from flask import Flask, jsonify, request
import geopandas as gpd
import rasterio
from rasterio.features import shapes
from shapely.geometry import shape
import numpy as np

app = Flask(__name__)

# Define a function to get terrain stability data
def get_terrain_stability_data(lon, lat):
    """
    Retrieves terrain stability data for a given location.

    Args:
        lon (float): Longitude of the location.
        lat (float): Latitude of the location.

    Returns:
        dict: Terrain stability data.
    """
    try:
        # Load the terrain stability raster file
        with rasterio.open('terrain_stability.tif') as src:
            # Read the raster data
            data = src.read(1)

            # Get the transform
            transform = src.transform

            # Calculate the index of the pixel
            idx = int((lon - transform.xoff) / transform.a)
            idy = int((lat - transform.yoff) / transform.e)

            # Check if the index is within bounds
            if idx < 0 or idy < 0 or idx >= data.shape[1] or idy >= data.shape[0]:
                return {"error": "Location out of bounds"}

            # Get the terrain stability value
            value = data[idy, idx]

            # Interpret the value
            if value < 0.3:
                stability = "Unstable"
            elif value < 0.6:
                stability = "Moderately Stable"
            else:
                stability = "Stable"

            return {"stability": stability, "value": float(value)}

    except Exception as e:
        return {"error": str(e)}

# Define a function to get construction risk data
def get_construction_risk_data(lon, lat):
    """
    Retrieves construction risk data for a given location.

    Args:
        lon (float): Longitude of the location.
        lat (float): Latitude of the location.

    Returns:
        dict: Construction risk data.
    """
    try:
        # Load the construction risk GeoJSON file
        gdf = gpd.read_file('construction_risk.geojson')

        # Get the location
        location = shape({"type": "Point", "coordinates": [lon, lat]})

        # Check if the location intersects with any features
        for idx, row in gdf.iterrows():
            if row.geometry.intersects(location):
                return {"risk": row["risk"], "description": row["description"]}

        return {"risk": "Low", "description": "No risk"}

    except Exception as e:
        return {"error": str(e)}

# Define the API endpoint for terrain stability data
@app.route('/terrain-stability', methods=['GET'])
def terrain_stability_endpoint():
    lon = request.args.get('lon', type=float)
    lat = request.args.get('lat', type=float)

    if lon is None or lat is None:
        return jsonify({"error": "Longitude and latitude are required"}), 400

    data = get_terrain_stability_data(lon, lat)
    return jsonify(data)

# Define the API endpoint for construction risk data
@app.route('/construction-risk', methods=['GET'])
def construction_risk_endpoint():
    lon = request.args.get('lon', type=float)
    lat = request.args.get('lat', type=float)

    if lon is None or lat is None:
        return jsonify({"error": "Longitude and latitude are required"}), 400

    data = get_construction_risk_data(lon, lat)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
```
