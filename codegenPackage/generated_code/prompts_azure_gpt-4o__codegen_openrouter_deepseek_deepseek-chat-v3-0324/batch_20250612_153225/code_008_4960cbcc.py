"""
Generated Code Metadata:
========================
Original URL: https://samional.com
Prompt: Suggest tools or frameworks for designing a corporate identity guide and catalog, as referenced on samional.com, and provide example code for generating a PDF catalog.
Generated: DETERMINISTIC_4960cbcc4df23550
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Required libraries: reportlab, PyPDF2, Pillow
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

def generate_catalog(output_path, company_data, products):
    """
    Generate a PDF catalog for corporate identity.
    
    Args:
        output_path (str): Path to save the PDF file
        company_data (dict): Company information including name, logo, colors
        products (list): List of product dictionaries with name, description, image
    """
    
    try:
        # Register custom font if needed
        font_path = os.path.join('fonts', 'Arial.ttf')
        if os.path.exists(font_path):
            pdfmetrics.registerFont(TTFont('Arial', font_path))
        
        # Create document with specified page size
        doc = SimpleDocTemplate(
            output_path,
            pagesize=letter,
            rightMargin=72,
            leftMargin=72,
            topMargin=72,
            bottomMargin=72
        )
        
        # Define styles
        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(
            name='CompanyTitle',
            fontSize=24,
            leading=28,
            textColor=colors.HexColor(company_data.get('primary_color', '#000000')),
            fontName='Helvetica-Bold'
        ))
        
        styles.add(ParagraphStyle(
            name='ProductTitle',
            fontSize=18,
            leading=22,
            textColor=colors.HexColor(company_data.get('secondary_color', '#333333')),
            fontName='Helvetica-Bold'
        ))
        
        # Build story (content)
        story = []
        
        # Cover page
        if company_data.get('logo'):
            logo = Image(company_data['logo'], width=3*inch, height=3*inch)
            logo.hAlign = 'CENTER'
            story.append(logo)
            story.append(Spacer(1, 0.5*inch))
        
        story.append(Paragraph(company_data['name'], styles['CompanyTitle']))
        story.append(Spacer(1, 0.5*inch))
        story.append(Paragraph("Product Catalog", styles['CompanyTitle']))
        story.append(PageBreak())
        
        # Table of contents
        story.append(Paragraph("Table of Contents", styles['CompanyTitle']))
        story.append(Spacer(1, 0.25*inch))
        
        for i, product in enumerate(products, 1):
            story.append(Paragraph(f"{i}. {product['name']}", styles['Normal']))
        
        story.append(PageBreak())
        
        # Product pages
        for product in products:
            story.append(Paragraph(product['name'], styles['ProductTitle']))
            story.append(Spacer(1, 0.25*inch))
            
            if product.get('image'):
                img = Image(product['image'], width=4*inch, height=4*inch)
                img.hAlign = 'CENTER'
                story.append(img)
                story.append(Spacer(1, 0.25*inch))
            
            story.append(Paragraph(product['description'], styles['Normal']))
            story.append(PageBreak())
        
        # Generate PDF
        doc.build(story)
        print(f"Catalog generated successfully at: {output_path}")
        
    except Exception as e:
        print(f"Error generating catalog: {str(e)}")
        raise

# Example usage
if __name__ == "__main__":
    company_data = {
        'name': 'Acme Corporation',
        'logo': 'logo.png',
        'primary_color': '#1E3A8A',
        'secondary_color': '#3B82F6'
    }
    
    products = [
        {
            'name': 'Premium Widget',
            'description': 'Our flagship product with advanced features.',
            'image': 'widget.jpg'
        },
        {
            'name': 'Standard Widget',
            'description': 'Reliable and affordable solution for everyday needs.',
            'image': 'standard_widget.jpg'
        }
    ]
    
    generate_catalog('acme_catalog.pdf', company_data, products)
```
