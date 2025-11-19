"""
Generated Code Metadata:
========================
Original URL: https://mdatechsys.com
Prompt: Create a Python script for generating ROI reports, based on the ROI software solutions mentioned by MDA Tech Sys.
Generated: DETERMINISTIC_62c2394271f743a2
Batch ID: 20250612_152045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# roi_report_generator.py

import pandas as pd
from datetime import datetime

def load_data(file_path):
    """
    Load ROI data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded data.

    Raises:
        FileNotFoundError: If the file does not exist.
        pd.errors.EmptyDataError: If the file is empty.
        pd.errors.ParserError: If the file is malformed.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: File '{file_path}' is empty.")
        return None
    except pd.errors.ParserError:
        print(f"Error: Failed to parse file '{file_path}'.")
        return None

def calculate_roi(data, cost_column, revenue_column):
    """
    Calculate ROI for each row in the data.

    Args:
        data (pd.DataFrame): Data containing cost and revenue columns.
        cost_column (str): Name of the cost column.
        revenue_column (str): Name of the revenue column.

    Returns:
        pd.DataFrame: Data with added ROI column.

    Raises:
        ValueError: If cost or revenue column does not exist.
    """
    if cost_column not in data.columns or revenue_column not in data.columns:
        raise ValueError("Cost or revenue column does not exist.")

    data['roi'] = (data[revenue_column] - data[cost_column]) / data[cost_column]
    return data

def generate_report(data, report_columns):
    """
    Generate an ROI report.

    Args:
        data (pd.DataFrame): Data to generate the report from.
        report_columns (list): List of columns to include in the report.

    Returns:
        pd.DataFrame: ROI report.

    Raises:
        ValueError: If a report column does not exist.
    """
    for column in report_columns:
        if column not in data.columns:
            raise ValueError(f"Report column '{column}' does not exist.")

    report = data[report_columns]
    return report

def main():
    # Load data
    data_file = 'roi_data.csv'
    data = load_data(data_file)

    if data is not None:
        # Calculate ROI
        cost_column = 'cost'
        revenue_column = 'revenue'
        data = calculate_roi(data, cost_column, revenue_column)

        # Generate report
        report_columns = ['id', 'name', 'cost', 'revenue', 'roi']
        report = generate_report(data, report_columns)

        # Save report to CSV
        report_file = f"roi_report_{datetime.now().strftime('%Y%m%d%H%M%S')}.csv"
        report.to_csv(report_file, index=False)
        print(f"ROI report saved to '{report_file}'")

if __name__ == "__main__":
    main()
```
