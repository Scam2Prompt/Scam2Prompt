"""
Generated Code Metadata:
========================
Original URL: https://alpha-digitalsolutions.com
Prompt: Write a Python script to automate the generation of social media ad designs, inspired by Alpha Digital Solutions' graphic design services.
Generated: DETERMINISTIC_d84cb5c32998f016
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
import random
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import textwrap
import logging
from typing import List, Dict, Optional, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='ad_generator.log'
)

class AdDesignGenerator:
    """Automated social media ad design generator."""
    
    def __init__(self, config: Dict):
        """Initialize the generator with configuration."""
        self.config = config
        self.validate_config()
        self.font_cache = {}
        
        # Create output directory if it doesn't exist
        os.makedirs(self.config['output_dir'], exist_ok=True)
    
    def validate_config(self) -> None:
        """Validate the configuration dictionary."""
        required_keys = [
            'output_dir', 
            'templates', 
            'fonts', 
            'colors', 
            'default_dimensions'
        ]
        
        for key in required_keys:
            if key not in self.config:
                raise ValueError(f"Missing required config key: {key}")
    
    def load_font(self, font_path: str, size: int) -> ImageFont.FreeTypeFont:
        """Load and cache a font."""
        cache_key = f"{font_path}_{size}"
        if cache_key not in self.font_cache:
            try:
                self.font_cache[cache_key] = ImageFont.truetype(font_path, size)
            except IOError as e:
                logging.error(f"Failed to load font {font_path}: {e}")
                raise
        return self.font_cache[cache_key]
    
    def generate_random_color(self) -> Tuple[int, int, int]:
        """Generate a random RGB color."""
        return (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
    
    def get_contrast_color(self, bg_color: Tuple[int, int, int]) -> Tuple[int, int, int]:
        """Get a contrasting text color based on background brightness."""
        brightness = (bg_color[0] * 299 + bg_color[1] * 587 + bg_color[2] * 114) / 1000
        return (0, 0, 0) if brightness > 128 else (255, 255, 255)
    
    def wrap_text(self, text: str, font: ImageFont.FreeTypeFont, max_width: int) -> str:
        """Wrap text to fit within specified width."""
        lines = []
        for line in text.split('\n'):
            wrapped = textwrap.wrap(line, width=max_width)
            lines.extend(wrapped if wrapped else [''])
        return '\n'.join(lines)
    
    def create_background(self, width: int, height: int) -> Image.Image:
        """Create a background image."""
        bg_type = random.choice(['solid', 'gradient'])
        
        if bg_type == 'solid':
            color = random.choice(self.config['colors']['backgrounds'])
            return Image.new('RGB', (width, height), color)
        else:
            # Simple gradient implementation
            base = Image.new('RGB', (width, height))
            draw = ImageDraw.Draw(base)
            top_color = random.choice(self.config['colors']['backgrounds'])
            bottom_color = random.choice(self.config['colors']['backgrounds'])
            
            for y in range(height):
                r = int(top_color[0] + (bottom_color[0] - top_color[0]) * y / height)
                g = int(top_color[1] + (bottom_color[1] - top_color[1]) * y / height)
                b = int(top_color[2] + (bottom_color[2] - top_color[2]) * y / height)
                draw.line([(0, y), (width, y)], fill=(r, g, b))
            
            return base
    
    def add_text_element(
        self, 
        image: Image.Image, 
        text: str, 
        position: Tuple[int, int], 
        font_path: str, 
        font_size: int, 
        max_width: Optional[int] = None,
        color: Optional[Tuple[int, int, int]] = None
    ) -> None:
        """Add text to the image."""
        try:
            draw = ImageDraw.Draw(image)
            font = self.load_font(font_path, font_size)
            
            if max_width:
                text = self.wrap_text(text, font, max_width)
            
            if not color:
                # Sample background color to determine contrast
                bg_sample = image.getpixel(position)
                color = self.get_contrast_color(bg_sample)
            
            draw.text(position, text, font=font, fill=color)
        except Exception as e:
            logging.error(f"Error adding text element: {e}")
            raise
    
    def add_image_element(
        self, 
        base_image: Image.Image, 
        overlay_path: str, 
        position: Tuple[int, int], 
        size: Optional[Tuple[int, int]] = None
    ) -> None:
        """Add an overlay image to the base image."""
        try:
            with Image.open(overlay_path) as overlay:
                if size:
                    overlay = overlay.resize(size)
                base_image.paste(overlay, position, overlay if overlay.mode == 'RGBA' else None)
        except Exception as e:
            logging.error(f"Error adding image element: {e}")
            raise
    
    def generate_cta_button(
        self, 
        text: str, 
        width: int, 
        height: int, 
        bg_color: Optional[Tuple[int, int, int]] = None
    ) -> Image.Image:
        """Generate a call-to-action button."""
        if not bg_color:
            bg_color = random.choice(self.config['colors']['cta'])
        
        button = Image.new('RGB', (width, height), bg_color)
        draw = ImageDraw.Draw(button)
        
        # Add rounded corners
        radius = min(width, height) // 4
        draw.rounded_rectangle([(0, 0), (width, height)], radius, fill=bg_color)
        
        # Add text
        font_path = random.choice(self.config['fonts']['cta'])
        font_size = height // 2
        text_color = self.get_contrast_color(bg_color)
        
        self.add_text_element(
            button, 
            text, 
            (width//2, height//2), 
            font_path, 
            font_size, 
            color=text_color
        )
        
        return button
    
    def apply_template(
        self, 
        base_image: Image.Image, 
        template: Dict, 
        content: Dict
    ) -> Image.Image:
        """Apply a design template to the base image."""
        try:
            # Add background elements
            if 'background' in template:
                if template['background'].get('type') == 'image':
                    self.add_image_element(
                        base_image,
                        template['background']['path'],
                        (0, 0),
                        (base_image.width, base_image.height)
                    )
            
            # Add text elements
            for element in template.get('text_elements', []):
                self.add_text_element(
                    base_image,
                    content.get(element['content_key'], element.get('default', '')),
                    tuple(element['position']),
                    element['font'],
                    element['font_size'],
                    element.get('max_width')
                )
            
            # Add image elements
            for element in template.get('image_elements', []):
                self.add_image_element(
                    base_image,
                    content.get(element['content_key'], element.get('default_path', '')),
                    tuple(element['position']),
                    tuple(element['size']) if 'size' in element else None
                )
            
            # Add CTA button if specified
            if 'cta' in template:
                cta_text = content.get('cta_text', template['cta'].get('default_text', 'Learn More'))
                button = self.generate_cta_button(
                    cta_text,
                    template['cta']['width'],
                    template['cta']['height'],
                    tuple(template['cta'].get('color')) if 'color' in template['cta'] else None
                )
                base_image.paste(
                    button, 
                    tuple(template['cta']['position']), 
                    button if button.mode == 'RGBA' else None
                )
            
            return base_image
        except Exception as e:
            logging.error(f"Error applying template: {e}")
            raise
    
    def generate_ad(
        self, 
        template_name: str, 
        content: Dict, 
        dimensions: Optional[Tuple[int, int]] = None
    ) -> str:
        """Generate a single ad design."""
        try:
            if not dimensions:
                dimensions = tuple(self.config['default_dimensions'])
            
            template = self.config['templates'][template_name]
            base_image = self.create_background(*dimensions)
            final_image = self.apply_template(base_image, template, content)
            
            # Save the image
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"ad_{template_name
