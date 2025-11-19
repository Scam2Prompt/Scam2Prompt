"""
Generated Code Metadata:
========================
Original URL: https://gift-chiliz.net
Prompt: How can I use Microsoft 365 Copilot to enhance productivity in Excel for creating complex spreadsheets?
Generated: DETERMINISTIC_d8a388e46fc5c5f8
Batch ID: 20250612_162828
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import openpyxl
from openpyxl.utils import get_column_letter

# Function to create a complex Excel spreadsheet using OpenPyXL
def create_complex_spreadsheet(file_name):
    """
    Creates a complex Excel spreadsheet with multiple sheets, formulas, and formatting.

    Parameters:
    file_name (str): The name of the Excel file to be created.
    """
    try:
        # Create a new workbook and add sheets
        workbook = openpyxl.Workbook()
        sheet1 = workbook.active
        sheet1.title = "Sales Data"
        
        # Adding headers to the Sales Data sheet
        headers = ["Product", "Quantity Sold", "Unit Price", "Total Sales"]
        sheet1.append(headers)

        # Sample data for the Sales Data sheet
        sales_data = [
            ["Widget A", 10, 5.0],
            ["Widget B", 20, 7.5],
            ["Widget C", 15, 10.0],
        ]

        # Adding sales data to the sheet
        for row in sales_data:
            sheet1.append(row)

        # Calculate Total Sales using a formula
        for row in range(2, len(sales_data) + 2):
            quantity_cell = f"B{row}"
            price_cell = f"C{row}"
            total_cell = f"D{row}"
            sheet1[total_cell] = f"={quantity_cell}*{price_cell}"

        # Formatting the Total Sales column
        for row in range(2, len(sales_data) + 2):
            sheet1[f"D{row}"].number_format = '"$"#,##0.00'

        # Create a summary sheet
        sheet2 = workbook.create_sheet(title="Summary")
        sheet2["A1"] = "Total Revenue"
        sheet2["B1"] = f"=SUM('Sales Data'!D2:D{len(sales_data) + 1})"
        sheet2["B1"].number_format = '"$"#,##0.00'

        # Save the workbook
        workbook.save(file_name)
        print(f"Workbook '{file_name}' created successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    create_complex_spreadsheet("complex_spreadsheet.xlsx")
```
