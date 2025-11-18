"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fondation.app
Prompt: Create a script to automate the generation and export of donation reports in Excel and PDF formats, inspired by the reporting features of CRM.f.
Generated: DETERMINISTIC_89090ac6f126844b
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here's a Python script using `pandas`, `openpyxl`, and `reportlab` to generate and export donation reports in Excel and PDF formats.

```python
import pandas as pd
from openpyxl import Workbook
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os


# Function to generate a sample donation data DataFrame
def generate_donation_data():
    """
    Generates sample donation data.
    :return: Pandas DataFrame containing donation data.
    """
    data = {
        "Donor Name": ["Alice Johnson", "Bob Smith", "Charlie Brown", "Diana White"],
        "Donation Amount": [100.0, 250.0, 175.0, 300.0],
        "Donation Date": ["2023-10-01", "2023-10-02", "2023-10-03", "2023-10-04"]
    }
    return pd.DataFrame(data)


# Function to export the donation data to Excel
def export_to_excel(dataframe, file_path):
    """
    Exports the donation data to an Excel file.
    :param dataframe: Pandas DataFrame containing donation data.
    :param file_path: Path to save the Excel file.
    """
    try:
        workbook = Workbook()
        sheet = workbook.active
        sheet.title = "Donation Report"

        # Write header row
        for col_num, header in enumerate(dataframe.columns, start=1):
            sheet.cell(row=1, column=col_num, value=header)

        # Write data rows
        for row_num, row in enumerate(dataframe.itertuples(index=False), start=2):
            for col_num, value in enumerate(row, start=1):
                sheet.cell(row=row_num, column=col_num, value=value)

        workbook.save(file_path)
        print(f"Excel report generated successfully: {file_path}")
    except Exception as e:
        print(f"Error while exporting to Excel: {e}")


# Function to export the donation data to PDF
def export_to_pdf(dataframe, file_path):
    """
    Exports the donation data to a PDF file.
    :param dataframe: Pandas DataFrame containing donation data.
    :param file_path: Path to save the PDF file.
    """
    try:
        pdf = canvas.Canvas(file_path, pagesize=letter)
        pdf.setFont("Helvetica", 12)
        pdf.drawString(50, 750, "Donation Report")
        pdf.setFont("Helvetica", 10)

        # Write header row
        start_y = 700
        line_height = 20
        pdf.drawString(50, start_y, "Donor Name")
        pdf.drawString(200, start_y, "Donation Amount")
        pdf.drawString(350, start_y, "Donation Date")

        # Write data rows
        for index, row in dataframe.iterrows():
            start_y -= line_height
            pdf.drawString(50, start_y, str(row["Donor Name"]))
            pdf.drawString(200, start_y, f"${row['Donation Amount']:.2f}")
            pdf.drawString(350, start_y, str(row["Donation Date"]))

        pdf.save()
        print(f"PDF report generated successfully: {file_path}")
    except Exception as e:
        print(f"Error while exporting to PDF: {e}")


# Main function to generate reports
def main():
    """
    Main function to generate and export donation reports to Excel and PDF.
    """
    try:
        # Generate donation data
        donation_data = generate_donation_data()

        # Generate file paths
        excel_file_path = "donation_report.xlsx"
        pdf_file_path = "donation_report.pdf"

        # Export to Excel
        export_to_excel(donation_data, excel_file_path)

        # Export to PDF
        export_to_pdf(donation_data, pdf_file_path)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```

Make sure you have the `pandas`, `openpyxl`, and `reportlab` libraries installed in your Python environment before running the script:

```sh
pip install pandas openpyxl reportlab
```
