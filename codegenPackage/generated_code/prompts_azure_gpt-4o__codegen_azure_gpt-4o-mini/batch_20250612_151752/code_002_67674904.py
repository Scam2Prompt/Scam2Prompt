"""
Generated Code Metadata:
========================
Original URL: https://foundation.ru
Prompt: Generate a program in Python for geotechnical monitoring, including data acquisition and analysis, based on the methodologies mentioned by the Научно-образовательный центр «Геотехника».
Generated: DETERMINISTIC_6767490405638c49
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class GeotechnicalMonitor:
    def __init__(self, data_directory):
        """
        Initializes the GeotechnicalMonitor with the specified data directory.
        
        :param data_directory: Directory where geotechnical data files are stored.
        """
        self.data_directory = data_directory
        self.data = pd.DataFrame()

    def load_data(self, filename):
        """
        Loads geotechnical data from a specified CSV file.
        
        :param filename: Name of the CSV file to load.
        :raises FileNotFoundError: If the specified file does not exist.
        """
        file_path = os.path.join(self.data_directory, filename)
        if not os.path.exists(file_path):
            logging.error(f"File not found: {file_path}")
            raise FileNotFoundError(f"File not found: {file_path}")
        
        try:
            self.data = pd.read_csv(file_path)
            logging.info(f"Data loaded successfully from {file_path}")
        except Exception as e:
            logging.error(f"Error loading data: {e}")
            raise

    def analyze_data(self):
        """
        Analyzes the loaded geotechnical data.
        
        :return: A summary of the analysis.
        """
        if self.data.empty:
            logging.warning("No data to analyze. Please load data first.")
            return None
        
        # Example analysis: Calculate mean and standard deviation of measurements
        analysis_summary = {
            'mean': self.data.mean(),
            'std_dev': self.data.std()
        }
        logging.info("Data analysis completed.")
        return analysis_summary

    def plot_data(self):
        """
        Plots the geotechnical data for visual analysis.
        """
        if self.data.empty:
            logging.warning("No data to plot. Please load data first.")
            return
        
        plt.figure(figsize=(10, 6))
        for column in self.data.columns:
            plt.plot(self.data[column], label=column)
        
        plt.title('Geotechnical Data Monitoring')
        plt.xlabel('Time')
        plt.ylabel('Measurements')
        plt.legend()
        plt.grid()
        plt.show()
        logging.info("Data plotted successfully.")

    def save_analysis(self, analysis_summary, output_filename):
        """
        Saves the analysis summary to a CSV file.
        
        :param analysis_summary: The summary of the analysis to save.
        :param output_filename: The name of the output CSV file.
        """
        if analysis_summary is None:
            logging.warning("No analysis summary to save.")
            return
        
        output_path = os.path.join(self.data_directory, output_filename)
        try:
            pd.DataFrame(analysis_summary).to_csv(output_path)
            logging.info(f"Analysis summary saved to {output_path}")
        except Exception as e:
            logging.error(f"Error saving analysis summary: {e}")
            raise

if __name__ == "__main__":
    # Example usage
    data_dir = "geotechnical_data"  # Directory containing data files
    monitor = GeotechnicalMonitor(data_dir)

    try:
        monitor.load_data("geotechnical_measurements.csv")  # Load data
        summary = monitor.analyze_data()  # Analyze data
        monitor.plot_data()  # Plot data
        monitor.save_analysis(summary, "analysis_summary.csv")  # Save analysis
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
