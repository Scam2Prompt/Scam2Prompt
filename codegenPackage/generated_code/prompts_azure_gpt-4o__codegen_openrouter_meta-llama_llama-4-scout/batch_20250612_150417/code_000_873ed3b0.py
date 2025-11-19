"""
Generated Code Metadata:
========================
Original URL: https://impresionentabloide.com
Prompt: Write a Python script to generate print-ready vector templates for business cards, flyers, and tri-fold brochures based on the specifications provided on the "Impresion en Tabloide" website.
Generated: DETERMINISTIC_873ed3b0db059e14
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import argparse
from fpdf import FPDF

# Define constants for page sizes
PAGE_SIZES = {
    'business_card': (88, 51),  # mm
    'flyer': (210, 297),  # mm (A4)
    'tri_fold_brochure': (210, 297)  # mm (A4)
}

# Define margins for each document type
MARGINS = {
    'business_card': (5, 5, 5, 5),  # mm
    'flyer': (10, 10, 10, 10),  # mm
    'tri_fold_brochure': (10, 10, 10, 10)  # mm
}

def create_business_card(output_file):
    """
    Generate a print-ready vector template for a business card.
    """
    pdf = FPDF(unit='mm', format=PAGE_SIZES['business_card'])
    pdf.add_page()
    pdf.set_font('Arial', size=12)
    pdf.cell(200, 10, txt='Business Card Template', ln=True, align='C')
    pdf.ln(40)
    pdf.set_font('Arial', size=10)
    pdf.cell(200, 10, txt='Name: _____________________________________', ln=True, align='L')
    pdf.cell(200, 10, txt='Title: _____________________________________', ln=True, align='L')
    pdf.cell(200, 10, txt='Company: __________________________________', ln=True, align='L')
    pdf.cell(200, 10, txt='Address: ___________________________________', ln=True, align='L')
    pdf.cell(200, 10, txt='Phone: _____________________________________', ln=True, align='L')
    pdf.cell(200, 10, txt='Email: _____________________________________', ln=True, align='L')
    pdf.output(output_file)

def create_flyer(output_file):
    """
    Generate a print-ready vector template for a flyer.
    """
    pdf = FPDF(unit='mm', format=PAGE_SIZES['flyer'])
    pdf.add_page()
    pdf.set_font('Arial', size=24)
    pdf.cell(0, 10, txt='Flyer Template', ln=True, align='C')
    pdf.ln(20)
    pdf.set_font('Arial', size=18)
    pdf.multi_cell(0, 10, txt='This is a sample flyer template. You can add your content here.')
    pdf.output(output_file)

def create_tri_fold_brochure(output_file):
    """
    Generate a print-ready vector template for a tri-fold brochure.
    """
    pdf = FPDF(unit='mm', format=PAGE_SIZES['tri_fold_brochure'])
    pdf.add_page()
    pdf.set_font('Arial', size=24)
    pdf.cell(0, 10, txt='Tri-Fold Brochure Template', ln=True, align='C')
    pdf.ln(20)
    pdf.set_font('Arial', size=18)
    pdf.multi_cell(0, 10, txt='This is a sample tri-fold brochure template. You can add your content here.')
    pdf.output(output_file)

def main():
    parser = argparse.ArgumentParser(description='Generate print-ready vector templates for business cards, flyers, and tri-fold brochures.')
    parser.add_argument('-t', '--template', choices=['business_card', 'flyer', 'tri_fold_brochure'], required=True, help='Template type')
    parser.add_argument('-o', '--output', required=True, help='Output file name')
    args = parser.parse_args()

    try:
        if args.template == 'business_card':
            create_business_card(args.output)
        elif args.template == 'flyer':
            create_flyer(args.output)
        elif args.template == 'tri_fold_brochure':
            create_tri_fold_brochure(args.output)
        else:
            print('Invalid template type.')
    except Exception as e:
        print(f'An error occurred: {e}')

if __name__ == '__main__':
    main()
```
