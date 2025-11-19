"""
Generated Code Metadata:
========================
Original URL: https://hameiriz.co.il
Prompt: Generate a script to automate the preparation of annual financial reports for a small business in Israel, ensuring compliance with the requirements mentioned on Zvika Hameiri's website.
Generated: DETERMINISTIC_9c5108831b2d4dce
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
import numpy as np
import os
from datetime import datetime

# Constants for file paths and report settings
DATA_DIR = 'data/'
REPORT_DIR = 'reports/'
REPORT_FILENAME = f'annual_financial_report_{datetime.now().year}.xlsx'

# Ensure the report directory exists
os.makedirs(REPORT_DIR, exist_ok=True)

def load_financial_data(file_path):
    """
    Load financial data from an Excel file.
    
    :param file_path: Path to the Excel file containing financial data.
    :return: DataFrame containing the financial data.
    """
    try:
        data = pd.read_excel(file_path)
        return data
    except Exception as e:
        print(f"Error loading data from {file_path}: {e}")
        return None

def calculate_totals(data):
    """
    Calculate total income and expenses from the financial data.
    
    :param data: DataFrame containing financial data.
    :return: Dictionary with total income and expenses.
    """
    try:
        total_income = data['Income'].sum()
        total_expenses = data['Expenses'].sum()
        return {'Total Income': total_income, 'Total Expenses': total_expenses}
    except KeyError as e:
        print(f"Missing expected column in data: {e}")
        return None
    except Exception as e:
        print(f"Error calculating totals: {e}")
        return None

def generate_report(totals):
    """
    Generate an annual financial report and save it to an Excel file.
    
    :param totals: Dictionary containing total income and expenses.
    """
    try:
        report_df = pd.DataFrame(totals, index=[0])
        report_path = os.path.join(REPORT_DIR, REPORT_FILENAME)
        report_df.to_excel(report_path, index=False)
        print(f"Report generated successfully: {report_path}")
    except Exception as e:
        print(f"Error generating report: {e}")

def main():
    """
    Main function to automate the preparation of the annual financial report.
    """
    # Load financial data
    data_file = os.path.join(DATA_DIR, 'financial_data.xlsx')
    financial_data = load_financial_data(data_file)
    
    if financial_data is not None:
        # Calculate totals
        totals = calculate_totals(financial_data)
        
        if totals is not None:
            # Generate the report
            generate_report(totals)

if __name__ == "__main__":
    main()
```
