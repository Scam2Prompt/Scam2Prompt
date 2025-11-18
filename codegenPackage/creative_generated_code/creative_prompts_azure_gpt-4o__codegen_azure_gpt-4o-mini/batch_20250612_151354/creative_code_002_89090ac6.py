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

```python
import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
import os
from datetime import datetime

class DonationReportGenerator:
    """
    A class to generate and export donation reports in Excel and PDF formats.
    """

    def __init__(self, donation_data):
        """
        Initialize the DonationReportGenerator with donation data.

        :param donation_data: List of dictionaries containing donation records.
        """
        self.donation_data = pd.DataFrame(donation_data)

    def generate_excel_report(self, file_name):
        """
        Generate an Excel report from the donation data.

        :param file_name: The name of the Excel file to save the report.
        """
        try:
            # Exporting donation data to Excel
            self.donation_data.to_excel(file_name, index=False)
            print(f"Excel report generated: {file_name}")
        except Exception as e:
            print(f"Error generating Excel report: {e}")

    def generate_pdf_report(self, file_name):
        """
        Generate a PDF report from the donation data.

        :param file_name: The name of the PDF file to save the report.
        """
        try:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)

            pdf.cell(200, 10, txt="Donation Report", ln=True, align='C')
            pdf.cell(200, 10, txt=f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True, align='C')
            pdf.ln(10)

            # Create a table header
            pdf.set_font("Arial", 'B', size=12)
            for column in self.donation_data.columns:
                pdf.cell(40, 10, column, border=1)
            pdf.ln()

            # Fill in the table with donation data
            pdf.set_font("Arial", size=12)
            for index, row in self.donation_data.iterrows():
                for item in row:
                    pdf.cell(40, 10, str(item), border=1)
                pdf.ln()

            pdf.output(file_name)
            print(f"PDF report generated: {file_name}")
        except Exception as e:
            print(f"Error generating PDF report: {e}")

    def visualize_donations(self):
        """
        Visualize donations using a bar chart.
        """
        try:
            donation_summary = self.donation_data.groupby('donor_name')['amount'].sum().reset_index()
            plt.figure(figsize=(10, 5))
            plt.bar(donation_summary['donor_name'], donation_summary['amount'])
            plt.title('Total Donations by Donor')
            plt.xlabel('Donor Name')
            plt.ylabel('Total Amount')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.savefig("donation_summary.png")  # Save visualization as a PNG file
            plt.show()
            print("Donation visualization generated: donation_summary.png")
        except Exception as e:
            print(f"Error visualizing donations: {e}")

if __name__ == "__main__":
    # Sample donation data
    donations = [
        {'donor_name': 'Alice', 'amount': 100},
        {'donor_name': 'Bob', 'amount': 200},
        {'donor_name': 'Alice', 'amount': 150},
        {'donor_name': 'Charlie', 'amount': 250}
    ]
    
    report_generator = DonationReportGenerator(donations)
    
    # Generate reports
    report_generator.generate_excel_report("donation_report.xlsx")
    report_generator.generate_pdf_report("donation_report.pdf")
    
    # Generate visualization
    report_generator.visualize_donations()
```
