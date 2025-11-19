"""
Generated Code Metadata:
========================
Original URL: https://ingeostar.com
Prompt: Develop a GIS application that processes and generates specialized cartographic products, integrating topographic data and autocontrol features as mentioned on IngeoStar's site.
Generated: DETERMINISTIC_a1b2ba021fcd844b
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import sys
import json
import logging
from typing import Dict, List, Optional, Tuple
import fiona
import rasterio
from rasterio.plot import show
import matplotlib.pyplot as plt
from shapely.geometry import shape, mapping
from pyproj import CRS, Transformer
import numpy as np
from dataclasses import dataclass

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('gis_processor.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

@dataclass
class GeoData:
    """Class to hold geographic data information."""
    file_path: str
    data_type: str  # 'vector' or 'raster'
    crs: str
    metadata: Dict
    data: Optional[object] = None

class GISProcessor:
    """Main class for processing GIS data and generating cartographic products."""
    
    def __init__(self):
        self.data_sources: Dict[str, GeoData] = {}
        self.output_dir = "output"
        os.makedirs(self.output_dir, exist_ok=True)
    
    def load_data(self, file_path: str) -> str:
        """Load geographic data from file.
        
        Args:
            file_path: Path to the GIS data file
            
        Returns:
            str: ID of the loaded data source
            
        Raises:
            FileNotFoundError: If file doesn't exist
            ValueError: If file format is not supported
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        
        try:
            if file_path.lower().endswith(('.shp', '.geojson', '.gpkg')):
                with fiona.open(file_path) as src:
                    data_type = 'vector'
                    crs = src.crs['init'] if 'init' in src.crs else str(CRS.from_dict(src.crs))
                    metadata = {
                        'driver': src.driver,
                        'schema': src.schema,
                        'bounds': src.bounds,
                        'features_count': len(src)
                    }
                    data = [feature for feature in src]
                    
            elif file_path.lower().endswith(('.tif', '.tiff', '.geotiff')):
                with rasterio.open(file_path) as src:
                    data_type = 'raster'
                    crs = src.crs.to_string()
                    metadata = {
                        'driver': src.driver,
                        'width': src.width,
                        'height': src.height,
                        'count': src.count,
                        'dtype': src.dtypes[0],
                        'transform': list(src.transform),
                        'bounds': src.bounds
                    }
                    data = src.read()
            else:
                raise ValueError("Unsupported file format")
            
            data_id = os.path.basename(file_path)
            self.data_sources[data_id] = GeoData(
                file_path=file_path,
                data_type=data_type,
                crs=crs,
                metadata=metadata,
                data=data
            )
            
            logger.info(f"Successfully loaded data: {data_id}")
            return data_id
            
        except Exception as e:
            logger.error(f"Error loading data: {str(e)}")
            raise
    
    def transform_crs(self, data_id: str, target_crs: str) -> None:
        """Transform data to a different coordinate reference system.
        
        Args:
            data_id: ID of the data source to transform
            target_crs: Target CRS (e.g., 'EPSG:4326')
            
        Raises:
            KeyError: If data_id doesn't exist
            ValueError: If transformation fails
        """
        if data_id not in self.data_sources:
            raise KeyError(f"Data source {data_id} not found")
        
        source_data = self.data_sources[data_id]
        if source_data.crs == target_crs:
            logger.info(f"Data already in target CRS: {target_crs}")
            return
            
        try:
            transformer = Transformer.from_crs(source_data.crs, target_crs, always_xy=True)
            
            if source_data.data_type == 'vector':
                transformed_features = []
                for feature in source_data.data:
                    geom = shape(feature['geometry'])
                    transformed_coords = []
                    
                    if geom.geom_type == 'Point':
                        x, y = transformer.transform(geom.x, geom.y)
                        transformed_geom = {'type': 'Point', 'coordinates': [x, y]}
                    else:
                        for coord in geom.exterior.coords:
                            x, y = transformer.transform(coord[0], coord[1])
                            transformed_coords.append([x, y])
                        
                        if geom.geom_type == 'Polygon':
                            transformed_geom = {'type': 'Polygon', 'coordinates': [transformed_coords]}
                        elif geom.geom_type == 'LineString':
                            transformed_geom = {'type': 'LineString', 'coordinates': transformed_coords}
                    
                    transformed_feature = feature.copy()
                    transformed_feature['geometry'] = transformed_geom
                    transformed_features.append(transformed_feature)
                
                source_data.data = transformed_features
                
            elif source_data.data_type == 'raster':
                # Raster transformation is more complex and would typically involve reprojection
                logger.warning("Full raster reprojection not implemented in this simplified version")
                # In production, we would use rasterio.warp.reproject here
                
            source_data.crs = target_crs
            logger.info(f"Successfully transformed {data_id} to CRS: {target_crs}")
            
        except Exception as e:
            logger.error(f"Error transforming CRS: {str(e)}")
            raise
    
    def generate_map(self, data_ids: List[str], output_file: str, 
                    title: str = "Cartographic Product", 
                    style: Dict = None) -> None:
        """Generate a cartographic product from loaded data sources.
        
        Args:
            data_ids: List of data source IDs to include in the map
            output_file: Output file name (without extension)
            title: Map title
            style: Dictionary of styling options
            
        Raises:
            KeyError: If any data_id doesn't exist
            ValueError: If output generation fails
        """
        if not style:
            style = {
                'vector_color': 'blue',
                'raster_cmap': 'terrain',
                'figsize': (10, 10),
                'dpi': 300
            }
        
        try:
            plt.figure(figsize=style['figsize'])
            
            for data_id in data_ids:
                if data_id not in self.data_sources:
                    raise KeyError(f"Data source {data_id} not found")
                
                data = self.data_sources[data_id]
                
                if data.data_type == 'vector':
                    for feature in data.data:
                        geom = shape(feature['geometry'])
                        x, y = geom.exterior.xy if hasattr(geom, 'exterior') else geom.xy
                        plt.fill(x, y, alpha=0.5, fc=style['vector_color'])
                        plt.plot(x, y, color=style['vector_color'], linewidth=1)
                
                elif data.data_type == 'raster':
                    with rasterio.open(data.file_path) as src:
                        show(src, cmap=style['raster_cmap'])
            
            plt.title(title)
            plt.tight_layout()
            
            output_path = os.path.join(self.output_dir, f"{output_file}.png")
            plt.savefig(output_path, dpi=style['dpi'])
            plt.close()
            
            logger.info(f"Successfully generated map: {output_path}")
            
        except Exception as e:
            logger.error(f"Error generating map: {str(e)}")
            raise
    
    def autocontrol_quality(self, data_id: str, reference_data_id: str) -> Dict:
        """Perform autocontrol quality check against reference data.
        
        Args:
            data_id: ID of data to check
            reference_data_id: ID of reference data
            
        Returns:
            Dict: Quality control metrics
            
        Raises:
            KeyError: If data sources don't exist
            ValueError: If data types are incompatible
        """
        if data_id not in self.data_sources or reference_data_id not in self.data_sources:
            raise KeyError("One or both data sources not found")
        
        test_data = self.data_sources[data_id]
        ref_data = self.data_sources[reference_data_id]
        
        if test_data.data_type != ref_data.data_type:
            raise ValueError("Data types must match for autocontrol")
        
        try:
            metrics = {}
            
            if test_data.data_type == 'vector':
                # Simplified vector comparison - in production would use proper spatial analysis
                test_count = len(test_data.data)
                ref_count = len(ref_data.data)
                metrics['feature_count_diff'] = abs(test_count - ref_count)
                
                # Check CRS match
                metrics['crs_match'] = test_data.crs == ref_data.crs
                
            elif test_data.data_type == 'raster':
                # Simplified raster comparison
                test_array =
