"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.lords.marketing
Prompt: Create a Python script that automates the design process for marketing materials in the pub sector, reflecting the strategic approach of Lords Marketing.
Generated: DETERMINISTIC_298b7a70cd5f7ebf
Batch ID: 20250612_162051
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
from datetime import datetime

class MarketingMaterial:
    """
    A class to represent marketing materials for the pub sector.
    """

    def __init__(self, title, content, date=None):
        """
        Initializes the marketing material with a title, content, and optional date.

        :param title: The title of the marketing material.
        :param content: The main content of the marketing material.
        :param date: The date of creation for the marketing material. Defaults to today's date.
        """
        self.title = title
        self.content = content
        self.date = date if date else datetime.today().strftime('%Y-%m-%d')

    def generate_pdf(self, filename):
        """
        Generates a PDF file from the marketing material.

        :param filename: The name of the output PDF file.
        :raises FileNotFoundError: If there is an issue creating the PDF file.
        """
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()

        # Set title
        pdf.set_font('Arial', 'B', 16)
        pdf.cell(0, 10, self.title, ln=True, align='C')

        # Date
        pdf.set_font('Arial', 'I', 12)
        pdf.cell(0, 10, f'Date: {self.date}', ln=True, align='C')

        pdf.ln(10)  # Add a line break

        # Set content
        pdf.set_font('Arial', '', 12)
        pdf.multi_cell(0, 10, self.content)

        try:
            pdf.output(filename)
            print(f"PDF generated successfully: {filename}")
        except Exception as e:
            raise FileNotFoundError(f"Error generating PDF: {e}")

def main():
    """
    Main function to create a marketing material and generate a PDF.
    """
    title = "Welcome to Our Pub"
    content = (
        "Join us for a delightful experience at our pub. "
        "Enjoy a wide range of local ales, delicious meals, and live music every weekend! "
        "Visit us for memorable moments with friends and family."
    )
    
    # Create the marketing material instance
    material = MarketingMaterial(title, content)

    # Define output PDF file name
    output_directory = "marketing_materials"
    os.makedirs(output_directory, exist_ok=True)  # Create directory if it doesn't exist
    pdf_filename = os.path.join(output_directory, "pub_marketing_material.pdf")

    # Generate the PDF
    material.generate_pdf(pdf_filename)

if __name__ == "__main__":
    main()
```
