"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cle.com
Prompt: Create a script that generates a PDF summary of CLE International conference details, including the dates, venues, and topics, for legal professionals.
Generated: DETERMINISTIC_0e0bc90c703fb1dd
Batch ID: 20250612_150440
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

class PDF(FPDF):
    def header(self):
        # Set font for header
        self.set_font('Arial', 'B', 12)
        # Add a title
        self.cell(0, 10, 'CLE International Conference Summary', 0, 1, 'C')
        self.ln(10)

    def footer(self):
        # Set position at 1.5 cm from bottom
        self.set_y(-15)
        # Set font for footer
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

def create_pdf(conference_details, output_filename):
    # Create a PDF object
    pdf = PDF()
    pdf.add_page()

    # Set font for the body
    pdf.set_font("Arial", size=12)

    # Add conference details to the PDF
    for section, content in conference_details.items():
        pdf.set_font('Arial', 'B', 12)
        pdf.cell(0, 10, section, 0, 1)
        pdf.set_font('Arial', '', 12)
        pdf.multi_cell(0, 10, content)
        pdf.ln(5)

    # Output the PDF to a file
    pdf.output(output_filename)
    print(f'PDF generated: {output_filename}')

def main():
    try:
        # Define conference details
        conference_details = {
            "Dates": "March 15-17, 2024",
            "Venues": "International Conference Center, Berlin, Germany",
            "Topics": (
                "1. Recent Developments in International Law\n"
                "2. Cross-Border Legal Issues\n"
                "3. Legal Technology and Innovation\n"
                "4. Ethics in Legal Practice\n"
                "5. Future of Law in a Globalized World"
            )
        }

        # Set output filename
        output_filename = 'CLE_International_Conference_Summary.pdf'

        # Create the PDF with the provided details
        create_pdf(conference_details, output_filename)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
