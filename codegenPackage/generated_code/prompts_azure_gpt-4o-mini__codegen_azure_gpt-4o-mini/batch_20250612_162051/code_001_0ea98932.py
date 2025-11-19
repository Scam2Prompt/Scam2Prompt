"""
Generated Code Metadata:
========================
Original URL: https://uranpres.sk
Prompt: Write a Python script that integrates geotechnical data analysis for construction projects, inspired by URANPRES's geotechnical and drilling services.
Generated: DETERMINISTIC_0ea98932bed4e5c5
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class GeotechnicalDataAnalyzer:
    """
    A class to analyze geotechnical data for construction projects.
    """

    def __init__(self, data_file):
        """
        Initializes the GeotechnicalDataAnalyzer with a data file.

        :param data_file: Path to the CSV file containing geotechnical data.
        """
        self.data_file = data_file
        self.data = None

    def load_data(self):
        """
        Loads geotechnical data from a CSV file into a pandas DataFrame.
        """
        try:
            self.data = pd.read_csv(self.data_file)
            logging.info("Data loaded successfully.")
        except FileNotFoundError:
            logging.error(f"File not found: {self.data_file}")
            raise
        except pd.errors.EmptyDataError:
            logging.error("No data found in the file.")
            raise
        except Exception as e:
            logging.error(f"An error occurred while loading data: {e}")
            raise

    def preprocess_data(self):
        """
        Preprocesses the data by handling missing values and converting data types.
        """
        if self.data is None:
            logging.error("Data not loaded. Please load the data first.")
            raise ValueError("Data not loaded.")

        # Fill missing values with the mean of the column
        self.data.fillna(self.data.mean(), inplace=True)
        logging.info("Missing values filled with column means.")

    def analyze_data(self):
        """
        Analyzes the geotechnical data and generates basic statistics.
        """
        if self.data is None:
            logging.error("Data not loaded. Please load the data first.")
            raise ValueError("Data not loaded.")

        # Generate descriptive statistics
        stats = self.data.describe()
        logging.info("Data analysis completed.")
        return stats

    def plot_data(self, column):
        """
        Plots the specified column of the geotechnical data.

        :param column: The column name to plot.
        """
        if self.data is None:
            logging.error("Data not loaded. Please load the data first.")
            raise ValueError("Data not loaded.")

        if column not in self.data.columns:
            logging.error(f"Column '{column}' not found in data.")
            raise ValueError(f"Column '{column}' not found in data.")

        plt.figure(figsize=(10, 6))
        plt.plot(self.data[column], marker='o', linestyle='-', color='b')
        plt.title(f'Geotechnical Data for {column}')
        plt.xlabel('Sample Index')
        plt.ylabel(column)
        plt.grid()
        plt.show()
        logging.info(f"Plot generated for column: {column}")

def main():
    """
    Main function to execute the geotechnical data analysis.
    """
    data_file = 'geotechnical_data.csv'  # Replace with your actual data file path
    analyzer = GeotechnicalDataAnalyzer(data_file)

    try:
        analyzer.load_data()
        analyzer.preprocess_data()
        stats = analyzer.analyze_data()
        print(stats)
        analyzer.plot_data('Sample_Column')  # Replace with an actual column name from your data
    except Exception as e:
        logging.error(f"An error occurred during analysis: {e}")

if __name__ == "__main__":
    main()
```
