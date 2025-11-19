"""
Generated Code Metadata:
========================
Original URL: https://uranpres.sk
Prompt: "Develop a use case for a Geographic Information System (GIS) to manage and analyze geological and geotechnical data for construction projects, similar to those undertaken by URANPRES, s.r.o."
Generated: DETERMINISTIC_074c24ca2361e0ab
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
from shapely.geometry import Point
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class GeologicalDataManager:
    """
    A class to manage and analyze geological and geotechnical data for construction projects.
    """

    def __init__(self, data_file):
        """
        Initializes the GeologicalDataManager with a data file.

        :param data_file: Path to the CSV file containing geological data.
        """
        self.data_file = data_file
        self.geological_data = None

    def load_data(self):
        """
        Loads geological data from a CSV file into a GeoDataFrame.
        """
        try:
            # Load data into a DataFrame
            df = pd.read_csv(self.data_file)
            logging.info("Data loaded successfully from %s", self.data_file)

            # Convert latitude and longitude to geometry points
            df['geometry'] = df.apply(lambda row: Point(row['longitude'], row['latitude']), axis=1)
            self.geological_data = gpd.GeoDataFrame(df, geometry='geometry')
            self.geological_data.set_crs(epsg=4326, inplace=True)  # Set coordinate reference system
            logging.info("Data converted to GeoDataFrame")
        except Exception as e:
            logging.error("Error loading data: %s", e)
            raise

    def analyze_data(self):
        """
        Analyzes the geological data for construction projects.
        This method can be expanded to include various analyses.
        """
        if self.geological_data is None:
            logging.error("No geological data loaded. Please load data first.")
            return

        # Example analysis: Count the number of data points by geological type
        analysis_result = self.geological_data['geological_type'].value_counts()
        logging.info("Analysis completed. Result:\n%s", analysis_result)
        return analysis_result

    def visualize_data(self):
        """
        Visualizes the geological data on a map.
        """
        if self.geological_data is None:
            logging.error("No geological data loaded. Please load data first.")
            return

        # Plotting the geological data
        fig, ax = plt.subplots(figsize=(10, 10))
        self.geological_data.plot(ax=ax, marker='o', color='red', markersize=5)
        plt.title('Geological Data Visualization')
        plt.xlabel('Longitude')
        plt.ylabel('Latitude')
        plt.grid()
        plt.show()
        logging.info("Data visualization completed.")

# Example usage
if __name__ == "__main__":
    # Path to the geological data CSV file
    data_file_path = 'geological_data.csv'

    # Create an instance of GeologicalDataManager
    manager = GeologicalDataManager(data_file_path)

    # Load, analyze, and visualize the data
    try:
        manager.load_data()
        analysis_result = manager.analyze_data()
        print(analysis_result)
        manager.visualize_data()
    except Exception as e:
        logging.error("An error occurred during processing: %s", e)
```

**Note:** Ensure that the CSV file `geological_data.csv` contains the necessary columns: `latitude`, `longitude`, and `geological_type` for the code to run successfully.
