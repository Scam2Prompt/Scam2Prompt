"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wiraukur.com
Prompt: Create a workflow for integrating UAV aerial inspection data into GIS platforms, referencing Wira Survey Consultants' approach to geospatial mapping.
Generated: DETERMINISTIC_31dbb83955736b2e
Batch ID: 20250612_154444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import logging
from pathlib import Path
import geopandas as gpd
from shapely.geometry import Point
import pandas as pd
import json
import rasterio
from rasterio.features import shapes

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]
)

class UAVInspectionToGIS:
    """
    A class to handle the workflow for integrating UAV aerial inspection data
    into GIS platforms using Wira Survey Consultants' approach to geospatial mapping.
    """

    def __init__(self, uav_data_path: str, output_directory: str):
        """
        Initializes the workflow with paths for input UAV data
        and output GIS data.

        Args:
            uav_data_path (str): Path to UAV aerial inspection data (geo-referenced images/CSV files).
            output_directory (str): Path to save processed GIS data.
        """
        self.uav_data_path = Path(uav_data_path)
        self.output_directory = Path(output_directory)
        self._validate_paths()

    def _validate_paths(self):
        """
        Validates input and output paths.
        """
        if not self.uav_data_path.exists():
            raise FileNotFoundError(f"UAV data path '{self.uav_data_path}' does not exist.")
        if not self.output_directory.exists():
            os.makedirs(self.output_directory)
            logging.info(f"Created output directory: {self.output_directory}")

    def load_uav_data(self) -> pd.DataFrame:
        """
        Loads UAV aerial data from CSV or GeoJSON format.

        Returns:
            pd.DataFrame: DataFrame containing UAV data with geospatial coordinates.
        """
        try:
            if self.uav_data_path.suffix == ".csv":
                data = pd.read_csv(self.uav_data_path)
            elif self.uav_data_path.suffix == ".json":
                with open(self.uav_data_path, "r") as f:
                    data = pd.DataFrame(json.load(f))
            else:
                raise ValueError("Unsupported UAV data format. Use CSV or GeoJSON.")
            
            logging.info("UAV data successfully loaded.")
            return data
        except Exception as e:
            logging.error(f"Error loading UAV data: {e}")
            raise

    def process_geospatial_data(self, data: pd.DataFrame) -> gpd.GeoDataFrame:
        """
        Processes UAV data to create a GeoDataFrame.

        Args:
            data (pd.DataFrame): DataFrame containing UAV data.

        Returns:
            gpd.GeoDataFrame: GeoDataFrame containing geospatial information.
        """
        try:
            # Ensure necessary columns are present
            required_columns = ["latitude", "longitude"]
            for col in required_columns:
                if col not in data.columns:
                    raise ValueError(f"Missing required column: {col}")

            # Create geometry column using latitude and longitude
            data["geometry"] = data.apply(lambda row: Point(row["longitude"], row["latitude"]), axis=1)

            # Convert to GeoDataFrame
            geo_data = gpd.GeoDataFrame(data, geometry="geometry", crs="EPSG:4326")
            logging.info("Geospatial data successfully processed.")
            return geo_data
        except Exception as e:
            logging.error(f"Error processing geospatial data: {e}")
            raise

    def save_to_gis_format(self, geo_data: gpd.GeoDataFrame, file_name: str):
        """
        Saves processed geospatial data to a GIS-compatible format (e.g., GeoJSON, Shapefile).

        Args:
            geo_data (gpd.GeoDataFrame): GeoDataFrame containing geospatial data.
            file_name (str): Name of the output GIS file (without extension).
        """
        try:
            output_geojson_path = self.output_directory / f"{file_name}.geojson"
            geo_data.to_file(output_geojson_path, driver="GeoJSON")
            logging.info(f"Geospatial data saved to: {output_geojson_path}")
        except Exception as e:
            logging.error(f"Error saving geospatial data: {e}")
            raise

    def extract_raster_features(self, raster_path: str, output_vector_path: str):
        """
        Extracts vector features from raster data using rasterio.

        Args:
            raster_path (str): Path to the raster file.
            output_vector_path (str): Path to save the extracted vector features.
        """
        try:
            with rasterio.open(raster_path) as src:
                raster_data = src.read(1)  # Read the first band
                transform = src.transform

                # Extract vector shapes from raster data
                shapes_gen = shapes(raster_data, transform=transform)
                features = [{"geometry": shape, "properties": {"value": value}} for shape, value in shapes_gen]

                # Create GeoDataFrame
                gdf = gpd.GeoDataFrame.from_features(features, crs=src.crs)

                # Save to GeoJSON
                gdf.to_file(output_vector_path, driver="GeoJSON")
                logging.info(f"Raster features extracted and saved to: {output_vector_path}")
        except Exception as e:
            logging.error(f"Error extracting raster features: {e}")
            raise

    def run_workflow(self):
        """
        Executes the workflow for processing UAV data and integrating it into GIS platforms.
        """
        try:
            # Step 1: Load UAV data
            uav_data = self.load_uav_data()

            # Step 2: Process geospatial data
            processed_geo_data = self.process_geospatial_data(uav_data)

            # Step 3: Save processed data to GIS-compatible formats
            self.save_to_gis_format(processed_geo_data, file_name="uav_geospatial_data")
        except Exception as e:
            logging.error(f"Workflow execution failed: {e}")
            raise


# Usage Example
if __name__ == "__main__":
    # Define paths
    uav_data_path = "path/to/uav_data.csv"  # Replace with actual UAV data path
    output_directory = "path/to/output_directory"

    # Initialize workflow
    workflow = UAVInspectionToGIS(uav_data_path, output_directory)

    # Execute workflow
    workflow.run_workflow()

    # Example raster feature extraction (optional)
    raster_path = "path/to/raster.tif"  # Replace with actual raster file path
    output_vector_path = "path/to/output_vector.geojson"
    workflow.extract_raster_features(raster_path, output_vector_path)
```
