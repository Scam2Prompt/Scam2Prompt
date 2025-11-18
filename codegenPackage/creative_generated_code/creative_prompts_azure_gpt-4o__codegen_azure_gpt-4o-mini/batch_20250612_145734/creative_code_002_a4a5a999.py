"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prize-steth.com
Prompt: Generate code to use Microsoft 365 Copilot to analyze data in an Excel spreadsheet and create a summary report.
Generated: DETERMINISTIC_a4a5a999a2e84e20
Batch ID: 20250612_145734
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import openpyxl
from openpyxl import Workbook

def load_excel_data(file_path):
    """
    Load data from an Excel file into a pandas DataFrame.

    :param file_path: Path to the Excel file.
    :return: DataFrame containing the data from the Excel file.
    :raises FileNotFoundError: If the file does not exist.
    :raises ValueError: If the file is not a valid Excel file.
    """
    try:
        data = pd.read_excel(file_path)
        return data
    except FileNotFoundError as fnf_error:
        print(f"Error: {fnf_error}")
        raise
    except ValueError as val_error:
        print(f"Error: {val_error}")
        raise

def generate_summary_report(data):
    """
    Generate a summary report from the provided DataFrame.

    :param data: DataFrame containing the data to analyze.
    :return: A summary DataFrame with aggregated results.
    """
    # Example of generating summary statistics
    summary = {
        'Total Rows': len(data),
        'Columns': list(data.columns),
        'Mean Values': data.mean(numeric_only=True).to_dict(),
        'Median Values': data.median(numeric_only=True).to_dict(),
        'Standard Deviation': data.std(numeric_only=True).to_dict()
    }
    
    return pd.DataFrame(summary)

def save_summary_report(summary, output_file):
    """
    Save the summary DataFrame to an Excel file.

    :param summary: Summary DataFrame to save.
    :param output_file: Path to the output Excel file.
    :raises IOError: If there is an error writing to the file.
    """
    try:
        with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
            summary.to_excel(writer, sheet_name='Summary', index=False)
    except IOError as io_error:
        print(f"Error: {io_error}")
        raise

def main():
    """
    Main function to load data, generate summary, and save the report.
    """
    input_file = 'input_data.xlsx'  # Path to the input Excel file
    output_file = 'summary_report.xlsx'  # Path to the output summary report

    # Load data from Excel file
    data = load_excel_data(input_file)

    # Generate summary report
    summary = generate_summary_report(data)

    # Save the summary report to an Excel file
    save_summary_report(summary, output_file)

if __name__ == "__main__":
    main()
```
