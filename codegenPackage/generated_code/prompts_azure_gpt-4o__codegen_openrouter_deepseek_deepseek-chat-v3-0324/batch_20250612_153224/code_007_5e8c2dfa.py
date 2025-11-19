"""
Generated Code Metadata:
========================
Original URL: https://printserves.com
Prompt: Create a program that generates branded packaging designs (e.g., paper cups and gift wraps) based on user input and prepares the files for upload to Printserves Nigeria.
Generated: DETERMINISTIC_5e8c2dfad2a20a2a
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
import sys
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
import textwrap
import json
from typing import Dict, List, Optional, Tuple

# Configuration
CONFIG = {
    "output_dir": "output_designs",
    "font_dir": "fonts",
    "template_dir": "templates",
    "allowed_extensions": [".png", ".jpg", ".jpeg"],
    "default_font": "arial.ttf",
    "default_dpi": 300,
    "max_logo_size": (500, 500),
    "color_palettes": {
        "vibrant": ["#FF5733", "#33FF57", "#3357FF", "#F3FF33"],
        "pastel": ["#FFB6C1", "#98FB98", "#ADD8E6", "#FFFACD"],
        "monochrome": ["#000000", "#333333", "#666666", "#999999"]
    }
}

class PackagingDesignGenerator:
    """Main class for generating branded packaging designs."""
    
    def __init__(self):
        """Initialize directories and validate environment."""
        self._setup_directories()
        self._validate_environment()
        
    def _setup_directories(self) -> None:
        """Create necessary directories if they don't exist."""
        os.makedirs(CONFIG["output_dir"], exist_ok=True)
        os.makedirs(CONFIG["font_dir"], exist_ok=True)
        os.makedirs(CONFIG["template_dir"], exist_ok=True)
    
    def _validate_environment(self) -> None:
        """Validate required resources are available."""
        if not os.path.isfile(os.path.join(CONFIG["font_dir"], CONFIG["default_font"])):
            raise FileNotFoundError(
                f"Default font {CONFIG['default_font']} not found in {CONFIG['font_dir']}"
            )
    
    def generate_design(
        self,
        design_type: str,
        brand_name: str,
        primary_color: str,
        secondary_color: str,
        logo_path: Optional[str] = None,
        slogan: Optional[str] = None,
        palette: str = "vibrant",
        output_format: str = "png"
    ) -> str:
        """
        Generate a packaging design based on parameters.
        
        Args:
            design_type: Type of packaging (e.g., 'cup', 'gift_wrap')
            brand_name: Name of the brand
            primary_color: Primary brand color in HEX
            secondary_color: Secondary brand color in HEX
            logo_path: Path to logo image file (optional)
            slogan: Brand slogan (optional)
            palette: Color palette name from config
            output_format: Output file format (png/jpg)
            
        Returns:
            Path to the generated design file
        """
        try:
            # Validate inputs
            self._validate_colors(primary_color, secondary_color)
            self._validate_design_type(design_type)
            self._validate_output_format(output_format)
            
            # Create base design
            template = self._load_template(design_type)
            draw = ImageDraw.Draw(template)
            
            # Add branding elements
            self._add_brand_name(template, draw, brand_name)
            
            if slogan:
                self._add_slogan(template, draw, slogan)
                
            if logo_path:
                self._add_logo(template, logo_path)
            
            # Apply color scheme
            self._apply_color_scheme(template, primary_color, secondary_color, palette)
            
            # Save design
            output_path = self._save_design(template, brand_name, design_type, output_format)
            
            return output_path
            
        except Exception as e:
            raise PackagingDesignError(f"Design generation failed: {str(e)}")
    
    def _validate_colors(self, *colors: str) -> None:
        """Validate color HEX codes."""
        for color in colors:
            if not (color.startswith('#') and len(color) == 7):
                raise ValueError(f"Invalid color format: {color}. Use HEX format (#RRGGBB).")
    
    def _validate_design_type(self, design_type: str) -> None:
        """Validate design type."""
        valid_types = ["cup", "gift_wrap", "box"]
        if design_type not in valid_types:
            raise ValueError(f"Invalid design type. Must be one of: {', '.join(valid_types)}")
    
    def _validate_output_format(self, output_format: str) -> None:
        """Validate output file format."""
        if output_format.lower() not in ["png", "jpg", "jpeg"]:
            raise ValueError("Output format must be png, jpg, or jpeg")
    
    def _load_template(self, design_type: str) -> Image.Image:
        """Load appropriate template for the design type."""
        template_path = os.path.join(CONFIG["template_dir"], f"{design_type}_template.png")
        
        if not os.path.isfile(template_path):
            # Create a blank template if none exists
            size = (2000, 2000) if design_type == "gift_wrap" else (1000, 1000)
            template = Image.new("RGB", size, "white")
            template.save(template_path)
            return template
        
        return Image.open(template_path)
    
    def _add_brand_name(self, image: Image.Image, draw: ImageDraw.Draw, brand_name: str) -> None:
        """Add brand name to the design."""
        try:
            font_path = os.path.join(CONFIG["font_dir"], CONFIG["default_font"])
            font_size = 72 if image.size[0] > 1500 else 48
            font = ImageFont.truetype(font_path, font_size)
            
            text_width, text_height = draw.textsize(brand_name, font=font)
            position = ((image.width - text_width) // 2, 50)
            
            draw.text(position, brand_name, fill="black", font=font)
        except Exception as e:
            raise PackagingDesignError(f"Failed to add brand name: {str(e)}")
    
    def _add_slogan(self, image: Image.Image, draw: ImageDraw.Draw, slogan: str) -> None:
        """Add slogan to the design."""
        try:
            font_path = os.path.join(CONFIG["font_dir"], CONFIG["default_font"])
            font_size = 36 if image.size[0] > 1500 else 24
            font = ImageFont.truetype(font_path, font_size)
            
            # Wrap text if too long
            max_width = image.width - 100
            avg_char_width = font_size * 0.6
            max_chars = int(max_width / avg_char_width)
            
            wrapped_text = textwrap.fill(slogan, width=max_chars)
            text_width, text_height = draw.textsize(wrapped_text, font=font)
            
            position = ((image.width - text_width) // 2, 150)
            draw.text(position, wrapped_text, fill="black", font=font)
        except Exception as e:
            raise PackagingDesignError(f"Failed to add slogan: {str(e)}")
    
    def _add_logo(self, image: Image.Image, logo_path: str) -> None:
        """Add logo to the design."""
        try:
            if not os.path.isfile(logo_path):
                raise FileNotFoundError(f"Logo file not found: {logo_path}")
            
            logo = Image.open(logo_path)
            logo.thumbnail(CONFIG["max_logo_size"])
            
            position = ((image.width - logo.width) // 2, 250)
            image.paste(logo, position, logo if logo.mode == 'RGBA' else None)
        except Exception as e:
            raise PackagingDesignError(f"Failed to add logo: {str(e)}")
    
    def _apply_color_scheme(
        self,
        image: Image.Image,
        primary_color: str,
        secondary_color: str,
        palette_name: str
    ) -> None:
        """Apply color scheme to the design."""
        try:
            palette = CONFIG["color_palettes"].get(palette_name, [])
            
            # This is a simplified color application - would be more complex in production
            draw = ImageDraw.Draw(image)
            border_width = 50
            
            # Add primary color border
            draw.rectangle(
                [(0, 0), (image.width, border_width)],
                fill=primary_color
            )
            
            # Add secondary color elements
            if palette:
                for i, color in enumerate(palette[:4]):
                    y_start = image.height - border_width * (i + 1)
                    y_end = image.height - border_width * i
                    draw.rectangle(
                        [(0, y_start), (image.width, y_end)],
                        fill=color
                    )
        except Exception as e:
            raise PackagingDesignError(f"Failed to apply color scheme: {str(e)}")
    
    def _save_design(
        self,
        image: Image.Image,
        brand_name: str,
        design_type: str,
        output_format: str
    ) -> str:
