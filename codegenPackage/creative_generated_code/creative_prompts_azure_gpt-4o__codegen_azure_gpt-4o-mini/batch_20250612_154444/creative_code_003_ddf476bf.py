"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wiraukur.com
Prompt: Write a script to analyze terrestrial and airborne LiDAR data for geospatial mapping, referencing Wira Survey Consultants' expertise in laser scanning technologies.
Generated: DETERMINISTIC_ddf476bf55c93f02
Batch ID: 20250612_154444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import pandas as pd
import geopandas as gpd
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt

class LiDARDataAnalyzer:
    """
    A class to analyze terrestrial and airborne LiDAR data for geospatial mapping.
    """

    def __init__(self, lidar_data: pd.DataFrame):
        """
        Initializes the LiDARDataAnalyzer with the provided LiDAR data.

        Args:
            lidar_data (pd.DataFrame): A DataFrame containing LiDAR data with columns 
                                        ['X', 'Y', 'Z', 'Intensity'].
        
        Raises:
            ValueError: If the input DataFrame does not contain required columns.
        """
        required_columns = ['X', 'Y', 'Z', 'Intensity']
        if not all(col in lidar_data.columns for col in required_columns):
            raise ValueError(f"Input DataFrame must contain the columns: {required_columns}")
        
        self.lidar_data = lidar_data

    def generate_delaunay_triangulation(self):
        """
        Generate Delaunay triangulation from the LiDAR data.

        Returns:
            Delaunay: A Delaunay triangulation object.
        """
        points = self.lidar_data[['X', 'Y']].values
        return Delaunay(points)

    def visualize_lidar_data(self):
        """
        Visualize the LiDAR data using a scatter plot and triangulation.
        """
        plt.figure(figsize=(10, 7))
        plt.scatter(self.lidar_data['X'], self.lidar_data['Y'], c=self.lidar_data['Z'], 
                    cmap='viridis', marker='o', s=1)
        plt.colorbar(label='Elevation (Z)')
        plt.title('LiDAR Data Visualization')
        plt.xlabel('X Coordinate')
        plt.ylabel('Y Coordinate')
        plt.axis('equal')
        plt.show()

    def save_to_geojson(self, output_file: str):
        """
        Save the LiDAR data to a GeoJSON file.

        Args:
            output_file (str): The path to the output GeoJSON file.

        Raises:
            IOError: If there is an issue writing to the specified file.
        """
        try:
            gdf = gpd.GeoDataFrame(self.lidar_data, 
                                   geometry=gpd.points_from_xy(self.lidar_data.X, self.lidar_data.Y),
                                   crs='EPSG:4326')  # Assuming WGS84
            gdf.to_file(output_file, driver='GeoJSON')
        except Exception as e:
            raise IOError(f"Error saving to GeoJSON: {e}")

# Example usage:
if __name__ == "__main__":
    # Load LiDAR data
    try:
        lidar_data = pd.read_csv('lidar_data.csv')  # Replace with actual data source
        analyzer = LiDARDataAnalyzer(lidar_data)

        # Generate Delaunay triangulation
        triangulation = analyzer.generate_delaunay_triangulation()
        
        # Visualize LiDAR data
        analyzer.visualize_lidar_data()

        # Save to GeoJSON
        analyzer.save_to_geojson('output_lidar.geojson')

    except Exception as e:
        print(f"An error occurred: {e}")
```
