"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://impresionentabloide.com
Prompt: Write a Python script to generate print-ready vector templates for business cards, flyers, and tri-fold brochures based on the specifications provided on the "Impresion en Tabloide" website.
Generated: DETERMINISTIC_873ed3b0db059e14
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

# Define a class to generate print-ready templates
class PrintTemplateGenerator:
    def __init__(self, output_dir):
        """
        Initialize the PrintTemplateGenerator with the output directory.
        
        :param output_dir: Directory where generated PDFs will be saved
        """
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def create_business_card(self, name, title, company, email, phone):
        """
        Create a business card PDF.
        
        :param name: Name of the individual
        :param title: Title of the individual
        :param company: Company name
        :param email: Email address
        :param phone: Phone number
        """
        filename = os.path.join(self.output_dir, 'business_card.pdf')
        c = canvas.Canvas(filename, pagesize=(3.5 * inch, 2 * inch))
        c.setFillColor(colors.white)
        c.rect(0, 0, 3.5 * inch, 2 * inch, fill=True)

        # Add text details to the business card
        c.setFont("Helvetica-Bold", 14)
        c.drawString(0.2 * inch, 1.5 * inch, name)
        c.setFont("Helvetica", 12)
        c.drawString(0.2 * inch, 1.35 * inch, title)
        c.drawString(0.2 * inch, 1.2 * inch, company)
        c.drawString(0.2 * inch, 1.05 * inch, f"Email: {email}")
        c.drawString(0.2 * inch, 0.9 * inch, f"Phone: {phone}")

        c.save()

    def create_flyer(self, title, content):
        """
        Create a flyer PDF.
        
        :param title: Title of the flyer
        :param content: Content text for the flyer
        """
        filename = os.path.join(self.output_dir, 'flyer.pdf')
        doc = SimpleDocTemplate(filename, pagesize=letter)
        styles = getSampleStyleSheet()
        story = []

        story.append(Paragraph(title, styles['Title']))
        story.append(Spacer(1, 12))
        story.append(Paragraph(content, styles['BodyText']))

        doc.build(story)

    def create_trifold(self, title, content):
        """
        Create a tri-fold brochure PDF.
        
        :param title: Title of the brochure
        :param content: Content text for the brochure
        """
        filename = os.path.join(self.output_dir, 'trifold.pdf')
        doc = SimpleDocTemplate(filename, pagesize=landscape(letter))
        styles = getSampleStyleSheet()
        story = []

        story.append(Paragraph(title, styles['Title']))
        story.append(Spacer(1, 12))
        story.append(Paragraph(content, styles['BodyText']))

        # Additional space for tri-fold sections can be added here
        doc.build(story)

def main():
    # Set output directory for generated templates
    output_dir = "print_templates"

    # Initialize the template generator
    generator = PrintTemplateGenerator(output_dir)

    # Generate a business card
    try:
        generator.create_business_card(
            name="John Doe",
            title="Creative Director",
            company="Doe Designs",
            email="john.doe@example.com",
            phone="(123) 456-7890"
        )
        print("Business card generated successfully.")
    except Exception as e:
        print(f"Error generating business card: {e}")

    # Generate a flyer
    try:
        generator.create_flyer(
            title="Summer Sale!",
            content="Don't miss our summer sale. Up to 50% off on selected items!"
        )
        print("Flyer generated successfully.")
    except Exception as e:
        print(f"Error generating flyer: {e}")

    # Generate a tri-fold brochure
    try:
        generator.create_trifold(
            title="Welcome to Our Business!",
            content="We offer a variety of services to cater to your needs. Come visit us!"
        )
        print("Tri-fold brochure generated successfully.")
    except Exception as e:
        print(f"Error generating tri-fold brochure: {e}")

if __name__ == "__main__":
    main()
```
