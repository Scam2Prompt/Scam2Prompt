"""
Generated Code Metadata:
========================
Original URL: https://www.lords.marketing
Prompt: Create a Python script that automates the design process for marketing materials in the pub sector, reflecting the strategic approach of Lords Marketing.
Generated: DETERMINISTIC_298b7a70cd5f7ebf
Batch ID: 20250612_162051
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
import logging
from typing import Dict, List, Optional, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('marketing_designer.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class MarketingMaterialDesigner:
    """
    A class to automate the design process for pub sector marketing materials.
    Follows Lords Marketing's strategic approach.
    """
    
    def __init__(self, config_path: str = 'config.json'):
        """
        Initialize the designer with configuration.
        
        Args:
            config_path: Path to the configuration JSON file.
        """
        self.config = self._load_config(config_path)
        self._validate_config()
        self.fonts = self._load_fonts()
        
    def _load_config(self, config_path: str) -> Dict:
        """
        Load configuration from JSON file.
        
        Args:
            config_path: Path to the config file.
            
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
            logger.error(f"Config file not found at {config_path}")
            raise
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON in config file: {e}")
            raise
    
    def _validate_config(self) -> None:
        """
        Validate the configuration.
        
        Raises:
            ValueError: If required config values are missing.
        """
        required_fields = [
            'output_dir',
            'templates',
            'brand_colors',
            'default_fonts'
        ]
        
        for field in required_fields:
            if field not in self.config:
                raise ValueError(f"Missing required config field: {field}")
                
        if not os.path.exists(self.config['output_dir']):
            os.makedirs(self.config['output_dir'])
    
    def _load_fonts(self) -> Dict[str, ImageFont.FreeTypeFont]:
        """
        Load fonts from configuration.
        
        Returns:
            Dictionary mapping font names to font objects.
            
        Raises:
            IOError: If font files cannot be loaded.
        """
        fonts = {}
        try:
            for name, path in self.config['default_fonts'].items():
                fonts[name] = ImageFont.truetype(path, size=40)  # Default size
            return fonts
        except IOError as e:
            logger.error(f"Failed to load fonts: {e}")
            raise
    
    def _get_template(self, template_name: str) -> Dict:
        """
        Get template configuration by name.
        
        Args:
            template_name: Name of the template to retrieve.
            
        Returns:
            Template configuration dictionary.
            
        Raises:
            ValueError: If template doesn't exist.
        """
        if template_name not in self.config['templates']:
            raise ValueError(f"Template '{template_name}' not found in config")
        return self.config['templates'][template_name]
    
    def _get_output_path(self, template_name: str) -> str:
        """
        Generate output path for the design.
        
        Args:
            template_name: Name of the template being used.
            
        Returns:
            Full output path for the generated image.
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{template_name}_{timestamp}.png"
        return os.path.join(self.config['output_dir'], filename)
    
    def _hex_to_rgb(self, hex_color: str) -> Tuple[int, int, int]:
        """
        Convert hex color to RGB tuple.
        
        Args:
            hex_color: Color in hex format (e.g., '#RRGGBB').
            
        Returns:
            RGB tuple.
            
        Raises:
            ValueError: If hex color is invalid.
        """
        hex_color = hex_color.lstrip('#')
        if len(hex_color) != 6:
            raise ValueError(f"Invalid hex color: {hex_color}")
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    
    def _create_base_image(self, width: int, height: int, bg_color: str) -> Image.Image:
        """
        Create a base image with specified dimensions and background color.
        
        Args:
            width: Image width in pixels.
            height: Image height in pixels.
            bg_color: Background color in hex format.
            
        Returns:
            PIL Image object.
        """
        try:
            color = self._hex_to_rgb(bg_color)
            return Image.new('RGB', (width, height), color=color)
        except ValueError as e:
            logger.error(f"Error creating base image: {e}")
            raise
    
    def _add_text_to_image(
        self,
        image: Image.Image,
        text: str,
        position: Tuple[int, int],
        font_name: str,
        font_size: int,
        color: str,
        max_width: Optional[int] = None,
        align: str = 'left'
    ) -> Image.Image:
        """
        Add text to an image with proper formatting.
        
        Args:
            image: PIL Image to add text to.
            text: Text content.
            position: (x, y) coordinates for text position.
            font_name: Name of the font to use.
            font_size: Font size in points.
            color: Text color in hex format.
            max_width: Maximum width for text wrapping (optional).
            align: Text alignment ('left', 'center', 'right').
            
        Returns:
            Modified PIL Image with text added.
        """
        draw = ImageDraw.Draw(image)
        
        try:
            font = self.fonts[font_name].font_variant(size=font_size)
            text_color = self._hex_to_rgb(color)
            
            if max_width:
                # Wrap text if max_width is specified
                avg_char_width = font_size * 0.6  # Approximate average character width
                max_chars = int(max_width / avg_char_width)
                wrapped_text = textwrap.fill(text, width=max_chars)
                text = wrapped_text
            
            draw.text(position, text, fill=text_color, font=font, align=align)
            return image
        except KeyError:
            logger.error(f"Font '{font_name}' not found")
            raise
        except ValueError as e:
            logger.error(f"Error adding text: {e}")
            raise
    
    def _add_image_element(
        self,
        base_image: Image.Image,
        image_path: str,
        position: Tuple[int, int],
        size: Optional[Tuple[int, int]] = None
    ) -> Image.Image:
        """
        Add an image element to the base image.
        
        Args:
            base_image: Base PIL Image.
            image_path: Path to the image to add.
            position: (x, y) coordinates for positioning.
            size: Optional (width, height) to resize the image.
            
        Returns:
            Modified PIL Image with the element added.
            
        Raises:
            FileNotFoundError: If image file doesn't exist.
        """
        try:
            element = Image.open(image_path)
            if size:
                element = element.resize(size)
            base_image.paste(element, position)
            return base_image
        except FileNotFoundError:
            logger.error(f"Image file not found: {image_path}")
            raise
    
    def create_design(
        self,
        template_name: str,
        content: Dict[str, str],
        custom_image_path: Optional[str] = None
    ) -> str:
        """
        Create a marketing material design based on a template.
        
        Args:
            template_name: Name of the template to use.
            content: Dictionary containing text content for the template.
            custom_image_path: Optional path to a custom image to include.
            
        Returns:
            Path to the generated image file.
            
        Raises:
            ValueError: If required content is missing.
        """
        try:
            template = self._get_template(template_name)
            output_path = self._get_output_path(template_name)
            
            # Create base image
            width = template['dimensions']['width']
            height = template['dimensions']['height']
            bg_color = template.get('background_color', '#FFFFFF')
            image = self._create_base_image(width, height, bg_color)
            
            # Add template elements
            for element in template['elements']:
                if element['type'] == 'text':
                    required_fields = ['text_key', 'position', 'font', 'size', 'color']
                    for field in required_fields:
                        if field not in element:
                            raise ValueError(f"Missing required field '{field}' in text element")
                    
                    text_key = element['text_key']
                    if text_key not in content:
                        raise ValueError(f"Missing content for text key '{text_key}'")
                    
                    image = self._add_text_to_image(
                        image=image,
