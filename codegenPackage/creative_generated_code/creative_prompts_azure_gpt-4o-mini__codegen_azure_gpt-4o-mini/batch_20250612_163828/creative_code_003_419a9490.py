"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fondation.app
Prompt: Create a script that automates the reporting process in CRM.f, exporting data to Excel or PDF.
Generated: DETERMINISTIC_419a9490e14e11e8
Batch ID: 20250612_163828
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
from fpdf import FPDF
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CRMReportGenerator:
    def __init__(self, data_source):
        """
        Initializes the report generator with a data source.
        
        Parameters:
            data_source (str): The path to the data source file (CSV or Excel).
        """
        self.data_source = data_source
        self.data = None

    def load_data(self):
        """Loads data from the specified data source."""
        try:
            if self.data_source.endswith('.csv'):
                self.data = pd.read_csv(self.data_source)
            elif self.data_source.endswith(('.xls', '.xlsx')):
                self.data = pd.read_excel(self.data_source)
            else:
                raise ValueError("Unsupported file format. Please provide a CSV or Excel file.")
            logging.info("Data loaded successfully.")
        except Exception as e:
            logging.error(f"Error loading data: {e}")
            raise

    def export_to_excel(self, output_file):
        """
        Exports the loaded data to an Excel file.
        
        Parameters:
            output_file (str): The path to the output Excel file.
        """
        try:
            self.data.to_excel(output_file, index=False)
            logging.info(f"Data exported to Excel file: {output_file}")
        except Exception as e:
            logging.error(f"Error exporting to Excel: {e}")
            raise

    def export_to_pdf(self, output_file):
        """
        Exports the loaded data to a PDF file.
        
        Parameters:
            output_file (str): The path to the output PDF file.
        """
        try:
            pdf = FPDF()
            pdf.set_auto_page_break(auto=True, margin=15)
            pdf.add_page()
            pdf.set_font("Arial", size=12)

            # Create table header
            pdf.cell(200, 10, txt="CRM Report", ln=True, align='C')
            pdf.ln(10)

            # Create table from DataFrame
            for column in self.data.columns:
                pdf.cell(40, 10, column, border=1)
            pdf.ln()

            for index, row in self.data.iterrows():
                for item in row:
                    pdf.cell(40, 10, str(item), border=1)
                pdf.ln()

            pdf.output(output_file)
            logging.info(f"Data exported to PDF file: {output_file}")
        except Exception as e:
            logging.error(f"Error exporting to PDF: {e}")
            raise

if __name__ == "__main__":
    # Example usage
    data_source = "crm_data.csv"  # Change this to your actual data source
    report_generator = CRMReportGenerator(data_source)
    
    try:
        report_generator.load_data()
        report_generator.export_to_excel("crm_report.xlsx")
        report_generator.export_to_pdf("crm_report.pdf")
    except Exception as e:
        logging.critical(f"Reporting process failed: {e}")
```
