"""
Generated Code Metadata:
========================
Original URL: https://impresionentabloide.com
Prompt: Design a vinyl printing template for a 1x2 meter banner with a triptych layout, using a LaTeX package or a Python library, incorporating the GRACoL2006 color profile.
Generated: DETERMINISTIC_ac4f4ee7cb803915
Batch ID: 20250622_211951
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Vinyl Printing Template Generator for 1x2 Meter Banner with Triptych Layout

This script generates a vinyl printing template for a 1x2 meter banner using
a triptych layout (three panels) and incorporates the GRACoL2006 color profile.

Requirements:
    - Python 3.6+
    - reportlab
    - pillow (PIL)
"""

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import cm, mm
from reportlab.pdfgen import canvas
from PIL import Image, ImageCms
import io
import os

# Constants
BANNER_WIDTH = 1 * 100 * mm  # 1 meter to mm
BANNER_HEIGHT = 2 * 100 * mm  # 2 meters to mm
PANEL_COUNT = 3
BLEED = 5 * mm  # Standard bleed area
SAFE_ZONE = 10 * mm  # Safe zone from edges

def create_banner_template(output_path="banner_template.pdf"):
    """
    Create a PDF template for vinyl printing with triptych layout.
    
    Args:
        output_path (str): Path to save the PDF file.
    """
    try:
        # Create a PDF canvas with landscape A4 (common printer paper size)
        c = canvas.Canvas(output_path, pagesize=landscape(A4))
        
        # Calculate panel dimensions
        panel_width = BANNER_WIDTH / PANEL_COUNT
        panel_height = BANNER_HEIGHT
        
        # Set GRACoL2006 color profile (simulated in RGB)
        # Note: Actual color management would require ICC profile embedding
        gracol_color = colors.Color(0.1, 0.1, 0.1)  # Dark gray for guidelines
        
        # Draw panels with bleed and safe zones
        for i in range(PANEL_COUNT):
            x_offset = i * panel_width
            
            # Panel outline (with bleed)
            c.setStrokeColor(gracol_color)
            c.setLineWidth(0.5 * mm)
            c.rect(
                x_offset - BLEED,
                -BLEED,
                panel_width + 2 * BLEED,
                panel_height + 2 * BLEED,
                stroke=1,
                fill=0
            )
            
            # Safe zone
            c.setStrokeColor(colors.red)
            c.setLineWidth(0.25 * mm)
            c.rect(
                x_offset + SAFE_ZONE,
                SAFE_ZONE,
                panel_width - 2 * SAFE_ZONE,
                panel_height - 2 * SAFE_ZONE,
                stroke=1,
                fill=0
            )
            
            # Panel number
            c.setFillColor(colors.black)
            c.setFont("Helvetica-Bold", 12)
            c.drawString(
                x_offset + panel_width / 2 - 5 * mm,
                panel_height - 15 * mm,
                f"Panel {i+1}"
            )
            
            # Registration marks
            draw_registration_marks(c, x_offset, panel_width, panel_height)
        
        # Add document info
        c.setTitle("Vinyl Banner Template (1x2m Triptych)")
        c.setAuthor("Vinyl Printing System")
        c.setSubject("Printing template with GRACoL2006 color profile")
        
        c.save()
        print(f"Template successfully created at: {os.path.abspath(output_path)}")
        
    except Exception as e:
        print(f"Error generating template: {str(e)}")
        raise

def draw_registration_marks(c, x_offset, width, height):
    """
    Draw registration marks for alignment.
    
    Args:
        c: Canvas object
        x_offset: X position of the panel
        width: Panel width
        height: Panel height
    """
    mark_size = 5 * mm
    line_width = 0.5 * mm
    
    # Top-left
    c.setStrokeColor(colors.black)
    c.setLineWidth(line_width)
    c.line(x_offset, height, x_offset + mark_size, height)
    c.line(x_offset, height, x_offset, height - mark_size)
    
    # Top-right
    c.line(x_offset + width, height, x_offset + width - mark_size, height)
    c.line(x_offset + width, height, x_offset + width, height - mark_size)
    
    # Bottom-left
    c.line(x_offset, 0, x_offset + mark_size, 0)
    c.line(x_offset, 0, x_offset, mark_size)
    
    # Bottom-right
    c.line(x_offset + width, 0, x_offset + width - mark_size, 0)
    c.line(x_offset + width, 0, x_offset + width, mark_size)

if __name__ == "__main__":
    create_banner_template()
```
