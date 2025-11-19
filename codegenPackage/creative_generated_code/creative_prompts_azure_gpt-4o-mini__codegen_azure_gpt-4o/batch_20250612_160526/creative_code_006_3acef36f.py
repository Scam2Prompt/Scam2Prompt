"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://axtempl.cc
Prompt: Explain how to use axtempl.pro to create a customizable invoice template in Excel format, including specific fields to include.
Generated: DETERMINISTIC_3acef36fe6e7b7b1
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script uses the `xlsxwriter` library to create a customizable invoice template
in Excel format. The template includes fields such as Invoice Number, Customer Name,
Date, Item Description, Quantity, Unit Price, and Total Price.

Install the required library:
pip install xlsxwriter

Usage:
Run the script to generate an Excel file named "invoice_template.xlsx".
"""

import xlsxwriter

def create_invoice_template(file_name):
    try:
        # Create an Excel workbook and worksheet
        workbook = xlsxwriter.Workbook(file_name)
        worksheet = workbook.add_worksheet("Invoice")

        # Define cell formats
        header_format = workbook.add_format({
            'bold': True,
            'align': 'center',
            'valign': 'vcenter',
            'bg_color': '#D9EAD3',
            'border': 1
        })
        cell_format = workbook.add_format({
            'border': 1,
            'align': 'left',
            'valign': 'vcenter'
        })

        # Define column widths
        column_widths = {
            'A': 15,  # Invoice Number
            'B': 20,  # Customer Name
            'C': 15,  # Date
            'D': 25,  # Item Description
            'E': 10,  # Quantity
            'F': 15,  # Unit Price
            'G': 15   # Total Price
        }

        # Set column widths
        for col, width in column_widths.items():
            worksheet.set_column(f"{col}:{col}", width)

        # Define header row
        headers = [
            "Invoice Number", "Customer Name", "Date",
            "Item Description", "Quantity", "Unit Price", "Total Price"
        ]

        # Write headers to the first row
        for col_idx, header in enumerate(headers):
            worksheet.write(0, col_idx, header, header_format)

        # Add a few example rows for demonstration (optional)
        example_rows = [
            ["INV-001", "John Doe", "2023-10-15", "Widget A", 5, 10.00, "=E2*F2"],
            ["INV-002", "Jane Smith", "2023-10-16", "Widget B", 3, 12.50, "=E3*F3"]
        ]

        for row_idx, row_data in enumerate(example_rows, start=1):
            for col_idx, cell_data in enumerate(row_data):
                worksheet.write(row_idx, col_idx, cell_data, cell_format)

        # Add a total calculation formula at the bottom (optional)
        worksheet.write(len(example_rows) + 1, 6, "=SUM(G2:G3)", header_format)

        # Close the workbook
        workbook.close()

        print(f"Invoice template created successfully: {file_name}")

    except Exception as e:
        print(f"An error occurred while creating the invoice template: {e}")


if __name__ == "__main__":
    create_invoice_template("invoice_template.xlsx")
```
