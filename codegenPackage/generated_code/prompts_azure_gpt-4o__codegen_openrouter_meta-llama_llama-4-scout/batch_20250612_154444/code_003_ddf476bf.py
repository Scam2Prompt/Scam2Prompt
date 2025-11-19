"""
Generated Code Metadata:
========================
Original URL: https://wiraukur.com
Prompt: Write a script to analyze terrestrial and airborne LiDAR data for geospatial mapping, referencing Wira Survey Consultants' expertise in laser scanning technologies.
Generated: DETERMINISTIC_ddf476bf55c93f02
Batch ID: 20250612_154444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import numpy as np
import pandas as pd
from laspy import read, write
from pyproj import Transformer
import matplotlib.pyplot as plt
from sklearn.neighbors import KDTree

def read_lidar_data(file_path):
    """
    Read LiDAR data from a LAS file.

    Args:
    file_path (str): Path to the LAS file.

    Returns:
    las_data (laspy.las.LAS): LiDAR data.
    """
    try:
        las_data = read(file_path)
        return las_data
    except Exception as e:
        print(f"Error reading LiDAR data: {e}")
        return None

def filter_ground_points(las_data):
    """
    Filter ground points from LiDAR data.

    Args:
    las_data (laspy.las.LAS): LiDAR data.

    Returns:
    ground_points (numpy.array): Ground points.
    """
    try:
        # Assuming ground points have a specific classification (e.g., 2)
        ground_points = np.array([point for point in las_data.xys if point[3] == 2])
        return ground_points
    except Exception as e:
        print(f"Error filtering ground points: {e}")
        return None

def transform_coordinates(points, src_crs, dst_crs):
    """
    Transform coordinates from one CRS to another.

    Args:
    points (numpy.array): Points to transform.
    src_crs (str): Source CRS.
    dst_crs (str): Destination CRS.

    Returns:
    transformed_points (numpy.array): Transformed points.
    """
    try:
        transformer = Transformer.from_crs(src_crs, dst_crs)
        transformed_points = np.array(transformer.transform(points[:, 0], points[:, 1]))
        return np.column_stack((transformed_points[0], transformed_points[1], points[:, 2]))
    except Exception as e:
        print(f"Error transforming coordinates: {e}")
        return None

def create_dsm(ground_points, resolution):
    """
    Create a digital surface model (DSM) from ground points.

    Args:
    ground_points (numpy.array): Ground points.
    resolution (float): DSM resolution.

    Returns:
    dsm (numpy.array): DSM.
    """
    try:
        # Use a KDTree to efficiently query points
        kdtree = KDTree(ground_points[:, :2])
        dsm = np.zeros((int(np.ceil((ground_points[:, 0].max() - ground_points[:, 0].min()) / resolution)),
                        int(np.ceil((ground_points[:, 1].max() - ground_points[:, 1].min()) / resolution))))
        for i in range(dsm.shape[0]):
            for j in range(dsm.shape[1]):
                x = ground_points[:, 0].min() + j * resolution
                y = ground_points[:, 1].min() + i * resolution
                dist, idx = kdtree.query((x, y))
                if dist < resolution:
                    dsm[i, j] = ground_points[idx, 2]
        return dsm
    except Exception as e:
        print(f"Error creating DSM: {e}")
        return None

def plot_dsm(dsm):
    """
    Plot the DSM.

    Args:
    dsm (numpy.array): DSM.
    """
    try:
        plt.imshow(dsm, cmap='viridis', origin='lower')
        plt.colorbar(label='Elevation')
        plt.show()
    except Exception as e:
        print(f"Error plotting DSM: {e}")

def main():
    # Read LiDAR data
    las_data = read_lidar_data('data.las')

    # Filter ground points
    ground_points = filter_ground_points(las_data)

    # Transform coordinates to a specific CRS (e.g., EPSG:4326)
    transformed_points = transform_coordinates(ground_points, las_data.crs, 'epsg:4326')

    # Create DSM
    dsm = create_dsm(transformed_points, 1.0)

    # Plot DSM
    plot_dsm(dsm)

if __name__ == "__main__":
    main()
```
