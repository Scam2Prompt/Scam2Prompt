"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jauconsulting.com
Prompt: Write code to integrate business intelligence tools for automating report generation in engineering projects, as highlighted by Jau Consulting.
Generated: DETERMINISTIC_5ca4d225c6d78325
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import os

class ReportGenerator:
    """
    A class to automate report generation for engineering projects using business intelligence tools.
    """

    def __init__(self, data_file, output_directory):
        """
        Initializes the ReportGenerator with the data file and output directory.

        Args:
            data_file (str): Path to the data file (CSV format).
            output_directory (str): Directory where the generated reports will be saved.
        """
        self.data_file = data_file
        self.output_directory = output_directory
        self.data = None

        # Check if the output directory exists, if not create it
        os.makedirs(self.output_directory, exist_ok=True)

    def load_data(self):
        """
        Loads data from the specified CSV file into a pandas DataFrame.
        
        Raises:
            FileNotFoundError: If the data file does not exist.
            pd.errors.EmptyDataError: If the data file is empty.
        """
        try:
            self.data = pd.read_csv(self.data_file)
            print(f"Data loaded successfully from {self.data_file}")
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {self.data_file} was not found.")
        except pd.errors.EmptyDataError:
            raise ValueError("The data file is empty.")

    def generate_summary(self):
        """
        Generates a summary report of the data and saves it as a CSV file.

        Saves the summary report in the output directory.
        """
        summary = self.data.describe()
        summary_file_path = os.path.join(self.output_directory, 'summary_report.csv')
        summary.to_csv(summary_file_path)
        print(f"Summary report saved to {summary_file_path}")

    def generate_visualizations(self):
        """
        Generates visualizations from the data and saves them as image files.
        
        Creates a histogram and a box plot for the numerical columns in the data.
        """
        numerical_cols = self.data.select_dtypes(include=['float64', 'int64']).columns

        for col in numerical_cols:
            plt.figure(figsize=(10, 5))

            # Histogram
            plt.subplot(1, 2, 1)
            sns.histplot(self.data[col], bins=30, kde=True)
            plt.title(f'Histogram of {col}')
            plt.xlabel(col)
            plt.ylabel('Frequency')

            # Box plot
            plt.subplot(1, 2, 2)
            sns.boxplot(y=self.data[col])
            plt.title(f'Box Plot of {col}')
            plt.ylabel(col)

            visualization_file_path = os.path.join(self.output_directory, f'{col}_visualization.png')
            plt.tight_layout()
            plt.savefig(visualization_file_path)
            plt.close()  # Close the figure to avoid display
            print(f"Visualization for {col} saved to {visualization_file_path}")

    def run(self):
        """
        Runs the report generation process: loads data, generates summary and visualizations.
        """
        self.load_data()
        self.generate_summary()
        self.generate_visualizations()


if __name__ == "__main__":
    # Example usage
    try:
        data_file_path = 'path/to/your/data.csv'  # Update with the actual path
        output_dir = 'reports'  # Directory to save reports

        report_generator = ReportGenerator(data_file_path, output_dir)
        report_generator.run()

    except Exception as e:
        print(f"An error occurred: {e}")
```
