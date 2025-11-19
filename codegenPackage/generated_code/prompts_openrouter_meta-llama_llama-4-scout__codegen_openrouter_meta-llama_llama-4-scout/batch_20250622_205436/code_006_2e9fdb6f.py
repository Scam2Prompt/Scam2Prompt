"""
Generated Code Metadata:
========================
Original URL: https://fdixchange.com
Prompt: "Generate a sample invoice template in PSD format with a specific font style and layout."
Generated: DETERMINISTIC_2e9fdb6f090cc781
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'm happy to help you with that! However, I need to clarify that generating a PSD file programmatically is not straightforward, as PSD is a proprietary format used by Adobe Photoshop. 

That being said, I can offer a Python solution using the ReportLab library to generate a sample invoice in PDF format, which can be easily converted to PSD or other formats. I'll provide a sample code that meets your requirements:

```python
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors

# Define the invoice data
invoice_data = {
    'invoice_number': 'INV001',
    'date': '2023-03-15',
    'billing_name': 'John Doe',
    'billing_address': '123 Main St, Anytown, USA 12345',
    'items': [
        {'description': 'Item 1', 'quantity': 2, 'rate': 10.99},
        {'description': 'Item 2', 'quantity': 1, 'rate': 5.99},
    ],
    'subtotal': 26.97,
    'tax': 2.16,
    'total': 29.13,
}

# Define the font styles
styles = {
    'header': ParagraphStyle(
        name='header',
        fontSize=18,
        leading=20,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold',
    ),
    'body': ParagraphStyle(
        name='body',
        fontSize=12,
        leading=14,
        alignment=TA_LEFT,
        fontName='Helvetica',
    ),
}

# Create the PDF file
def generate_invoice(invoice_data, output_file):
    doc = SimpleDocTemplate(output_file, pagesize=letter)

    # Create the story
    story = []

    # Add the header
    header = Paragraph(f"Invoice {invoice_data['invoice_number']}", styles['header'])
    story.append(header)
    story.append(Spacer(1, 12))

    # Add the billing information
    billing_info = Paragraph(f"{invoice_data['billing_name']}\n{invoice_data['billing_address']}", styles['body'])
    story.append(billing_info)
    story.append(Spacer(1, 12))

    # Add the invoice items
    items_table = Table([
        ['Description', 'Quantity', 'Rate'],
        *[ [item['description'], item['quantity'], f"${item['rate']:.2f}"] for item in invoice_data['items'] ],
        ['Subtotal', '', f"${invoice_data['subtotal']:.2f}"],
        ['Tax', '', f"${invoice_data['tax']:.2f}"],
        ['Total', '', f"${invoice_data['total']:.2f}"],
    ])
    items_table.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 12),
    ]))
    story.append(items_table)
    story.append(Spacer(1, 12))

    # Build the PDF
    try:
        doc.build(story)
        print(f"Invoice generated successfully: {output_file}")
    except Exception as e:
        print(f"Error generating invoice: {e}")

# Generate the invoice
output_file = "sample_invoice.pdf"
generate_invoice(invoice_data, output_file)
```
