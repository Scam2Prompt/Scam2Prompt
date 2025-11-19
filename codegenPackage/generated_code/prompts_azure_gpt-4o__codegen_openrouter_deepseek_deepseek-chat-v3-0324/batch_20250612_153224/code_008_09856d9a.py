"""
Generated Code Metadata:
========================
Original URL: https://crownadvertise.com
Prompt: Write code to generate branded brochures and business cards for a Dubai-based company, using design principles mentioned by Crown Advertising.
Generated: DETERMINISTIC_09856d9a678a0762
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from fpdf import FPDF
from PIL import Image, ImageDraw, ImageFont
import textwrap
import uuid
from typing import Optional, Tuple, List, Dict

# Constants for design parameters
BRAND_COLORS = {
    "primary": "#FFD700",  # Gold
    "secondary": "#C0C0C0",  # Silver
    "accent": "#000000",  # Black
    "background": "#FFFFFF"  # White
}

FONT_PATHS = {
    "title": "fonts/PlayfairDisplay-Bold.ttf",
    "subtitle": "fonts/PlayfairDisplay-Regular.ttf",
    "body": "fonts/Roboto-Regular.ttf"
}

LOGO_PATH = "assets/company_logo.png"
COMPANY_INFO = {
    "name": "Dubai Luxury Holdings",
    "slogan": "Excellence in Every Endeavor",
    "address": "Sheikh Zayed Road, Dubai, UAE",
    "phone": "+971 4 123 4567",
    "email": "contact@dubailuxury.ae",
    "website": "www.dubailuxury.ae"
}

class BrandMaterialGenerator:
    """Generates branded marketing materials following Crown Advertising design principles."""
    
    def __init__(self):
        self._validate_resources()
        
    def _validate_resources(self) -> None:
        """Ensure all required resources are available."""
        if not os.path.exists(LOGO_PATH):
            raise FileNotFoundError(f"Logo file not found at {LOGO_PATH}")
            
        for font_type, font_path in FONT_PATHS.items():
            if not os.path.exists(font_path):
                raise FileNotFoundError(f"Font file not found for {font_type} at {font_path}")
    
    def generate_business_card(self, output_path: str, contact_info: Optional[Dict] = None) -> str:
        """
        Generate a business card PDF.
        
        Args:
            output_path: Directory to save the business card
            contact_info: Optional contact info to override default company info
            
        Returns:
            Path to generated business card
        """
        if contact_info is None:
            contact_info = COMPANY_INFO
            
        # Create PDF
        pdf = FPDF(unit="mm", format=(85, 55))  # Standard business card size
        pdf.add_page()
        
        # Background
        pdf.set_fill_color(*self._hex_to_rgb(BRAND_COLORS["background"]))
        pdf.rect(0, 0, 85, 55, "F")
        
        # Logo
        logo_width = 25
        pdf.image(LOGO_PATH, x=10, y=10, w=logo_width)
        
        # Contact info
        pdf.set_font("Arial", "B", 12)
        pdf.set_text_color(*self._hex_to_rgb(BRAND_COLORS["accent"]))
        pdf.text(40, 15, contact_info["name"])
        
        pdf.set_font("Arial", "", 10)
        pdf.text(40, 20, contact_info["slogan"])
        
        pdf.set_font("Arial", "", 8)
        pdf.text(40, 30, contact_info["address"])
        pdf.text(40, 35, f"Phone: {contact_info['phone']}")
        pdf.text(40, 40, f"Email: {contact_info['email']}")
        pdf.text(40, 45, f"Website: {contact_info['website']}")
        
        # Decorative elements
        pdf.set_draw_color(*self._hex_to_rgb(BRAND_COLORS["primary"]))
        pdf.set_line_width(0.5)
        pdf.line(10, 25, 35, 25)
        
        # Save file
        filename = f"business_card_{uuid.uuid4().hex[:6]}.pdf"
        full_path = os.path.join(output_path, filename)
        pdf.output(full_path)
        
        return full_path
    
    def generate_brochure(self, output_path: str, content: List[Dict]) -> str:
        """
        Generate a tri-fold brochure PDF.
        
        Args:
            output_path: Directory to save the brochure
            content: List of sections with title and body text
            
        Returns:
            Path to generated brochure
        """
        pdf = FPDF(unit="mm", format=(210, 297))  # A4 size
        pdf.add_page()
        
        # Front cover
        self._draw_brochure_cover(pdf)
        
        # Inside panels
        for i, section in enumerate(content[:3]):  # Only first 3 sections for demo
            pdf.add_page()
            self._draw_brochure_section(pdf, section, i+1)
            
        # Back cover
        pdf.add_page()
        self._draw_brochure_back(pdf)
        
        # Save file
        filename = f"brochure_{uuid.uuid4().hex[:6]}.pdf"
        full_path = os.path.join(output_path, filename)
        pdf.output(full_path)
        
        return full_path
    
    def _draw_brochure_cover(self, pdf: FPDF) -> None:
        """Draw the brochure front cover."""
        # Background
        pdf.set_fill_color(*self._hex_to_rgb(BRAND_COLORS["primary"]))
        pdf.rect(0, 0, 210, 297, "F")
        
        # Logo
        pdf.image(LOGO_PATH, x=60, y=100, w=90)
        
        # Title
        pdf.set_font("Arial", "B", 24)
        pdf.set_text_color(*self._hex_to_rgb(BRAND_COLORS["background"]))
        pdf.text(50, 200, COMPANY_INFO["name"])
        
        # Subtitle
        pdf.set_font("Arial", "I", 16)
        pdf.text(65, 210, COMPANY_INFO["slogan"])
    
    def _draw_brochure_section(self, pdf: FPDF, section: Dict, panel_num: int) -> None:
        """Draw a brochure content section."""
        # Background
        pdf.set_fill_color(*self._hex_to_rgb(BRAND_COLORS["background"]))
        pdf.rect(0, 0, 210, 297, "F")
        
        # Section header
        pdf.set_font("Arial", "B", 18)
        pdf.set_text_color(*self._hex_to_rgb(BRAND_COLORS["primary"]))
        pdf.text(20, 30, section.get("title", f"Section {panel_num}"))
        
        # Decorative line
        pdf.set_draw_color(*self._hex_to_rgb(BRAND_COLORS["secondary"]))
        pdf.set_line_width(1)
        pdf.line(20, 35, 190, 35)
        
        # Content
        pdf.set_font("Arial", "", 12)
        pdf.set_text_color(*self._hex_to_rgb(BRAND_COLORS["accent"]))
        
        text = section.get("body", "Content goes here...")
        lines = textwrap.wrap(text, width=80)
        
        for i, line in enumerate(lines):
            pdf.text(20, 50 + (i * 6), line)
            
        # Footer
        pdf.set_font("Arial", "I", 8)
        pdf.text(20, 280, COMPANY_INFO["website"])
    
    def _draw_brochure_back(self, pdf: FPDF) -> None:
        """Draw the brochure back cover."""
        # Background
        pdf.set_fill_color(*self._hex_to_rgb(BRAND_COLORS["secondary"]))
        pdf.rect(0, 0, 210, 297, "F")
        
        # Contact info
        pdf.set_font("Arial", "B", 14)
        pdf.set_text_color(*self._hex_to_rgb(BRAND_COLORS["background"]))
        pdf.text(60, 100, "Contact Us")
        
        pdf.set_font("Arial", "", 12)
        pdf.text(60, 120, COMPANY_INFO["address"])
        pdf.text(60, 130, f"Phone: {COMPANY_INFO['phone']}")
        pdf.text(60, 140, f"Email: {COMPANY_INFO['email']}")
        pdf.text(60, 150, f"Website: {COMPANY_INFO['website']}")
        
        # QR code placeholder
        pdf.set_draw_color(*self._hex_to_rgb(BRAND_COLORS["primary"]))
        pdf.rect(80, 180, 50, 50, "D")
        pdf.set_font("Arial", "I", 10)
        pdf.text(75, 240, "Scan for more information")
    
    def _hex_to_rgb(self, hex_color: str) -> Tuple[int, int, int]:
        """Convert hex color to RGB tuple."""
        hex_color = hex_color.lstrip("#")
        return tuple(int(hex_color[i:i+2],
