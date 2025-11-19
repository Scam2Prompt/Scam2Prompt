"""
Generated Code Metadata:
========================
Original URL: https://henfruit.ro
Prompt: "Create a branding guide for a company, including a logo design, brand design, and social graphics, using Henfruit's approach to visual identity."
Generated: DETERMINISTIC_1747e24a5209177c
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Branding Guide Generator for Henfruit Visual Identity
This script generates a branding guide including logo, brand design, and social graphics
using Henfruit's visual identity approach.
"""

import os
from dataclasses import dataclass
from typing import List, Optional
from enum import Enum
from PIL import Image, ImageDraw, ImageFont
import colorsys
import random
import textwrap

# Constants
OUTPUT_DIR = "branding_guide"
LOGO_SIZE = (500, 500)
SOCIAL_MEDIA_SIZES = {
    "facebook": (1200, 630),
    "instagram": (1080, 1080),
    "twitter": (1500, 500)
}
FONT_PATH = "arial.ttf"  # Fallback font, replace with brand font
PRIMARY_COLOR = (76, 175, 80)  # Henfruit green
SECONDARY_COLOR = (255, 193, 7)  # Henfruit yellow
ACCENT_COLOR = (33, 150, 243)  # Henfruit blue
TEXT_COLOR = (33, 33, 33)  # Dark gray
BACKGROUND_COLOR = (255, 255, 255)  # White

class BrandElementType(Enum):
    LOGO = "logo"
    COLOR_PALETTE = "color_palette"
    TYPOGRAPHY = "typography"
    SOCIAL_GRAPHIC = "social_graphic"

@dataclass
class BrandElement:
    element_type: BrandElementType
    name: str
    description: str
    image_path: Optional[str] = None

class BrandingGuideGenerator:
    def __init__(self, company_name: str, tagline: str):
        self.company_name = company_name
        self.tagline = tagline
        self.brand_elements: List[BrandElement] = []
        self._setup_directories()
        
    def _setup_directories(self):
        """Create necessary output directories."""
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        os.makedirs(os.path.join(OUTPUT_DIR, "logos"), exist_ok=True)
        os.makedirs(os.path.join(OUTPUT_DIR, "social_graphics"), exist_ok=True)
    
    def _generate_logo(self) -> str:
        """Generate a logo based on Henfruit's visual identity."""
        logo = Image.new("RGB", LOGO_SIZE, BACKGROUND_COLOR)
        draw = ImageDraw.Draw(logo)
        
        # Draw circular background
        draw.ellipse([(50, 50), (450, 450)], fill=PRIMARY_COLOR)
        
        # Draw leaf shape (simplified)
        leaf_points = [
            (250, 100), (350, 200), (300, 350),
            (200, 350), (150, 200)
        ]
        draw.polygon(leaf_points, fill=SECONDARY_COLOR)
        
        # Add company name
        font_size = 40
        font = ImageFont.truetype(FONT_PATH, font_size)
        text_width, text_height = draw.textsize(self.company_name, font=font)
        draw.text(
            ((LOGO_SIZE[0] - text_width) / 2, LOGO_SIZE[1] - 100),
            self.company_name,
            font=font,
            fill=TEXT_COLOR
        )
        
        # Save logo
        logo_path = os.path.join(OUTPUT_DIR, "logos", f"{self.company_name.lower()}_logo.png")
        logo.save(logo_path)
        return logo_path
    
    def _generate_color_palette_image(self) -> str:
        """Generate an image showing the brand color palette."""
        img = Image.new("RGB", (400, 200), BACKGROUND_COLOR)
        draw = ImageDraw.Draw(img)
        
        colors = [PRIMARY_COLOR, SECONDARY_COLOR, ACCENT_COLOR, TEXT_COLOR]
        color_names = ["Primary", "Secondary", "Accent", "Text"]
        
        for i, (color, name) in enumerate(zip(colors, color_names)):
            draw.rectangle([(i*100, 0), ((i+1)*100, 150)], fill=color)
            draw.text((i*100 + 10, 160), name, fill=TEXT_COLOR)
        
        palette_path = os.path.join(OUTPUT_DIR, "color_palette.png")
        img.save(palette_path)
        return palette_path
    
    def _generate_social_media_graphic(self, platform: str) -> str:
        """Generate social media graphics for specified platform."""
        size = SOCIAL_MEDIA_SIZES[platform]
        img = Image.new("RGB", size, BACKGROUND_COLOR)
        draw = ImageDraw.Draw(img)
        
        # Draw background pattern
        for i in range(0, size[0], 100):
            for j in range(0, size[1], 100):
                if (i + j) % 200 == 0:
                    draw.rectangle([(i, j), (i+100, j+100)], fill=PRIMARY_COLOR)
        
        # Add company name and tagline
        title_font = ImageFont.truetype(FONT_PATH, 60)
        tagline_font = ImageFont.truetype(FONT_PATH, 30)
        
        wrapped_tagline = textwrap.fill(self.tagline, width=30)
        
        draw.text(
            (size[0]//4, size[1]//3),
            self.company_name,
            font=title_font,
            fill=SECONDARY_COLOR
        )
        
        draw.text(
            (size[0]//4, size[1]//2),
            wrapped_tagline,
            font=tagline_font,
            fill=TEXT_COLOR
        )
        
        # Save graphic
        graphic_path = os.path.join(
            OUTPUT_DIR,
            "social_graphics",
            f"{self.company_name.lower()}_{platform}.png"
        )
        img.save(graphic_path)
        return graphic_path
    
    def generate_branding_guide(self):
        """Generate complete branding guide."""
        try:
            # Generate logo
            logo_path = self._generate_logo()
            self.brand_elements.append(
                BrandElement(
                    element_type=BrandElementType.LOGO,
                    name="Primary Logo",
                    description="The main logo featuring the company name and brand mark.",
                    image_path=logo_path
                )
            )
            
            # Generate color palette
            palette_path = self._generate_color_palette_image()
            self.brand_elements.append(
                BrandElement(
                    element_type=BrandElementType.COLOR_PALETTE,
                    name="Color Palette",
                    description="Primary, secondary, and accent colors for the brand.",
                    image_path=palette_path
                )
            )
            
            # Generate social media graphics
            for platform in SOCIAL_MEDIA_SIZES.keys():
                graphic_path = self._generate_social_media_graphic(platform)
                self.brand_elements.append(
                    BrandElement(
                        element_type=BrandElementType.SOCIAL_GRAPHIC,
                        name=f"{platform.capitalize()} Graphic",
                        description=f"Social media graphic optimized for {platform}.",
                        image_path=graphic_path
                    )
                )
            
            # Generate branding guide document
            self._generate_guide_document()
            
            return True
        except Exception as e:
            print(f"Error generating branding guide: {e}")
            return False
    
    def _generate_guide_document(self):
        """Generate a PDF or text document summarizing the branding guide."""
        # In a production environment, this would generate a proper PDF
        # For this example, we'll create a simple text file
        guide_path = os.path.join(OUTPUT_DIR, "branding_guide.txt")
        
        with open(guide_path, "w") as f:
            f.write(f"Branding Guide for {self.company_name}\n")
            f.write("=" * 50 + "\n\n")
            f.write(f"Tagline: {self.tagline}\n\n")
            
            f.write("Brand Elements:\n")
            for element in self.brand_elements:
                f.write(f"\n- {element.name} ({element.element_type.value}):\n")
                f.write(f"  {element.description}\n")
                if element.image_path:
                    f.write(f"  Location: {element.image_path}\n")

# Example usage
if __name__ == "__main__":
    company_name = "ExampleCo"
    tagline = "Delivering quality since 2023"
    
    generator = BrandingGuideGenerator(company_name, tagline)
    if generator.generate_branding_guide():
        print(f"Branding guide successfully generated in the '{OUTPUT_DIR}' directory.")
    else:
        print("Failed to generate branding guide.")
```
