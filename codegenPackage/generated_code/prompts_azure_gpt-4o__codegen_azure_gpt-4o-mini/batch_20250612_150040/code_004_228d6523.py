"""
Generated Code Metadata:
========================
Original URL: https://fantom.de
Prompt: Create a Python script to automate the process of designing print media layouts, referencing Fantom Internet Dienst's print media services.
Generated: DETERMINISTIC_228d652300ed9762
Batch ID: 20250612_150040
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

class PrintMediaLayout:
    """
    A class to automate the creation of print media layouts using the FPDF library.
    """

    def __init__(self, title, subtitle, content, output_file):
        """
        Initializes the PrintMediaLayout with title, subtitle, content, and output file name.

        :param title: Title of the print media
        :param subtitle: Subtitle of the print media
        :param content: Main content of the print media
        :param output_file: Name of the output PDF file
        """
        self.title = title
        self.subtitle = subtitle
        self.content = content
        self.output_file = output_file

    def create_pdf(self):
        """
        Creates a PDF file with the specified layout and content.
        """
        try:
            # Create a PDF object
            pdf = FPDF()
            pdf.add_page()

            # Set title font and size
            pdf.set_font("Arial", 'B', 16)
            pdf.cell(0, 10, self.title, ln=True, align='C')

            # Set subtitle font and size
            pdf.set_font("Arial", 'I', 12)
            pdf.cell(0, 10, self.subtitle, ln=True, align='C')

            # Add a line break
            pdf.ln(10)

            # Set content font and size
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, self.content)

            # Output the PDF to a file
            pdf.output(self.output_file)
            print(f"PDF created successfully: {self.output_file}")

        except Exception as e:
            print(f"An error occurred while creating the PDF: {e}")

def main():
    """
    Main function to execute the print media layout creation.
    """
    # Define the content for the print media
    title = "Fantom Internet Dienst Print Media"
    subtitle = "Your Trusted Partner in Print Solutions"
    content = (
        "At Fantom Internet Dienst, we offer a wide range of print media services "
        "to help you reach your audience effectively. Our services include brochures, "
        "flyers, business cards, and more. Contact us today to learn more!"
    )
    output_file = "print_media_layout.pdf"

    # Create an instance of PrintMediaLayout
    layout = PrintMediaLayout(title, subtitle, content, output_file)

    # Create the PDF
    layout.create_pdf()

if __name__ == "__main__":
    main()
```
