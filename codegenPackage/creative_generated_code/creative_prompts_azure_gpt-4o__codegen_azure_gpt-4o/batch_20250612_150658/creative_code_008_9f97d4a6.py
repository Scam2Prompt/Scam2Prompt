"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gift-chiliz.net
Prompt: Write a script to use the Microsoft Excel API for generating a budget spreadsheet automatically, leveraging Copilot's AI-powered templates.
Generated: DETERMINISTIC_9f97d4a656014b1c
Batch ID: 20250612_150658
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import os
import openpyxl
from openpyxl.styles import Font
from openpyxl.utils.exceptions import InvalidFileException

# Define constants
FILE_NAME = "BudgetSpreadsheet.xlsx"
SHEET_NAME = "Budget"
HEADERS = ["Category", "Planned Amount", "Actual Amount", "Difference"]
DEFAULT_BUDGET_CATEGORIES = [
    {"Category": "Housing", "Planned Amount": 1500},
    {"Category": "Transportation", "Planned Amount": 300},
    {"Category": "Food", "Planned Amount": 500},
    {"Category": "Utilities", "Planned Amount": 200},
    {"Category": "Entertainment", "Planned Amount": 150},
]

def create_budget_spreadsheet(file_name: str, sheet_name: str, headers: list, budget_data: list):
    """
    Creates a budget spreadsheet with pre-defined headers and budget data.

    Args:
    file_name (str): Name of the spreadsheet file.
    sheet_name (str): Name of the worksheet.
    headers (list): List of column headers.
    budget_data (list): List of dictionaries with budget data.
    """
    try:
        # Create a new workbook and select the active sheet
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.title = sheet_name

        # Write headers to the first row
        for col, header in enumerate(headers, start=1):
            cell = sheet.cell(row=1, column=col, value=header)
            cell.font = Font(bold=True)  # Apply bold font style to headers

        # Populate the budget data
        for row, entry in enumerate(budget_data, start=2):
            sheet.cell(row=row, column=1, value=entry["Category"])
            sheet.cell(row=row, column=2, value=entry["Planned Amount"])
            sheet.cell(row=row, column=3, value=0)  # Default Actual Amount to 0
            sheet.cell(row=row, column=4, value=f"=B{row}-C{row}")  # Difference formula

        # Save the workbook to the specified file
        workbook.save(file_name)
        print(f"Spreadsheet '{file_name}' created successfully.")
    except InvalidFileException as e:
        print(f"Error: Invalid file format. Details: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    # Ensure the script runs only when executed directly
    try:
        # Check if the file already exists
        if os.path.exists(FILE_NAME):
            print(f"Error: File '{FILE_NAME}' already exists. Please delete it or choose a different name.")
        else:
            # Generate the budget spreadsheet
            create_budget_spreadsheet(FILE_NAME, SHEET_NAME, HEADERS, DEFAULT_BUDGET_CATEGORIES)
    except Exception as e:
        print(f"An error occurred while creating the spreadsheet: {str(e)}")
```
