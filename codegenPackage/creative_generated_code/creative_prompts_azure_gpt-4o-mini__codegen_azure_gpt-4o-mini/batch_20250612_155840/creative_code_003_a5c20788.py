"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ajp.cl
Prompt: Suggest a library for creating interactive maps that visualize rural water supply projects, inspired by the project designs from AJP Ingenieros.
Generated: DETERMINISTIC_a5c2078813bbda29
Batch ID: 20250612_155840
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import folium
from folium.plugins import MarkerCluster
import pandas as pd

class WaterSupplyMap:
    """
    A class to create an interactive map visualizing rural water supply projects.
    
    Attributes:
        location: A tuple representing the initial coordinates (latitude, longitude) of the map.
        zoom_start: Initial zoom level for the map.
        projects_data: A DataFrame containing details of water supply projects.
        map: The folium Map object.
    """

    def __init__(self, location=(0, 0), zoom_start=6):
        """
        Initialize the WaterSupplyMap with a location and zoom level.
        
        Args:
            location (tuple): A tuple of latitude and longitude for the map center.
            zoom_start (int): The initial zoom level for the map.
        """
        self.location = location
        self.zoom_start = zoom_start
        self.projects_data = pd.DataFrame()  # Placeholder for projects data
        self.map = folium.Map(location=self.location, zoom_start=self.zoom_start)

    def load_projects_data(self, csv_file):
        """
        Load water supply projects from a CSV file into a DataFrame.
        
        Args:
            csv_file (str): The path to the CSV file containing project data.
        
        Raises:
            FileNotFoundError: If the specified file does not exist.
            pd.errors.EmptyDataError: If the provided CSV file is empty.
        """
        try:
            self.projects_data = pd.read_csv(csv_file)
        except FileNotFoundError:
            print(f"Error: The file {csv_file} was not found.")
            raise
        except pd.errors.EmptyDataError:
            print("Error: The provided CSV file is empty.")
            raise

    def add_projects_to_map(self):
        """
        Add markers for each project in the DataFrame to the map.
        
        Uses MarkerCluster to handle overlapping markers.
        """
        marker_cluster = MarkerCluster().add_to(self.map)
        
        for _, project in self.projects_data.iterrows():
            folium.Marker(
                location=(project['latitude'], project['longitude']),
                popup=folium.Popup(f"Project: {project['name']}\nDetails: {project['details']}", parse_html=True),
                icon=folium.Icon(color="blue")
            ).add_to(marker_cluster)

    def save_map(self, output_file):
        """
        Save the map to an HTML file.
        
        Args:
            output_file (str): The path where the HTML file will be saved.
        """
        self.map.save(output_file)

# Example usage
if __name__ == "__main__":
    water_supply_map = WaterSupplyMap(location=(10.0, -84.0))  # Set initial coordinates to a suitable location
    water_supply_map.load_projects_data('water_supply_projects.csv')
    water_supply_map.add_projects_to_map()
    water_supply_map.save_map('water_supply_map.html')
```

**Note:** Replace `'water_supply_projects.csv'` with the actual path to your CSV file containing the water supply project data, which should have at least the columns 'latitude', 'longitude', 'name', and 'details'.
