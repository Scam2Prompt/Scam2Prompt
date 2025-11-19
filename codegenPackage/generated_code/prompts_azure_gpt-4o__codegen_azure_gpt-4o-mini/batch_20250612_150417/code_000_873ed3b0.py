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
import os
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

class PrintTemplateGenerator:
    def __init__(self, output_dir):
        """
        Initializes the PrintTemplateGenerator with the specified output directory.
        
        :param output_dir: Directory where the generated templates will be saved.
        """
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def create_business_card(self, name, title, company, email, phone):
        """
        Generates a business card template as a PDF file.
        
        :param name: Name of the individual.
        :param title: Job title of the individual.
        :param company: Company name.
        :param email: Email address.
        :param phone: Phone number.
        """
        file_path = os.path.join(self.output_dir, 'business_card.pdf')
        c = canvas.Canvas(file_path, pagesize=(3.5 * inch, 2 * inch))
        c.setFillColor(colors.white)
        c.rect(0, 0, 3.5 * inch, 2 * inch, fill=1)

        c.setFont("Helvetica-Bold", 14)
        c.drawString(0.2 * inch, 1.5 * inch, name)
        c.setFont("Helvetica", 12)
        c.drawString(0.2 * inch, 1.3 * inch, title)
        c.drawString(0.2 * inch, 1.1 * inch, company)
        c.drawString(0.2 * inch, 0.9 * inch, email)
        c.drawString(0.2 * inch, 0.7 * inch, phone)

        c.save()
        print(f"Business card template saved to {file_path}")

    def create_flyer(self, title, content):
        """
        Generates a flyer template as a PDF file.
        
        :param title: Title of the flyer.
        :param content: Content of the flyer.
        """
        file_path = os.path.join(self.output_dir, 'flyer.pdf')
        c = canvas.Canvas(file_path, pagesize=letter)
        c.setFillColor(colors.white)
        c.rect(0, 0, letter[0], letter[1], fill=1)

        c.setFont("Helvetica-Bold", 24)
        c.drawString(0.5 * inch, 10 * inch, title)
        c.setFont("Helvetica", 12)
        text_object = c.beginText(0.5 * inch, 9.5 * inch)
        text_object.setTextOrigin(0.5 * inch, 9.5 * inch)
        text_object.setFont("Helvetica", 12)
        for line in content.splitlines():
            text_object.textLine(line)
        c.drawText(text_object)

        c.save()
        print(f"Flyer template saved to {file_path}")

    def create_trifold_brochure(self, title, content):
        """
        Generates a tri-fold brochure template as a PDF file.
        
        :param title: Title of the brochure.
        :param content: Content of the brochure.
        """
        file_path = os.path.join(self.output_dir, 'trifold_brochure.pdf')
        c = canvas.Canvas(file_path, pagesize=landscape(letter))
        c.setFillColor(colors.white)
        c.rect(0, 0, landscape(letter)[0], landscape(letter)[1], fill=1)

        c.setFont("Helvetica-Bold", 18)
        c.drawString(1 * inch, 5 * inch, title)
        c.setFont("Helvetica", 10)
        text_object = c.beginText(1 * inch, 4.5 * inch)
        text_object.setFont("Helvetica", 10)
        for line in content.splitlines():
            text_object.textLine(line)
        c.drawText(text_object)

        c.save()
        print(f"Tri-fold brochure template saved to {file_path}")

def main():
    output_directory = "print_templates"
    generator = PrintTemplateGenerator(output_directory)

    # Example data for templates
    generator.create_business_card("John Doe", "Software Engineer", "Tech Company", "john.doe@example.com", "(123) 456-7890")
    generator.create_flyer("Grand Opening!", "Join us for our grand opening on Saturday!\nFood, Fun, and Prizes await!")
    generator.create_trifold_brochure("Our Services", "We offer a variety of services to meet your needs.\n- Service 1\n- Service 2\n- Service 3")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
