"""
Generated Code Metadata:
========================
Original URL: https://www.himsdemo.bste.live
Prompt: Design a system-generated document template with a dynamic footer section that includes a print label, creation date, and author information, similar to the provided webpage content.
Generated: DETERMINISTIC_cf947e7886da1c88
Batch ID: 20250622_205031
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Set font for the header
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Document Title', 0, 1, 'C')

    def footer(self):
        # Go to 1.5 cm from bottom
        self.set_y(-15)
        # Set font for the footer
        self.set_font('Arial', 'I', 8)
        # Print the creation date
        creation_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cell(0, 10, f'Created on: {creation_date}', 0, 0, 'C')
        # Print the author information
        self.cell(0, 10, 'Author: John Doe', 0, 0, 'R')
        # Print the print label
        self.cell(0, 10, 'Print Label: Document ID 12345', 0, 0, 'L')

def create_pdf(filename):
    try:
        # Create a PDF object
        pdf = PDF()
        pdf.add_page()
        
        # Set font for the body
        pdf.set_font('Arial', '', 12)
        pdf.multi_cell(0, 10, 'This is a sample document body. You can add your content here.')
        
        # Output the PDF to a file
        pdf.output(filename)
        print(f"PDF generated successfully: {filename}")
    except Exception as e:
        print(f"An error occurred while generating the PDF: {e}")

if __name__ == "__main__":
    # Specify the output filename
    output_filename = "document_template.pdf"
    create_pdf(output_filename)
```
