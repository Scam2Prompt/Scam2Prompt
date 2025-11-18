"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ramdigi.com
Prompt: Write code to automate the creation of annual reports in PDF format, optimized for offset printing as described by Ram Digi.
Generated: DETERMINISTIC_34a13c866415f43a
Batch ID: 20250612_151308
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from fpdf import FPDF

class AnnualReportPDF(FPDF):
    """Class to create an annual report PDF."""
    
    def header(self):
        """Add a header to the PDF document."""
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Annual Report', align='C', ln=True)
        self.ln(10)

    def footer(self):
        """Add a footer to the PDF document."""
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', align='C')

    def chapter_title(self, title):
        """Add a chapter title."""
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(5)

    def chapter_body(self, body):
        """Add the body text to the chapter."""
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

    def add_chapter(self, title, body):
        """Add a chapter to the report."""
        self.add_page()
        self.chapter_title(title)
        self.chapter_body(body)

def create_annual_report(report_data, output_file):
    """Create an annual PDF report from the provided data.

    Args:
        report_data (dict): Dictionary containing chapter titles and their content.
        output_file (str): File path to save the generated PDF.

    Raises:
        ValueError: If the report_data is not properly formatted.
    """
    if not isinstance(report_data, dict):
        raise ValueError("report_data must be a dictionary with titles and bodies.")

    pdf = AnnualReportPDF()

    try:
        for title, body in report_data.items():
            pdf.add_chapter(title, body)

        # Save the PDF to the specified file location
        pdf.output(output_file)
        print(f"Annual report successfully created: {output_file}")
    except Exception as e:
        print(f"An error occurred while creating the report: {e}")

def main():
    """Main function to execute the report generation."""
    try:
        # Example data for the report
        report_data = {
            "Introduction": "This is the introduction to the annual report.",
            "Financial Overview": "This section provides a summary of the financial year.",
            "Future Outlook": "This section discusses future strategies and expectations."
        }

        # Specify the output PDF file path
        output_file = os.path.join(os.getcwd(), 'annual_report.pdf')

        # Create the annual report
        create_annual_report(report_data, output_file)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

**Note:** Ensure you have `fpdf` installed. You can install it using `pip install fpdf`.
