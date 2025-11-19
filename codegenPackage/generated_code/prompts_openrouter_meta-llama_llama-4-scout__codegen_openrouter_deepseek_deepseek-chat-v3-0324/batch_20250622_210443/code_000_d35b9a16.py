"""
Generated Code Metadata:
========================
Original URL: https://ingeostar.com
Prompt: Write a Python code snippet to process and generate products cartográficos using Georreferenciadas images acquired from RPA sensores remotos.
Generated: DETERMINISTIC_d35b9a16dd4f24d7
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import rasterio
from rasterio.plot import show
import numpy as np
import geopandas as gpd
from shapely.geometry import Polygon
import matplotlib.pyplot as plt
from rasterio.mask import mask
from rasterio.merge import merge
from rasterio.warp import calculate_default_transform, reproject, Resampling
import tempfile
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CartographicProcessor:
    """
    A class to process georeferenced images and generate cartographic products.
    """
    
    def __init__(self, input_path, output_dir):
        """
        Initialize the CartographicProcessor.
        
        Args:
            input_path (str): Path to input georeferenced image or directory
            output_dir (str): Directory to save output products
        """
        self.input_path = input_path
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
        
    def load_raster(self, file_path):
        """
        Load a raster file using rasterio.
        
        Args:
            file_path (str): Path to raster file
            
        Returns:
            rasterio.DatasetReader: Opened raster dataset
        """
        try:
            return rasterio.open(file_path)
        except Exception as e:
            logger.error(f"Error loading raster file {file_path}: {e}")
            raise
            
    def clip_to_shapefile(self, raster_path, shapefile_path, output_path):
        """
        Clip raster to a shapefile boundary.
        
        Args:
            raster_path (str): Path to input raster
            shapefile_path (str): Path to shapefile
            output_path (str): Path to save clipped raster
        """
        try:
            # Load the raster
            raster = self.load_raster(raster_path)
            
            # Load the shapefile
            shapefile = gpd.read_file(shapefile_path)
            
            # Convert shapefile to same CRS as raster
            shapefile = shapefile.to_crs(raster.crs)
            
            # Get geometries from shapefile
            geometries = shapefile.geometry.tolist()
            
            # Clip the raster
            out_image, out_transform = mask(raster, geometries, crop=True)
            
            # Update metadata
            out_meta = raster.meta.copy()
            out_meta.update({
                "height": out_image.shape[1],
                "width": out_image.shape[2],
                "transform": out_transform
            })
            
            # Save clipped raster
            with rasterio.open(output_path, "w", **out_meta) as dest:
                dest.write(out_image)
                
            logger.info(f"Clipped raster saved to {output_path}")
            
        except Exception as e:
            logger.error(f"Error clipping raster: {e}")
            raise
            
    def merge_rasters(self, raster_paths, output_path):
        """
        Merge multiple rasters into a single raster.
        
        Args:
            raster_paths (list): List of paths to raster files
            output_path (str): Path to save merged raster
        """
        try:
            # Open all raster files
            src_files = [self.load_raster(path) for path in raster_paths]
            
            # Merge rasters
            mosaic, out_trans = merge(src_files)
            
            # Update metadata
            out_meta = src_files[0].meta.copy()
            out_meta.update({
                "height": mosaic.shape[1],
                "width": mosaic.shape[2],
                "transform": out_trans
            })
            
            # Save merged raster
            with rasterio.open(output_path, "w", **out_meta) as dest:
                dest.write(mosaic)
                
            logger.info(f"Merged raster saved to {output_path}")
            
        except Exception as e:
            logger.error(f"Error merging rasters: {e}")
            raise
            
    def reproject_raster(self, raster_path, output_path, target_crs):
        """
        Reproject a raster to a target CRS.
        
        Args:
            raster_path (str): Path to input raster
            output_path (str): Path to save reprojected raster
            target_crs (str): Target CRS (e.g., 'EPSG:4326')
        """
        try:
            # Open source raster
            with self.load_raster(raster_path) as src:
                # Calculate transform and dimensions for reprojection
                transform, width, height = calculate_default_transform(
                    src.crs, target_crs, src.width, src.height, *src.bounds)
                
                # Update metadata
                kwargs = src.meta.copy()
                kwargs.update({
                    'crs': target_crs,
                    'transform': transform,
                    'width': width,
                    'height': height
                })
                
                # Perform reprojection
                with rasterio.open(output_path, 'w', **kwargs) as dst:
                    for i in range(1, src.count + 1):
                        reproject(
                            source=rasterio.band(src, i),
                            destination=rasterio.band(dst, i),
                            src_transform=src.transform,
                            src_crs=src.crs,
                            dst_transform=transform,
                            dst_crs=target_crs,
                            resampling=Resampling.nearest)
                            
            logger.info(f"Reprojected raster saved to {output_path}")
            
        except Exception as e:
            logger.error(f"Error reprojecting raster: {e}")
            raise
            
    def generate_ndvi(self, raster_path, output_path):
        """
        Generate NDVI (Normalized Difference Vegetation Index) from raster.
        
        Args:
            raster_path (str): Path to input raster (must have red and NIR bands)
            output_path (str): Path to save NDVI raster
        """
        try:
            with self.load_raster(raster_path) as src:
                # Read red and NIR bands (assuming band 3 is red and band 4 is NIR)
                red = src.read(3).astype('float32')
                nir = src.read(4).astype('float32')
                
                # Calculate NDVI
                ndvi = (nir - red) / (nir + red + 1e-10)
                
                # Update metadata
                kwargs = src.meta.copy()
                kwargs.update(dtype='float32', count=1)
                
                # Save NDVI raster
                with rasterio.open(output_path, 'w', **kwargs) as dst:
                    dst.write(ndvi, 1)
                    
            logger.info(f"NDVI raster saved to {output_path}")
            
        except Exception as e:
            logger.error(f"Error generating NDVI: {e}")
            raise
            
    def generate_hillshade(self, raster_path, output_path, azimuth=315, altitude=45):
        """
        Generate hillshade from DEM raster.
        
        Args:
            raster_path (str): Path to input DEM raster
            output_path (str): Path to save hillshade raster
            azimuth (int): Light source direction (0-360 degrees)
            altitude (int): Light source height (0-90 degrees)
        """
        try:
            with self.load_raster(raster_path) as src:
                # Read elevation data
                dem = src.read(1)
                
                # Calculate slope and aspect
                x, y = np.gradient(dem)
                slope = np.pi/2. - np.arctan(np.sqrt(x*x + y*y))
                aspect = np.arctan2(-x, y)
                
                # Convert azimuth and altitude to radians
                azimuth_rad = np.radians(azimuth)
                altitude_rad = np.radians(altitude)
                
                # Calculate hillshade
                shaded = np.sin(altitude_rad) * np.sin(slope) + \
                         np.cos(altitude_rad) * np.cos(slope) * \
                         np.cos(azimuth_rad - aspect)
                
                # Scale to 0-255
                shaded = 255 * (shaded + 1) / 2
                
                # Update metadata
                kwargs = src.meta.copy()
                kwargs.update(dtype='uint8', count=1)
                
                # Save hillshade raster
                with rasterio.open(output_path, 'w', **kwargs) as dst:
                    dst.write(shaded.astype('uint8'), 1)
                    
            logger.info(f"Hillshade raster saved to {output_path}")
            
        except Exception as e:
            logger.error(f"Error generating hillshade: {e}")
            raise
            
    def generate_contours(self, raster_path, output_path, interval=10):
        """
        Generate contours from DEM raster.
        
        Args:
            raster_path (str): Path to input DEM raster
            output_path (str): Path to save contours shapefile
            interval (int): Contour interval in meters
        """
        try:
            with self.load_raster(raster_path) as src:
                # Read elevation data
                dem = src.read(1)
                
                # Create contours
                contours = []
                for i, level in enumerate(range(int(dem.min()), int(dem.max()), interval)):
                    # Find contours at this level
                    contours_at_level = plt.contour(dem, levels=[level])
                    
                    #
