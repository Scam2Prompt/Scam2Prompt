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
import os
import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Font

class InvoiceGenerator:
    """
    A class to generate customizable invoice templates in Excel format.

    Attributes
    ----------
    invoice_data : dict
        A dictionary holding the data for the invoice.

    Methods
    -------
    create_invoice_template(file_path: str):
        Generates an Excel invoice template and saves it to the specified path.
    """

    def __init__(self, invoice_data):
        """
        Initializes the InvoiceGenerator with invoice data.

        Parameters
        ----------
        invoice_data : dict
            A dictionary containing invoice details such as customer name, 
            invoice number, items, and total amount.
        """
        self.invoice_data = invoice_data

    def create_invoice_template(self, file_path: str):
        """
        Creates an Excel invoice template with the specified fields.

        Parameters
        ----------
        file_path : str
            The path where the Excel file will be saved.
        
        Raises
        ------
        FileNotFoundError
            If the specified path is invalid.
        Exception
            For any other errors during the file generation.
        """
        try:
            # Ensure the directory exists
            os.makedirs(os.path.dirname(file_path), exist_ok=True)

            # Create a new workbook and select the active worksheet
            workbook = Workbook()
            sheet = workbook.active
            sheet.title = "Invoice"

            # Define header fields for the invoice
            headers = [
                "Invoice Number", "Customer Name", "Date", 
                "Item Description", "Quantity", "Unit Price", "Total"
            ]

            # Set headers in the first row
            for col_num, header in enumerate(headers, start=1):
                cell = sheet.cell(row=1, column=col_num)
                cell.value = header
                cell.font = Font(bold=True)

            # Populate invoice data
            row_num = 2
            for item in self.invoice_data.get("items", []):
                sheet.cell(row=row_num, column=1, value=self.invoice_data.get("invoice_number"))
                sheet.cell(row=row_num, column=2, value=self.invoice_data.get("customer_name"))
                sheet.cell(row=row_num, column=3, value=self.invoice_data.get("date"))
                sheet.cell(row=row_num, column=4, value=item.get("description"))
                sheet.cell(row=row_num, column=5, value=item.get("quantity"))
                sheet.cell(row=row_num, column=6, value=item.get("unit_price"))
                sheet.cell(row=row_num, column=7, value=item.get("total"))

                row_num += 1

            # Save the workbook to the specified path
            workbook.save(file_path)

        except FileNotFoundError as e:
            print(f"Error: Specified path not found - {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    invoice_data_example = {
        "invoice_number": "INV-001",
        "customer_name": "John Doe",
        "date": "2023-10-01",
        "items": [
            {"description": "Widget A", "quantity": 2, "unit_price": 15.00, "total": 30.00},
            {"description": "Widget B", "quantity": 1, "unit_price": 25.00, "total": 25.00},
        ]
    }

    # Create an instance of InvoiceGenerator with the example data
    invoice_generator = InvoiceGenerator(invoice_data_example)

    # Specify the file path where the invoice will be saved
    output_file_path = "invoices/invoice_001.xlsx"

    # Generate the invoice template
    invoice_generator.create_invoice_template(output_file_path)
```
