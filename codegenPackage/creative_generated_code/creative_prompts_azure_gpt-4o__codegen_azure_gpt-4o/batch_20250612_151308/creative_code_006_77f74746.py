"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ramdigi.com
Prompt: Generate a script to create and format brochures and leaflets for digital offset printing, incorporating layout design principles mentioned on Ram Digi's website.
Generated: DETERMINISTIC_77f74746a21a43d6
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
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import cm
import os


def create_brochure(output_file, title, content_sections, images=None):
    """
    Generates a digital-ready brochure PDF following layout design principles.
    
    Args:
        output_file (str): Path to the output PDF file.
        title (str): Title of the brochure.
        content_sections (list of dict): List of sections, each with 'heading' and 'body'.
        images (list of str): List of image paths to include in the brochure (optional).
    
    Returns:
        None
    """
    try:
        # Initialize canvas
        c = canvas.Canvas(output_file, pagesize=A4)
        width, height = A4

        # Define margins and layout spacing
        margin_x = 2 * cm
        margin_y = 2 * cm
        content_width = width - 2 * margin_x
        content_height = height - 2 * margin_y

        # Title Section
        c.setFont("Helvetica-Bold", 20)
        c.setFillColor(colors.darkblue)
        c.drawCentredString(width / 2, height - margin_y, title)

        # Divider line below title
        c.setStrokeColor(colors.gray)
        c.setLineWidth(1)
        c.line(margin_x, height - margin_y - 1 * cm, width - margin_x, height - margin_y - 1 * cm)

        # Content Sections
        y_position = height - margin_y - 3 * cm  # Start below the title
        c.setFont("Helvetica", 12)

        for section in content_sections:
            if y_position < margin_y:
                c.showPage()  # Start a new page
                y_position = height - margin_y

            # Heading
            c.setFont("Helvetica-Bold", 14)
            c.setFillColor(colors.black)
            c.drawString(margin_x, y_position, section['heading'])
            y_position -= 1 * cm

            # Body Text
            c.setFont("Helvetica", 12)
            c.setFillColor(colors.black)
            text = c.beginText(margin_x, y_position)
            text.setFont("Helvetica", 12)
            text.setLeading(15)

            for line in section['body'].split('\n'):
                if y_position < margin_y:
                    c.drawText(text)  # Render previous text
                    c.showPage()  # Start a new page
                    y_position = height - margin_y
                    text = c.beginText(margin_x, y_position)
                    text.setFont("Helvetica", 12)
                    text.setLeading(15)
                text.textLine(line)
                y_position -= 15  # Adjust position for each line
            
            c.drawText(text)  # Render text on canvas
            y_position -= 1 * cm  # Extra spacing between sections

        # Images Section (if provided)
        if images:
            for img_path in images:
                if not os.path.exists(img_path):
                    raise FileNotFoundError(f"Image file not found: {img_path}")

                if y_position < 5 * cm:  # Check if there's sufficient space for the image
                    c.showPage()  # Start a new page
                    y_position = height - margin_y

                c.drawImage(img_path, margin_x, y_position - 5 * cm, width=content_width / 2, height=5 * cm)
                y_position -= 6 * cm  # Adjust position for the next image

        # Finalize and save PDF
        c.save()
        print(f"Brochure successfully created: {output_file}")

    except Exception as e:
        print(f"An error occurred while generating the brochure: {str(e)}")


# Example Usage
if __name__ == "__main__":
    title = "Welcome to Our Services"
    sections = [
        {
            'heading': 'About Us',
            'body': 'We are dedicated to providing the best digital offset printing services.\n'
                    'Our team ensures high-quality output and attention to detail.'
        },
        {
            'heading': 'Services',
            'body': '1. Brochure Printing\n2. Leaflet Design\n3. Custom Layouts\n'
                    'Contact us for more details on our services.'
        },
        {
            'heading': 'Contact Us',
            'body': 'Phone: 123-456-7890\nEmail: contact@ramdigi.com\nAddress: 123 Printing St, Design City'
        }
    ]
    image_paths = ['logo.png', 'product_sample.jpg']
    output_pdf = "brochure.pdf"

    create_brochure(output_pdf, title, sections, images=image_paths)
```
