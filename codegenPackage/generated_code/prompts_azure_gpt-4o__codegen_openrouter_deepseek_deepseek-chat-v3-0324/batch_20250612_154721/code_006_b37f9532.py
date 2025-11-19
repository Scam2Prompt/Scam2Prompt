"""
Generated Code Metadata:
========================
Original URL: https://get-link.io
Prompt: Provide a Python-based solution to map the geographic distribution of MIT alumni and their contributions to innovation, using geospatial libraries like GeoPandas or Folium.
Generated: DETERMINISTIC_b37f953258cf2b73
Batch ID: 20250612_154721
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import geopandas as gpd
import folium
from folium.plugins import MarkerCluster
import matplotlib.pyplot as plt
from shapely.geometry import Point
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class MITAlumniMapper:
    """
    A class to map the geographic distribution of MIT alumni and their contributions.
    """
    
    def __init__(self, alumni_data_path, world_map_path=None):
        """
        Initialize the MITAlumniMapper with paths to data files.
        
        Args:
            alumni_data_path (str): Path to the CSV file containing alumni data.
            world_map_path (str, optional): Path to the world map shapefile. Defaults to None.
        """
        self.alumni_data_path = alumni_data_path
        self.world_map_path = world_map_path
        self.alumni_data = None
        self.world_map = None
        
    def load_data(self):
        """
        Load and preprocess the alumni data and world map data.
        """
        try:
            # Load alumni data
            self.alumni_data = pd.read_csv(self.alumni_data_path)
            logger.info("Successfully loaded alumni data")
            
            # Check required columns
            required_columns = ['name', 'latitude', 'longitude', 'contribution']
            if not all(col in self.alumni_data.columns for col in required_columns):
                raise ValueError("Alumni data is missing required columns")
                
            # Convert to GeoDataFrame
            geometry = [Point(xy) for xy in zip(self.alumni_data['longitude'], self.alumni_data['latitude'])]
            self.alumni_data = gpd.GeoDataFrame(self.alumni_data, geometry=geometry, crs="EPSG:4326")
            
            # Load world map if provided
            if self.world_map_path and os.path.exists(self.world_map_path):
                self.world_map = gpd.read_file(self.world_map_path)
                logger.info("Successfully loaded world map data")
                
        except Exception as e:
            logger.error(f"Error loading data: {e}")
            raise
            
    def create_interactive_map(self, output_file='mit_alumni_map.html'):
        """
        Create an interactive Folium map showing MIT alumni locations and contributions.
        
        Args:
            output_file (str): Path to save the HTML map file.
        """
        try:
            if self.alumni_data is None:
                raise ValueError("Alumni data not loaded. Call load_data() first.")
                
            # Create base map centered on average coordinates
            avg_lat = self.alumni_data['latitude'].mean()
            avg_lon = self.alumni_data['longitude'].mean()
            m = folium.Map(location=[avg_lat, avg_lon], zoom_start=2)
            
            # Add marker cluster
            marker_cluster = MarkerCluster().add_to(m)
            
            # Add alumni markers
            for idx, row in self.alumni_data.iterrows():
                popup_text = f"<b>Name:</b> {row['name']}<br><b>Contribution:</b> {row['contribution']}"
                folium.Marker(
                    location=[row['latitude'], row['longitude']],
                    popup=popup_text,
                    icon=folium.Icon(color='red', icon='graduation-cap', prefix='fa')
                ).add_to(marker_cluster)
            
            # Add world boundaries if available
            if self.world_map is not None:
                folium.GeoJson(
                    self.world_map,
                    name='World Boundaries',
                    style_function=lambda x: {'fillColor': '#ffff00', 'color': '#000000', 'weight': 0.5}
                ).add_to(m)
            
            # Save the map
            m.save(output_file)
            logger.info(f"Successfully created interactive map: {output_file}")
            
        except Exception as e:
            logger.error(f"Error creating interactive map: {e}")
            raise
            
    def create_static_map(self, output_file='mit_alumni_distribution.png'):
        """
        Create a static map showing MIT alumni distribution.
        
        Args:
            output_file (str): Path to save the PNG image file.
        """
        try:
            if self.alumni_data is None:
                raise ValueError("Alumni data not loaded. Call load_data() first.")
                
            if self.world_map is None:
                raise ValueError("World map data not loaded.")
                
            # Create figure
            fig, ax = plt.subplots(figsize=(15, 10))
            
            # Plot world map
            self.world_map.plot(ax=ax, color='lightgray', edgecolor='black')
            
            # Plot alumni locations
            self.alumni_data.plot(ax=ax, markersize=50, color='red', marker='o', alpha=0.7)
            
            # Customize plot
            plt.title('Geographic Distribution of MIT Alumni and Their Contributions')
            plt.xlabel('Longitude')
            plt.ylabel('Latitude')
            
            # Save the figure
            plt.savefig(output_file, dpi=300, bbox_inches='tight')
            logger.info(f"Successfully created static map: {output_file}")
            
        except Exception as e:
            logger.error(f"Error creating static map: {e}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        # Initialize mapper (replace with actual file paths)
        mapper = MITAlumniMapper(
            alumni_data_path='mit_alumni.csv',
            world_map_path='world_map.shp'
        )
        
        # Load data
        mapper.load_data()
        
        # Create maps
        mapper.create_interactive_map()
        mapper.create_static_map()
        
    except Exception as e:
        logger.error(f"Error in main execution: {e}")
```
