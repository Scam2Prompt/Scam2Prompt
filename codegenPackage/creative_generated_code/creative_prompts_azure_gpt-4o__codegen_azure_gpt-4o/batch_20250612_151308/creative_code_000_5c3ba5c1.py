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
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.colors import black, lightpink, white
from reportlab.graphics.shapes import Rect

def create_wedding_invitation_card(output_filename):
    """
    Generates a print-ready PDF for wedding invitation cards.
    
    Args:
        output_filename (str): The name of the output PDF file.
    """
    try:
        # Define page size and margins
        page_width, page_height = A4
        margin = 0.5 * inch
        
        # Create canvas for the PDF
        pdf_canvas = canvas.Canvas(output_filename, pagesize=A4)
        
        # Set background color (light pink)
        pdf_canvas.setFillColor(lightpink)
        pdf_canvas.rect(0, 0, page_width, page_height, stroke=0, fill=1)

        # Draw header banner
        header_height = 1.5 * inch
        pdf_canvas.setFillColor(black)
        pdf_canvas.rect(0, page_height - header_height, page_width, header_height, stroke=0, fill=1)
        
        # Add header text (e.g., "Wedding Invitation")
        pdf_canvas.setFont("Helvetica-Bold", 24)
        pdf_canvas.setFillColor(white)
        pdf_canvas.drawCentredString(page_width / 2, page_height - header_height / 2, "Wedding Invitation")
        
        # Draw footer banner
        footer_height = 1 * inch
        pdf_canvas.setFillColor(black)
        pdf_canvas.rect(0, 0, page_width, footer_height, stroke=0, fill=1)
        
        # Add footer text (e.g., "Save the Date")
        pdf_canvas.setFont("Helvetica-Bold", 18)
        pdf_canvas.setFillColor(white)
        pdf_canvas.drawCentredString(page_width / 2, footer_height / 2, "Save the Date")

        # Add main invitation text
        pdf_canvas.setFont("Times-Roman", 16)
        pdf_canvas.setFillColor(black)
        invitation_text = (
            "Together with their families,\n\n"
            "Emma Johnson & Liam Smith\n\n"
            "Request the honor of your presence\n"
            "at their wedding celebration\n\n"
            "Saturday, June 24th, 2023\n"
            "at 4:00 pm\n\n"
            "The Grand Venue\n"
            "123 Celebration Street\n"
            "Hometown, USA"
        )
        text_x = margin
        text_y = page_height - header_height - margin
        pdf_canvas.drawText(
            pdf_canvas.beginText(
                text_x, text_y
            ).setTextOrigin(margin, page_height - header_height - margin).setFont("Times-Roman", 14)
