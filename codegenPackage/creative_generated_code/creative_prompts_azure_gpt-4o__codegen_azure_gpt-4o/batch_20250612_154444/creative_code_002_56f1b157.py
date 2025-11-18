"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wiraukur.com
Prompt: Generate code to detect underground utilities using remote sensing data, incorporating techniques described by Wira Survey Consultants.
Generated: DETERMINISTIC_56f1b15705778368
Batch ID: 20250612_154444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Utility Detection using Remote Sensing Data

This script processes remote sensing data to detect underground utilities.
It incorporates techniques inspired by Wira Survey Consultants, emphasizing best practices
for handling geospatial data and feature extraction.

Requirements:
- Python 3.8 or later
- Packages: numpy, pandas, geopandas, rasterio, matplotlib, scikit-learn

Author: Professional Software Developer
"""

# Import necessary libraries
import numpy as np
import pandas as pd
import geopandas as gpd
import rasterio
from rasterio.plot import show
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Constants and configurations
REMOTE_SENSING_DATA_PATH = "path/to/remote_sensing_data.tif"  # Input file path
OUTPUT_DETECTED_UTILITIES = "output_detected_utilities.geojson"  # Output GeoJSON file
NUM_CLUSTERS = 3  # Number of clusters for KMeans
RANDOM_STATE = 42  # Seed for reproducibility

def load_raster_data(file_path):
    """
    Load raster data from a GeoTIFF file.

    :param file_path: Path to the raster file.
    :return: Raster data array and metadata.
    """
    try:
        with rasterio.open(file_path) as src:
            raster_data = src.read(1)  # Read the first band
            metadata = src.meta
        return raster_data, metadata
    except rasterio.errors.RasterioIOError as e:
        raise IOError(f"Error loading raster file: {file_path}. Details: {e}")

def preprocess_data(raster_data):
    """
    Preprocess the raster data for clustering.

    :param raster_data: Input raster array.
    :return: Flattened array of raster values.
    """
    # Reshape the raster data into a 1D array for clustering
    raster_values = raster_data.flatten()
    # Remove nodata values (assuming negative values are nodata)
    raster_values = raster_values[raster_values >= 0]
    return raster_values

def detect_utilities(raster_values, num_clusters):
    """
    Apply clustering algorithm to detect underground utilities.

    :param raster_values: Preprocessed raster data values.
    :param num_clusters: Number of clusters for KMeans.
    :return: Cluster labels and model instance.
    """
    try:
        # Perform clustering using KMeans
        kmeans = KMeans(n_clusters=num_clusters, random_state=RANDOM_STATE)
        cluster_labels = kmeans.fit_predict(raster_values.reshape(-1, 1))
        return cluster_labels, kmeans
    except Exception as e:
        raise RuntimeError(f"Error during clustering: {e}")

def generate_geospatial_data(cluster_labels, metadata):
    """
    Generate geospatial data from cluster labels.

    :param cluster_labels: Labels from clustering.
    :param metadata: Metadata from the raster file.
    :return: GeoDataFrame containing detected features.
    """
    try:
        # Reshape cluster labels back to original raster dimensions
        raster_shape = metadata["height"], metadata["width"]
        labeled_raster = np.reshape(cluster_labels, raster_shape)
        
        # Create a GeoDataFrame for visualization/export
        gdf = gpd.GeoDataFrame({'cluster': labeled_raster.flatten()})
        gdf['geometry'] = gpd.points_from_xy(
            np.repeat(np.arange(metadata["width"]), metadata["height"]),
            np.tile(np.arange(metadata["height"]), metadata["width"])
        )
        return gdf
    except Exception as e:
        raise RuntimeError(f"Error generating geospatial data: {e}")

def save_detected_utilities(gdf, output_path):
    """
    Save detected utilities to a GeoJSON file.

    :param gdf: GeoDataFrame containing detected features.
    :param output_path: Output file path.
    """
    try:
        gdf.to_file(output_path, driver="GeoJSON")
        print(f"Utilities successfully saved to: {output_path}")
    except Exception as e:
        raise IOError(f"Error saving GeoJSON file: {e}")

def main():
    """
    Main function to orchestrate utility detection from remote sensing data.
    """
    try:
        print("Loading remote sensing data...")
        raster_data, metadata = load_raster_data(REMOTE_SENSING_DATA_PATH)

        print("Preprocessing raster data...")
        raster_values = preprocess_data(raster_data)

        print("Detecting underground utilities...")
        cluster_labels, _ = detect_utilities(raster_values, NUM_CLUSTERS)

        print("Generating geospatial data...")
        gdf = generate_geospatial_data(cluster_labels, metadata)

        print("Saving detected utilities...")
        save_detected_utilities(gdf, OUTPUT_DETECTED_UTILITIES)

        print("Utility detection process completed successfully.")
    except Exception as e:
        print(f"Error: {e}")

# Entry point
if __name__ == "__main__":
    main()
```
