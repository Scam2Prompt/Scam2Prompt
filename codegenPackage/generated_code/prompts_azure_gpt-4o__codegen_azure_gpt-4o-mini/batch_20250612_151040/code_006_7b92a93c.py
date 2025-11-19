"""
Generated Code Metadata:
========================
Original URL: https://fodyem.com
Prompt: Write code to generate a PDF magazine for tourism programs like the "Consulter le programme 2025" feature on FODYEM, including package details and blog highlights.
Generated: DETERMINISTIC_7b92a93ce8b28600
Batch ID: 20250612_151040
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
from datetime import datetime

class PDF(FPDF):
    def header(self):
        # Set font for the header
        self.set_font('Arial', 'B', 12)
        # Title
        self.cell(0, 10, 'Tourism Programs Magazine 2025', 0, 1, 'C')

    def footer(self):
        # Go to 1.5 cm from bottom
        self.set_y(-15)
        # Set font for the footer
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, title):
        # Set font for chapter title
        self.set_font('Arial', 'B', 12)
        # Title
        self.cell(0, 10, title, 0, 1, 'L')
        # Line break
        self.ln(5)

    def chapter_body(self, body):
        # Set font for chapter body
        self.set_font('Arial', '', 12)
        # Output justified text
        self.multi_cell(0, 10, body)
        # Line break
        self.ln()

def generate_pdf(package_details, blog_highlights, output_filename):
    """
    Generate a PDF magazine for tourism programs.

    :param package_details: List of dictionaries containing package details.
    :param blog_highlights: List of strings containing blog highlights.
    :param output_filename: The filename for the generated PDF.
    """
    pdf = PDF()
    pdf.add_page()

    # Add package details
    pdf.chapter_title('Tourism Packages')
    for package in package_details:
        title = package.get('title', 'No Title')
        description = package.get('description', 'No Description')
        price = package.get('price', 'N/A')
        pdf.chapter_body(f'Title: {title}\nDescription: {description}\nPrice: {price}\n')

    # Add blog highlights
    pdf.chapter_title('Blog Highlights')
    for highlight in blog_highlights:
        pdf.chapter_body(highlight)

    # Save the PDF to a file
    try:
        pdf.output(output_filename)
        print(f'Successfully generated PDF: {output_filename}')
    except Exception as e:
        print(f'Error generating PDF: {e}')

if __name__ == "__main__":
    # Sample data for package details and blog highlights
    packages = [
        {'title': 'Beach Getaway', 'description': 'Enjoy a relaxing beach vacation.', 'price': '$499'},
        {'title': 'Mountain Adventure', 'description': 'Experience the thrill of mountain climbing.', 'price': '$799'},
    ]

    blogs = [
        'Discover the hidden gems of our beautiful country.',
        'Top 10 travel tips for a memorable vacation.',
        'How to travel sustainably and responsibly.',
    ]

    # Define output filename with current date
    output_file = f'tourism_magazine_{datetime.now().strftime("%Y%m%d")}.pdf'

    # Generate the PDF
    generate_pdf(packages, blogs, output_file)
```
