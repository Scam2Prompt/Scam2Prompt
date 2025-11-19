"""
Generated Code Metadata:
========================
Original URL: https://ramdigi.com
Prompt: Write a Python script that automates the creation of flyers and brochures, incorporating design elements mentioned in Ram Digi's print media services.
Generated: DETERMINISTIC_e5444e88794ca9f6
Batch ID: 20250612_163728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT

class FlyerBrochureGenerator:
    """
    A class to automate the creation of flyers and brochures with customizable design elements.
    """

    def __init__(self, output_path="output.pdf", page_size=letter):
        """
        Initialize the generator with output path and page size.
        
        Args:
            output_path (str): Path to save the generated PDF. Defaults to "output.pdf".
            page_size (tuple): Page dimensions (width, height). Defaults to letter size.
        """
        self.output_path = output_path
        self.page_size = page_size
        self.styles = getSampleStyleSheet()
        self._setup_custom_styles()

    def _setup_custom_styles(self):
        """Setup custom paragraph styles for the flyer/brochure."""
        # Title style
        self.styles.add(ParagraphStyle(
            name="Title",
            parent=self.styles["Heading1"],
            fontSize=24,
            leading=28,
            alignment=TA_CENTER,
            spaceAfter=0.5 * inch,
            textColor=colors.darkblue
        ))

        # Subtitle style
        self.styles.add(ParagraphStyle(
            name="Subtitle",
            parent=self.styles["Heading2"],
            fontSize=18,
            leading=22,
            alignment=TA_CENTER,
            spaceAfter=0.3 * inch,
            textColor=colors.darkblue
        ))

        # Body text style
        self.styles.add(ParagraphStyle(
            name="Body",
            parent=self.styles["BodyText"],
            fontSize=12,
            leading=16,
            alignment=TA_LEFT,
            spaceAfter=0.2 * inch,
            textColor=colors.black
        ))

        # Footer style
        self.styles.add(ParagraphStyle(
            name="Footer",
            parent=self.styles["Normal"],
            fontSize=10,
            leading=12,
            alignment=TA_CENTER,
            textColor=colors.gray
        ))

    def _add_logo(self, elements, logo_path, width=2*inch, height=1*inch):
        """
        Add a logo to the document elements.
        
        Args:
            elements (list): List of document elements.
            logo_path (str): Path to the logo image file.
            width (float): Width of the logo. Defaults to 2 inches.
            height (float): Height of the logo. Defaults to 1 inch.
        """
        if os.path.exists(logo_path):
            logo = Image(logo_path, width=width, height=height)
            elements.append(logo)
            elements.append(Spacer(1, 0.2 * inch))
        else:
            raise FileNotFoundError(f"Logo file not found at {logo_path}")

    def _add_footer(self, elements):
        """Add a footer with contact information."""
        footer_text = "Ram Digi's Print Media Services | Contact: info@ramdigi.com | Phone: +1 (123) 456-7890"
        footer = Paragraph(footer_text, self.styles["Footer"])
        elements.append(Spacer(1, 0.5 * inch))
        elements.append(footer)

    def create_flyer(self, title, subtitle, body_text, logo_path=None):
        """
        Create a single-page flyer with the given content.
        
        Args:
            title (str): Title of the flyer.
            subtitle (str): Subtitle of the flyer.
            body_text (str): Main content of the flyer.
            logo_path (str, optional): Path to the logo image file. Defaults to None.
        """
        doc = SimpleDocTemplate(self.output_path, pagesize=self.page_size)
        elements = []

        # Add logo if provided
        if logo_path:
            self._add_logo(elements, logo_path)

        # Add title
        elements.append(Paragraph(title, self.styles["Title"]))

        # Add subtitle
        elements.append(Paragraph(subtitle, self.styles["Subtitle"]))

        # Add body text
        for paragraph in body_text.split("\n"):
            if paragraph.strip():
                elements.append(Paragraph(paragraph, self.styles["Body"]))
                elements.append(Spacer(1, 0.1 * inch))

        # Add footer
        self._add_footer(elements)

        # Build the document
        doc.build(elements)

    def create_brochure(self, pages_data, logo_path=None):
        """
        Create a multi-page brochure with the given content.
        
        Args:
            pages_data (list of dict): List of page data, each containing title, subtitle, and body_text.
            logo_path (str, optional): Path to the logo image file. Defaults to None.
        """
        doc = SimpleDocTemplate(self.output_path, pagesize=self.page_size)
        elements = []

        for page in pages_data:
            # Add logo if provided (only on first page)
            if logo_path and len(elements) == 0:
                self._add_logo(elements, logo_path)

            # Add title
            elements.append(Paragraph(page["title"], self.styles["Title"]))

            # Add subtitle
            elements.append(Paragraph(page["subtitle"], self.styles["Subtitle"]))

            # Add body text
            for paragraph in page["body_text"].split("\n"):
                if paragraph.strip():
                    elements.append(Paragraph(paragraph, self.styles["Body"]))
                    elements.append(Spacer(1, 0.1 * inch))

            # Add footer to each page
            self._add_footer(elements)

            # Add page break if not last page
            if page != pages_data[-1]:
                elements.append(PageBreak())

        # Build the document
        doc.build(elements)

# Example usage
if __name__ == "__main__":
    try:
        # Example flyer creation
        generator = FlyerBrochureGenerator("flyer.pdf")
        flyer_title = "Summer Sale Event"
        flyer_subtitle = "50% Off All Services This Week Only!"
        flyer_body = """Join us for our annual summer sale event where all print media services are 50% off!\n\nOffer valid from July 1st to July 7th. Don't miss this incredible opportunity to get high-quality flyers, brochures, and business cards at half the regular price."""
        
        generator.create_flyer(
            title=flyer_title,
            subtitle=flyer_subtitle,
            body_text=flyer_body,
            logo_path="logo.png"  # Replace with actual logo path
        )

        # Example brochure creation
        generator = FlyerBrochureGenerator("brochure.pdf")
        brochure_pages = [
            {
                "title": "Our Services",
                "subtitle": "Professional Print Media Solutions",
                "body_text": """We offer a wide range of print media services including:\n\n- Flyer Design & Printing\n- Brochure Creation\n- Business Cards\n- Posters\n\nAll our products are made with high-quality materials and cutting-edge design."""
            },
            {
                "title": "Why Choose Us?",
                "subtitle": "Quality You Can Trust",
                "body_text": """With over 10 years in the industry, we pride ourselves on:\n\n- Fast turnaround times\n- Competitive pricing\n- Exceptional customer service\n- Environmentally friendly materials\n\nLet us bring your vision to life!"""
            }
        ]
        
        generator.create_brochure(
            pages_data=brochure_pages,
            logo_path="logo.png"  # Replace with actual logo path
        )

    except Exception as e:
        print(f"An error occurred: {e}")
```
