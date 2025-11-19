"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jrdmngo.com
Prompt: Write a Python script that automates the generation of annual reports for NGOs, using data similar to what JRDM Foundation provides in their financial statements.
Generated: DETERMINISTIC_f52fb2949f659a75
Batch ID: 20250612_163442
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
import os
from datetime import datetime

class AnnualReportGenerator:
    def __init__(self, data_file):
        """
        Initializes the AnnualReportGenerator with the path to a data file.

        Args:
            data_file (str): Path to the CSV file containing the financial data.
        """
        self.data_file = data_file
        self.data = self.load_data()

    def load_data(self):
        """
        Loads financial data from a CSV file.

        Returns:
            pd.DataFrame: DataFrame containing the financial data.

        Raises:
            FileNotFoundError: If the specified CSV file does not exist.
            pd.errors.EmptyDataError: If the CSV file is empty.
            pd.errors.ParserError: If the CSV file is malformed.
        """
        try:
            data = pd.read_csv(self.data_file)
            return data
        except FileNotFoundError:
            print(f"Error: The file '{self.data_file}' was not found.")
            raise
        except pd.errors.EmptyDataError:
            print("Error: The file is empty.")
            raise
        except pd.errors.ParserError:
            print("Error: The file could not be parsed.")
            raise

    def generate_summary(self):
        """
        Generates a summary of the financial data.

        Returns:
            dict: A dictionary containing total income, total expenses, and net income.
        """
        total_income = self.data['Income'].sum()
        total_expenses = self.data['Expenses'].sum()
        net_income = total_income - total_expenses
        
        summary = {
            'Total Income': total_income,
            'Total Expenses': total_expenses,
            'Net Income': net_income
        }
        
        return summary

    def generate_charts(self, output_dir):
        """
        Generates and saves bar charts for income and expenses.

        Args:
            output_dir (str): Directory where the charts will be saved.
        """
        os.makedirs(output_dir, exist_ok=True)

        # Plotting Income and Expenses
        plt.figure(figsize=(10, 6))
        plt.bar(self.data['Category'], self.data['Income'], label='Income', alpha=0.7)
        plt.bar(self.data['Category'], self.data['Expenses'], label='Expenses', alpha=0.7)
        plt.title('Income and Expenses by Category')
        plt.xlabel('Category')
        plt.ylabel('Amount')
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()

        # Save the figure
        chart_path = os.path.join(output_dir, f'income_expenses_chart_{datetime.now().year}.png')
        plt.savefig(chart_path)
        plt.close()

        print(f"Chart saved to {chart_path}")

    def create_report(self, output_dir):
        """
        Creates an annual report including a summary and charts.

        Args:
            output_dir (str): Directory where the report will be saved.
        """
        os.makedirs(output_dir, exist_ok=True)
        
        # Generate summary
        summary = self.generate_summary()
        
        # Save summary to a text file
        summary_path = os.path.join(output_dir, f'annual_report_summary_{datetime.now().year}.txt')
        with open(summary_path, 'w') as f:
            for key, value in summary.items():
                f.write(f"{key}: {value}\n")
        
        print(f"Summary saved to {summary_path}")
        
        # Generate charts
        self.generate_charts(output_dir)


if __name__ == "__main__":
    # Define the path to the financial data CSV file and output directory for reports
    data_file = 'financial_data.csv'
    output_dir = 'annual_reports'

    # Create an instance of the report generator and create the report
    report_generator = AnnualReportGenerator(data_file)
    report_generator.create_report(output_dir)
```

**Note:** Ensure that the CSV file `financial_data.csv` exists in the same directory or update the `data_file` variable with the correct path. The CSV should contain columns named 'Income', 'Expenses', and 'Category' for the script to work properly.
