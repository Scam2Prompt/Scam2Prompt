"""
Generated Code Metadata:
========================
Original URL: https://wiraukur.com
Prompt: Develop a Python script to automate the analysis of remote sensing data for agricultural development, referencing Wira Survey Consultants' experience with government entities.
Generated: DETERMINISTIC_9127c0683bd7a03b
Batch ID: 20250612_154444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Remote Sensing Data Analysis for Agricultural Development

This script automates the analysis of remote sensing data to support agricultural
development initiatives, leveraging techniques similar to those used by Wira Survey
Consultants in collaboration with government entities.

Key Features:
- NDVI (Normalized Difference Vegetation Index) calculation
- Land cover classification
- Time-series analysis for crop monitoring
- Report generation for decision-making

Requirements:
- Python 3.8+
- rasterio
- numpy
- matplotlib
- scikit-learn
- geopandas
- pandas
"""

import os
import sys
import logging
import argparse
from datetime import datetime
import numpy as np
import rasterio
from rasterio.plot import show
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import geopandas as gpd
import pandas as pd


class RemoteSensingAnalyzer:
    """Main class for remote sensing data analysis for agricultural development."""

    def __init__(self, input_path, output_dir="output"):
        """
        Initialize the analyzer with input data path and output directory.

        Args:
            input_path (str): Path to input raster file or directory
            output_dir (str): Directory to save output files (default: "output")
        """
        self.input_path = input_path
        self.output_dir = output_dir
        self._setup_logging()
        self._validate_inputs()
        self._create_output_dir()

    def _setup_logging(self):
        """Configure logging for the application."""
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            handlers=[
                logging.FileHandler("remote_sensing_analysis.log"),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)

    def _validate_inputs(self):
        """Validate input paths and files."""
        if not os.path.exists(self.input_path):
            self.logger.error(f"Input path does not exist: {self.input_path}")
            raise FileNotFoundError(f"Input path not found: {self.input_path}")

    def _create_output_dir(self):
        """Create output directory if it doesn't exist."""
        os.makedirs(self.output_dir, exist_ok=True)
        self.logger.info(f"Output directory: {os.path.abspath(self.output_dir)}")

    def calculate_ndvi(self, red_band_path, nir_band_path, output_filename="ndvi.tif"):
        """
        Calculate NDVI (Normalized Difference Vegetation Index).

        Args:
            red_band_path (str): Path to red band raster
            nir_band_path (str): Path to near-infrared band raster
            output_filename (str): Name for output NDVI file (default: "ndvi.tif")

        Returns:
            str: Path to generated NDVI file
        """
        try:
            with rasterio.open(red_band_path) as red_src, rasterio.open(nir_band_path) as nir_src:
                # Read bands as numpy arrays
                red = red_src.read(1).astype('float32')
                nir = nir_src.read(1).astype('float32')

                # Calculate NDVI
                ndvi = (nir - red) / (nir + red + 1e-10)  # Small value to avoid division by zero

                # Save NDVI to file
                output_path = os.path.join(self.output_dir, output_filename)
                with rasterio.open(
                    output_path,
                    'w',
                    driver='GTiff',
                    height=ndvi.shape[0],
                    width=ndvi.shape[1],
                    count=1,
                    dtype=ndvi.dtype,
                    crs=red_src.crs,
                    transform=red_src.transform,
                ) as dst:
                    dst.write(ndvi, 1)

                self.logger.info(f"NDVI calculation complete. Saved to: {output_path}")
                return output_path

        except Exception as e:
            self.logger.error(f"Error calculating NDVI: {str(e)}")
            raise

    def classify_land_cover(self, raster_path, n_clusters=5, output_filename="land_cover.tif"):
        """
        Perform unsupervised land cover classification using K-means clustering.

        Args:
            raster_path (str): Path to input raster file
            n_clusters (int): Number of clusters/classes (default: 5)
            output_filename (str): Name for output classified file (default: "land_cover.tif")

        Returns:
            str: Path to generated classified file
        """
        try:
            with rasterio.open(raster_path) as src:
                # Read all bands
                data = src.read()
                height, width = data.shape[1], data.shape[2]

                # Reshape for clustering
                reshaped_data = data.reshape(data.shape[0], -1).T

                # Perform K-means clustering
                kmeans = KMeans(n_clusters=n_clusters, random_state=42)
                labels = kmeans.fit_predict(reshaped_data)

                # Reshape back to original dimensions
                classified = labels.reshape(height, width)

                # Save classified image
                output_path = os.path.join(self.output_dir, output_filename)
                with rasterio.open(
                    output_path,
                    'w',
                    driver='GTiff',
                    height=height,
                    width=width,
                    count=1,
                    dtype='uint8',
                    crs=src.crs,
                    transform=src.transform,
                ) as dst:
                    dst.write(classified, 1)

                self.logger.info(f"Land cover classification complete. Saved to: {output_path}")
                return output_path

        except Exception as e:
            self.logger.error(f"Error performing land cover classification: {str(e)}")
            raise

    def generate_time_series_report(self, ndvi_files, output_filename="crop_growth_report.csv"):
        """
        Generate a time series report of NDVI values for crop monitoring.

        Args:
            ndvi_files (list): List of paths to NDVI files over time
            output_filename (str): Name for output report file (default: "crop_growth_report.csv")

        Returns:
            str: Path to generated report file
        """
        try:
            stats = []
            for file_path in ndvi_files:
                with rasterio.open(file_path) as src:
                    ndvi = src.read(1)
                    valid_values = ndvi[~np.isnan(ndvi)]
                    
                    # Get date from filename if possible
                    file_date = os.path.basename(file_path).split('_')[0]
                    try:
                        date = datetime.strptime(file_date, "%Y%m%d").date()
                    except ValueError:
                        date = os.path.getmtime(file_path)
                        date = datetime.fromtimestamp(date).date()

                    stats.append({
                        'date': date,
                        'mean_ndvi': np.mean(valid_values),
                        'median_ndvi': np.median(valid_values),
                        'min_ndvi': np.min(valid_values),
                        'max_ndvi': np.max(valid_values),
                        'area_ha': (valid_values.size * abs(src.transform[0]) * abs(src.transform[4])) / 10000
                    })

            # Create DataFrame and save to CSV
            df = pd.DataFrame(stats).sort_values('date')
            output_path = os.path.join(self.output_dir, output_filename)
            df.to_csv(output_path, index=False)

            self.logger.info(f"Time series report generated. Saved to: {output_path}")
            return output_path

        except Exception as e:
            self.logger.error(f"Error generating time series report: {str(e)}")
            raise

    def visualize_results(self, raster_path, title="Result Visualization", output_filename="visualization.png"):
        """
        Generate visualization of raster data.

        Args:
            raster_path (str): Path to raster file
            title (str): Title for the visualization (default: "Result Visualization")
            output_filename (str): Name for output image file (default: "visualization.png")

        Returns:
            str: Path to generated visualization file
        """
        try:
            with rasterio.open(raster_path) as src:
                fig, ax = plt.subplots(figsize=(10, 10))
                show(src, ax=ax, title=title)
                
                output_path = os.path.join(self.output_dir, output_filename)
                plt.savefig(output_path, dpi=300, bbox_inches='tight')
                plt.close()

                self.logger.info(f"Visualization saved to: {output_path}")
                return output_path

        except Exception as e:
            self.logger.error(f"Error generating visualization: {str(e)}")
            raise


def main():
    """Main function to handle command-line execution."""
    parser = argparse.ArgumentParser(
        description="Remote Sensing Data Analysis for Agricultural Development",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    
    parser.add_argument(
        "-i", "--input",
        required=True,
        help="Input raster file or directory containing raster files"
    )
    
    parser.add_argument(
        "-o", "--output",
