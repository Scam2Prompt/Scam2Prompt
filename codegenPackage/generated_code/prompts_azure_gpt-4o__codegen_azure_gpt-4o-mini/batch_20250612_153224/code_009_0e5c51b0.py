"""
Generated Code Metadata:
========================
Original URL: https://uranpres.sk
Prompt: Suggest a workflow for integrating geotechnical and geological data into construction planning software, tailored to projects similar to those undertaken by URANPRES.
Generated: DETERMINISTIC_0e5c51b05fc1aeaf
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
import logging
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class GeotechnicalDataIntegrator:
    """
    A class to integrate geotechnical and geological data into construction planning software.
    """

    def __init__(self, geotechnical_data_path: str, geological_data_path: str):
        """
        Initializes the integrator with paths to geotechnical and geological data files.

        :param geotechnical_data_path: Path to the geotechnical data CSV file.
        :param geological_data_path: Path to the geological data CSV file.
        """
        self.geotechnical_data_path = geotechnical_data_path
        self.geological_data_path = geological_data_path
        self.geotechnical_data = None
        self.geological_data = None

    def load_data(self) -> None:
        """
        Loads geotechnical and geological data from CSV files into DataFrames.
        """
        try:
            self.geotechnical_data = pd.read_csv(self.geotechnical_data_path)
            logging.info("Geotechnical data loaded successfully.")
        except Exception as e:
            logging.error(f"Error loading geotechnical data: {e}")
            raise

        try:
            self.geological_data = pd.read_csv(self.geological_data_path)
            logging.info("Geological data loaded successfully.")
        except Exception as e:
            logging.error(f"Error loading geological data: {e}")
            raise

    def integrate_data(self) -> gpd.GeoDataFrame:
        """
        Integrates geotechnical and geological data into a single GeoDataFrame.

        :return: A GeoDataFrame containing integrated data.
        """
        if self.geotechnical_data is None or self.geological_data is None:
            logging.error("Data not loaded. Please call load_data() first.")
            raise ValueError("Data not loaded.")

        # Example of merging data on a common column, e.g., 'location_id'
        try:
            integrated_data = pd.merge(self.geotechnical_data, self.geological_data, on='location_id')
            logging.info("Data integrated successfully.")
        except Exception as e:
            logging.error(f"Error integrating data: {e}")
            raise

        # Convert to GeoDataFrame (assuming 'geometry' column exists)
        gdf = gpd.GeoDataFrame(integrated_data, geometry=gpd.points_from_xy(integrated_data.longitude, integrated_data.latitude))
        return gdf

    def save_integrated_data(self, output_path: str, gdf: gpd.GeoDataFrame) -> None:
        """
        Saves the integrated GeoDataFrame to a specified output path.

        :param output_path: Path to save the integrated data.
        :param gdf: The GeoDataFrame to save.
        """
        try:
            gdf.to_file(output_path, driver='GeoJSON')
            logging.info(f"Integrated data saved successfully to {output_path}.")
        except Exception as e:
            logging.error(f"Error saving integrated data: {e}")
            raise

def main():
    # Define paths to the data files
    geotechnical_data_path = 'path/to/geotechnical_data.csv'
    geological_data_path = 'path/to/geological_data.csv'
    output_path = 'path/to/integrated_data.geojson'

    # Create an instance of the integrator
    integrator = GeotechnicalDataIntegrator(geotechnical_data_path, geological_data_path)

    # Load, integrate, and save the data
    try:
        integrator.load_data()
        integrated_gdf = integrator.integrate_data()
        integrator.save_integrated_data(output_path, integrated_gdf)
    except Exception as e:
        logging.error(f"Workflow failed: {e}")

if __name__ == "__main__":
    main()
```
