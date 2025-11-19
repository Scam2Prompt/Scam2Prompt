"""
Generated Code Metadata:
========================
Original URL: https://jrdmngo.com
Prompt: Write a Python script that automates the generation of annual reports for NGOs, using data similar to what JRDM Foundation provides in their financial statements.
Generated: DETERMINISTIC_f52fb2949f659a75
Batch ID: 20250612_163442
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
from datetime import datetime
import os

class NGOAnnualReportGenerator:
    """
    A class to generate annual reports for NGOs based on financial data.
    """

    def __init__(self, data_file):
        """
        Initializes the report generator with the provided data file.

        :param data_file: Path to the CSV file containing financial data.
        """
        self.data_file = data_file
        self.data = None
        self.report_dir = "annual_reports"

        # Create report directory if it doesn't exist
        os.makedirs(self.report_dir, exist_ok=True)

    def load_data(self):
        """
        Loads financial data from the CSV file into a DataFrame.
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
        except Exception as e:
            print(f"An error occurred while loading data: {e}")
            raise

    def generate_summary(self):
        """
        Generates a summary of the financial data.
        :return: A DataFrame containing the summary.
        """
        if self.data is None:
            raise ValueError("Data not loaded. Please load the data first.")

        summary = {
            'Total Income': self.data['Income'].sum(),
            'Total Expenses': self.data['Expenses'].sum(),
            'Net Income': self.data['Income'].sum() - self.data['Expenses'].sum(),
            'Total Assets': self.data['Assets'].sum(),
            'Total Liabilities': self.data['Liabilities'].sum(),
        }
        return pd.DataFrame(summary, index=[0])

    def create_visualizations(self):
        """
        Creates visualizations for the financial data and saves them as images.
        """
        if self.data is None:
            raise ValueError("Data not loaded. Please load the data first.")

        # Income vs Expenses
        plt.figure(figsize=(10, 6))
        plt.bar(['Income', 'Expenses'], [self.data['Income'].sum(), self.data['Expenses'].sum()], color=['green', 'red'])
        plt.title('Total Income vs Total Expenses')
        plt.ylabel('Amount')
        plt.savefig(os.path.join(self.report_dir, 'income_vs_expenses.png'))
        plt.close()

        # Assets vs Liabilities
        plt.figure(figsize=(10, 6))
        plt.bar(['Assets', 'Liabilities'], [self.data['Assets'].sum(), self.data['Liabilities'].sum()], color=['blue', 'orange'])
        plt.title('Total Assets vs Total Liabilities')
        plt.ylabel('Amount')
        plt.savefig(os.path.join(self.report_dir, 'assets_vs_liabilities.png'))
        plt.close()

    def generate_report(self):
        """
        Generates the annual report by creating a summary and visualizations.
        """
        summary = self.generate_summary()
        report_file = os.path.join(self.report_dir, f"annual_report_{datetime.now().year}.txt")

        with open(report_file, 'w') as f:
            f.write("Annual Report\n")
            f.write("====================\n")
            f.write(summary.to_string(index=False))
            f.write("\n\nVisualizations saved in the 'annual_reports' directory.\n")

        print(f"Report generated successfully: {report_file}")

    def run(self):
        """
        Executes the report generation process.
        """
        self.load_data()
        self.create_visualizations()
        self.generate_report()


if __name__ == "__main__":
    # Path to the financial data CSV file
    data_file_path = "financial_data.csv"  # Update this path as needed

    # Create an instance of the report generator and run it
    report_generator = NGOAnnualReportGenerator(data_file_path)
    report_generator.run()
```

Make sure to have a CSV file named `financial_data.csv` with the appropriate columns (`Income`, `Expenses`, `Assets`, `Liabilities`) in the same directory as this script for it to run successfully.
