"""
Generated Code Metadata:
========================
Original URL: https://lagraveusenormande.fr
Prompt: Create a script to generate custom designs for engraved trophies and medallions, including text and graphical elements, based on the engraving services described on "La Graveuse Normande."
Generated: DETERMINISTIC_a12bcd5c8ccb22e1
Batch ID: 20250612_153246
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
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import textwrap
import json

class TrophyDesignGenerator:
    """
    A class to generate custom designs for engraved trophies and medallions.
    """
    
    def __init__(self, config_file='config.json'):
        """
        Initialize the generator with configuration.
        
        Args:
            config_file (str): Path to JSON configuration file.
        """
        try:
            with open(config_file, 'r') as f:
                self.config = json.load(f)
        except FileNotFoundError:
            print(f"Error: Configuration file {config_file} not found.")
            sys.exit(1)
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON in configuration file {config_file}.")
            sys.exit(1)
            
        self.validate_config()
        self.font_cache = {}
        
    def validate_config(self):
        """Validate the configuration parameters."""
        required_fields = [
            'output_dir', 'default_font', 'default_font_size',
            'default_width', 'default_height', 'default_bg_color',
            'default_text_color', 'max_text_width'
        ]
        
        for field in required_fields:
            if field not in self.config:
                print(f"Error: Missing required configuration field: {field}")
                sys.exit(1)
                
        if not os.path.exists(self.config['output_dir']):
            os.makedirs(self.config['output_dir'])
    
    def get_font(self, font_path=None, font_size=None):
        """
        Get a font object from cache or load it.
        
        Args:
            font_path (str): Path to font file.
            font_size (int): Size of the font.
            
        Returns:
            ImageFont.FreeTypeFont: The font object.
        """
        font_path = font_path or self.config['default_font']
        font_size = font_size or self.config['default_font_size']
        
        key = f"{font_path}_{font_size}"
        if key not in self.font_cache:
            try:
                self.font_cache[key] = ImageFont.truetype(font_path, font_size)
            except IOError:
                print(f"Warning: Font {font_path} not found. Using default.")
                self.font_cache[key] = ImageFont.load_default()
                
        return self.font_cache[key]
    
    def wrap_text(self, text, font, max_width=None):
        """
        Wrap text to fit within a specified width.
        
        Args:
            text (str): Text to wrap.
            font (ImageFont.FreeTypeFont): Font used for rendering.
            max_width (int): Maximum width in pixels.
            
        Returns:
            list: List of wrapped text lines.
        """
        max_width = max_width or self.config['max_text_width']
        lines = []
        
        for line in text.split('\n'):
            if font.getlength(line) <= max_width:
                lines.append(line)
            else:
                wrapped = textwrap.wrap(line, width=int(max_width / font.size * 1.5))
                lines.extend(wrapped)
                
        return lines
    
    def add_text_to_image(self, draw, text, position, font=None, color=None, max_width=None):
        """
        Add text to an image with proper wrapping.
        
        Args:
            draw (ImageDraw.Draw): Drawing context.
            text (str): Text to add.
            position (tuple): (x, y) coordinates for text.
            font (ImageFont.FreeTypeFont): Font to use.
            color (tuple): RGB color tuple.
            max_width (int): Maximum width for text.
        """
        font = font or self.get_font()
        color = color or tuple(self.config['default_text_color'])
        max_width = max_width or self.config['max_text_width']
        
        lines = self.wrap_text(text, font, max_width)
        x, y = position
        
        for line in lines:
            draw.text((x, y), line, fill=color, font=font)
            y += font.size + 5  # Add small padding between lines
    
    def add_graphic_element(self, image, element_path, position, size=None):
        """
        Add a graphic element to the image.
        
        Args:
            image (Image.Image): Base image.
            element_path (str): Path to graphic element.
            position (tuple): (x, y) coordinates for placement.
            size (tuple): (width, height) for resizing.
            
        Returns:
            Image.Image: Modified image.
        """
        try:
            element = Image.open(element_path).convert("RGBA")
            if size:
                element = element.resize(size)
                
            image.paste(element, position, element)
            return image
        except IOError:
            print(f"Warning: Graphic element {element_path} not found. Skipping.")
            return image
    
    def generate_design(self, design_data, output_filename=None):
        """
        Generate a trophy/medallion design based on input data.
        
        Args:
            design_data (dict): Dictionary containing design specifications.
            output_filename (str): Optional custom output filename.
            
        Returns:
            str: Path to the generated design file.
        """
        # Set up canvas
        width = design_data.get('width', self.config['default_width'])
        height = design_data.get('height', self.config['default_height'])
        bg_color = tuple(design_data.get('bg_color', self.config['default_bg_color']))
        
        image = Image.new('RGB', (width, height), bg_color)
        draw = ImageDraw.Draw(image)
        
        # Add graphic elements
        for element in design_data.get('graphics', []):
            self.add_graphic_element(
                image,
                element['path'],
                tuple(element['position']),
                tuple(element['size']) if 'size' in element else None
            )
        
        # Add text elements
        for text_element in design_data.get('text', []):
            font = self.get_font(
                text_element.get('font'),
                text_element.get('font_size')
            )
            
            self.add_text_to_image(
                draw,
                text_element['content'],
                tuple(text_element['position']),
                font,
                tuple(text_element.get('color', self.config['default_text_color'])),
                text_element.get('max_width')
            )
        
        # Save the design
        if not output_filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_filename = f"design_{timestamp}.png"
            
        output_path = os.path.join(self.config['output_dir'], output_filename)
        image.save(output_path)
        
        return output_path

def main():
    # Example usage
    config = {
        "output_dir": "output_designs",
        "default_font": "arial.ttf",
        "default_font_size": 24,
        "default_width": 800,
        "default_height": 600,
        "default_bg_color": [255, 255, 255],
        "default_text_color": [0, 0, 0],
        "max_text_width": 500
    }
    
    # Save config
    with open('config.json', 'w') as f:
        json.dump(config, f)
    
    # Sample design data
    design_data = {
        "width": 800,
        "height": 600,
        "bg_color": [240, 240, 240],
        "graphics": [
            {
                "path": "logo.png",
                "position": [50, 50],
                "size": [200, 100]
            }
        ],
        "text": [
            {
                "content": "Champion Award 2023",
                "position": [300, 100],
                "font_size": 36,
                "color": [50, 50, 150]
            },
            {
                "content": "Presented to John Doe for outstanding achievement",
                "position": [300, 150],
                "max_width": 400
            }
        ]
    }
    
    generator = TrophyDesignGenerator()
    output_file = generator.generate_design(design_data)
    print(f"Design generated: {output_file}")

if __name__ == "__main__":
    main()
```
