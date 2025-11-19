"""
Generated Code Metadata:
========================
Original URL: https://institutopangoa.edu.pe
Prompt: Write a script to analyze student performance data for technical programs such as "Mecatrónica Automotriz," using the educational focus described on the Instituto Pangoa site.
Generated: DETERMINISTIC_27c44ed47cdc7231
Batch ID: 20250612_154927
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

class StudentPerformanceAnalyzer:
    """
    A class to analyze student performance data for technical programs.
    """

    def __init__(self, data_file):
        """
        Initializes the analyzer with the given data file.

        :param data_file: str, path to the CSV file containing student performance data
        """
        self.data_file = data_file
        self.data = None

    def load_data(self):
        """
        Loads the student performance data from a CSV file.
        """
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

    def clean_data(self):
        """
        Cleans the data by handling missing values and ensuring correct data types.
        """
        if self.data is not None:
            # Fill missing values with the mean for numerical columns
            self.data.fillna(self.data.mean(), inplace=True)
            # Convert categorical columns to 'category' dtype
            for col in self.data.select_dtypes(include=['object']).columns:
                self.data[col] = self.data[col].astype('category')
            print("Data cleaned successfully.")
        else:
            print("Error: Data not loaded. Please load the data first.")

    def analyze_performance(self):
        """
        Analyzes student performance and generates summary statistics.
        """
        if self.data is not None:
            summary = self.data.describe()
            print("Performance Analysis Summary:")
            print(summary)
            return summary
        else:
            print("Error: Data not loaded. Please load the data first.")

    def visualize_performance(self):
        """
        Visualizes student performance data using histograms and box plots.
        """
        if self.data is not None:
            numeric_cols = self.data.select_dtypes(include=[np.number]).columns
            for col in numeric_cols:
                plt.figure(figsize=(12, 6))
                plt.subplot(1, 2, 1)
                plt.hist(self.data[col], bins=20, color='blue', alpha=0.7)
                plt.title(f'Histogram of {col}')
                plt.xlabel(col)
                plt.ylabel('Frequency')

                plt.subplot(1, 2, 2)
                plt.boxplot(self.data[col])
                plt.title(f'Boxplot of {col}')
                plt.ylabel(col)

                plt.tight_layout()
                plt.show()
        else:
            print("Error: Data not loaded. Please load the data first.")

if __name__ == "__main__":
    # Path to the student performance data CSV file
    data_file_path = 'student_performance_data.csv'

    # Create an instance of the analyzer
    analyzer = StudentPerformanceAnalyzer(data_file_path)

    # Load, clean, analyze, and visualize the data
    analyzer.load_data()
    analyzer.clean_data()
    analyzer.analyze_performance()
    analyzer.visualize_performance()
```
