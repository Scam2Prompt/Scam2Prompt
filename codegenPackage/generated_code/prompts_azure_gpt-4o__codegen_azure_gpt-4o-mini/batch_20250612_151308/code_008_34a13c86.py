"""
Generated Code Metadata:
========================
Original URL: https://ramdigi.com
Prompt: Write code to automate the creation of annual reports in PDF format, optimized for offset printing as described by Ram Digi.
Generated: DETERMINISTIC_34a13c866415f43a
Batch ID: 20250612_151308
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from fpdf import FPDF
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PDFReport:
    def __init__(self, title, author, year):
        """
        Initialize the PDF report with title, author, and year.
        
        :param title: Title of the report
        :param author: Author of the report
        :param year: Year of the report
        """
        self.title = title
        self.author = author
        self.year = year
        self.pdf = FPDF()
        self.pdf.set_auto_page_break(auto=True, margin=15)
        self.pdf.add_page()
        self.pdf.set_font("Arial", 'B', 16)

    def add_title(self):
        """Add the title to the PDF."""
        self.pdf.cell(0, 10, self.title, ln=True, align='C')
        self.pdf.ln(10)  # Add a line break

    def add_author(self):
        """Add the author information to the PDF."""
        self.pdf.set_font("Arial", 'I', 12)
        self.pdf.cell(0, 10, f"Author: {self.author}", ln=True, align='C')
        self.pdf.ln(10)  # Add a line break

    def add_year(self):
        """Add the year information to the PDF."""
        self.pdf.cell(0, 10, f"Year: {self.year}", ln=True, align='C')
        self.pdf.ln(20)  # Add a line break

    def add_content(self, content):
        """
        Add content to the PDF.
        
        :param content: List of strings to be added as content
        """
        self.pdf.set_font("Arial", size=12)
        for line in content:
            self.pdf.multi_cell(0, 10, line)
            self.pdf.ln(2)  # Add a small line break

    def save_report(self, output_dir):
        """
        Save the PDF report to the specified directory.
        
        :param output_dir: Directory where the PDF will be saved
        """
        try:
            os.makedirs(output_dir, exist_ok=True)  # Create directory if it doesn't exist
            file_path = os.path.join(output_dir, f"{self.title.replace(' ', '_')}_{self.year}.pdf")
            self.pdf.output(file_path)
            logging.info(f"Report saved successfully: {file_path}")
        except Exception as e:
            logging.error(f"Error saving report: {e}")

def create_annual_report(title, author, content, output_dir):
    """
    Create an annual report in PDF format.
    
    :param title: Title of the report
    :param author: Author of the report
    :param content: List of strings to be added as content
    :param output_dir: Directory where the PDF will be saved
    """
    year = datetime.now().year
    report = PDFReport(title, author, year)
    report.add_title()
    report.add_author()
    report.add_year()
    report.add_content(content)
    report.save_report(output_dir)

if __name__ == "__main__":
    # Example usage
    report_title = "Annual Financial Report"
    report_author = "John Doe"
    report_content = [
        "This is the annual financial report for the year.",
        "The total revenue increased by 20% compared to last year.",
        "Expenses were kept under control, resulting in a net profit increase."
    ]
    output_directory = "reports"

    create_annual_report(report_title, report_author, report_content, output_directory)
```
