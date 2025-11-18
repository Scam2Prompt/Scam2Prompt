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
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, tabloid, landscape
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Frame, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

# Define constants for dimensions and specifications
BUSINESS_CARD_SIZE = (3.5 * 72, 2 * 72)  # 3.5 x 2 inches
FLYER_SIZE = tabloid  # Tabloid size: 11 x 17 inches
BROCHURE_SIZE = tabloid  # Tabloid size, landscape for tri-fold
SAFE_MARGIN = 0.25 * 72  # 0.25-inch margin for safe zone
BLEED_MARGIN = 0.125 * 72  # 0.125-inch bleed margin
OUTPUT_DIR = "print_templates"

# Create output directory if it doesn't exist
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)


def draw_guides(c, width, height):
    """
    Draws safe and bleed margins on the canvas.
    """
    # Draw safe margin (green)
    c.setStrokeColor(colors.green)
    c.setDash(3, 3)
    c.rect(SAFE_MARGIN, SAFE_MARGIN, width - 2 * SAFE_MARGIN, height - 2 * SAFE_MARGIN, stroke=1, fill=0)

    # Draw bleed margin (red)
    c.setStrokeColor(colors.red)
    c.setDash(6, 3)
    c.rect(-BLEED_MARGIN, -BLEED_MARGIN, width + 2 * BLEED_MARGIN, height + 2 * BLEED_MARGIN, stroke=1, fill=0)

    # Reset dash style
    c.setDash()


def create_business_card_template():
    """
    Generates a print-ready PDF template for business cards.
    """
    filename = os.path.join(OUTPUT_DIR, "business_card_template.pdf")
    c = canvas.Canvas(filename, pagesize=BUSINESS_CARD_SIZE)

    width, height = BUSINESS_CARD_SIZE

    # Draw guides for bleed and safe zones
    draw_guides(c, width, height)

    # Add a label
    c.setFont("Helvetica", 10)
    c.drawString(SAFE_MARGIN, height - SAFE_MARGIN - 12, "Business Card Template (3.5 x 2 inches)")

    c.showPage()
    c.save()
    print(f"Business card template saved to {filename}")


def create_flyer_template():
    """
    Generates a print-ready PDF template for flyers.
    """
    filename = os.path.join(OUTPUT_DIR, "flyer_template.pdf")
    c = canvas.Canvas(filename, pagesize=FLYER_SIZE)

    width, height = FLYER_SIZE

    # Draw guides for bleed and safe zones
    draw_guides(c, width, height)

    # Add a label
    c.setFont("Helvetica", 14)
    c.drawString(SAFE_MARGIN, height - SAFE_MARGIN - 20, "Flyer Template (Tabloid: 11 x 17 inches)")

    c.showPage()
    c.save()
    print(f"Flyer template saved to {filename}")


def create_brochure_template():
    """
    Generates a print-ready PDF template for tri-fold brochures.
    """
    filename = os.path.join(OUTPUT_DIR, "brochure_template.pdf")
    c = canvas.Canvas(filename, pagesize=landscape(BROCHURE_SIZE))

    width, height = landscape(BROCHURE_SIZE)

    # Draw guides for bleed and safe zones
    draw_guides(c, width, height)

    # Add fold lines for tri-fold (divide into three equal sections)
    fold_line_1 = width / 3
    fold_line_2 = 2 * width / 3

    c.setStrokeColor(colors.blue)
    c.setLineWidth(0.5)
    c.line(fold_line_1, 0, fold_line_1, height)
    c.line(fold_line_2, 0, fold_line_2, height)

    # Add a label
    c.setFont("Helvetica", 14)
    c.drawString(SAFE_MARGIN, height - SAFE_MARGIN - 20,
                 "Tri-Fold Brochure Template (Tabloid Landscape: 17 x 11 inches)")

    c.showPage()
    c.save()
    print(f"Brochure template saved to {filename}")


if __name__ == "__main__":
    try:
        # Generate templates
        create_business_card_template()
        create_flyer_template()
        create_brochure_template()
        print("All templates generated successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
```
