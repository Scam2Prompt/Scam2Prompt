"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thebookkeepingdiaries.com
Prompt: How can I create a monthly financial statement generator in Excel that aligns with the bookkeeping strategies mentioned on The Bookkeeping Diaries?
Generated: DETERMINISTIC_8d4b5d9075c402a1
Batch ID: 20250612_161301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is Python code using the `openpyxl` library to create a monthly financial statement generator in Excel. The code includes proper structure, error handling, and comments.

```python
import openpyxl
from openpyxl.styles import Font, Alignment
import datetime

def create_monthly_financial_statement(file_name, month, year, data):
    """
    Generates a monthly financial statement Excel file.

    Args:
        file_name (str): Name of the Excel file to save the statement.
        month (int): Month for the financial statement (1=Jan, 2=Feb, etc.).
        year (int): Year for the financial statement.
        data (list of dict): Financial data, e.g.,
                             [{"Date": "2023-10-01", "Description": "Income", "Amount": 5000, "Type": "Credit"},
                              {"Date": "2023-10-02", "Description": "Rent", "Amount": 2000, "Type": "Debit"}]
    Raises:
        ValueError: If input data or parameters are invalid.
    """

    # Validate input parameters
    if not (1 <= month <= 12):
        raise ValueError("Invalid month. Month should be between 1 and 12.")
    if year < 1900 or year > datetime.datetime.now().year:
        raise ValueError("Invalid year. Year should be within a valid range.")
    if not isinstance(data, list) or not all(isinstance(entry, dict) for entry in data):
        raise ValueError("Invalid data format. Data must be a list of dictionaries.")

    try:
        # Create a new workbook and worksheet
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.title = f"{datetime.date(year, month, 1).strftime('%B')} {year} Statement"

        # Add headers to the worksheet
        headers = ["Date", "Description", "Amount", "Type"]
        sheet.append(headers)

        # Apply styling to headers
        header_font = Font(bold=True)
        for col in range(1, len(headers) + 1):
            cell = sheet.cell(row=1, column=col)
            cell.font = header_font
            cell.alignment = Alignment(horizontal="center")

        # Populate financial data into the worksheet
        for entry in data:
            # Ensure mandatory fields exist
            if all(key in entry for key in headers):
                sheet.append([entry["Date"], entry["Description"], entry["Amount"], entry["Type"]])
            else:
                raise ValueError("Missing one or more required keys in data entry.")

        # Auto-adjust column widths
        for column in sheet.columns:
            max_length = 0
            column_letter = column[0].column_letter
            for cell in column:
                try:
                    if cell.value:
                        max_length = max(max_length, len(str(cell.value)))
                except:
                    pass
            adjusted_width = max_length + 2  # Add some padding
            sheet.column_dimensions[column_letter].width = adjusted_width

        # Save the workbook to a file
        workbook.save(file_name)
        print(f"Monthly financial statement saved as '{file_name}'.")

    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An error occurred while generating the financial statement: {e}")

# Example usage
if __name__ == "__main__":
    # Sample financial data
    sample_data = [
        {"Date": "2023-10-01", "Description": "Income", "Amount": 5000, "Type": "Credit"},
        {"Date": "2023-10-02", "Description": "Rent", "Amount": -2000, "Type": "Debit"},
        {"Date": "2023-10-15", "Description": "Utilities", "Amount": -300, "Type": "Debit"},
        {"Date": "2023-10-20", "Description": "Freelance Payment", "Amount": 1500, "Type": "Credit"}
    ]

    # Create statement for October 2023
    create_monthly_financial_statement("October_2023_Statement.xlsx", month=10, year=2023, data=sample_data)
```

This code generates a well-formatted Excel file with monthly financial data provided by the user. It adheres to best practices, including validation and error handling.
