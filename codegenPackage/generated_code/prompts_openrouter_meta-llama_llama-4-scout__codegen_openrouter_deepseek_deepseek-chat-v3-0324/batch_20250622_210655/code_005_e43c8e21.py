"""
Generated Code Metadata:
========================
Original URL: https://www.lords.marketing
Prompt: "Develop a code snippet for generating creative artwork for pub promotions using a design and marketing agency's branding guidelines."
Generated: DETERMINISTIC_e43c8e21911041ba
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import math
from PIL import Image, ImageDraw, ImageFont
from typing import Tuple, List, Optional

class PubArtGenerator:
    """
    Generates creative artwork for pub promotions following branding guidelines.
    """
    
    def __init__(self, brand_colors: List[Tuple[int, int, int]], logo_path: Optional[str] = None):
        """
        Initialize with brand colors and optional logo.
        
        Args:
            brand_colors: List of RGB tuples representing brand colors
            logo_path: Path to brand logo image file (optional)
        """
        self.brand_colors = brand_colors
        self.logo_path = logo_path
        self.font_path = "arial.ttf"  # Default font, can be replaced with brand font
        
    def _get_random_brand_color(self) -> Tuple[int, int, int]:
        """Return a random color from brand colors."""
        return random.choice(self.brand_colors)
    
    def _create_gradient(self, width: int, height: int) -> Image.Image:
        """Create a gradient background using brand colors."""
        base = Image.new('RGB', (width, height), self._get_random_brand_color())
        top = Image.new('RGB', (width, height), self._get_random_brand_color())
        mask = Image.new('L', (width, height))
        mask_data = []
        for y in range(height):
            mask_data.extend([int(255 * (y / height))] * width)
        mask.putdata(mask_data)
        base.paste(top, (0, 0), mask)
        return base
    
    def _add_text(self, image: Image.Image, text: str, position: Tuple[int, int], 
                 font_size: int = 40, color: Tuple[int, int, int] = (255, 255, 255)) -> None:
        """Add text to the image following brand guidelines."""
        try:
            font = ImageFont.truetype(self.font_path, font_size)
        except IOError:
            font = ImageFont.load_default()
            
        draw = ImageDraw.Draw(image)
        draw.text(position, text, font=font, fill=color)
    
    def _add_logo(self, image: Image.Image) -> None:
        """Add brand logo to the image if provided."""
        if self.logo_path:
            try:
                logo = Image.open(self.logo_path)
                logo_width, logo_height = logo.size
                img_width, img_height = image.size
                position = (img_width - logo_width - 20, img_height - logo_height - 20)
                image.paste(logo, position, logo)
            except IOError as e:
                print(f"Error loading logo: {e}")
    
    def _add_decorative_elements(self, image: Image.Image) -> None:
        """Add decorative elements following brand style."""
        draw = ImageDraw.Draw(image)
        width, height = image.size
        
        # Add some circles
        for _ in range(5):
            x = random.randint(0, width)
            y = random.randint(0, height)
            radius = random.randint(10, 50)
            draw.ellipse([x-radius, y-radius, x+radius, y+radius], 
                        outline=self._get_random_brand_color(), width=2)
        
        # Add some lines
        for _ in range(3):
            x1 = random.randint(0, width)
            y1 = random.randint(0, height)
            x2 = random.randint(0, width)
            y2 = random.randint(0, height)
            draw.line([x1, y1, x2, y2], fill=self._get_random_brand_color(), width=3)
    
    def generate_promotion_art(self, promotion_text: str, size: Tuple[int, int] = (800, 600)) -> Image.Image:
        """
        Generate promotional artwork with given text.
        
        Args:
            promotion_text: Text to display on the artwork
            size: Dimensions of the output image (width, height)
            
        Returns:
            Generated PIL Image object
        """
        try:
            # Create base image
            image = self._create_gradient(*size)
            
            # Add main promotion text
            text_position = (size[0] // 4, size[1] // 3)
            self._add_text(image, promotion_text, text_position, font_size=48)
            
            # Add decorative elements
            self._add_decorative_elements(image)
            
            # Add logo if available
            self._add_logo(image)
            
            return image
            
        except Exception as e:
            print(f"Error generating artwork: {e}")
            # Return blank image if error occurs
            return Image.new('RGB', size, (255, 255, 255))

# Example usage:
if __name__ == "__main__":
    # Brand colors (RGB values)
    brand_colors = [
        (12, 35, 64),    # Dark blue
        (240, 180, 41),  # Gold
        (200, 16, 46),   # Red
        (255, 255, 255)  # White
    ]
    
    generator = PubArtGenerator(brand_colors)
    artwork = generator.generate_promotion_art("Happy Hour!\n5-7pm Daily")
    artwork.save("pub_promotion.png")
```
