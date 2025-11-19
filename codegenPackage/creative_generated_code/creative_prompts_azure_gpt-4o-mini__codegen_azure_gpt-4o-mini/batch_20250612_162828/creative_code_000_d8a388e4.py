"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gift-chiliz.net
Prompt: How can I use Microsoft 365 Copilot to enhance productivity in Excel for creating complex spreadsheets?
Generated: DETERMINISTIC_d8a388e46fc5c5f8
Batch ID: 20250612_162828
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import openpyxl
from openpyxl.styles import Font
from openpyxl.utils import get_column_letter

def create_complex_spreadsheet(file_name: str, data: list, headers: list):
    """
    Create a complex spreadsheet in Excel using OpenPyXL.

    Parameters:
    file_name (str): The name of the Excel file to create.
    data (list): A list of lists containing the data to write to the spreadsheet.
    headers (list): A list of headers to use for the spreadsheet columns.

    Returns:
    str: A message indicating the result of the operation.
    """
    try:
        # Create a new workbook and select the active worksheet
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.title = "Complex Data"

        # Adding headers to the spreadsheet
        for col_num, header in enumerate(headers, 1):
            cell = sheet.cell(row=1, column=col_num)
            cell.value = header
            cell.font = Font(bold=True)  # Make headers bold

        # Adding data to the spreadsheet
        for row_num, row_data in enumerate(data, 2):  # Start from the second row
            for col_num, value in enumerate(row_data, 1):
                sheet.cell(row=row_num, column=col_num, value=value)

        # Adjust the width of the columns
        for col_num in range(1, len(headers) + 1):
            column_letter = get_column_letter(col_num)
            sheet.column_dimensions[column_letter].width = 20  # Set a default width

        # Save the workbook to a file
        workbook.save(file_name)
        return f"Spreadsheet '{file_name}' created successfully."

    except Exception as e:
        return f"An error occurred: {str(e)}"

# Example usage
if __name__ == "__main__":
    headers = ["Date", "Sales", "Expenses", "Profit"]
    data = [
        ["2023-01-01", 2000, 1500, 500],
        ["2023-01-02", 2500, 1200, 1300],
        ["2023-01-03", 1800, 800, 1000]
    ]
    result = create_complex_spreadsheet("complex_data.xlsx", data, headers)
    print(result)
```
