"""
Generated Code Metadata:
========================
Original URL: https://kalinski-energia.pl
Prompt: Generate code to automate energy consumption analysis for enterprises, using Python and Excel, based on the solutions provided by Jacek Kaliński.
Generated: DETERMINISTIC_ad88308f168fcafc
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
from openpyxl import load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows

# Define a function to load Excel file
def load_excel_file(file_path):
    """
    Load Excel file into a pandas DataFrame.

    Args:
        file_path (str): Path to the Excel file.

    Returns:
        pd.DataFrame: Loaded data.
    """
    try:
        data = pd.read_excel(file_path)
        return data
    except Exception as e:
        print(f"Error loading Excel file: {e}")
        return None

# Define a function to analyze energy consumption
def analyze_energy_consumption(data):
    """
    Analyze energy consumption based on the provided data.

    Args:
        data (pd.DataFrame): Data containing energy consumption information.

    Returns:
        dict: Analysis results.
    """
    try:
        # Assuming data has columns: 'Date', 'Energy_Consumption'
        data['Date'] = pd.to_datetime(data['Date'])
        monthly_consumption = data.groupby(pd.Grouper(key='Date', freq='M'))['Energy_Consumption'].sum()
        average_consumption = data['Energy_Consumption'].mean()
        peak_consumption = data['Energy_Consumption'].max()
        return {
            'monthly_consumption': monthly_consumption,
            'average_consumption': average_consumption,
            'peak_consumption': peak_consumption
        }
    except Exception as e:
        print(f"Error analyzing energy consumption: {e}")
        return None

# Define a function to save results to Excel
def save_results_to_excel(results, file_path):
    """
    Save analysis results to an Excel file.

    Args:
        results (dict): Analysis results.
        file_path (str): Path to the output Excel file.
    """
    try:
        wb = load_workbook(file_path)
        ws = wb.active
        ws.title = "Energy Consumption Analysis"
        
        # Delete existing content
        ws.delete_rows(1, ws.max_row)

        # Write header
        ws.append(["Category", "Value"])

        # Write results
        for category, value in results.items():
            if category == 'monthly_consumption':
                for date, consumption in value.items():
                    ws.append([f"{category.capitalize()} on {date}", consumption])
            else:
                ws.append([category.capitalize(), value])

        wb.save(file_path)
    except Exception as e:
        print(f"Error saving results to Excel: {e}")

# Main function
def main():
    input_file_path = "energy_consumption_data.xlsx"
    output_file_path = "energy_consumption_analysis.xlsx"

    data = load_excel_file(input_file_path)
    if data is not None:
        results = analyze_energy_consumption(data)
        if results is not None:
            save_results_to_excel(results, output_file_path)

if __name__ == "__main__":
    main()
```
