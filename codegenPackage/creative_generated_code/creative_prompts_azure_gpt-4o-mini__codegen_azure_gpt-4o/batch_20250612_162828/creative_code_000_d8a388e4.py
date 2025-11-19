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
"""
Microsoft 365 Copilot is an AI-driven tool integrated into Office applications like Excel to enhance productivity.
While interacting programmatically with Copilot isn't possible (since it's a built-in feature), you can use Python 
to automate Excel tasks using libraries like `openpyxl` or `pandas` for creating complex spreadsheets.

Below is a Python script using `openpyxl` to create a complex Excel spreadsheet programmatically.
This serves as an alternative to enhance productivity if Copilot is not available.
"""

from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, Border, Side
import os

def create_complex_spreadsheet(file_name):
    """
    Creates a complex Excel spreadsheet with styled headers, formulas, and data.
    
    :param file_name: The name of the file to save the Excel spreadsheet to.
    """
    try:
        # Create a new workbook and select the active worksheet
        wb = Workbook()
        ws = wb.active
        ws.title = "Sales Data"

        # Define header row and data
        headers = ["Product", "Region", "Sales Q1", "Sales Q2", "Sales Q3", "Sales Q4", "Total Sales"]
        data = [
            ["Product A", "North", 1200, 1350, 1400, 1500],
            ["Product B", "South", 800, 950, 1000, 1100],
            ["Product C", "East", 1500, 1600, 1700, 1800],
            ["Product D", "West", 1000, 1050, 1100, 1200],
        ]

        # Apply styling to header row
        header_font = Font(bold=True, color="FFFFFF")
        header_fill_color = "4F81BD"  # Light blue
        header_alignment = Alignment(horizontal="center", vertical="center")
        border_style = Border(left=Side(style="thin"),
                              right=Side(style="thin"),
                              top=Side(style="thin"),
                              bottom=Side(style="thin"))

        for col, header in enumerate(headers, start=1):
            cell = ws.cell(row=1, column=col, value=header)
            cell.font = header_font
            cell.alignment = header_alignment
            cell.fill = openpyxl.styles.PatternFill(start_color=header_fill_color, end_color=header_fill_color, fill_type="solid")
            cell.border = border_style

        # Add data rows
        for row_num, row_data in enumerate(data, start=2):
            for col_num, value in enumerate(row_data, start=1):
                ws.cell(row=row_num, column=col_num, value=value)

            # Add formula for Total Sales column
            total_sales_formula = f"=SUM(C{row_num}:F{row_num})"
            ws.cell(row=row_num, column=len(headers), value=total_sales_formula)

        # Adjust column widths for better readability
        for col in ws.columns:
            max_length = max(len(str(cell.value)) if cell.value is not None else 0 for cell in col)
            adjusted_width = max_length + 2
            ws.column_dimensions[col[0].column_letter].width = adjusted_width

        # Save the spreadsheet to the specified file
        wb.save(file_name)
        print(f"Spreadsheet created successfully: {file_name}")

    except Exception as e:
        print(f"An error occurred while creating the spreadsheet: {e}")


# Main script execution
if __name__ == "__main__":
    # File name for the spreadsheet
    output_file_name = "Complex_Spreadsheet.xlsx"
    create_complex_spreadsheet(output_file_name)
```
