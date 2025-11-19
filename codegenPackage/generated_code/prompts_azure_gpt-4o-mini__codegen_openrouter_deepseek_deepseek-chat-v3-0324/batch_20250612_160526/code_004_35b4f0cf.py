"""
Generated Code Metadata:
========================
Original URL: https://teamadver.com
Prompt: Design a logo and branding package for a startup, using the design principles highlighted by Team Adver in their animation and graphic services.
Generated: DETERMINISTIC_35b4f0cf2c20e7f1
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Logo and Branding Generator for Startups
Inspired by Team Adver's design principles
"""

from PIL import Image, ImageDraw, ImageFont
import random
import os
import json
from typing import Tuple, Dict, List
from dataclasses import dataclass

@dataclass
class BrandColors:
    primary: str
    secondary: str
    accent: str
    text: str

@dataclass
class BrandFonts:
    heading: str
    body: str
    logo: str

@dataclass
class BrandAssets:
    logo: Image.Image
    color_palette: BrandColors
    fonts: BrandFonts
    patterns: List[Image.Image]

class BrandingGenerator:
    def __init__(self, company_name: str, industry: str):
        self.company_name = company_name
        self.industry = industry
        self.output_dir = f"branding_{company_name.lower().replace(' ', '_')}"
        os.makedirs(self.output_dir, exist_ok=True)
        
    def generate_color_palette(self) -> BrandColors:
        """Generate a harmonious color palette based on industry"""
        industry_colors = {
            "tech": ["#2A5CAA", "#4A90E2", "#FF6B6B", "#333333"],
            "health": ["#3A7D44", "#83C5BE", "#FFDDD2", "#1F1F1F"],
            "finance": ["#1A3A8F", "#577590", "#F94144", "#000000"],
            "creative": ["#6A4C93", "#8AC926", "#FFCA3A", "#242423"],
            "default": ["#264653", "#2A9D8F", "#E9C46A", "#212121"]
        }
        
        colors = industry_colors.get(self.industry.lower(), industry_colors["default"])
        return BrandColors(
            primary=colors[0],
            secondary=colors[1],
            accent=colors[2],
            text=colors[3]
        )
    
    def select_fonts(self) -> BrandFonts:
        """Select appropriate fonts based on industry"""
        font_mapping = {
            "tech": ("Roboto Bold", "Roboto Regular", "Montserrat Bold"),
            "health": ("Lato Bold", "Lato Regular", "Poppins SemiBold"),
            "finance": ("Open Sans Bold", "Open Sans Regular", "Playfair Display Bold"),
            "creative": ("Nunito Bold", "Nunito Regular", "Pacifico Regular"),
            "default": ("Arial Bold", "Arial Regular", "Impact Regular")
        }
        
        fonts = font_mapping.get(self.industry.lower(), font_mapping["default"])
        return BrandFonts(
            heading=fonts[0],
            body=fonts[1],
            logo=fonts[2]
        )
    
    def generate_logo(self, colors: BrandColors, fonts: BrandFonts) -> Image.Image:
        """Generate a modern, clean logo based on Team Adver principles"""
        size = (800, 800)
        logo = Image.new("RGB", size, colors.primary)
        draw = ImageDraw.Draw(logo)
        
        # Create abstract shape
        shape_type = random.choice(["circle", "square", "triangle", "abstract"])
        
        if shape_type == "circle":
            draw.ellipse([(150, 150), (650, 650)], fill=colors.secondary)
        elif shape_type == "square":
            draw.rectangle([(200, 200), (600, 600)], fill=colors.secondary)
        elif shape_type == "triangle":
            draw.polygon([(400, 200), (200, 600), (600, 600)], fill=colors.secondary)
        else:  # abstract
            draw.polygon(
                [(300, 200), (200, 400), (300, 600), (500, 600), (600, 400), (500, 200)],
                fill=colors.secondary
            )
        
        # Add company initials
        initials = "".join([word[0].upper() for word in self.company_name.split()[:2]])
        if len(initials) == 0:
            initials = "CO"
        
        try:
            font = ImageFont.truetype(fonts.logo.split()[0].lower() + ".ttf", 200)
        except:
            font = ImageFont.load_default()
        
        text_width, text_height = draw.textsize(initials, font=font)
        position = ((size[0] - text_width) // 2, (size[1] - text_height) // 2)
        draw.text(position, initials, fill=colors.accent, font=font)
        
        return logo
    
    def generate_patterns(self, colors: BrandColors) -> List[Image.Image]:
        """Generate brand patterns for various applications"""
        patterns = []
        pattern_size = (200, 200)
        
        # Pattern 1: Dots
        dot_pattern = Image.new("RGB", pattern_size, colors.primary)
        dot_draw = ImageDraw.Draw(dot_pattern)
        for i in range(0, pattern_size[0], 40):
            for j in range(0, pattern_size[1], 40):
                dot_draw.ellipse([(i, j), (i+20, j+20)], fill=colors.secondary)
        patterns.append(dot_pattern)
        
        # Pattern 2: Lines
        line_pattern = Image.new("RGB", pattern_size, colors.primary)
        line_draw = ImageDraw.Draw(line_pattern)
        for i in range(0, pattern_size[0], 30):
            line_draw.line([(i, 0), (i, pattern_size[1])], fill=colors.accent, width=5)
        patterns.append(line_pattern)
        
        return patterns
    
    def generate_style_guide(self, assets: BrandAssets) -> None:
        """Generate a comprehensive style guide PDF"""
        # In a real implementation, this would use ReportLab or similar to create a PDF
        style_data = {
            "company_name": self.company_name,
            "colors": {
                "primary": assets.color_palette.primary,
                "secondary": assets.color_palette.secondary,
                "accent": assets.color_palette.accent,
                "text": assets.color_palette.text
            },
            "fonts": {
                "heading": assets.fonts.heading,
                "body": assets.fonts.body,
                "logo": assets.fonts.logo
            },
            "logo_usage": "The logo should always have clear space around it equal to 20% of its width.",
            "typography_scale": {
                "h1": "48px",
                "h2": "36px",
                "h3": "24px",
                "body": "16px",
                "caption": "12px"
            }
        }
        
        with open(f"{self.output_dir}/style_guide.json", "w") as f:
            json.dump(style_data, f, indent=4)
    
    def save_assets(self, assets: BrandAssets) -> None:
        """Save all branding assets to disk"""
        # Save logo
        assets.logo.save(f"{self.output_dir}/logo.png")
        
        # Save color palette
        palette_img = Image.new("RGB", (400, 100), "#FFFFFF")
        draw = ImageDraw.Draw(palette_img)
        colors = [
            assets.color_palette.primary,
            assets.color_palette.secondary,
            assets.color_palette.accent,
            assets.color_palette.text
        ]
        
        for i, color in enumerate(colors):
            draw.rectangle([(i*100, 0), ((i+1)*100, 100)], fill=color)
        
        palette_img.save(f"{self.output_dir}/color_palette.png")
        
        # Save patterns
        for i, pattern in enumerate(assets.patterns):
            pattern.save(f"{self.output_dir}/pattern_{i+1}.png")
        
        # Generate style guide
        self.generate_style_guide(assets)
    
    def generate_brand_package(self) -> BrandAssets:
        """Generate complete branding package"""
        colors = self.generate_color_palette()
        fonts = self.select_fonts()
        logo = self.generate_logo(colors, fonts)
        patterns = self.generate_patterns(colors)
        
        assets = BrandAssets(
            logo=logo,
            color_palette=colors,
            fonts=fonts,
            patterns=patterns
        )
        
        self.save_assets(assets)
        return assets

# Example usage
if __name__ == "__main__":
    try:
        company_name = input("Enter your company name: ")
        industry = input("Enter your industry (tech/health/finance/creative): ")
        
        generator = BrandingGenerator(company_name, industry)
        branding = generator.generate_brand_package()
        
        print(f"Branding package generated successfully in directory: {generator.output_dir}")
    except Exception as e:
        print(f"Error generating branding package:
