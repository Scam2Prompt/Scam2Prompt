"""
Generated Code Metadata:
========================
Original URL: https://fondation.app
Prompt: Create a script to automate the generation and export of donation reports in Excel and PDF formats, inspired by the reporting features of CRM.f.
Generated: DETERMINISTIC_89090ac6f126844b
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from fpdf import FPDF
import os
from datetime import datetime

class DonationReportGenerator:
    def __init__(self, donations):
        """
        Initializes the DonationReportGenerator with a list of donations.

        :param donations: List of dictionaries containing donation data.
        """
        self.donations = donations

    def generate_report(self):
        """
        Generates a donation report in both Excel and PDF formats.
        """
        try:
            self.export_to_excel()
            self.export_to_pdf()
            print("Reports generated successfully.")
        except Exception as e:
            print(f"An error occurred while generating reports: {e}")

    def export_to_excel(self):
        """
        Exports the donation data to an Excel file.
        """
        try:
            # Create a DataFrame from the donations list
            df = pd.DataFrame(self.donations)
            # Define the output file name
            excel_file = f"donation_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
            # Export the DataFrame to an Excel file
            df.to_excel(excel_file, index=False)
            print(f"Excel report generated: {excel_file}")
        except Exception as e:
            print(f"Failed to export to Excel: {e}")

    def export_to_pdf(self):
        """
        Exports the donation data to a PDF file.
        """
        try:
            # Define the output file name
            pdf_file = f"donation_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
            # Create a PDF object
            pdf = FPDF()
            pdf.set_auto_page_break(auto=True, margin=15)
            pdf.add_page()
            pdf.set_font("Arial", size=12)

            # Add a title
            pdf.cell(200, 10, txt="Donation Report", ln=True, align='C')

            # Add column headers
            pdf.set_font("Arial", 'B', size=12)
            headers = self.donations[0].keys()
            for header in headers:
                pdf.cell(40, 10, header, border=1)
            pdf.ln()

            # Add donation data
            pdf.set_font("Arial", size=12)
            for donation in self.donations:
                for value in donation.values():
                    pdf.cell(40, 10, str(value), border=1)
                pdf.ln()

            # Save the PDF to a file
            pdf.output(pdf_file)
            print(f"PDF report generated: {pdf_file}")
        except Exception as e:
            print(f"Failed to export to PDF: {e}")

if __name__ == "__main__":
    # Sample donation data
    donations_data = [
        {"Donor": "John Doe", "Amount": 100, "Date": "2023-01-01"},
        {"Donor": "Jane Smith", "Amount": 200, "Date": "2023-01-02"},
        {"Donor": "Alice Johnson", "Amount": 150, "Date": "2023-01-03"},
    ]

    # Create an instance of the report generator
    report_generator = DonationReportGenerator(donations_data)
    # Generate the reports
    report_generator.generate_report()
```
