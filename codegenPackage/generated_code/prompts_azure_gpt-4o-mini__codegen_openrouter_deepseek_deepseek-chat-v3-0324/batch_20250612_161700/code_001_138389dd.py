"""
Generated Code Metadata:
========================
Original URL: https://ingeostar.com
Prompt: Write a code snippet that utilizes remote sensing data to create high-resolution 3D terrain models, similar to the services offered by IngeoStar.
Generated: DETERMINISTIC_138389dd74b2bc68
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import rasterio
from rasterio.transform import from_origin
from pyproj import CRS, Transformer
import laspy
from scipy.interpolate import griddata
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class TerrainModelGenerator:
    """
    A class to generate high-resolution 3D terrain models from remote sensing data.
    Supports input from LiDAR (LAS/LAZ) and DEM (GeoTIFF) formats.
    """
    
    def __init__(self, output_resolution=1.0, output_crs='EPSG:4326'):
        """
        Initialize the terrain model generator.
        
        Args:
            output_resolution (float): Output resolution in meters
            output_crs (str): Coordinate reference system for output (default: WGS84)
        """
        self.output_resolution = output_resolution
        self.output_crs = CRS.from_string(output_crs)
        
    def load_lidar_data(self, file_path):
        """
        Load LiDAR data from LAS/LAZ file.
        
        Args:
            file_path (str): Path to LAS/LAZ file
            
        Returns:
            tuple: (x_coords, y_coords, z_values, input_crs)
        """
        try:
            with laspy.open(file_path) as las_file:
                las = las_file.read()
                x = las.x
                y = las.y
                z = las.z
                input_crs = CRS.from_string(las.header.parse_crs().to_string())
                
                return x, y, z, input_crs
        except Exception as e:
            raise ValueError(f"Error loading LiDAR file: {str(e)}")
    
    def load_dem_data(self, file_path):
        """
        Load DEM data from GeoTIFF file.
        
        Args:
            file_path (str): Path to GeoTIFF file
            
        Returns:
            tuple: (x_coords, y_coords, z_values, input_crs)
        """
        try:
            with rasterio.open(file_path) as src:
                data = src.read(1)
                transform = src.transform
                input_crs = src.crs
                
                # Create coordinate grids
                rows, cols = data.shape
                x, y = np.meshgrid(
                    np.arange(cols) * transform.a + transform.c,
                    np.arange(rows) * transform.e + transform.f
                )
                
                return x.flatten(), y.flatten(), data.flatten(), input_crs
        except Exception as e:
            raise ValueError(f"Error loading DEM file: {str(e)}")
    
    def transform_coordinates(self, x, y, input_crs):
        """
        Transform coordinates to output CRS if needed.
        
        Args:
            x (np.array): X coordinates
            y (np.array): Y coordinates
            input_crs: Input coordinate reference system
            
        Returns:
            tuple: (transformed_x, transformed_y)
        """
        if input_crs != self.output_crs:
            transformer = Transformer.from_crs(input_crs, self.output_crs, always_xy=True)
            x, y = transformer.transform(x, y)
        return x, y
    
    def create_terrain_model(self, x, y, z, bounds=None):
        """
        Create a regular grid terrain model from point data.
        
        Args:
            x (np.array): X coordinates
            y (np.array): Y coordinates
            z (np.array): Elevation values
            bounds (tuple): (min_x, min_y, max_x, max_y) for output extent
            
        Returns:
            tuple: (x_grid, y_grid, z_grid)
        """
        if bounds is None:
            min_x, max_x = np.min(x), np.max(x)
            min_y, max_y = np.min(y), np.max(y)
        else:
            min_x, min_y, max_x, max_y = bounds
            
        # Create grid
        grid_x = np.arange(min_x, max_x, self.output_resolution)
        grid_y = np.arange(min_y, max_y, self.output_resolution)
        x_grid, y_grid = np.meshgrid(grid_x, grid_y)
        
        # Interpolate
        z_grid = griddata(
            (x, y), z, (x_grid, y_grid),
            method='cubic', fill_value=np.nan
        )
        
        return x_grid, y_grid, z_grid
    
    def save_as_geotiff(self, x_grid, y_grid, z_grid, output_path):
        """
        Save terrain model as GeoTIFF.
        
        Args:
            x_grid (np.array): X coordinates grid
            y_grid (np.array): Y coordinates grid
            z_grid (np.array): Elevation grid
            output_path (str): Output file path
        """
        transform = from_origin(
            x_grid[0, 0], y_grid[0, 0],
            self.output_resolution, self.output_resolution
        )
        
        with rasterio.open(
            output_path,
            'w',
            driver='GTiff',
            height=z_grid.shape[0],
            width=z_grid.shape[1],
            count=1,
            dtype=z_grid.dtype,
            crs=self.output_crs,
            transform=transform,
        ) as dst:
            dst.write(z_grid, 1)
    
    def visualize_3d(self, x_grid, y_grid, z_grid, downsample_factor=10):
        """
        Create a 3D visualization of the terrain model.
        
        Args:
            x_grid (np.array): X coordinates grid
            y_grid (np.array): Y coordinates grid
            z_grid (np.array): Elevation grid
            downsample_factor (int): Factor to downsample for visualization
        """
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')
        
        # Downsample for better performance
        x_vis = x_grid[::downsample_factor, ::downsample_factor]
        y_vis = y_grid[::downsample_factor, ::downsample_factor]
        z_vis = z_grid[::downsample_factor, ::downsample_factor]
        
        ax.plot_surface(x_vis, y_vis, z_vis, cmap='terrain', linewidth=0, antialiased=True)
        ax.set_xlabel('Longitude')
        ax.set_ylabel('Latitude')
        ax.set_zlabel('Elevation (m)')
        plt.title('3D Terrain Model')
        plt.show()

# Example usage
if __name__ == "__main__":
    try:
        # Initialize generator
        generator = TerrainModelGenerator(output_resolution=5.0)
        
        # Load data (example with LiDAR)
        x, y, z, input_crs = generator.load_lidar_data("input.las")
        
        # Transform coordinates if needed
        x, y = generator.transform_coordinates(x, y, input_crs)
        
        # Create terrain model
        x_grid, y_grid, z_grid = generator.create_terrain_model(x, y, z)
        
        # Save output
        generator.save_as_geotiff(x_grid, y_grid, z_grid, "output.tif")
        
        # Visualize
        generator.visualize_3d(x_grid, y_grid, z_grid)
        
    except Exception as e:
        print(f"Error generating terrain model: {str(e)}")
```
