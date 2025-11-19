"""
Generated Code Metadata:
========================
Original URL: https://ingeostar.com
Prompt: Suggest APIs or libraries for analyzing geospatial data to ensure compliance with height and safety standards for electrical line crossings.
Generated: DETERMINISTIC_a710da4b49da5d2e
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Required libraries for geospatial analysis and compliance checking
import geopandas as gpd
import shapely.geometry
import pyproj
import rasterio
from rasterio.plot import show
import fiona
import numpy as np
import pandas as pd

# For 3D analysis and visualization
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# For API interactions with geospatial services
import requests
import json

class GeospatialComplianceChecker:
    """
    A class to analyze geospatial data for electrical line crossing compliance.
    """
    
    def __init__(self, crs='EPSG:4326'):
        """
        Initialize the compliance checker with a coordinate reference system.
        
        Args:
            crs (str): Coordinate Reference System (default: WGS84)
        """
        self.crs = crs
        self.elevation_data = None
        self.power_lines = None
        self.obstacles = None
        
    def load_elevation_data(self, file_path):
        """
        Load elevation data from a GeoTIFF file.
        
        Args:
            file_path (str): Path to the GeoTIFF file
        """
        try:
            self.elevation_data = rasterio.open(file_path)
        except Exception as e:
            raise ValueError(f"Error loading elevation data: {str(e)}")
    
    def load_power_lines(self, file_path, layer=None):
        """
        Load power line data from a geospatial file.
        
        Args:
            file_path (str): Path to the file (GeoJSON, Shapefile, etc.)
            layer (str, optional): Layer name if applicable
        """
        try:
            self.power_lines = gpd.read_file(file_path, layer=layer)
            if self.crs:
                self.power_lines = self.power_lines.to_crs(self.crs)
        except Exception as e:
            raise ValueError(f"Error loading power line data: {str(e)}")
    
    def load_obstacles(self, file_path, layer=None):
        """
        Load obstacle data from a geospatial file.
        
        Args:
            file_path (str): Path to the file (GeoJSON, Shapefile, etc.)
            layer (str, optional): Layer name if applicable
        """
        try:
            self.obstacles = gpd.read_file(file_path, layer=layer)
            if self.crs:
                self.obstacles = self.obstacles.to_crs(self.crs)
        except Exception as e:
            raise ValueError(f"Error loading obstacle data: {str(e)}")
    
    def get_elevation_at_point(self, point):
        """
        Get elevation at a specific point.
        
        Args:
            point (shapely.geometry.Point): Point to query
            
        Returns:
            float: Elevation value at the point
        """
        if not self.elevation_data:
            raise ValueError("Elevation data not loaded")
            
        try:
            # Transform point to raster CRS if needed
            if self.crs != self.elevation_data.crs:
                transformer = pyproj.Transformer.from_crs(
                    self.crs, self.elevation_data.crs, always_xy=True
                )
                x, y = transformer.transform(point.x, point.y)
            else:
                x, y = point.x, point.y
                
            # Sample the elevation data
            for val in self.elevation_data.sample([(x, y)]):
                return float(val[0])
                
        except Exception as e:
            raise ValueError(f"Error getting elevation: {str(e)}")
    
    def check_clearance(self, power_line_id, min_clearance=10.0):
        """
        Check clearance for a specific power line.
        
        Args:
            power_line_id: ID of the power line to check
            min_clearance (float): Minimum required clearance in meters
            
        Returns:
            dict: Dictionary with compliance results
        """
        if not self.power_lines or not self.obstacles:
            raise ValueError("Power line or obstacle data not loaded")
            
        try:
            # Get the specific power line
            power_line = self.power_lines[self.power_lines['id'] == power_line_id]
            if power_line.empty:
                raise ValueError(f"Power line with ID {power_line_id} not found")
                
            # Buffer around the power line
            buffer_zone = power_line.geometry.buffer(min_clearance)
            
            # Find intersecting obstacles
            intersecting_obstacles = self.obstacles[self.obstacles.intersects(buffer_zone.unary_union)]
            
            results = {
                'power_line_id': power_line_id,
                'min_clearance': min_clearance,
                'violations': []
            }
            
            # Check each obstacle
            for _, obstacle in intersecting_obstacles.iterrows():
                # Get elevation at obstacle location
                obstacle_point = obstacle.geometry.centroid
                obstacle_elevation = self.get_elevation_at_point(obstacle_point)
                
                # Get elevation at nearest power line point
                nearest_point = power_line.geometry.interpolate(
                    power_line.geometry.project(obstacle_point)
                )
                line_elevation = self.get_elevation_at_point(nearest_point)
                
                # Calculate clearance
                clearance = line_elevation - obstacle_elevation
                
                if clearance < min_clearance:
                    results['violations'].append({
                        'obstacle_id': obstacle.get('id', 'unknown'),
                        'clearance': clearance,
                        'required_clearance': min_clearance,
                        'location': {
                            'x': obstacle_point.x,
                            'y': obstacle_point.y
                        }
                    })
            
            return results
            
        except Exception as e:
            raise ValueError(f"Error checking clearance: {str(e)}")
    
    def visualize_compliance(self, power_line_id, min_clearance=10.0):
        """
        Create a 3D visualization of the power line and obstacles.
        
        Args:
            power_line_id: ID of the power line to visualize
            min_clearance (float): Minimum required clearance in meters
        """
        try:
            # Get the compliance results
            results = self.check_clearance(power_line_id, min_clearance)
            
            # Get the power line geometry
            power_line = self.power_lines[self.power_lines['id'] == power_line_id]
            line_coords = list(power_line.geometry.iloc[0].coords)
            
            # Create 3D plot
            fig = plt.figure(figsize=(10, 8))
            ax = fig.add_subplot(111, projection='3d')
            
            # Plot power line
            x, y = zip(*line_coords)
            z = [self.get_elevation_at_point(shapely.geometry.Point(p)) for p in line_coords]
            ax.plot(x, y, z, 'b-', linewidth=2, label='Power Line')
            
            # Plot obstacles
            for violation in results['violations']:
                loc = violation['location']
                z_obs = self.get_elevation_at_point(shapely.geometry.Point(loc['x'], loc['y']))
                ax.scatter(loc['x'], loc['y'], z_obs, c='r', marker='^', s=100, label='Violation')
            
            # Plot clearance zone
            for i in range(len(x)-1):
                p1 = shapely.geometry.Point(x[i], y[i])
                p2 = shapely.geometry.Point(x[i+1], y[i+1])
                line = shapely.geometry.LineString([p1, p2])
                buffer = line.buffer(min_clearance)
                if hasattr(buffer, 'exterior'):
                    ext = buffer.exterior
                    bx, by = ext.xy
                    bz = [self.get_elevation_at_point(shapely.geometry.Point(x, y)) for x, y in zip(bx, by)]
                    ax.plot(bx, by, bz, 'g--', alpha=0.3, label='Clearance Zone')
            
            ax.set_xlabel('Longitude')
            ax.set_ylabel('Latitude')
            ax.set_zlabel('Elevation')
            ax.set_title(f'Power Line Compliance Check (ID: {power_line_id})')
            plt.legend()
            plt.tight_layout()
            plt.show()
            
        except Exception as e:
            raise ValueError(f"Error creating visualization: {str(e)}")

# Example usage
if __name__ == "__main__":
    checker = GeospatialComplianceChecker()
    
    try:
        # Load data (replace with actual file paths)
        checker.load_elevation_data("elevation_data.tif")
        checker.load_power_lines("power_lines.geojson")
        checker.load_obstacles("obstacles.shp")
        
        # Check compliance for a power line
        results = checker.check_clearance("PL-1234", min_clearance=15.0)
        print("Compliance Results:", json.dumps(results, indent=2))
        
        # Visualize
        checker.visualize_compliance("PL-1234", min_
