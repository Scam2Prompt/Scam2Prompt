"""
Generated Code Metadata:
========================
Original URL: https://ingeostar.com
Prompt: Create a script to automate the process of Levantamiento e inspección de líneas eléctricas, including Análisis and proceso de información Geoespacial.
Generated: DETERMINISTIC_bd369db1b5c83535
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
import json
import time
import requests
import geopandas as gpd
import pandas as pd
from shapely.geometry import LineString, Point
from fiona.crs import from_epsg
from typing import Dict, List, Optional, Tuple
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='powerline_inspection.log'
)
logger = logging.getLogger(__name__)

class PowerLineInspector:
    """
    Automated power line inspection and geospatial analysis tool.
    """
    
    def __init__(self, config_file: str = 'config.json'):
        """
        Initialize the inspector with configuration.
        
        Args:
            config_file: Path to JSON configuration file
        """
        self.config = self._load_config(config_file)
        self.gis_data = None
        self.inspection_results = None
        
    def _load_config(self, config_file: str) -> Dict:
        """
        Load configuration from JSON file.
        
        Args:
            config_file: Path to JSON file
            
        Returns:
            Dictionary with configuration
            
        Raises:
            FileNotFoundError: If config file doesn't exist
            json.JSONDecodeError: If config file is invalid JSON
        """
        try:
            with open(config_file) as f:
                return json.load(f)
        except FileNotFoundError:
            logger.error(f"Config file {config_file} not found")
            raise
        except json.JSONDecodeError:
            logger.error(f"Invalid JSON in config file {config_file}")
            raise
    
    def load_gis_data(self, file_path: str) -> None:
        """
        Load GIS data from file (GeoJSON, Shapefile, etc.).
        
        Args:
            file_path: Path to GIS data file
            
        Raises:
            FileNotFoundError: If file doesn't exist
            ValueError: If file format is unsupported
        """
        try:
            self.gis_data = gpd.read_file(file_path)
            logger.info(f"Successfully loaded GIS data from {file_path}")
            
            # Ensure data has proper CRS
            if self.gis_data.crs is None:
                self.gis_data.crs = from_epsg(4326)
                logger.warning("No CRS detected, defaulting to EPSG:4326")
                
        except FileNotFoundError:
            logger.error(f"GIS data file {file_path} not found")
            raise
        except Exception as e:
            logger.error(f"Error loading GIS data: {str(e)}")
            raise ValueError(f"Unsupported file format or corrupt data: {str(e)}")
    
    def analyze_power_lines(self) -> gpd.GeoDataFrame:
        """
        Analyze power lines for potential issues.
        
        Returns:
            GeoDataFrame with analysis results
            
        Raises:
            RuntimeError: If GIS data hasn't been loaded
        """
        if self.gis_data is None:
            logger.error("No GIS data loaded for analysis")
            raise RuntimeError("Load GIS data before analysis")
            
        try:
            results = self.gis_data.copy()
            
            # Add analysis columns
            results['length_km'] = results.geometry.length / 1000
            results['needs_inspection'] = False
            results['issues_found'] = None
            
            # Simple example analysis - flag lines longer than threshold
            threshold = self.config.get('length_threshold_km', 50)
            results.loc[results['length_km'] > threshold, 'needs_inspection'] = True
            
            self.inspection_results = results
            logger.info("Power line analysis completed")
            return results
            
        except Exception as e:
            logger.error(f"Error during analysis: {str(e)}")
            raise
    
    def generate_inspection_points(self, interval_km: float = 5) -> gpd.GeoDataFrame:
        """
        Generate inspection points along power lines at regular intervals.
        
        Args:
            interval_km: Distance between inspection points in kilometers
            
        Returns:
            GeoDataFrame with inspection points
            
        Raises:
            RuntimeError: If analysis hasn't been performed
        """
        if self.inspection_results is None:
            logger.error("No analysis results available")
            raise RuntimeError("Perform analysis first")
            
        try:
            inspection_points = []
            
            for idx, row in self.inspection_results.iterrows():
                if not row['needs_inspection']:
                    continue
                    
                line = row.geometry
                length_km = row['length_km']
                
                # Calculate number of points needed
                num_points = int(length_km // interval_km) + 1
                
                # Generate points along the line
                for i in range(num_points):
                    distance = min(i * interval_km * 1000, line.length)
                    point = line.interpolate(distance)
                    inspection_points.append({
                        'line_id': idx,
                        'point_id': f"{idx}_{i}",
                        'distance_km': distance / 1000,
                        'geometry': point
                    })
            
            if not inspection_points:
                logger.warning("No inspection points generated")
                return None
                
            points_gdf = gpd.GeoDataFrame(
                inspection_points,
                crs=self.inspection_results.crs
            )
            
            logger.info(f"Generated {len(points_gdf)} inspection points")
            return points_gdf
            
        except Exception as e:
            logger.error(f"Error generating inspection points: {str(e)}")
            raise
    
    def export_results(self, output_dir: str, formats: List[str] = ['geojson', 'csv']) -> None:
        """
        Export analysis results to specified formats.
        
        Args:
            output_dir: Directory to save results
            formats: List of formats to export ('geojson', 'csv', 'shp')
            
        Raises:
            RuntimeError: If no results to export
            ValueError: If invalid format specified
        """
        if self.inspection_results is None:
            logger.error("No results to export")
            raise RuntimeError("Perform analysis first")
            
        try:
            os.makedirs(output_dir, exist_ok=True)
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            base_path = os.path.join(output_dir, f"powerline_inspection_{timestamp}")
            
            for fmt in formats:
                if fmt == 'geojson':
                    path = f"{base_path}.geojson"
                    self.inspection_results.to_file(path, driver='GeoJSON')
                elif fmt == 'csv':
                    path = f"{base_path}.csv"
                    self.inspection_results.drop('geometry', axis=1).to_csv(path, index=False)
                elif fmt == 'shp':
                    path = f"{base_path}.shp"
                    self.inspection_results.to_file(path)
                else:
                    raise ValueError(f"Unsupported format: {fmt}")
                
                logger.info(f"Exported results to {path} as {fmt}")
                
        except Exception as e:
            logger.error(f"Error exporting results: {str(e)}")
            raise
    
    def fetch_weather_data(self, points_gdf: gpd.GeoDataFrame) -> Optional[pd.DataFrame]:
        """
        Fetch weather data for inspection points.
        
        Args:
            points_gdf: GeoDataFrame with inspection points
            
        Returns:
            DataFrame with weather data or None if API fails
            
        Note:
            Requires weather API configuration in config.json
        """
        if 'weather_api' not in self.config:
            logger.warning("No weather API configured")
            return None
            
        try:
            api_key = self.config['weather_api']['key']
            base_url = self.config['weather_api']['url']
            
            weather_data = []
            
            for idx, row in points_gdf.iterrows():
                point = row.geometry
                url = f"{base_url}?lat={point.y}&lon={point.x}&appid={api_key}"
                
                response = requests.get(url, timeout=10)
                response.raise_for_status()
                
                data = response.json()
                weather_data.append({
                    'point_id': row['point_id'],
                    'temperature': data['main']['temp'],
                    'humidity': data['main']['humidity'],
                    'wind_speed': data['wind']['speed'],
                    'weather_condition': data['weather'][0]['main']
                })
                
            logger.info(f"Fetched weather data for {len(weather_data)} points")
            return pd.DataFrame(weather_data)
            
        except Exception as e:
            logger.error(f"Error fetching weather data: {str(e)}")
            return None

def main():
    """
    Main execution function for power line inspection workflow.
    """
    try:
        # Initialize inspector
        inspector = PowerLineInspector()
        
        # Load GIS data
        inspector.load_gis_data('power_lines.geojson')
        
        # Analyze power lines
        results = inspector.analyze_power_lines()
        
        # Generate inspection points
        inspection_points = inspector.generate_inspection_points()
        
        # Fetch weather data if available
        if inspection_points is not None:
            weather_data = inspector.fetch_weather_data(inspection_points)
            if weather_data is not None:
                print("Weather data sample:")
                print(
