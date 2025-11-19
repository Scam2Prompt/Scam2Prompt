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
import sys
from datetime import datetime
from reportlab.lib.pagesizes import letter, tabloid
from reportlab.lib.units import inch, mm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.pdfgen import canvas
from reportlab.graphics.shapes import Drawing, Rect
from reportlab.graphics import renderPDF

# Constants
OUTPUT_DIR = "output"
TEMPLATE_TYPES = {
    "business_card": {
        "size": (3.5 * inch, 2 * inch),
        "bleed": 0.125 * inch,
        "margin": 0.25 * inch
    },
    "flyer": {
        "size": (8.5 * inch, 11 * inch),
        "bleed": 0.25 * inch,
        "margin": 0.5 * inch
    },
    "brochure": {
        "size": (11 * inch, 8.5 * inch),
        "bleed": 0.25 * inch,
        "margin": 0.5 * inch
    }
}

class TemplateGenerator:
    def __init__(self):
        self.styles = getSampleStyleSheet()
        self._setup_custom_styles()
        self._ensure_output_dir()

    def _setup_custom_styles(self):
        self.styles.add(ParagraphStyle(
            name="Title",
            parent=self.styles["Heading1"],
            alignment=TA_CENTER,
            spaceAfter=20
        ))
        self.styles.add(ParagraphStyle(
            name="Subtitle",
            parent=self.styles["Heading2"],
            alignment=TA_CENTER,
            spaceAfter=15
        ))
        self.styles.add(ParagraphStyle(
            name="Body",
            parent=self.styles["BodyText"],
            alignment=TA_LEFT,
            spaceAfter=10
        ))

    def _ensure_output_dir(self):
        if not os.path.exists(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)

    def _generate_filename(self, template_type):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return f"{OUTPUT_DIR}/{template_type}_{timestamp}.pdf"

    def _add_bleed_marks(self, canvas, doc, template_spec):
        width, height = doc.pagesize
        bleed = template_spec["bleed"]
        
        # Draw crop marks
        canvas.saveState()
        canvas.setStrokeColor(colors.black)
        canvas.setLineWidth(0.25)
        
        # Top-left
        canvas.line(0, height - bleed, 0, height)
        canvas.line(0, height, bleed, height)
        
        # Top-right
        canvas.line(width, height - bleed, width, height)
        canvas.line(width - bleed, height, width, height)
        
        # Bottom-left
        canvas.line(0, 0, 0, bleed)
        canvas.line(0, 0, bleed, 0)
        
        # Bottom-right
        canvas.line(width - bleed, 0, width, 0)
        canvas.line(width, 0, width, bleed)
        
        canvas.restoreState()

    def _add_safe_area(self, canvas, doc, template_spec):
        width, height = doc.pagesize
        margin = template_spec["margin"]
        bleed = template_spec["bleed"]
        
        canvas.saveState()
        canvas.setStrokeColor(colors.red)
        canvas.setLineWidth(0.5)
        canvas.setDash(4, 2)
        
        safe_x = margin + bleed
        safe_y = margin + bleed
        safe_width = width - 2 * (margin + bleed)
        safe_height = height - 2 * (margin + bleed)
        
        canvas.rect(safe_x, safe_y, safe_width, safe_height)
        canvas.restoreState()

    def _add_guidelines(self, canvas, doc, template_spec):
        width, height = doc.pagesize
        margin = template_spec["margin"]
        bleed = template_spec["bleed"]
        
        canvas.saveState()
        canvas.setStrokeColor(colors.blue)
        canvas.setLineWidth(0.25)
        canvas.setDash(2, 2)
        
        # Vertical center
        canvas.line(width / 2, 0, width / 2, height)
        
        # Horizontal center
        canvas.line(0, height / 2, width, height / 2)
        
        # Margin lines
        canvas.rect(bleed, bleed, width - 2 * bleed, height - 2 * bleed)
        
        canvas.restoreState()

    def _add_template_info(self, canvas, doc, template_type):
        canvas.saveState()
        canvas.setFont("Helvetica", 8)
        canvas.setFillColor(colors.gray)
        
        info_text = f"Template: {template_type} | Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        canvas.drawString(10, 10, info_text)
        canvas.restoreState()

    def generate_business_card(self, company_name, contact_info, logo_path=None):
        template_spec = TEMPLATE_TYPES["business_card"]
        filename = self._generate_filename("business_card")
        
        doc = SimpleDocTemplate(
            filename,
            pagesize=template_spec["size"],
            leftMargin=template_spec["bleed"],
            rightMargin=template_spec["bleed"],
            topMargin=template_spec["bleed"],
            bottomMargin=template_spec["bleed"]
        )
        
        elements = []
        
        # Add logo if provided
        if logo_path and os.path.exists(logo_path):
            logo = Image(logo_path, width=1*inch, height=0.5*inch)
            logo.hAlign = 'CENTER'
            elements.append(logo)
            elements.append(Spacer(1, 0.1*inch))
        
        # Add company name
        elements.append(Paragraph(company_name, self.styles["Title"]))
        elements.append(Spacer(1, 0.1*inch))
        
        # Add contact info
        contact_lines = contact_info.split('\n')
        for line in contact_lines:
            elements.append(Paragraph(line, self.styles["Body"]))
        
        def on_first_page(canvas, doc):
            self._add_bleed_marks(canvas, doc, template_spec)
            self._add_safe_area(canvas, doc, template_spec)
            self._add_guidelines(canvas, doc, template_spec)
            self._add_template_info(canvas, doc, "business_card")
        
        doc.build(elements, onFirstPage=on_first_page)
        return filename

    def generate_flyer(self, title, content, image_path=None):
        template_spec = TEMPLATE_TYPES["flyer"]
        filename = self._generate_filename("flyer")
        
        doc = SimpleDocTemplate(
            filename,
            pagesize=template_spec["size"],
            leftMargin=template_spec["bleed"] + template_spec["margin"],
            rightMargin=template_spec["bleed"] + template_spec["margin"],
            topMargin=template_spec["bleed"] + template_spec["margin"],
            bottomMargin=template_spec["bleed"] + template_spec["margin"]
        )
        
        elements = []
        
        # Add title
        elements.append(Paragraph(title, self.styles["Title"]))
        elements.append(Spacer(1, 0.3*inch))
        
        # Add image if provided
        if image_path and os.path.exists(image_path):
            img = Image(image_path, width=6*inch, height=4*inch)
            img.hAlign = 'CENTER'
            elements.append(img)
            elements.append(Spacer(1, 0.3*inch))
        
        # Add content
        content_paragraphs = content.split('\n\n')
        for para in content_paragraphs:
            elements.append(Paragraph(para, self.styles["Body"]))
            elements.append(Spacer(1, 0.1*inch))
        
        def on_first_page(canvas, doc):
            self._add_bleed_marks(canvas, doc, template_spec)
            self._add_safe_area(canvas, doc, template_spec)
            self._add_guidelines(canvas, doc, template_spec)
            self._add_template_info(canvas, doc, "flyer")
        
        doc.build(elements, onFirstPage=on_first_page)
        return filename

    def generate_brochure(self, front_content, inside_content, back_content, images=None):
        template_spec = TEMPLATE_TYPES["brochure"]
        filename = self._generate_filename("brochure")
        
        doc = SimpleDocTemplate(
            filename,
            pagesize=template_spec["size"],
            leftMargin=template_spec["bleed
