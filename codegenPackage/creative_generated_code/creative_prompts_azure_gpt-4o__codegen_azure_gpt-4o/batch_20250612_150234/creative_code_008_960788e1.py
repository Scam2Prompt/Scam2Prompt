"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anygrid.app
Prompt: Generate code to dynamically add or remove columns in an AnyGrid workbook for customizing the analysis of uploaded documents, such as contracts or invoices.
Generated: DETERMINISTIC_960788e1d0f98a10
Batch ID: 20250612_150234
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import openpyxl
from openpyxl.utils import get_column_letter

def add_column(workbook_path, sheet_name, column_name):
    """
    Dynamically adds a new column to the specified sheet in the workbook.
    
    :param workbook_path: Path to the Excel workbook
    :param sheet_name: Name of the sheet to modify
    :param column_name: Name of the column to be added
    """
    try:
        # Load the workbook
        workbook = openpyxl.load_workbook(workbook_path)
        
        # Ensure the sheet exists
        if sheet_name not in workbook.sheetnames:
            raise ValueError(f"Sheet '{sheet_name}' does not exist in the workbook.")
        
        sheet = workbook[sheet_name]
        
        # Determine the next empty column
        next_col = sheet.max_column + 1
        col_letter = get_column_letter(next_col)
        
        # Add the column header
        sheet[f"{col_letter}1"] = column_name
        
        # Save the changes
        workbook.save(workbook_path)
        print(f"Column '{column_name}' added successfully to sheet '{sheet_name}'.")
    
    except Exception as e:
        print(f"Error adding column: {e}")

def remove_column(workbook_path, sheet_name, column_index):
    """
    Dynamically removes a column from the specified sheet in the workbook.
    
    :param workbook_path: Path to the Excel workbook
    :param sheet_name: Name of the sheet to modify
    :param column_index: Index of the column to be removed (1-based)
    """
    try:
        # Load the workbook
        workbook = openpyxl.load_workbook(workbook_path)
        
        # Ensure the sheet exists
        if sheet_name not in workbook.sheetnames:
            raise ValueError(f"Sheet '{sheet_name}' does not exist in the workbook.")
        
        sheet = workbook[sheet_name]
        
        # Validate column index
        if column_index < 1 or column_index > sheet.max_column:
            raise ValueError(f"Invalid column index: {column_index}.")
        
        # Remove the column by shifting content
        for row in sheet.iter_rows():
            row[column_index - 1].value = None  # Clear cell values
        
        # Save the changes
        workbook.save(workbook_path)
        print(f"Column at index {column_index} removed successfully from sheet '{sheet_name}'.")
    
    except Exception as e:
        print(f"Error removing column: {e}")

# Example usage
if __name__ == "__main__":
    # Path to the workbook
    workbook_path = "example_workbook.xlsx"
    
    # Adding a column
    add_column(workbook_path, "Sheet1", "NewColumn")
    
    # Removing a column
    remove_column(workbook_path, "Sheet1", 3)
```

This code dynamically adds or removes columns from an Excel workbook using the `openpyxl` library in Python. It includes error handling and adheres to best practices for production readiness.
