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
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

def generate_wedding_invitation(output_path):
    """
    Generate a print-ready PDF wedding invitation card.
    
    Args:
        output_path (str): Path to save the generated PDF.
    """
    try:
        # Register custom fonts
        font_dir = os.path.join(os.path.dirname(__file__), 'fonts')
        if not os.path.exists(font_dir):
            os.makedirs(font_dir)
        
        # Check if fonts exist, otherwise use defaults
        try:
            pdfmetrics.registerFont(TTFont('GreatVibes', 'GreatVibes-Regular.ttf'))
            pdfmetrics.registerFont(TTFont('PlayfairDisplay', 'PlayfairDisplay-Regular.ttf'))
        except:
            print("Custom fonts not found. Using default fonts.")
        
        # Create document with bleed area (0.125 inch on each side)
        doc = SimpleDocTemplate(
            output_path,
            pagesize=letter,
            leftMargin=0.125*inch,
            rightMargin=0.125*inch,
            topMargin=0.125*inch,
            bottomMargin=0.125*inch
        )
        
        # Define styles
        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(
            name='Title',
            fontName='GreatVibes',
            fontSize=48,
            leading=50,
            alignment=TA_CENTER,
            textColor=colors.HexColor('#8B4513')
        ))
        styles.add(ParagraphStyle(
            name='Subtitle',
            fontName='PlayfairDisplay',
            fontSize=18,
            leading=22,
            alignment=TA_CENTER,
            textColor=colors.HexColor('#555555')
        ))
        styles.add(ParagraphStyle(
            name='Body',
            fontName='PlayfairDisplay',
            fontSize=14,
            leading=18,
            alignment=TA_CENTER,
            textColor=colors.black
        ))
        styles.add(ParagraphStyle(
            name='Footer',
            fontName='PlayfairDisplay',
            fontSize=10,
            leading=12,
            alignment=TA_CENTER,
            textColor=colors.HexColor('#777777')
        ))
        
        # Content elements
        elements = []
        
        # Add decorative elements (replace with actual images if available)
        try:
            elements.append(Spacer(1, 0.5*inch))
            elements.append(Image('floral_divider.png', width=3*inch, height=0.5*inch))
            elements.append(Spacer(1, 0.5*inch))
        except:
            pass
        
        # Main content
        elements.append(Paragraph("The Wedding Of", styles['Subtitle']))
        elements.append(Spacer(1, 0.25*inch))
        
        elements.append(Paragraph("Sarah<br/> & <br/>Michael", styles['Title']))
        elements.append(Spacer(1, 0.5*inch))
        
        elements.append(Paragraph("Saturday, the fifteenth of June<br/>"
                                "Two thousand twenty-four<br/>"
                                "at half past four in the afternoon", styles['Body']))
        elements.append(Spacer(1, 0.5*inch))
        
        elements.append(Paragraph("The Grand Ballroom<br/>"
                                "123 Park Avenue<br/>"
                                "New York, NY", styles['Body']))
        elements.append(Spacer(1, 0.75*inch))
        
        elements.append(Paragraph("Dinner & Dancing to Follow", styles['Subtitle']))
        elements.append(Spacer(1, 0.5*inch))
        
        # RSVP information
        elements.append(Paragraph("Kindly RSVP by May 15th<br/>"
                                "Sarah: (555) 123-4567<br/>"
                                "Michael: (555) 987-6543", styles['Body']))
        elements.append(Spacer(1, 0.5*inch))
        
        # Footer
        elements.append(Paragraph("Formal Attire Requested", styles['Footer']))
        
        # Build the PDF
        doc.build(elements)
        
        print(f"Successfully generated wedding invitation at: {output_path}")
        
    except Exception as e:
        print(f"Error generating PDF: {str(e)}")
        raise

if __name__ == "__main__":
    generate_wedding_invitation("wedding_invitation.pdf")
```
