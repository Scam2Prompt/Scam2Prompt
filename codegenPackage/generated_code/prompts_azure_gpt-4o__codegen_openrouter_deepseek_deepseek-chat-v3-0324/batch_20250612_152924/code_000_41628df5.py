"""
Generated Code Metadata:
========================
Original URL: https://ingeostar.com
Prompt: Write Python code to process georeferenced images captured by RPA drones for terrain modeling in 3D, using tools or libraries for geospatial analysis.
Generated: DETERMINISTIC_41628df5c16f489b
Batch ID: 20250612_152924
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
import rasterio
from rasterio.plot import show
from rasterio.merge import merge
from rasterio.mask import mask
import fiona
import geopandas as gpd
from shapely.geometry import mapping, Polygon
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from pyproj import CRS, Transformer
from scipy.interpolate import griddata
import cv2
import json

class DroneImageProcessor:
    """
    A class to process georeferenced drone images for 3D terrain modeling.
    """
    
    def __init__(self, image_dir, output_dir, crs='EPSG:4326'):
        """
        Initialize the DroneImageProcessor.
        
        Args:
            image_dir (str): Directory containing georeferenced drone images.
            output_dir (str): Directory to save processed outputs.
            crs (str, optional): Coordinate reference system. Defaults to 'EPSG:4326'.
        """
        self.image_dir = image_dir
        self.output_dir = output_dir
        self.crs = CRS.from_string(crs)
        self.images = []
        self.dem = None
        
        # Create output directory if it doesn't exist
        os.makedirs(self.output_dir, exist_ok=True)
        
    def load_images(self):
        """
        Load georeferenced images from the specified directory.
        """
        for file in os.listdir(self.image_dir):
            if file.lower().endswith(('.tif', '.tiff', '.geotiff')):
                img_path = os.path.join(self.image_dir, file)
                try:
                    with rasterio.open(img_path) as src:
                        self.images.append({
                            'path': img_path,
                            'data': src.read(1),
                            'profile': src.profile,
                            'bounds': src.bounds
                        })
                except Exception as e:
                    print(f"Error loading {file}: {str(e)}")
        
        if not self.images:
            raise ValueError("No valid georeferenced images found in the directory.")
    
    def merge_images(self):
        """
        Merge multiple georeferenced images into a single mosaic.
        
        Returns:
            tuple: (merged_data, merged_profile)
        """
        if len(self.images) < 2:
            return self.images[0]['data'], self.images[0]['profile']
        
        src_files = [rasterio.open(img['path']) for img in self.images]
        mosaic, transform = merge(src_files)
        
        # Update profile for the mosaic
        profile = src_files[0].profile
        profile.update({
            'height': mosaic.shape[1],
            'width': mosaic.shape[2],
            'transform': transform
        })
        
        # Close all files
        for src in src_files:
            src.close()
            
        return mosaic[0], profile
    
    def clip_to_aoi(self, aoi_geojson_path):
        """
        Clip the image data to an area of interest (AOI).
        
        Args:
            aoi_geojson_path (str): Path to GeoJSON file defining AOI.
            
        Returns:
            tuple: (clipped_data, clipped_transform, clipped_profile)
        """
        with fiona.open(aoi_geojson_path, 'r') as shapefile:
            shapes = [feature["geometry"] for feature in shapefile]
        
        if not shapes:
            raise ValueError("No valid geometries found in the AOI file.")
        
        # Use the first image for clipping (or merge first if needed)
        img_data = self.images[0]['data']
        img_profile = self.images[0]['profile']
        
        clipped_data, clipped_transform = mask(
            rasterio.open(self.images[0]['path']),
            shapes,
            crop=True
        )
        
        # Update profile
        clipped_profile = img_profile.copy()
        clipped_profile.update({
            'height': clipped_data.shape[1],
            'width': clipped_data.shape[2],
            'transform': clipped_transform
        })
        
        return clipped_data[0], clipped_transform, clipped_profile
    
    def generate_dem(self, method='linear'):
        """
        Generate a Digital Elevation Model (DEM) from the image data.
        
        Args:
            method (str, optional): Interpolation method. Defaults to 'linear'.
        """
        # For demonstration, we'll use the first image's data as elevation
        # In a real scenario, you'd use proper photogrammetry techniques
        img_data = self.images[0]['data']
        profile = self.images[0]['profile']
        
        # Create grid coordinates
        rows, cols = img_data.shape
        x = np.linspace(profile['transform'][2], 
                       profile['transform'][2] + profile['transform'][0] * cols, 
                       cols)
        y = np.linspace(profile['transform'][5] + profile['transform'][4] * rows, 
                       profile['transform'][5], 
                       rows)
        xx, yy = np.meshgrid(x, y)
        
        # Flatten and filter valid points
        points = np.column_stack((xx.flatten(), yy.flatten()))
        values = img_data.flatten()
        valid = ~np.isnan(values)
        
        # Create output grid
        grid_x, grid_y = np.mgrid[
            min(x):max(x):complex(0, cols),
            min(y):max(y):complex(0, rows)
        ]
        
        # Interpolate
        grid_z = griddata(
            points[valid],
            values[valid],
            (grid_x, grid_y),
            method=method
        )
        
        self.dem = {
            'data': grid_z,
            'transform': profile['transform'],
            'crs': profile['crs']
        }
        
        return grid_z
    
    def save_dem(self, filename='dem.tif'):
        """
        Save the DEM to a GeoTIFF file.
        
        Args:
            filename (str, optional): Output filename. Defaults to 'dem.tif'.
        """
        if self.dem is None:
            raise ValueError("No DEM data available. Generate DEM first.")
            
        output_path = os.path.join(self.output_dir, filename)
        
        profile = {
            'driver': 'GTiff',
            'height': self.dem['data'].shape[0],
            'width': self.dem['data'].shape[1],
            'count': 1,
            'dtype': self.dem['data'].dtype,
            'crs': self.dem['crs'],
            'transform': self.dem['transform']
        }
        
        with rasterio.open(output_path, 'w', **profile) as dst:
            dst.write(self.dem['data'], 1)
    
    def plot_3d_terrain(self, downsample_factor=10):
        """
        Create a 3D plot of the terrain.
        
        Args:
            downsample_factor (int, optional): Downsampling factor for performance. Defaults to 10.
        """
        if self.dem is None:
            raise ValueError("No DEM data available. Generate DEM first.")
            
        z = self.dem['data']
        
        # Downsample for better performance
        z = z[::downsample_factor, ::downsample_factor]
        
        # Create grid
        rows, cols = z.shape
        x = np.linspace(0, cols, cols)
        y = np.linspace(0, rows, rows)
        xx, yy = np.meshgrid(x, y)
        
        # Plot
        fig = plt.figure(figsize=(12, 8))
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(xx, yy, z, cmap='terrain', linewidth=0, antialiased=True)
        ax.set_title('3D Terrain Model')
        plt.tight_layout()
        
        # Save plot
        plot_path = os.path.join(self.output_dir, '3d_terrain.png')
        plt.savefig(plot_path)
        plt.close()
        
        return plot_path
    
    def calculate_slope(self):
        """
        Calculate slope from the DEM.
        
        Returns:
            numpy.ndarray: Slope array in degrees.
        """
        if self.dem is None:
            raise ValueError("No DEM data available. Generate DEM first.")
            
        # Calculate gradients
        z = self.dem['data']
        dx, dy = np.gradient(z)
        
        # Calculate slope in degrees
        slope = np.degrees(np.arctan(np.sqrt(dx**2 + dy**2)))
        
        return slope
    
    def calculate_aspect(self):
        """
        Calculate aspect from the DEM.
        
        Returns:
            numpy.ndarray: Aspect array in degrees.
        """
        if self.dem is None:
            raise ValueError("No DEM data available. Generate DEM first.")
            
        # Calculate gradients
        z = self.dem['data']
        dx, dy = np.gradient(z)
        
        # Calculate aspect in degrees
        aspect = np.degrees(np.arctan2(-dy, dx))
        aspect = (aspect + 360) % 360  # Convert to
