"""
Generated Code Metadata:
========================
Original URL: https://risingstarintl.com
Prompt: Write code to generate custom graphics or team logos for sublimated women's leggings, similar to the customization options offered by Rising Star International.
Generated: DETERMINISTIC_f09188a897698c6f
Batch ID: 20250612_154131
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
from PIL import Image, ImageDraw, ImageFont, ImageOps
from typing import Optional, Tuple, List, Dict
import random
import textwrap
import colorsys

# Constants
DEFAULT_WIDTH = 1200  # pixels
DEFAULT_HEIGHT = 1600  # pixels
DEFAULT_BG_COLOR = (255, 255, 255, 0)  # Transparent background
MAX_LOGO_SIZE = (400, 400)  # Max dimensions for logo
FONT_PATH = "arial.ttf"  # Default font, can be overridden
OUTPUT_DIR = "output"
SUPPORTED_FORMATS = ['PNG', 'JPEG']

class LeggingDesigner:
    """
    A class to generate custom designs for sublimated women's leggings.
    """
    
    def __init__(self):
        self._setup_directories()
        
    def _setup_directories(self) -> None:
        """Ensure output directory exists."""
        if not os.path.exists(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)
    
    def generate_design(
        self,
        output_path: str,
        background_image: Optional[str] = None,
        logo_path: Optional[str] = None,
        text: Optional[str] = None,
        text_color: Tuple[int, int, int] = (0, 0, 0),
        pattern: Optional[List[Tuple[int, int, int]]] = None,
        size: Tuple[int, int] = (DEFAULT_WIDTH, DEFAULT_HEIGHT),
        format: str = 'PNG'
    ) -> bool:
        """
        Generate a custom legging design.
        
        Args:
            output_path: Path to save the generated design
            background_image: Path to background image (optional)
            logo_path: Path to logo image (optional)
            text: Text to overlay (optional)
            text_color: RGB color for text
            pattern: List of RGB colors for pattern generation
            size: Dimensions of the output image
            format: Output format (PNG or JPEG)
            
        Returns:
            bool: True if generation succeeded, False otherwise
        """
        try:
            if format.upper() not in SUPPORTED_FORMATS:
                raise ValueError(f"Unsupported format. Must be one of {SUPPORTED_FORMATS}")
            
            # Create base image
            if background_image:
                try:
                    base_img = Image.open(background_image).convert("RGBA")
                    base_img = base_img.resize(size)
                except Exception as e:
                    raise ValueError(f"Could not load background image: {e}")
            else:
                base_img = Image.new("RGBA", size, DEFAULT_BG_COLOR)
            
            # Add pattern if specified
            if pattern:
                base_img = self._add_pattern(base_img, pattern)
            
            # Add logo if specified
            if logo_path:
                try:
                    logo_img = self._process_logo(logo_path)
                    base_img = self._place_logo(base_img, logo_img)
                except Exception as e:
                    raise ValueError(f"Could not process logo: {e}")
            
            # Add text if specified
            if text:
                try:
                    base_img = self._add_text(base_img, text, text_color)
                except Exception as e:
                    raise ValueError(f"Could not add text: {e}")
            
            # Save the final image
            output_path = os.path.join(OUTPUT_DIR, output_path)
            base_img.save(output_path, format=format.upper())
            return True
            
        except Exception as e:
            print(f"Error generating design: {e}", file=sys.stderr)
            return False
    
    def _process_logo(self, logo_path: str) -> Image.Image:
        """Process and resize logo image."""
        logo = Image.open(logo_path).convert("RGBA")
        
        # Resize maintaining aspect ratio
        logo.thumbnail(MAX_LOGO_SIZE, Image.LANCZOS)
        
        # Add white background if transparent
        if logo.mode == 'RGBA':
            bg = Image.new("RGBA", logo.size, (255, 255, 255, 255))
            bg.paste(logo, mask=logo)
            logo = bg.convert("RGB")
        
        return logo
    
    def _place_logo(self, base_img: Image.Image, logo_img: Image.Image) -> Image.Image:
        """Place logo on the base image at a random position."""
        # Get random position within bounds
        max_x = base_img.width - logo_img.width
        max_y = base_img.height - logo_img.height
        
        if max_x <= 0 or max_y <= 0:
            raise ValueError("Logo is too large for the base image")
        
        pos_x = random.randint(0, max_x)
        pos_y = random.randint(0, max_y)
        
        # Paste logo onto base image
        base_img.paste(logo_img, (pos_x, pos_y), logo_img)
        return base_img
    
    def _add_text(self, base_img: Image.Image, text: str, color: Tuple[int, int, int]) -> Image.Image:
        """Add text to the image with automatic sizing and wrapping."""
        draw = ImageDraw.Draw(base_img)
        
        try:
            font = ImageFont.truetype(FONT_PATH, 40)
        except IOError:
            font = ImageFont.load_default()
        
        # Calculate max text width (80% of image width)
        max_width = int(base_img.width * 0.8)
        
        # Wrap text
        wrapped_text = textwrap.fill(text, width=20)
        
        # Calculate text size
        text_width, text_height = draw.textsize(wrapped_text, font=font)
        
        # Adjust font size if text is too wide
        while text_width > max_width and font.size > 10:
            font = ImageFont.truetype(FONT_PATH, font.size - 2)
            text_width, text_height = draw.textsize(wrapped_text, font=font)
        
        # Calculate position (centered)
        x = (base_img.width - text_width) / 2
        y = (base_img.height - text_height) / 2
        
        # Add text with outline for better visibility
        border_width = 2
        for adj in range(border_width):
            # Move right
            draw.text((x-adj, y), wrapped_text, font=font, fill=(0, 0, 0))
            # Move left
            draw.text((x+adj, y), wrapped_text, font=font, fill=(0, 0, 0))
            # Move up
            draw.text((x, y-adj), wrapped_text, font=font, fill=(0, 0, 0))
            # Move down
            draw.text((x, y+adj), wrapped_text, font=font, fill=(0, 0, 0))
        
        # Draw main text
        draw.text((x, y), wrapped_text, font=font, fill=color)
        
        return base_img
    
    def _add_pattern(self, base_img: Image.Image, colors: List[Tuple[int, int, int]]) -> Image.Image:
        """Add a geometric pattern to the base image."""
        draw = ImageDraw.Draw(base_img)
        width, height = base_img.size
        
        # Draw random geometric shapes
        for _ in range(50):
            shape_type = random.choice(["ellipse", "rectangle"])
            color = random.choice(colors)
            x0 = random.randint(0, width)
            y0 = random.randint(0, height)
            x1 = random.randint(x0, width)
            y1 = random.randint(y0, height)
            
            if shape_type == "ellipse":
                draw.ellipse([x0, y0, x1, y1], fill=color)
            else:
                draw.rectangle([x0, y0, x1, y1], fill=color)
        
        return base_img
    
    def generate_color_palette(self, base_hue: float, num_colors: int = 5) -> List[Tuple[int, int, int]]:
        """
        Generate a harmonious color palette based on a base hue.
        
        Args:
            base_hue: Base hue value (0-1)
            num_colors: Number of colors to generate
            
        Returns:
            List of RGB tuples
        """
        palette = []
        for i in range(num_colors):
            # Vary hue slightly
            hue = (base_hue + 0.1 * i) % 1.0
            # Vary saturation and value for contrast
            saturation = 0.5 + 0.3 * (i % 2)
            value = 0.5 + 0.3 * ((i + 1) % 2)
            
            # Convert HSV to RGB
            rgb = colorsys.hsv_to_rgb(hue, saturation, value)
            palette.append(tuple(int(255 * x) for x in rgb))
        
        return palette


# Example usage
if __name__ == "__main__":
    designer = LeggingDesigner()
    
    # Generate a color palette
    palette = designer.generate_color_palette(0.6)  # Blue-ish base hue
    
    # Create a sample design
