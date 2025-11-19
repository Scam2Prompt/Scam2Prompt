"""
Generated Code Metadata:
========================
Original URL: https://fantom.de
Prompt: Create a Python script to automate the process of designing print media layouts, referencing Fantom Internet Dienst's print media services.
Generated: DETERMINISTIC_228d652300ed9762
Batch ID: 20250612_150040
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
import json
import logging
from typing import Optional, Dict, List, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('print_media_designer.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger('PrintMediaDesigner')

class PrintMediaDesigner:
    """
    A class to automate print media layout design with Fantom Internet Dienst's specifications.
    """
    
    def __init__(self, config_path: str = 'config.json'):
        """
        Initialize the designer with configuration.
        
        Args:
            config_path: Path to the configuration JSON file.
        """
        self.config = self._load_config(config_path)
        self.validate_config()
        self.font_cache = {}
        
    def _load_config(self, config_path: str) -> Dict:
        """
        Load configuration from JSON file.
        
        Args:
            config_path: Path to the configuration file.
            
        Returns:
            Dictionary containing configuration.
            
        Raises:
            FileNotFoundError: If config file doesn't exist.
            json.JSONDecodeError: If config file is invalid JSON.
        """
        try:
            with open(config_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.error(f"Configuration file not found: {config_path}")
            raise
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON in configuration file: {e}")
            raise
    
    def validate_config(self) -> None:
        """
        Validate the configuration parameters.
        
        Raises:
            ValueError: If any required configuration is missing or invalid.
        """
        required_fields = [
            'output_dir', 'default_font', 'default_font_size',
            'color_palette', 'page_sizes', 'margin'
        ]
        
        for field in required_fields:
            if field not in self.config:
                raise ValueError(f"Missing required configuration field: {field}")
                
        if not os.path.exists(self.config['output_dir']):
            os.makedirs(self.config['output_dir'])
            logger.info(f"Created output directory: {self.config['output_dir']}")
    
    def _get_font(self, font_name: Optional[str] = None, font_size: Optional[int] = None) -> ImageFont.FreeTypeFont:
        """
        Get a font object from cache or create a new one.
        
        Args:
            font_name: Name of the font (defaults to config).
            font_size: Size of the font (defaults to config).
            
        Returns:
            PIL ImageFont object.
        """
        font_name = font_name or self.config['default_font']
        font_size = font_size or self.config['default_font_size']
        
        cache_key = f"{font_name}_{font_size}"
        if cache_key not in self.font_cache:
            try:
                font = ImageFont.truetype(font_name, font_size)
                self.font_cache[cache_key] = font
            except IOError:
                logger.warning(f"Font {font_name} not found, using default")
                font = ImageFont.load_default()
                self.font_cache[cache_key] = font
                
        return self.font_cache[cache_key]
    
    def create_layout(
        self,
        content: Dict,
        page_size: str = 'A4',
        output_name: Optional[str] = None
    ) -> str:
        """
        Create a print media layout based on content and specifications.
        
        Args:
            content: Dictionary containing layout content (text, images, etc.)
            page_size: Page size from config (default: 'A4')
            output_name: Optional custom output filename
            
        Returns:
            Path to the generated layout file.
            
        Raises:
            ValueError: If page size is invalid or content is missing required fields.
        """
        if page_size not in self.config['page_sizes']:
            raise ValueError(f"Invalid page size. Available sizes: {list(self.config['page_sizes'].keys())}")
            
        if 'elements' not in content or not isinstance(content['elements'], list):
            raise ValueError("Content must contain 'elements' list")
            
        # Create blank canvas
        width, height = self.config['page_sizes'][page_size]
        layout = Image.new('RGB', (width, height), color=self.config['color_palette']['background'])
        draw = ImageDraw.Draw(layout)
        
        # Add elements to layout
        for element in content['elements']:
            self._add_element(draw, layout, element)
        
        # Save the layout
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_filename = output_name or f"layout_{timestamp}.png"
        output_path = os.path.join(self.config['output_dir'], output_filename)
        
        layout.save(output_path, quality=95)
        logger.info(f"Layout saved to: {output_path}")
        
        return output_path
    
    def _add_element(self, draw: ImageDraw.Draw, layout: Image.Image, element: Dict) -> None:
        """
        Add an element to the layout.
        
        Args:
            draw: ImageDraw object for drawing.
            layout: The layout image.
            element: Dictionary describing the element.
            
        Raises:
            ValueError: If element type is unsupported or missing required fields.
        """
        element_type = element.get('type')
        
        if element_type == 'text':
            self._add_text_element(draw, element)
        elif element_type == 'image':
            self._add_image_element(layout, element)
        elif element_type == 'rectangle':
            self._add_rectangle_element(draw, element)
        else:
            raise ValueError(f"Unsupported element type: {element_type}")
    
    def _add_text_element(self, draw: ImageDraw.Draw, element: Dict) -> None:
        """
        Add a text element to the layout.
        
        Args:
            draw: ImageDraw object for drawing.
            element: Dictionary describing the text element.
            
        Raises:
            ValueError: If required text fields are missing.
        """
        required_fields = ['text', 'position']
        for field in required_fields:
            if field not in element:
                raise ValueError(f"Text element missing required field: {field}")
                
        text = element['text']
        position = tuple(element['position'])
        color = tuple(element.get('color', self.config['color_palette']['text']))
        font = self._get_font(element.get('font'), element.get('font_size'))
        
        draw.text(position, text, fill=color, font=font)
    
    def _add_image_element(self, layout: Image.Image, element: Dict) -> None:
        """
        Add an image element to the layout.
        
        Args:
            layout: The layout image.
            element: Dictionary describing the image element.
            
        Raises:
            ValueError: If required image fields are missing.
            FileNotFoundError: If image file doesn't exist.
        """
        required_fields = ['path', 'position']
        for field in required_fields:
            if field not in element:
                raise ValueError(f"Image element missing required field: {field}")
                
        try:
            image = Image.open(element['path'])
            if 'size' in element:
                image = image.resize(tuple(element['size']))
            layout.paste(image, tuple(element['position']))
        except FileNotFoundError:
            logger.error(f"Image file not found: {element['path']}")
            raise
    
    def _add_rectangle_element(self, draw: ImageDraw.Draw, element: Dict) -> None:
        """
        Add a rectangle element to the layout.
        
        Args:
            draw: ImageDraw object for drawing.
            element: Dictionary describing the rectangle element.
            
        Raises:
            ValueError: If required rectangle fields are missing.
        """
        required_fields = ['position', 'size']
        for field in required_fields:
            if field not in element:
                raise ValueError(f"Rectangle element missing required field: {field}")
                
        position = [
            tuple(element['position']),
            (
                element['position'][0] + element['size'][0],
                element['position'][1] + element['size'][1]
            )
        ]
        color = tuple(element.get('color', self.config['color_palette']['accent']))
        outline = tuple(element.get('outline', color))
        
        draw.rectangle(position, fill=color, outline=outline)

def main():
    """
    Main function to demonstrate the PrintMediaDesigner functionality.
    """
    try:
        designer = PrintMediaDesigner()
        
        # Example content for a layout
        content = {
            "elements": [
                {
                    "type": "text",
                    "text": "Fantom Internet Dienst",
                    "position": [100, 100],
                    "font_size": 36,
                    "color": [0, 0, 0]
                },
                {
                    "type": "text",
                    "text": "Professional Print Media Services",
                    "position": [100, 150],
                    "font_size": 24,
                    "color": [50, 50, 50]
