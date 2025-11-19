"""
Generated Code Metadata:
========================
Original URL: https://ramdigi.com
Prompt: Write Python code to generate a print-ready PDF for wedding invitation cards, incorporating layout design principles similar to those described by Ram Digi's digital offset printing services.
Generated: DETERMINISTIC_5c3ba5c1e27a11ed
Batch ID: 20250612_151308
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

class WeddingInvitationPDF(FPDF):
    def header(self):
        # Set font for the header
        self.set_font('Arial', 'B', 12)
        # Title of the invitation
        self.cell(0, 10, 'You Are Invited!', 0, 1, 'C')

    def footer(self):
        # Set position for the footer
        self.set_y(-15)
        # Set font for the footer
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

def create_wedding_invitation(file_name, couple_names, date, time, venue, rsvp):
    """
    Create a wedding invitation PDF.

    :param file_name: Name of the output PDF file
    :param couple_names: Names of the couple
    :param date: Date of the wedding
    :param time: Time of the wedding
    :param venue: Venue of the wedding
    :param rsvp: RSVP details
    """
    try:
        # Create a PDF object
        pdf = WeddingInvitationPDF()
        pdf.add_page()

        # Set font for the body
        pdf.set_font('Arial', '', 12)

        # Add invitation details
        pdf.cell(0, 10, f'Join us to celebrate the wedding of', 0, 1, 'C')
        pdf.cell(0, 10, couple_names, 0, 1, 'C')
        pdf.cell(0, 10, f'On {date} at {time}', 0, 1, 'C')
        pdf.cell(0, 10, f'Location: {venue}', 0, 1, 'C')
        pdf.cell(0, 10, f'RSVP: {rsvp}', 0, 1, 'C')

        # Save the PDF to a file
        pdf.output(file_name)
        print(f'Wedding invitation PDF created successfully: {file_name}')

    except Exception as e:
        print(f'An error occurred while creating the PDF: {e}')

if __name__ == "__main__":
    # Define invitation details
    couple_names = "John Doe & Jane Smith"
    date = "Saturday, June 25, 2023"
    time = "4:00 PM"
    venue = "The Grand Ballroom, 123 Wedding St, City"
    rsvp = "Please RSVP by June 1, 2023 to (123) 456-7890"

    # Create the PDF file
    create_wedding_invitation("wedding_invitation.pdf", couple_names, date, time, venue, rsvp)
```

Make sure to install the `fpdf` library if you haven't already, using the following command:
```bash
pip install fpdf
```
