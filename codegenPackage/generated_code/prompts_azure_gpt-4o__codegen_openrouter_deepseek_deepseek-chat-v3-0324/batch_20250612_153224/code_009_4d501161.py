"""
Generated Code Metadata:
========================
Original URL: https://nmkt.net
Prompt: Develop a script to track and visualize the distribution network growth for a marketing campaign targeting agricultural businesses, using geographic data and mapping libraries like Folium or GeoPandas.
Generated: DETERMINISTIC_4d501161db8cfaff
Batch ID: 20250612_153224
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
import os
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='campaign_tracking.log'
)

class CampaignTracker:
    def __init__(self, data_path=None):
        """Initialize the campaign tracker with optional data path."""
        self.data_path = data_path
        self.campaign_data = None
        self.geo_data = None
        self.logger = logging.getLogger(__name__)
        
    def load_data(self, file_path):
        """Load campaign data from CSV file."""
        try:
            self.campaign_data = pd.read_csv(file_path)
            self.logger.info(f"Successfully loaded data from {file_path}")
            return True
        except Exception as e:
            self.logger.error(f"Error loading data: {str(e)}")
            return False
    
    def process_geodata(self):
        """Process geographical data and create GeoDataFrame."""
        if self.campaign_data is None:
            self.logger.error("No campaign data loaded")
            return False
            
        try:
            # Create geometry from lat/long columns
            geometry = [Point(xy) for xy in zip(
                self.campaign_data['longitude'], 
                self.campaign_data['latitude']
            )]
            
            # Create GeoDataFrame
            self.geo_data = gpd.GeoDataFrame(
                self.campaign_data,
                geometry=geometry,
                crs="EPSG:4326"
            )
            self.logger.info("Successfully processed geodata")
            return True
        except KeyError as e:
            self.logger.error(f"Missing required columns: {str(e)}")
            return False
        except Exception as e:
            self.logger.error(f"Error processing geodata: {str(e)}")
            return False
    
    def create_interactive_map(self, output_file='campaign_map.html'):
        """Create an interactive Folium map with campaign locations."""
        if self.geo_data is None:
            self.logger.error("No geodata available for mapping")
            return False
            
        try:
            # Calculate center of all points
            avg_lat = self.geo_data['latitude'].mean()
            avg_lon = self.geo_data['longitude'].mean()
            
            # Create base map
            campaign_map = folium.Map(
                location=[avg_lat, avg_lon],
                zoom_start=6,
                tiles='CartoDB positron'
            )
            
            # Add marker cluster
            marker_cluster = MarkerCluster().add_to(campaign_map)
            
            # Add points to map
            for _, row in self.geo_data.iterrows():
                popup_text = f"""
                <b>Business:</b> {row['business_name']}<br>
                <b>Location:</b> {row['city']}, {row['state']}<br>
                <b>Contact:</b> {row['contact_name']}<br>
                <b>Date Added:</b> {row['date_added']}
                """
                
                folium.Marker(
                    location=[row['latitude'], row['longitude']],
                    popup=folium.Popup(popup_text, max_width=300),
                    icon=folium.Icon(color='green', icon='leaf')
                ).add_to(marker_cluster)
            
            # Save the map
            campaign_map.save(output_file)
            self.logger.info(f"Map saved to {output_file}")
            return True
        except Exception as e:
            self.logger.error(f"Error creating map: {str(e)}")
            return False
    
    def generate_distribution_plot(self, output_file='distribution_plot.png'):
        """Generate a static plot showing geographic distribution."""
        if self.geo_data is None:
            self.logger.error("No geodata available for plotting")
            return False
            
        try:
            world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
            base = world.plot(color='lightgray', edgecolor='white', figsize=(12, 8))
            
            # Plot campaign points
            self.geo_data.plot(
                ax=base,
                marker='o',
                color='green',
                markersize=50,
                alpha=0.7,
                label='Agricultural Businesses'
            )
            
            plt.title('Agricultural Business Campaign Distribution')
            plt.legend()
            plt.savefig(output_file, dpi=300, bbox_inches='tight')
            plt.close()
            self.logger.info(f"Plot saved to {output_file}")
            return True
        except Exception as e:
            self.logger.error(f"Error generating plot: {str(e)}")
            return False
    
    def run_analysis(self, data_file, output_dir='output'):
        """Run complete analysis pipeline."""
        try:
            # Create output directory if it doesn't exist
            os.makedirs(output_dir, exist_ok=True)
            
            # Load and process data
            if not self.load_data(data_file):
                return False
                
            if not self.process_geodata():
                return False
            
            # Generate outputs
            map_path = os.path.join(output_dir, 'campaign_map.html')
            plot_path = os.path.join(output_dir, 'distribution_plot.png')
            
            success = (
                self.create_interactive_map(map_path) and
                self.generate_distribution_plot(plot_path)
            )
            
            if success:
                self.logger.info("Analysis completed successfully")
            else:
                self.logger.warning("Analysis completed with some errors")
            
            return success
        except Exception as e:
            self.logger.error(f"Analysis failed: {str(e)}")
            return False

# Example usage
if __name__ == "__main__":
    # Sample data structure (columns expected in input CSV):
    # business_name, contact_name, city, state, latitude, longitude, date_added
    
    tracker = CampaignTracker()
    tracker.run_analysis('agricultural_businesses.csv')
```
