"""
Generated Code Metadata:
========================
Original URL: https://crownadvertise.com
Prompt: Write code to design and optimize branding assets for a furniture business, referencing Crown Advertising's approach to creative design.
Generated: DETERMINISTIC_ff66045049c5fc7e
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Branding Asset Generator for Furniture Business
Inspired by Crown Advertising's creative design approach
"""

from PIL import Image, ImageDraw, ImageFont
import os
import json
import textwrap
import colorsys
from typing import Tuple, List, Dict, Optional
import random
import uuid
import logging
from dataclasses import dataclass

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@dataclass
class BrandConfig:
    name: str
    primary_color: str
    secondary_color: str
    accent_color: str
    font_family: str
    slogan: str
    logo_path: Optional[str] = None

class BrandAssetGenerator:
    """Generates branding assets for furniture business following design best practices."""
    
    def __init__(self, config: BrandConfig):
        self.config = config
        self.assets_dir = "branding_assets"
        self._validate_config()
        self._setup_directories()
        
    def _validate_config(self):
        """Validate brand configuration."""
        if not all([self.config.name, self.config.primary_color, 
                   self.config.secondary_color, self.config.font_family]):
            raise ValueError("Missing required brand configuration")
            
    def _setup_directories(self):
        """Create necessary directories for assets."""
        os.makedirs(self.assets_dir, exist_ok=True)
        os.makedirs(f"{self.assets_dir}/logos", exist_ok=True)
        os.makedirs(f"{self.assets_dir}/business_cards", exist_ok=True)
        os.makedirs(f"{self.assets_dir}/social_media", exist_ok=True)
        os.makedirs(f"{self.assets_dir}/color_palettes", exist_ok=True)
        
    def _hex_to_rgb(self, hex_color: str) -> Tuple[int, int, int]:
        """Convert hex color to RGB tuple."""
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    
    def _generate_color_variations(self, base_color: str) -> List[str]:
        """Generate complementary color variations."""
        r, g, b = self._hex_to_rgb(base_color)
        h, l, s = colorsys.rgb_to_hls(r/255, g/255, b/255)
        
        variations = []
        for i in range(1, 5):
            new_h = (h + 0.1 * i) % 1.0
            new_r, new_g, new_b = colorsys.hls_to_rgb(new_h, l, s)
            variations.append(f"#{int(new_r*255):02x}{int(new_g*255):02x}{int(new_b*255):02x}")
        
        return variations
    
    def _get_font(self, size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
        """Get font with specified size and weight."""
        try:
            font_path = f"fonts/{self.config.font_family}.ttf"
            if bold:
                font_path = f"fonts/{self.config.font_family}-Bold.ttf"
            return ImageFont.truetype(font_path, size)
        except IOError:
            logger.warning(f"Font {self.config.font_family} not found, using default")
            return ImageFont.load_default()
    
    def generate_logo(self) -> str:
        """Generate logo with brand name and optional graphic."""
        logo_size = (800, 400)
        logo = Image.new("RGB", logo_size, "white")
        draw = ImageDraw.Draw(logo)
        
        # Draw brand name
        font = self._get_font(48, bold=True)
        text_width, text_height = draw.textsize(self.config.name, font=font)
        position = ((logo_size[0] - text_width) // 2, (logo_size[1] - text_height) // 2)
        
        draw.text(position, self.config.name, fill=self.config.primary_color, font=font)
        
        # Add slogan if exists
        if self.config.slogan:
            slogan_font = self._get_font(24)
            slogan_width, slogan_height = draw.textsize(self.config.slogan, font=slogan_font)
            slogan_position = ((logo_size[0] - slogan_width) // 2, position[1] + text_height + 20)
            draw.text(slogan_position, self.config.slogan, fill=self.config.secondary_color, font=slogan_font)
        
        # Save logo
        logo_path = f"{self.assets_dir}/logos/{self.config.name.replace(' ', '_')}_logo.png"
        logo.save(logo_path)
        self.config.logo_path = logo_path
        return logo_path
    
    def generate_business_card(self) -> str:
        """Generate professional business card design."""
        if not self.config.logo_path:
            self.generate_logo()
            
        card_size = (850, 550)  # Standard business card size in pixels (3.5" x 2")
        card = Image.new("RGB", card_size, "white")
        draw = ImageDraw.Draw(card)
        
        # Add background elements
        draw.rectangle([(0, 0), (card_size[0], 100)], fill=self.config.primary_color)
        draw.rectangle([(0, card_size[1] - 80), (card_size[0], card_size[1])], fill=self.config.secondary_color)
        
        # Add logo
        logo = Image.open(self.config.logo_path).resize((300, 150))
        card.paste(logo, ((card_size[0] - logo.width) // 2, 20))
        
        # Add contact info
        contact_font = self._get_font(20)
        contact_info = [
            "123 Furniture Street",
            "Design District, City 10001",
            "Phone: (123) 456-7890",
            "Email: info@example.com",
            "www.example.com"
        ]
        
        y_position = 200
        for line in contact_info:
            draw.text((50, y_position), line, fill="black", font=contact_font)
            y_position += 30
            
        # Add accent elements
        draw.rectangle([(card_size[0] - 50, card_size[1] - 50), (card_size[0] - 20, card_size[1] - 20)], 
                      fill=self.config.accent_color)
        
        # Save card
        card_path = f"{self.assets_dir}/business_cards/{self.config.name.replace(' ', '_')}_business_card.png"
        card.save(card_path)
        return card_path
    
    def generate_social_media_post(self, post_text: str) -> str:
        """Generate branded social media post."""
        post_size = (1080, 1080)  # Standard Instagram post size
        post = Image.new("RGB", post_size, "white")
        draw = ImageDraw.Draw(post)
        
        # Create gradient background
        for i in range(post_size[1]):
            r, g, b = self._hex_to_rgb(self.config.primary_color)
            ratio = i / post_size[1]
            new_r = int(r * (1 - ratio) + 255 * ratio)
            new_g = int(g * (1 - ratio) + 255 * ratio)
            new_b = int(b * (1 - ratio) + 255 * ratio)
            draw.line([(0, i), (post_size[0], i)], fill=(new_r, new_g, new_b))
        
        # Add logo if exists
        if self.config.logo_path:
            logo = Image.open(self.config.logo_path).resize((400, 200))
            post.paste(logo, ((post_size[0] - logo.width) // 2, 50))
        
        # Add post text
        text_font = self._get_font(32)
        wrapped_text = textwrap.wrap(post_text, width=30)
        y_position = 300 if self.config.logo_path else 100
        
        for line in wrapped_text:
            text_width, text_height = draw.textsize(line, font=text_font)
            draw.text(((post_size[0] - text_width) // 2, y_position), 
                     line, fill="black", font=text_font)
            y_position += text_height + 20
        
        # Add call to action
        cta_font = self._get_font(36, bold=True)
        cta_text = "Visit our showroom today!"
        cta_width, cta_height = draw.textsize(cta_text, font=cta_font)
        draw.text(((post_size[0] - cta_width) // 2, y_position + 50), 
                 cta_text, fill=self.config.accent_color, font=cta_font)
        
        # Save post
        post_path = f"{self.assets_dir}/social_media/{self.config.name
