"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ramdigi.com
Prompt: Suggest a library for generating print-ready PDFs for products such as calendars and magazines, inspired by the digital print solutions provided by Ram Digi.
Generated: DETERMINISTIC_0c99a2653d16c456
Batch ID: 20250612_163728
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

class PDFGenerator:
    """Class to generate print-ready PDFs for products like calendars and magazines."""
    
    def __init__(self, title: str, output_path: str):
        """
        Initializes the PDFGenerator with a title and output path.

        :param title: Title of the PDF document
        :param output_path: Path where the PDF will be saved
        """
        self.title = title
        self.output_path = output_path
        self.pdf = FPDF()
        self.pdf.set_auto_page_break(auto=True, margin=15)
        
    def add_page(self):
        """Adds a new page to the PDF."""
        self.pdf.add_page()
        self.pdf.set_font("Arial", size=12)

    def add_title(self):
        """
        Adds the title to the PDF.

        This method should be called after adding a new page.
        """
        self.pdf.set_font("Arial", 'B', size=16)
        self.pdf.cell(0, 10, self.title, ln=True, align='C')
        self.pdf.ln(10)  # Add a line break

    def add_content(self, content: str):
        """
        Adds content to the PDF.

        :param content: The text content to add to the PDF
        """
        self.pdf.set_font("Arial", size=12)
        self.pdf.multi_cell(0, 10, content)
        
    def save_pdf(self):
        """Saves the generated PDF to the specified output path."""
        try:
            # Ensure the output directory exists
            os.makedirs(os.path.dirname(self.output_path), exist_ok=True)
            self.pdf.output(self.output_path)
            print(f"PDF saved successfully: {self.output_path}")
        except Exception as e:
            print(f"Error saving PDF: {e}")

def main():
    """Main function to demonstrate PDF generation."""
    title = "Sample Calendar"
    output_path = "output/sample_calendar.pdf"
    
    pdf_generator = PDFGenerator(title, output_path)
    pdf_generator.add_page()
    pdf_generator.add_title()
    content = "January 2024\n\nSun Mon Tue Wed Thu Fri Sat\n" \
              "1   2   3   4   5   6   7\n" \
              "8   9   10  11  12  13  14\n" \
              "15  16  17  18  19  20  21\n" \
              "22  23  24  25  26  27  28\n" \
              "29  30  31"
    pdf_generator.add_content(content)
    pdf_generator.save_pdf()

if __name__ == "__main__":
    main()
```
