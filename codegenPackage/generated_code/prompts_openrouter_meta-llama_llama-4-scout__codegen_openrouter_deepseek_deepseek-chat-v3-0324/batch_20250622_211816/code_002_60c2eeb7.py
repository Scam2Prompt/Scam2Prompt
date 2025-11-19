"""
Generated Code Metadata:
========================
Original URL: https://wiraukur.com
Prompt: "Generate code to analyze data from a terrestrial and airborne LIDAR / Laser Scanning survey using Geographic Information System (GIS) and data analytics."
Generated: DETERMINISTIC_60c2eeb7296d298a
Batch ID: 20250622_211816
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import numpy as np
import pandas as pd
import geopandas as gpd
import rasterio
from rasterio.plot import show
from shapely.geometry import Point, Polygon
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
import laspy

class LidarDataAnalyzer:
    """
    A class to analyze terrestrial and airborne LIDAR data using GIS and data analytics.
    
    Attributes:
        terrestrial_data (laspy.LasData): Terrestrial LIDAR data.
        airborne_data (laspy.LasData): Airborne LIDAR data.
        crs (str): Coordinate Reference System (e.g., 'EPSG:4326').
    """
    
    def __init__(self, terrestrial_las_path=None, airborne_las_path=None, crs='EPSG:4326'):
        """
        Initialize the LidarDataAnalyzer with LIDAR data paths and CRS.
        
        Args:
            terrestrial_las_path (str): Path to terrestrial LIDAR .las file.
            airborne_las_path (str): Path to airborne LIDAR .las file.
            crs (str): Coordinate Reference System (default: 'EPSG:4326').
        """
        self.terrestrial_data = None
        self.airborne_data = None
        self.crs = crs
        
        if terrestrial_las_path:
            self.load_terrestrial_data(terrestrial_las_path)
        if airborne_las_path:
            self.load_airborne_data(airborne_las_path)
    
    def load_terrestrial_data(self, las_path):
        """Load terrestrial LIDAR data from a .las file."""
        try:
            self.terrestrial_data = laspy.read(las_path)
            print(f"Terrestrial LIDAR data loaded from {las_path}")
        except Exception as e:
            raise ValueError(f"Error loading terrestrial LIDAR data: {e}")
    
    def load_airborne_data(self, las_path):
        """Load airborne LIDAR data from a .las file."""
        try:
            self.airborne_data = laspy.read(las_path)
            print(f"Airborne LIDAR data loaded from {las_path}")
        except Exception as e:
            raise ValueError(f"Error loading airborne LIDAR data: {e}")
    
    def las_to_geodataframe(self, las_data, data_type='terrestrial'):
        """
        Convert LIDAR data to a GeoDataFrame.
        
        Args:
            las_data (laspy.LasData): LIDAR data to convert.
            data_type (str): Type of data ('terrestrial' or 'airborne').
            
        Returns:
            geopandas.GeoDataFrame: GeoDataFrame containing LIDAR points.
        """
        if las_data is None:
            raise ValueError(f"No {data_type} LIDAR data loaded.")
        
        try:
            # Extract XYZ coordinates
            x = las_data.x
            y = las_data.y
            z = las_data.z
            
            # Create GeoDataFrame
            geometry = [Point(xy) for xy in zip(x, y)]
            gdf = gpd.GeoDataFrame({'Z': z}, geometry=geometry, crs=self.crs)
            
            return gdf
        except Exception as e:
            raise ValueError(f"Error converting {data_type} LIDAR data to GeoDataFrame: {e}")
    
    def visualize_lidar(self, gdf, title='LIDAR Data Visualization'):
        """
        Visualize LIDAR data points.
        
        Args:
            gdf (geopandas.GeoDataFrame): GeoDataFrame containing LIDAR points.
            title (str): Title for the plot.
        """
        try:
            fig, ax = plt.subplots(figsize=(10, 10))
            gdf.plot(ax=ax, markersize=1, column='Z', cmap='viridis', legend=True)
            plt.title(title)
            plt.xlabel('Longitude')
            plt.ylabel('Latitude')
            plt.show()
        except Exception as e:
            raise ValueError(f"Error visualizing LIDAR data: {e}")
    
    def cluster_points(self, gdf, eps=0.5, min_samples=10):
        """
        Cluster LIDAR points using DBSCAN.
        
        Args:
            gdf (geopandas.GeoDataFrame): GeoDataFrame containing LIDAR points.
            eps (float): DBSCAN parameter for maximum distance between points.
            min_samples (int): DBSCAN parameter for minimum points to form a cluster.
            
        Returns:
            geopandas.GeoDataFrame: GeoDataFrame with cluster labels.
        """
        try:
            # Extract coordinates
            coords = np.array([(point.x, point.y, z) for point, z in zip(gdf.geometry, gdf['Z'])])
            
            # Standardize features
            scaler = StandardScaler()
            coords_scaled = scaler.fit_transform(coords)
            
            # Apply DBSCAN
            dbscan = DBSCAN(eps=eps, min_samples=min_samples)
            labels = dbscan.fit_predict(coords_scaled)
            
            # Add labels to GeoDataFrame
            gdf['cluster'] = labels
            
            return gdf
        except Exception as e:
            raise ValueError(f"Error clustering LIDAR points: {e}")
    
    def generate_dem(self, gdf, output_path='dem.tif', resolution=1.0):
        """
        Generate a Digital Elevation Model (DEM) from LIDAR points.
        
        Args:
            gdf (geopandas.GeoDataFrame): GeoDataFrame containing LIDAR points.
            output_path (str): Path to save the DEM raster.
            resolution (float): Resolution of the DEM in meters.
        """
        try:
            # Create a grid from points
            from scipy.interpolate import griddata
            
            # Get bounds
            bounds = gdf.total_bounds
            x_min, y_min, x_max, y_max = bounds
            
            # Create grid
            grid_x, grid_y = np.mgrid[x_min:x_max:resolution, y_min:y_max:resolution]
            
            # Interpolate Z values
            points = np.array([(point.x, point.y) for point in gdf.geometry])
            values = gdf['Z'].values
            grid_z = griddata(points, values, (grid_x, grid_y), method='linear')
            
            # Save as GeoTIFF
            transform = rasterio.transform.from_origin(x_min, y_max, resolution, resolution)
            with rasterio.open(
                output_path,
                'w',
                driver='GTiff',
                height=grid_z.shape[0],
                width=grid_z.shape[1],
                count=1,
                dtype=grid_z.dtype,
                crs=self.crs,
                transform=transform,
            ) as dst:
                dst.write(grid_z, 1)
            
            print(f"DEM saved to {output_path}")
        except Exception as e:
            raise ValueError(f"Error generating DEM: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Initialize analyzer
        analyzer = LidarDataAnalyzer(
            terrestrial_las_path='terrestrial.las',
            airborne_las_path='airborne.las'
        )
        
        # Convert to GeoDataFrame
        terrestrial_gdf = analyzer.las_to_geodataframe(analyzer.terrestrial_data, 'terrestrial')
        airborne_gdf = analyzer.las_to_geodataframe(analyzer.airborne_data, 'airborne')
        
        # Visualize
        analyzer.visualize_lidar(terrestrial_gdf, 'Terrestrial LIDAR Data')
        analyzer.visualize_lidar(airborne_gdf, 'Airborne LIDAR Data')
        
        # Cluster points
        clustered_gdf = analyzer.cluster_points(airborne_gdf)
        analyzer.visualize_lidar(clustered_gdf, 'Clustered LIDAR Data')
        
        # Generate DEM
        analyzer.generate_dem(airborne_gdf, 'airborne_dem.tif')
        
    except Exception as e:
        print(f"Error in LIDAR data analysis: {e}")
```
