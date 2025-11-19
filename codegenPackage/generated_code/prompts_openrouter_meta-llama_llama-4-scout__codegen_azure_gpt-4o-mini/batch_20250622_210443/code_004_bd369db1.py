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
import geopandas as gpd
import pandas as pd
import logging
from shapely.geometry import Point

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ElectricLineInspection:
    def __init__(self, data_directory):
        """
        Initialize the ElectricLineInspection class.

        :param data_directory: Directory where input data files are stored.
        """
        self.data_directory = data_directory
        self.electric_lines = None
        self.inspection_results = None

    def load_data(self):
        """
        Load electric line data and inspection data from CSV files.
        """
        try:
            electric_lines_path = os.path.join(self.data_directory, 'electric_lines.csv')
            inspection_data_path = os.path.join(self.data_directory, 'inspection_data.csv')

            self.electric_lines = pd.read_csv(electric_lines_path)
            self.inspection_results = pd.read_csv(inspection_data_path)

            logging.info("Data loaded successfully.")
        except FileNotFoundError as e:
            logging.error(f"File not found: {e}")
            raise
        except Exception as e:
            logging.error(f"An error occurred while loading data: {e}")
            raise

    def analyze_data(self):
        """
        Analyze the electric line data and inspection results.
        This method can be expanded to include specific analysis logic.
        """
        try:
            # Example analysis: Count the number of inspections per electric line
            inspection_counts = self.inspection_results['line_id'].value_counts()
            logging.info("Analysis completed successfully.")
            return inspection_counts
        except Exception as e:
            logging.error(f"An error occurred during analysis: {e}")
            raise

    def process_geospatial_data(self):
        """
        Convert electric line data to a GeoDataFrame for geospatial analysis.
        """
        try:
            # Create GeoDataFrame from electric lines
            geometry = [Point(xy) for xy in zip(self.electric_lines['longitude'], self.electric_lines['latitude'])]
            gdf = gpd.GeoDataFrame(self.electric_lines, geometry=geometry)

            # Set the coordinate reference system (CRS)
            gdf.set_crs(epsg=4326, inplace=True)

            logging.info("Geospatial data processed successfully.")
            return gdf
        except Exception as e:
            logging.error(f"An error occurred while processing geospatial data: {e}")
            raise

    def run_inspection_process(self):
        """
        Execute the full inspection process: load data, analyze, and process geospatial data.
        """
        self.load_data()
        analysis_results = self.analyze_data()
        geospatial_data = self.process_geospatial_data()

        return analysis_results, geospatial_data

if __name__ == "__main__":
    # Define the directory containing the data files
    data_dir = 'path/to/data_directory'

    # Create an instance of the ElectricLineInspection class
    inspection = ElectricLineInspection(data_directory=data_dir)

    try:
        # Run the inspection process
        analysis_results, geospatial_data = inspection.run_inspection_process()

        # Output results
        print("Analysis Results:")
        print(analysis_results)
        print("\nGeospatial Data:")
        print(geospatial_data)
    except Exception as e:
        logging.error(f"An error occurred in the main process: {e}")
```
