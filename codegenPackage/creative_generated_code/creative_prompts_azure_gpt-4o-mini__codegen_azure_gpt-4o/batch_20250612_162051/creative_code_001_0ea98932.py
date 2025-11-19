"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uranpres.sk
Prompt: Write a Python script that integrates geotechnical data analysis for construction projects, inspired by URANPRES's geotechnical and drilling services.
Generated: DETERMINISTIC_0ea98932bed4e5c5
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Geotechnical Data Analysis Script for Construction Projects

This script analyzes geotechnical data and provides insights for construction projects, 
inspired by URANPRES's geotechnical and drilling services.

Features:
- Data import from CSV files containing geotechnical data
- Validation of data integrity and quality
- Computation of key metrics (e.g., soil stability, moisture content, bearing capacity)
- Visualization of results via graphs
- Error handling for data-related issues

Author: Expert Programmer
Date: YYYY-MM-DD
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import logging
from typing import Optional

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class GeotechnicalAnalysis:
    def __init__(self, file_path: str):
        """
        Constructor to initialize the geotechnical analysis with a data file.

        Parameters:
        file_path (str): Path to the CSV file containing geotechnical data.
        """
        self.file_path = file_path
        self.data = None

    def load_data(self):
        """
        Loads geotechnical data from a CSV file into a DataFrame.

        Raises:
        FileNotFoundError: If the file cannot be found.
        ValueError: If the file contents are invalid or corrupted.
        """
        try:
            logging.info(f"Loading data from file: {self.file_path}")
            self.data = pd.read_csv(self.file_path)
            
            # Basic validation to ensure necessary columns exist
            required_columns = ['Location', 'Soil_Type', 'Moisture_Content', 'Bearing_Capacity']
            if not all(col in self.data.columns for col in required_columns):
                raise ValueError(f"Missing required columns in the dataset. Expected: {required_columns}")
            
            logging.info("Data loaded successfully.")
        except FileNotFoundError as e:
            logging.error("File not found. Please check the file path.")
            raise e
        except Exception as e:
            logging.error("An error occurred while loading the data.")
            raise e

    def analyze_data(self):
        """
        Performs geotechnical data analysis and computes key metrics.

        Returns:
        dict: A dictionary of computed metrics (e.g., average moisture content, average bearing capacity).
        """
        if self.data is None:
            logging.error("No data loaded. Please load the data first.")
            raise ValueError("Data is not loaded.")

        logging.info("Performing data analysis...")
        metrics = {
            'Average_Moisture_Content': np.mean(self.data['Moisture_Content']),
            'Average_Bearing_Capacity': np.mean(self.data['Bearing_Capacity']),
            'Soil_Types': self.data['Soil_Type'].unique().tolist(),
        }
        
        logging.info("Data analysis completed successfully.")
        return metrics

    def visualize_data(self):
        """
        Generates graphs to visualize geotechnical data for better insights.

        Outputs:
        - Bar chart showing average moisture content per soil type
        - Bar chart showing average bearing capacity per soil type
        """
        if self.data is None:
            logging.error("No data loaded. Please load the data first.")
            raise ValueError("Data is not loaded.")

        logging.info("Generating visualizations...")
        # Average moisture content per soil type
        avg_moisture = self.data.groupby('Soil_Type')['Moisture_Content'].mean()
        avg_bearing = self.data.groupby('Soil_Type')['Bearing_Capacity'].mean()

        # Plot average moisture content
        plt.figure(figsize=(10, 5))
        avg_moisture.plot(kind='bar', color='skyblue', title="Average Moisture Content per Soil Type")
        plt.xlabel("Soil Type")
        plt.ylabel("Moisture Content (%)")
        plt.tight_layout()
        plt.show()

        # Plot average bearing capacity
        plt.figure(figsize=(10, 5))
        avg_bearing.plot(kind='bar', color='orange', title="Average Bearing Capacity per Soil Type")
        plt.xlabel("Soil Type")
        plt.ylabel("Bearing Capacity (kN/m²)")
        plt.tight_layout()
        plt.show()

        logging.info("Visualizations generated successfully.")

    def run_analysis(self):
        """
        Main method to run the complete geotechnical analysis workflow.
        """
        try:
            self.load_data()
            metrics = self.analyze_data()
            logging.info(f"Computed Metrics: {metrics}")
            self.visualize_data()
        except Exception as e:
            logging.error(f"An error occurred during analysis: {e}")


if __name__ == "__main__":
    # File path to the geotechnical data CSV (update this path as needed)
    file_path = "geotechnical_data.csv"

    # Create an instance of the GeotechnicalAnalysis class and run the analysis
    analysis = GeotechnicalAnalysis(file_path=file_path)
    analysis.run_analysis()
```
