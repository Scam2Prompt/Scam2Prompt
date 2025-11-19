"""
Generated Code Metadata:
========================
Original URL: https://sunsystems.hk
Prompt: Generate code to create a custom financial report using Infor SunSystems advanced reporting capabilities, tailored for Hong Kong businesses.
Generated: DETERMINISTIC_ac0c6e3bb2054cfb
Batch ID: 20250612_154226
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
from datetime import datetime

class FinancialReport:
    """
    A class to generate a custom financial report for Hong Kong businesses using Infor SunSystems data.
    """

    def __init__(self, data_source):
        """
        Initializes the FinancialReport with a data source.

        :param data_source: Path to the data source (CSV, Excel, etc.)
        """
        self.data_source = data_source
        self.data = None

    def load_data(self):
        """
        Loads financial data from the specified data source.
        """
        try:
            # Load data into a DataFrame
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

    def preprocess_data(self):
        """
        Preprocesses the data to prepare it for reporting.
        This includes handling missing values and converting data types.
        """
        if self.data is None:
            raise ValueError("Data not loaded. Please call load_data() first.")

        # Fill missing values with 0 for financial figures
        self.data.fillna(0, inplace=True)

        # Convert date columns to datetime format
        if 'transaction_date' in self.data.columns:
            self.data['transaction_date'] = pd.to_datetime(self.data['transaction_date'], errors='coerce')

    def generate_report(self):
        """
        Generates a financial report tailored for Hong Kong businesses.
        The report includes total revenue, total expenses, and net profit.
        """
        if self.data is None:
            raise ValueError("Data not loaded. Please call load_data() first.")

        # Group by month and calculate totals
        self.data['month'] = self.data['transaction_date'].dt.to_period('M')
        report = self.data.groupby('month').agg(
            total_revenue=pd.NamedAgg(column='revenue', aggfunc='sum'),
            total_expenses=pd.NamedAgg(column='expenses', aggfunc='sum')
        )

        # Calculate net profit
        report['net_profit'] = report['total_revenue'] - report['total_expenses']

        return report

    def save_report(self, report, output_file):
        """
        Saves the generated report to a specified output file.

        :param report: The report DataFrame to save
        :param output_file: Path to the output file (CSV, Excel, etc.)
        """
        try:
            report.to_csv(output_file, index=True)
            print(f"Report saved successfully to {output_file}.")
        except Exception as e:
            print(f"An error occurred while saving the report: {e}")
            raise

if __name__ == "__main__":
    # Example usage
    report_generator = FinancialReport(data_source='financial_data.csv')
    
    try:
        report_generator.load_data()
        report_generator.preprocess_data()
        financial_report = report_generator.generate_report()
        report_generator.save_report(financial_report, output_file='financial_report_hk.csv')
    except Exception as e:
        print(f"An error occurred during report generation: {e}")
```
