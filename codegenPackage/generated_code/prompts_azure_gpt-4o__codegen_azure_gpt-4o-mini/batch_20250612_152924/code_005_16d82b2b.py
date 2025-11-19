"""
Generated Code Metadata:
========================
Original URL: https://appdevistorias.com.br
Prompt: Write code to customize inspection report templates, including logo placement, font changes, and spacing adjustments, similar to the laudo personalization options in the BeSoft App Vistoria.
Generated: DETERMINISTIC_16d82b2b706c13dd
Batch ID: 20250612_152924
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

class InspectionReport:
    def __init__(self, title, logo_path, font_family='Arial', font_size=12, spacing=10):
        """
        Initializes the InspectionReport with the given parameters.

        :param title: Title of the inspection report
        :param logo_path: Path to the logo image
        :param font_family: Font family for the report text
        :param font_size: Font size for the report text
        :param spacing: Spacing between lines in the report
        """
        self.title = title
        self.logo_path = logo_path
        self.font_family = font_family
        self.font_size = font_size
        self.spacing = spacing
        self.pdf = FPDF()

    def add_logo(self):
        """
        Adds the logo to the PDF if the logo path is valid.
        """
        if os.path.exists(self.logo_path):
            self.pdf.image(self.logo_path, x=10, y=8, w=33)
        else:
            raise FileNotFoundError(f"Logo file not found: {self.logo_path}")

    def create_report(self, content):
        """
        Creates the inspection report PDF with the specified content.

        :param content: List of strings to be included in the report
        """
        self.pdf.add_page()
        self.pdf.set_font(self.font_family, size=self.font_size)

        # Add title
        self.pdf.cell(200, 10, self.title, ln=True, align='C')

        # Add logo
        self.add_logo()

        # Add content with specified spacing
        for line in content:
            self.pdf.cell(0, self.spacing, line, ln=True)

    def save_report(self, output_path):
        """
        Saves the generated PDF report to the specified output path.

        :param output_path: Path where the PDF report will be saved
        """
        try:
            self.pdf.output(output_path)
            print(f"Report saved successfully to {output_path}")
        except Exception as e:
            print(f"An error occurred while saving the report: {e}")

# Example usage
if __name__ == "__main__":
    report_title = "Inspection Report"
    logo_file_path = "path/to/logo.png"  # Update with the actual logo path
    report_content = [
        "Inspection Date: 2023-10-01",
        "Inspector: John Doe",
        "Location: 123 Main St.",
        "Findings: All systems operational."
    ]
    
    # Create an instance of InspectionReport
    inspection_report = InspectionReport(title=report_title, logo_path=logo_file_path)

    # Create the report with content
    inspection_report.create_report(content=report_content)

    # Save the report to a file
    inspection_report.save_report(output_path="inspection_report.pdf")
```
