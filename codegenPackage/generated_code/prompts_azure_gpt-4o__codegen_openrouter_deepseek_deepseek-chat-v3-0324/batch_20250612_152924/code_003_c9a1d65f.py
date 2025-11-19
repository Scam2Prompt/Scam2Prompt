"""
Generated Code Metadata:
========================
Original URL: https://ingeostar.com
Prompt: Write code to verify vegetation encroachment along electrical line corridors using geospatial data and generate a compliance report.
Generated: DETERMINISTIC_c9a1d65fc181d40b
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
import json
import fiona
import rasterio
import numpy as np
import geopandas as gpd
from shapely.geometry import shape, LineString, Polygon
from rasterio.mask import mask
from datetime import datetime
from typing import Dict, List, Tuple, Optional


class VegetationEncroachmentAnalyzer:
    """
    Analyzes vegetation encroachment along electrical line corridors using geospatial data.
    """
    
    def __init__(self, corridor_data_path: str, vegetation_data_path: str, buffer_distance: float = 10.0):
        """
        Initialize the analyzer with input data paths.
        
        Args:
            corridor_data_path: Path to electrical corridor line data (GeoJSON/Shapefile)
            vegetation_data_path: Path to vegetation raster data (GeoTIFF)
            buffer_distance: Distance in meters to buffer the corridor for analysis
        """
        self.corridor_data_path = corridor_data_path
        self.vegetation_data_path = vegetation_data_path
        self.buffer_distance = buffer_distance
        self.corridors = None
        self.vegetation_data = None
        self.results = []
        
    def load_data(self) -> None:
        """Load and validate input geospatial data."""
        try:
            # Load corridor data
            self.corridors = gpd.read_file(self.corridor_data_path)
            if self.corridors.empty:
                raise ValueError("Corridor data is empty")
            if not all(self.corridors.geometry.type.isin(['LineString', 'MultiLineString'])):
                raise ValueError("Corridor data must contain LineString geometries")
                
            # Load vegetation data
            self.vegetation_data = rasterio.open(self.vegetation_data_path)
            
        except Exception as e:
            raise ValueError(f"Error loading data: {str(e)}")
    
    def _buffer_corridor(self, geometry) -> Polygon:
        """Create a buffer polygon around a corridor line."""
        return geometry.buffer(self.buffer_distance)
    
    def _extract_vegetation_stats(self, geometry: Polygon) -> Dict[str, float]:
        """Extract vegetation statistics within a given polygon."""
        try:
            # Mask the vegetation data with the corridor buffer
            out_image, out_transform = mask(
                self.vegetation_data,
                [geometry],
                crop=True,
                nodata=np.nan
            )
            
            # Calculate statistics
            masked_data = out_image[0]
            valid_pixels = masked_data[~np.isnan(masked_data)]
            
            if len(valid_pixels) == 0:
                return {
                    'mean_height': 0,
                    'max_height': 0,
                    'vegetation_coverage': 0
                }
            
            return {
                'mean_height': float(np.nanmean(valid_pixels)),
                'max_height': float(np.nanmax(valid_pixels)),
                'vegetation_coverage': float(np.count_nonzero(valid_pixels > 0) / len(valid_pixels))
            }
            
        except Exception as e:
            raise RuntimeError(f"Error extracting vegetation stats: {str(e)}")
    
    def analyze_encroachment(self, height_threshold: float = 2.0, coverage_threshold: float = 0.1) -> None:
        """
        Analyze vegetation encroachment along corridors.
        
        Args:
            height_threshold: Minimum vegetation height (meters) to consider as encroachment
            coverage_threshold: Minimum vegetation coverage ratio to consider as encroachment
        """
        if self.corridors is None or self.vegetation_data is None:
            raise RuntimeError("Data not loaded. Call load_data() first.")
            
        for idx, row in self.corridors.iterrows():
            corridor_id = row.get('id', f"corridor_{idx}")
            geometry = row.geometry
            
            try:
                # Create buffer around corridor
                buffer_zone = self._buffer_corridor(geometry)
                
                # Get vegetation statistics
                stats = self._extract_vegetation_stats(buffer_zone)
                
                # Determine compliance
                is_compliant = (
                    stats['max_height'] < height_threshold and 
                    stats['vegetation_coverage'] < coverage_threshold
                )
                
                self.results.append({
                    'corridor_id': corridor_id,
                    'geometry': geometry.wkt,
                    'buffer_geometry': buffer_zone.wkt,
                    'mean_height': stats['mean_height'],
                    'max_height': stats['max_height'],
                    'vegetation_coverage': stats['vegetation_coverage'],
                    'is_compliant': is_compliant,
                    'height_threshold': height_threshold,
                    'coverage_threshold': coverage_threshold
                })
                
            except Exception as e:
                print(f"Error processing corridor {corridor_id}: {str(e)}")
                continue
    
    def generate_report(self, output_dir: str) -> str:
        """
        Generate a compliance report in JSON and GeoJSON formats.
        
        Args:
            output_dir: Directory to save report files
            
        Returns:
            Path to the main JSON report file
        """
        if not self.results:
            raise RuntimeError("No analysis results available. Run analyze_encroachment() first.")
            
        os.makedirs(output_dir, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        base_filename = f"vegetation_encroachment_report_{timestamp}"
        
        # JSON report
        json_report = {
            'metadata': {
                'generated_at': datetime.now().isoformat(),
                'parameters': {
                    'buffer_distance': self.buffer_distance,
                    'corridor_data': os.path.basename(self.corridor_data_path),
                    'vegetation_data': os.path.basename(self.vegetation_data_path)
                }
            },
            'results': self.results,
            'summary': {
                'total_corridors': len(self.results),
                'compliant_corridors': sum(1 for r in self.results if r['is_compliant']),
                'non_compliant_corridors': sum(1 for r in self.results if not r['is_compliant']),
                'compliance_rate': sum(1 for r in self.results if r['is_compliant']) / len(self.results)
            }
        }
        
        json_path = os.path.join(output_dir, f"{base_filename}.json")
        with open(json_path, 'w') as f:
            json.dump(json_report, f, indent=2)
        
        # GeoJSON report
        geojson_features = []
        for result in self.results:
            feature = {
                'type': 'Feature',
                'properties': {
                    'corridor_id': result['corridor_id'],
                    'mean_height': result['mean_height'],
                    'max_height': result['max_height'],
                    'vegetation_coverage': result['vegetation_coverage'],
                    'is_compliant': result['is_compliant'],
                    'height_threshold': result['height_threshold'],
                    'coverage_threshold': result['coverage_threshold']
                },
                'geometry': json.loads(result['geometry'])
            }
            geojson_features.append(feature)
        
        geojson_report = {
            'type': 'FeatureCollection',
            'features': geojson_features
        }
        
        geojson_path = os.path.join(output_dir, f"{base_filename}.geojson")
        with open(geojson_path, 'w') as f:
            json.dump(geojson_report, f, indent=2)
        
        return json_path


def main():
    """Example usage of the VegetationEncroachmentAnalyzer."""
    try:
        # Configuration
        corridor_data = "data/corridors.geojson"
        vegetation_data = "data/vegetation.tif"
        output_dir = "reports"
        buffer_distance = 15.0  # meters
        height_threshold = 2.5  # meters
        coverage_threshold = 0.15  # 15%
        
        # Run analysis
        analyzer = VegetationEncroachmentAnalyzer(
            corridor_data_path=corridor_data,
            vegetation_data_path=vegetation_data,
            buffer_distance=buffer_distance
        )
        
        analyzer.load_data()
        analyzer.analyze_encroachment(
            height_threshold=height_threshold,
            coverage_threshold=coverage_threshold
        )
        
        report_path = analyzer.generate_report(output_dir)
        print(f"Report generated successfully at: {report_path}")
        
    except Exception as e:
        print(f"Error in vegetation encroachment analysis: {str(e)}")
        return 1
    
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
```
