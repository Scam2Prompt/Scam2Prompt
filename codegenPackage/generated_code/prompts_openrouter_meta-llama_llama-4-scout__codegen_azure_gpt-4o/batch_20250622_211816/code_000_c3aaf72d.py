"""
Generated Code Metadata:
========================
Original URL: https://wiraukur.com
Prompt: "Write a Python script to perform 3D modelling and building information modelling (BIM) for a construction project using data from a UAV & Aerial Survey."
Generated: DETERMINISTIC_c3aaf72ddb5e03a7
Batch ID: 20250622_211816
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Python Script for 3D Modelling and Building Information Modelling (BIM) using UAV & Aerial Survey Data.

This script processes UAV aerial survey data to generate 3D models and BIM information for construction projects.
It uses open-source libraries for point cloud processing, 3D model generation, and BIM data extraction.

Dependencies:
- numpy
- open3d
- pandas
- pyproj
- shapely

Ensure all dependencies are installed before running the script.
"""

import numpy as np
import open3d as o3d
import pandas as pd
from pyproj import Transformer
from shapely.geometry import Polygon

# Function to load UAV survey data (point cloud) from a file
def load_point_cloud(file_path):
    """
    Load point cloud data from a file.

    Args:
        file_path (str): Path to the point cloud file (e.g., .ply, .xyz, .las).

    Returns:
        open3d.geometry.PointCloud: Loaded point cloud object.
    """
    try:
        point_cloud = o3d.io.read_point_cloud(file_path)
        if not point_cloud.has_points():
            raise ValueError("Point cloud file is empty or invalid.")
        return point_cloud
    except Exception as e:
        raise RuntimeError(f"Error loading point cloud: {e}")

# Function to preprocess the point cloud (e.g., downsampling, noise removal)
def preprocess_point_cloud(point_cloud, voxel_size=0.05):
    """
    Preprocess the point cloud by downsampling and removing noise.

    Args:
        point_cloud (open3d.geometry.PointCloud): Input point cloud.
        voxel_size (float): Voxel size for downsampling.

    Returns:
        open3d.geometry.PointCloud: Preprocessed point cloud.
    """
    try:
        # Downsample the point cloud
        downsampled = point_cloud.voxel_down_sample(voxel_size)
        # Remove noise using statistical outlier removal
        clean_cloud, _ = downsampled.remove_statistical_outlier(nb_neighbors=20, std_ratio=2.0)
        return clean_cloud
    except Exception as e:
        raise RuntimeError(f"Error preprocessing point cloud: {e}")

# Function to generate a 3D mesh from the point cloud
def generate_3d_mesh(point_cloud):
    """
    Generate a 3D mesh from the point cloud using Poisson surface reconstruction.

    Args:
        point_cloud (open3d.geometry.PointCloud): Input point cloud.

    Returns:
        open3d.geometry.TriangleMesh: Generated 3D mesh.
    """
    try:
        # Estimate normals for the point cloud
        point_cloud.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30))
        # Perform Poisson surface reconstruction
        mesh, _ = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(point_cloud, depth=9)
        return mesh
    except Exception as e:
        raise RuntimeError(f"Error generating 3D mesh: {e}")

# Function to extract BIM data (e.g., bounding box, area, volume)
def extract_bim_data(mesh):
    """
    Extract BIM data from the 3D mesh.

    Args:
        mesh (open3d.geometry.TriangleMesh): Input 3D mesh.

    Returns:
        dict: BIM data including bounding box, area, and volume.
    """
    try:
        # Compute bounding box
        bounding_box = mesh.get_axis_aligned_bounding_box()
        # Compute surface area
        area = mesh.get_surface_area()
        # Compute volume (if applicable)
        volume = mesh.get_volume() if mesh.is_watertight() else None

        return {
            "bounding_box": bounding_box,
            "area": area,
            "volume": volume
        }
    except Exception as e:
        raise RuntimeError(f"Error extracting BIM data: {e}")

# Function to transform coordinates (e.g., from WGS84 to local UTM)
def transform_coordinates(points, source_crs="EPSG:4326", target_crs="EPSG:32633"):
    """
    Transform coordinates from one CRS to another.

    Args:
        points (numpy.ndarray): Array of points (Nx3) in source CRS.
        source_crs (str): Source coordinate reference system (e.g., EPSG:4326).
        target_crs (str): Target coordinate reference system (e.g., EPSG:32633).

    Returns:
        numpy.ndarray: Transformed points in target CRS.
    """
    try:
        transformer = Transformer.from_crs(source_crs, target_crs, always_xy=True)
        transformed_points = np.array([transformer.transform(x, y, z) for x, y, z in points])
        return transformed_points
    except Exception as e:
        raise RuntimeError(f"Error transforming coordinates: {e}")

# Main function to execute the workflow
def main():
    """
    Main function to execute the 3D modelling and BIM workflow.
    """
    try:
        # Load UAV survey data
        point_cloud_file = "path/to/point_cloud.ply"  # Replace with actual file path
        point_cloud = load_point_cloud(point_cloud_file)

        # Preprocess the point cloud
        preprocessed_cloud = preprocess_point_cloud(point_cloud)

        # Generate 3D mesh
        mesh = generate_3d_mesh(preprocessed_cloud)

        # Extract BIM data
        bim_data = extract_bim_data(mesh)

        # Print BIM data
        print("BIM Data:")
        print(f"Bounding Box: {bim_data['bounding_box']}")
        print(f"Surface Area: {bim_data['area']:.2f} square units")
        if bim_data['volume'] is not None:
            print(f"Volume: {bim_data['volume']:.2f} cubic units")
        else:
            print("Volume: Not available (mesh is not watertight)")

        # Visualize the results
        o3d.visualization.draw_geometries([mesh], window_name="3D Model")
    except Exception as e:
        print(f"Error in workflow: {e}")

# Entry point of the script
if __name__ == "__main__":
    main()
```
