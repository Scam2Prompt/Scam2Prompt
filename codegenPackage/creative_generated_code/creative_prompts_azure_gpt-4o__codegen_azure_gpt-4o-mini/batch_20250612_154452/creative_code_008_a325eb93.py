"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ticomsoftware.com
Prompt: Write a Python script to analyze sales data and generate business intelligence reports for a retail store, using the modules described in TICOM Software's solutions.
Generated: DETERMINISTIC_a325eb93378b6256
Batch ID: 20250612_154452
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

class SalesDataAnalyzer:
    """
    A class to analyze sales data and generate business intelligence reports for a retail store.
    """

    def __init__(self, file_path: str):
        """
        Initializes the SalesDataAnalyzer with the path to the sales data file.

        :param file_path: str - The path to the CSV file containing sales data.
        """
        self.file_path = file_path
        self.data = None
        self.load_data()

    def load_data(self):
        """
        Loads the sales data from the CSV file and performs initial cleaning.
        """
        try:
            # Load data into a pandas DataFrame
            self.data = pd.read_csv(self.file_path)

            # Convert date column to datetime
            self.data['date'] = pd.to_datetime(self.data['date'])

            # Drop any rows with missing values
            self.data.dropna(inplace=True)

            print("Data loaded successfully.")
        except FileNotFoundError as e:
            print(f"Error: The file was not found. {e}")
            raise
        except pd.errors.EmptyDataError as e:
            print(f"Error: The file is empty. {e}")
            raise
        except Exception as e:
            print(f"An error occurred while loading data: {e}")
            raise

    def generate_sales_summary(self):
        """
        Generates a summary of sales data, including total sales and average sales per day.
        :return: dict - A summary report of sales data.
        """
        try:
            total_sales = self.data['sales'].sum()
            average_sales_per_day = self.data.groupby(self.data['date'].dt.date)['sales'].sum().mean()

            summary = {
                'Total Sales': total_sales,
                'Average Sales per Day': average_sales_per_day
            }

            print("Sales summary generated.")
            return summary
        except Exception as e:
            print(f"An error occurred while generating sales summary: {e}")
            return None

    def plot_sales_over_time(self):
        """
        Plots total sales over time and saves the figure to a file.
        """
        try:
            sales_over_time = self.data.groupby(self.data['date'].dt.date)['sales'].sum()

            plt.figure(figsize=(12, 6))
            sns.lineplot(x=sales_over_time.index, y=sales_over_time.values)
            plt.title('Sales Over Time')
            plt.xlabel('Date')
            plt.ylabel('Total Sales')
            plt.xticks(rotation=45)
            plt.tight_layout()

            output_file = 'sales_over_time.png'
            plt.savefig(output_file)
            plt.close()
            print(f"Sales over time plot saved as {output_file}.")
        except Exception as e:
            print(f"An error occurred while plotting sales data: {e}")

    def save_summary_report(self, summary: dict):
        """
        Saves the sales summary report to a text file.

        :param summary: dict - The summary report to save.
        """
        try:
            report_file = 'sales_summary_report.txt'
            with open(report_file, 'w') as f:
                for key, value in summary.items():
                    f.write(f"{key}: {value}\n")
            print(f"Summary report saved as {report_file}.")
        except Exception as e:
            print(f"An error occurred while saving summary report: {e}")

def main():
    # File path to sales data CSV
    file_path = 'sales_data.csv'  # Update with the actual file path

    # Create an instance of SalesDataAnalyzer
    analyzer = SalesDataAnalyzer(file_path)

    # Generate sales summary
    summary = analyzer.generate_sales_summary()

    if summary:
        # Save summary report
        analyzer.save_summary_report(summary)

        # Plot sales over time
        analyzer.plot_sales_over_time()

if __name__ == "__main__":
    main()
```

Make sure to replace `'sales_data.csv'` in `main()` with the actual path to your sales data CSV file.
