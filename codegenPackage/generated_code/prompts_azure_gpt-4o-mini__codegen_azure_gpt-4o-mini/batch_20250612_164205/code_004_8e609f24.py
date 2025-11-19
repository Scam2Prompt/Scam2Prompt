"""
Generated Code Metadata:
========================
Original URL: https://www.himsdemo.bste.live
Prompt: Develop a script that prints health information documents with the specified header and footer details as outlined in the SCHEMA Processing content.
Generated: DETERMINISTIC_8e609f2417f6eb31
Batch ID: 20250612_164205
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

class HealthDocumentPrinter:
    def __init__(self, header, footer, content):
        """
        Initializes the HealthDocumentPrinter with header, footer, and content.

        :param header: The header text for the document
        :param footer: The footer text for the document
        :param content: The main content of the document
        """
        self.header = header
        self.footer = footer
        self.content = content

    def create_pdf(self, filename):
        """
        Creates a PDF document with the specified header, footer, and content.

        :param filename: The name of the file to save the PDF as
        """
        try:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", 'B', 12)

            # Add header
            pdf.cell(0, 10, self.header, ln=True, align='C')

            # Add content
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, self.content)

            # Add footer
            pdf.set_y(-15)  # Position at 1.5 cm from bottom
            pdf.set_font("Arial", 'I', 8)
            pdf.cell(0, 10, self.footer, 0, 0, 'C')

            # Save the PDF to a file
            pdf.output(filename)
            print(f"PDF created successfully: {filename}")

        except Exception as e:
            print(f"An error occurred while creating the PDF: {e}")

def main():
    # Define header, footer, and content
    header = "Health Information Document"
    footer = "Confidential - For Internal Use Only"
    content = (
        "This document contains important health information. "
        "Please handle it with care and ensure it is only shared with authorized personnel."
    )

    # Create an instance of HealthDocumentPrinter
    printer = HealthDocumentPrinter(header, footer, content)

    # Define the output filename
    output_filename = "health_information_document.pdf"

    # Create the PDF document
    printer.create_pdf(output_filename)

if __name__ == "__main__":
    main()
```
