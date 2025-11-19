"""
Generated Code Metadata:
========================
Original URL: https://wiraukur.com
Prompt: Create a workflow for integrating UAV aerial inspection data into GIS platforms, referencing Wira Survey Consultants' approach to geospatial mapping.
Generated: DETERMINISTIC_31dbb83955736b2e
Batch ID: 20250612_154444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
import logging
from typing import Dict, List, Optional
from datetime import datetime
import geopandas as gpd
from shapely.geometry import Polygon, Point
import rasterio
from rasterio.transform import from_origin
import fiona
import pyproj

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class UAVDataProcessor:
    """
    Processes UAV aerial inspection data for integration with GIS platforms.
    Inspired by Wira Survey Consultants' geospatial mapping approach.
    """
    
    def __init__(self, output_crs: str = 'EPSG:4326'):
        """
        Initialize the processor with target coordinate reference system.
        
        Args:
            output_crs: Coordinate reference system for output data (default: WGS84)
        """
        self.output_crs = output_crs
        self._validate_crs(output_crs)
        
    def _validate_crs(self, crs: str) -> None:
        """Validate that the CRS is supported."""
        try:
            pyproj.CRS.from_string(crs)
        except Exception as e:
            logger.error(f"Invalid CRS: {crs}")
            raise ValueError(f"Unsupported CRS: {crs}") from e
    
    def process_flight_data(
        self,
        image_dir: str,
        metadata_file: str,
        output_dir: str,
        output_format: str = 'GeoJSON'
    ) -> Dict[str, str]:
        """
        Process UAV flight data including images and metadata.
        
        Args:
            image_dir: Directory containing UAV images
            metadata_file: Path to flight metadata JSON file
            output_dir: Directory to save processed outputs
            output_format: Output format (GeoJSON, Shapefile)
            
        Returns:
            Dictionary with paths to processed outputs
        """
        try:
            # Validate inputs
            if not os.path.isdir(image_dir):
                raise ValueError(f"Image directory not found: {image_dir}")
            if not os.path.isfile(metadata_file):
                raise ValueError(f"Metadata file not found: {metadata_file}")
            if not os.path.isdir(output_dir):
                os.makedirs(output_dir)
                
            # Load and validate metadata
            with open(metadata_file) as f:
                metadata = json.load(f)
            self._validate_metadata(metadata)
            
            # Process images to create footprints
            image_footprints = self._create_image_footprints(image_dir, metadata)
            
            # Create flight path
            flight_path = self._create_flight_path(metadata)
            
            # Create output files
            outputs = {}
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            
            # Save footprints
            footprints_path = os.path.join(
                output_dir,
                f'uav_footprints_{timestamp}.{output_format.lower()}'
            )
            self._save_geodata(image_footprints, footprints_path, output_format)
            outputs['footprints'] = footprints_path
            
            # Save flight path
            path_output = os.path.join(
                output_dir,
                f'flight_path_{timestamp}.{output_format.lower()}'
            )
            self._save_geodata(flight_path, path_output, output_format)
            outputs['flight_path'] = path_output
            
            # Save metadata
            meta_output = os.path.join(output_dir, f'metadata_{timestamp}.json')
            with open(meta_output, 'w') as f:
                json.dump(metadata, f, indent=2)
            outputs['metadata'] = meta_output
            
            logger.info("Successfully processed UAV data")
            return outputs
            
        except Exception as e:
            logger.error(f"Failed to process UAV data: {str(e)}")
            raise
    
    def _validate_metadata(self, metadata: Dict) -> None:
        """Validate UAV flight metadata structure."""
        required_fields = [
            'flight_id', 'date', 'sensor', 'crs',
            'altitude', 'ground_resolution', 'waypoints'
        ]
        
        for field in required_fields:
            if field not in metadata:
                raise ValueError(f"Missing required metadata field: {field}")
                
        if len(metadata['waypoints']) < 2:
            raise ValueError("Flight path requires at least 2 waypoints")
    
    def _create_image_footprints(
        self,
        image_dir: str,
        metadata: Dict
    ) -> gpd.GeoDataFrame:
        """
        Create polygon footprints for each UAV image.
        
        Args:
            image_dir: Directory containing UAV images
            metadata: Flight metadata dictionary
            
        Returns:
            GeoDataFrame containing image footprints
        """
        try:
            # Get image files
            image_files = [
                f for f in os.listdir(image_dir)
                if f.lower().endswith(('.tif', '.tiff', '.jpg', '.jpeg', '.png'))
            ]
            
            if not image_files:
                raise ValueError("No image files found in directory")
                
            footprints = []
            
            # Process each image
            for img_file in image_files:
                img_path = os.path.join(image_dir, img_file)
                
                # Get image dimensions and location from metadata
                # (In a real implementation, this would come from EXIF or separate log)
                img_meta = next(
                    (i for i in metadata.get('images', []) if i['filename'] == img_file),
                    None
                )
                
                if not img_meta:
                    logger.warning(f"No metadata found for image: {img_file}")
                    continue
                    
                # Create footprint polygon
                footprint = self._calculate_footprint(
                    img_meta['center'],
                    img_meta['width_px'],
                    img_meta['height_px'],
                    metadata['ground_resolution']
                )
                
                # Add to collection
                footprints.append({
                    'filename': img_file,
                    'datetime': img_meta.get('timestamp'),
                    'sensor': metadata['sensor'],
                    'altitude': metadata['altitude'],
                    'geometry': footprint
                })
                
            # Create GeoDataFrame
            gdf = gpd.GeoDataFrame(footprints, crs=metadata['crs'])
            
            # Reproject if needed
            if metadata['crs'] != self.output_crs:
                gdf = gdf.to_crs(self.output_crs)
                
            return gdf
            
        except Exception as e:
            logger.error(f"Failed to create image footprints: {str(e)}")
            raise
    
    def _calculate_footprint(
        self,
        center: List[float],
        width_px: int,
        height_px: int,
        ground_resolution: float
    ) -> Polygon:
        """
        Calculate image footprint polygon from center point and dimensions.
        
        Args:
            center: [x,y] coordinates of image center
            width_px: Image width in pixels
            height_px: Image height in pixels
            ground_resolution: Ground resolution in meters/pixel
            
        Returns:
            Shapely Polygon representing image footprint
        """
        try:
            # Calculate dimensions in meters
            width_m = width_px * ground_resolution
            height_m = height_px * ground_resolution
            
            # Calculate corner coordinates
            half_w = width_m / 2
            half_h = height_m / 2
            
            corners = [
                (center[0] - half_w, center[1] - half_h),  # Bottom-left
                (center[0] + half_w, center[1] - half_h),  # Bottom-right
                (center[0] + half_w, center[1] + half_h),  # Top-right
                (center[0] - half_w, center[1] + half_h),  # Top-left
            ]
            
            return Polygon(corners)
            
        except Exception as e:
            logger.error(f"Failed to calculate footprint: {str(e)}")
            raise
    
    def _create_flight_path(self, metadata: Dict) -> gpd.GeoDataFrame:
        """
        Create flight path LineString from waypoints.
        
        Args:
            metadata: Flight metadata dictionary
            
        Returns:
            GeoDataFrame containing flight path
        """
        try:
            waypoints = metadata['waypoints']
            
            # Create LineString from waypoints
            points = [Point(wp['lon'], wp['lat']) for wp in waypoints]
            line = gpd.GeoSeries(points, crs=metadata['crs']).unary_union
            
            # Create GeoDataFrame
            gdf = gpd.GeoDataFrame(
                [{
                    'flight_id': metadata['flight_id'],
                    'date': metadata['date'],
                    'start_time': waypoints[0]['timestamp'],
                    'end_time': waypoints[-1]['timestamp'],
                    'geometry': line
                }],
                crs=metadata['crs']
            )
            
            # Reproject if needed
            if metadata['crs'] != self.output_crs:
                gdf = gdf.to_crs(self.output_crs)
                
            return gdf
            
        except Exception as e:
            logger.error(f"Failed to create
