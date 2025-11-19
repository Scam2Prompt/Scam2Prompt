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
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class GeotechnicalDataAnalyzer:
    """A class to analyze geotechnical data for construction projects."""

    def __init__(self, data_file):
        """
        Initializes the GeotechnicalDataAnalyzer with the provided data file.

        Args:
            data_file (str): The path to the CSV file containing geotechnical data.
        """
        self.data_file = data_file
        self.data = None

    def load_data(self):
        """Loads geotechnical data from a CSV file into a pandas DataFrame."""
        try:
            self.data = pd.read_csv(self.data_file)
            print("Data loaded successfully.")
        except FileNotFoundError:
            print(f"Error: The file {self.data_file} was not found.")
            raise
        except pd.errors.EmptyDataError:
            print("Error: The file is empty.")
            raise
        except pd.errors.ParserError:
            print("Error: The file could not be parsed.")
            raise

    def preprocess_data(self):
        """Preprocess the geotechnical data (e.g., handle missing values)."""
        if self.data is None:
            raise RuntimeError("Data must be loaded before preprocessing.")

        # Fill missing values with the mean of each column
        self.data.fillna(self.data.mean(), inplace=True)
        print("Data preprocessed: missing values handled.")

    def analyze_data(self):
        """Conducts basic analysis on the geotechnical data."""
        if self.data is None:
            raise RuntimeError("Data must be loaded before analysis.")

        # Descriptive statistics
        stats = self.data.describe()
        print("Descriptive statistics:\n", stats)

        # Plotting data
        self.plot_data()

    def plot_data(self):
        """Generates plots for the geotechnical data."""
        if self.data is None:
            raise RuntimeError("Data must be loaded before plotting.")

        # Example: Plot the distribution of a specific geotechnical parameter
        for column in self.data.columns:
            plt.figure()
            plt.hist(self.data[column].dropna(), bins=20, alpha=0.7, color='blue')
            plt.title(f'Distribution of {column}')
            plt.xlabel(column)
            plt.ylabel('Frequency')
            plt.grid()
            plt.savefig(f'{column}_distribution.png')
            plt.close()
            print(f"Plot saved: {column}_distribution.png")

def main():
    """Main function to execute the geotechnical data analysis."""
    # Path to the geotechnical data file
    data_file = 'geotechnical_data.csv'
    
    # Create an instance of the analyzer
    analyzer = GeotechnicalDataAnalyzer(data_file)

    # Load, preprocess, and analyze the data
    analyzer.load_data()
    analyzer.preprocess_data()
    analyzer.analyze_data()

if __name__ == "__main__":
    main()
```
