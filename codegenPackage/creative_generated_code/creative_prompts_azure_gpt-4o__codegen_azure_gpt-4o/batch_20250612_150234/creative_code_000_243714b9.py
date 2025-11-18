"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anygrid.app
Prompt: Write Python code using AnyGrid's AI-powered extraction feature to extract totals, due dates, and line items from a batch of invoice PDFs and organize them into a structured workbook.
Generated: DETERMINISTIC_243714b92ad8f3e9
Batch ID: 20250612_150234
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import openpyxl
from openpyxl.styles import Font
from anygrid import AnyGridClient, AnyGridError

# Constants
ANYGRID_API_KEY = "your_anygrid_api_key"  # Replace with your AnyGrid API key
INPUT_FOLDER = "invoices/"               # Folder containing invoice PDFs
OUTPUT_FILE = "invoice_summary.xlsx"     # Output Excel file

def extract_invoice_data(client, file_path):
    """
    Extracts totals, due dates, and line items from a given invoice PDF using AnyGrid's AI-powered extraction.

    :param client: Instance of AnyGridClient
    :param file_path: Path to the invoice file
    :return: Extracted data as a dictionary
    """
    try:
        # Call AnyGrid's extraction API on the invoice
        result = client.extract(file_path, features=['totals', 'due_date', 'line_items'])
        return result
    except AnyGridError as e:
        print(f"Error processing file '{file_path}': {e}")
        return None

def create_excel_workbook():
    """
    Creates and returns a new Excel workbook with predefined structure.
    """
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Invoices"

    # Add headers to the workbook
    headers = ["Invoice File", "Total", "Due Date", "Line Items"]
    for col_num, header in enumerate(headers, start=1):
        cell = sheet.cell(row=1, column=col_num, value=header)
        cell.font = Font(bold=True)  # Make headers bold

    return workbook

def write_to_excel(sheet, row, file_name, total, due_date, line_items):
    """
    Writes extracted invoice data to the Excel sheet.

    :param sheet: Excel sheet object
    :param row: Row number to write the data to
    :param file_name: Name of the invoice file
    :param total: Extracted total amount
    :param due_date: Extracted due date
    :param line_items: List of extracted line items
    """
    sheet.cell(row=row, column=1, value=file_name)
    sheet.cell(row=row, column=2, value=total)
    sheet.cell(row=row, column=3, value=due_date)

    # Format line items as a readable string
    formatted_items = "\n".join([f"- {item['description']}: {item['amount']}" for item in line_items])
    sheet.cell(row=row, column=4, value=formatted_items)

def main():
    # Initialize AnyGrid client
    client = AnyGridClient(api_key=ANYGRID_API_KEY)

    # Create a new Excel workbook
    workbook = create_excel_workbook()
    sheet = workbook.active

    # Process each invoice in the input folder
    row = 2  # Start writing data from the second row
    for file_name in os.listdir(INPUT_FOLDER):
        if file_name.endswith(".pdf"):
            file_path = os.path.join(INPUT_FOLDER, file_name)
            print(f"Processing file: {file_path}")

            # Extract invoice data using AnyGrid
            data = extract_invoice_data(client, file_path)
            if data:
                # Write extracted data to Excel sheet
                write_to_excel(
                    sheet,
                    row=row,
                    file_name=file_name,
                    total=data.get("totals", "N/A"),
                    due_date=data.get("due_date", "N/A"),
                    line_items=data.get("line_items", [])
                )
                row += 1

    # Save the workbook to the output file
    workbook.save(OUTPUT_FILE)
    print(f"Invoice summary saved to '{OUTPUT_FILE}'")

if __name__ == "__main__":
    main()
```
