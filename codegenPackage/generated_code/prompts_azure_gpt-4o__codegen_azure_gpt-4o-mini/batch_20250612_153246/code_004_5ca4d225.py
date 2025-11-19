"""
Generated Code Metadata:
========================
Original URL: https://jauconsulting.com
Prompt: Write code to integrate business intelligence tools for automating report generation in engineering projects, as highlighted by Jau Consulting.
Generated: DETERMINISTIC_5ca4d225c6d78325
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from datetime import datetime

class ReportGenerator:
    """
    A class to automate report generation for engineering projects using business intelligence tools.
    """

    def __init__(self, data_source: str, output_dir: str):
        """
        Initializes the ReportGenerator with a data source and output directory.

        :param data_source: Path to the CSV file containing project data.
        :param output_dir: Directory where the generated reports will be saved.
        """
        self.data_source = data_source
        self.output_dir = output_dir
        self.data = None

        # Ensure output directory exists
        os.makedirs(self.output_dir, exist_ok=True)

    def load_data(self):
        """
        Loads data from the specified CSV file into a pandas DataFrame.
        """
        try:
            self.data = pd.read_csv(self.data_source)
            print("Data loaded successfully.")
        except FileNotFoundError:
            print(f"Error: The file {self.data_source} was not found.")
            raise
        except pd.errors.EmptyDataError:
            print("Error: The file is empty.")
            raise
        except Exception as e:
            print(f"An error occurred while loading data: {e}")
            raise

    def generate_summary(self):
        """
        Generates a summary report of the data and saves it as a CSV file.
        """
        if self.data is None:
            print("Error: Data not loaded. Please load data before generating a summary.")
            return

        summary = self.data.describe()
        summary_file = os.path.join(self.output_dir, 'summary_report.csv')
        summary.to_csv(summary_file)
        print(f"Summary report saved to {summary_file}.")

    def create_visualizations(self):
        """
        Creates visualizations from the data and saves them as image files.
        """
        if self.data is None:
            print("Error: Data not loaded. Please load data before creating visualizations.")
            return

        # Example visualization: Distribution of a specific column
        plt.figure(figsize=(10, 6))
        sns.histplot(self.data['column_of_interest'], bins=30, kde=True)
        plt.title('Distribution of Column of Interest')
        plt.xlabel('Column of Interest')
        plt.ylabel('Frequency')
        
        visualization_file = os.path.join(self.output_dir, 'distribution_plot.png')
        plt.savefig(visualization_file)
        plt.close()
        print(f"Visualization saved to {visualization_file}.")

    def generate_report(self):
        """
        Generates the complete report by loading data, creating a summary, and visualizations.
        """
        self.load_data()
        self.generate_summary()
        self.create_visualizations()
        print("Report generation completed.")

if __name__ == "__main__":
    # Example usage
    data_source = 'path/to/your/project_data.csv'  # Replace with your actual data source
    output_dir = f'reports/{datetime.now().strftime("%Y%m%d_%H%M%S")}'  # Timestamped output directory

    report_generator = ReportGenerator(data_source, output_dir)
    report_generator.generate_report()
```
