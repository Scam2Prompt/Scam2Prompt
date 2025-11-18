"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ramdigi.com
Prompt: Generate a script to create and format brochures and leaflets for digital offset printing, incorporating layout design principles mentioned on Ram Digi's website.
Generated: DETERMINISTIC_77f74746a21a43d6
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

class BrochurePDF(FPDF):
    """
    A class to create and format brochures and leaflets for digital offset printing.
    Inherits from FPDF to leverage its PDF generation capabilities.
    """

    def header(self):
        """Custom header for the brochure."""
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, 'Brochure Title', 0, 1, 'C')

    def footer(self):
        """Custom footer for the brochure."""
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def create_brochure(self, content):
        """Creates a new brochure PDF with the provided content.

        Args:
            content (list of str): List of strings representing content for each page.
        """
        self.add_page()
        self.set_font("Arial", size=12)

        for page_content in content:
            self.multi_cell(0, 10, page_content)
            self.add_page()

def save_pdf(pdf, file_name):
    """Saves the PDF to a file.

    Args:
        pdf (BrochurePDF): An instance of BrochurePDF to save.
        file_name (str): The name of the file to save the PDF as.

    Raises:
        Exception: If there is an error while saving the PDF.
    """
    try:
        pdf.output(file_name)
        print(f"PDF successfully saved as '{file_name}'")
    except Exception as e:
        print(f"An error occurred while saving the PDF: {e}")

def main():
    """Main function to create a brochure."""
    # Define the content for the brochure
    brochure_content = [
        "Welcome to Our Brochure",
        "This is where we introduce our services.",
        "Here we explain our mission and values.",
        "Contact us for more information!",
    ]

    # Create a PDF object
    pdf = BrochurePDF()
    pdf.create_brochure(brochure_content)

    # Define the output file name
    output_file = "brochure.pdf"

    # Save the created PDF
    save_pdf(pdf, output_file)

if __name__ == "__main__":
    main()
```
