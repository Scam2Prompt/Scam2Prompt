"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ramdigi.com
Prompt: Write Python code to generate a print-ready PDF for wedding invitation cards, incorporating layout design principles similar to those described by Ram Digi's digital offset printing services.
Generated: DETERMINISTIC_5c3ba5c1e27a11ed
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

class WeddingInvitationPDF(FPDF):
    def header(self):
        """Add a header to the PDF."""
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Wedding Invitation', 0, 1, 'C')

    def footer(self):
        """Add a footer to the PDF."""
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, title):
        """Add a chapter title with specific styling."""
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, title, 0, 1, 'C')
        self.ln(10)

    def chapter_body(self, body):
        """Add the body text of the invitation."""
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln(5)

def create_wedding_invitation(pdf_file_path, couple_names, wedding_details):
    """
    Create a wedding invitation PDF file.

    :param pdf_file_path: Path where the PDF will be saved.
    :param couple_names: Names of the couple.
    :param wedding_details: Details of the wedding.
    """
    try:
        # Create a PDF object
        pdf = WeddingInvitationPDF()
        pdf.add_page()

        # Set title and body of the invitation
        pdf.chapter_title(couple_names)
        pdf.chapter_body(wedding_details)

        # Save the PDF to file
        pdf.output(pdf_file_path)

        print(f"Wedding invitation PDF created successfully: {pdf_file_path}")
    except Exception as e:
        print(f"An error occurred while creating the PDF: {str(e)}")

if __name__ == "__main__":
    # Define file path and invitation content
    output_file = "wedding_invitation.pdf"
    couple = "John & Jane"
    details = (
        "You are cordially invited to the wedding of\n"
        "John Doe and Jane Smith\n\n"
        "Date: July 20, 2024\n"
        "Time: 4:00 PM\n"
        "Venue: The Grand Hall, 123 Celebration Ave.\n"
        "Please join us for a day filled with love and joy."
    )

    # Create the wedding invitation PDF
    create_wedding_invitation(output_file, couple, details)
```

Make sure to install the `fpdf` library before running the code:

```bash
pip install fpdf
```
