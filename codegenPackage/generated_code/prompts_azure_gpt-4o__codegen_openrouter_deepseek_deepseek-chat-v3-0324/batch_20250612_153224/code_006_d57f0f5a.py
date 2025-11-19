"""
Generated Code Metadata:
========================
Original URL: https://thumbsmaker.com
Prompt: Create a workflow automation script for managing YouTube Shorts and Reels thumbnail creation, inspired by ThumbsMaker’s process, using design libraries like PIL or Canva API.
Generated: DETERMINISTIC_d57f0f5acc53a235
Batch ID: 20250612_153224
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "http://": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import os
import sys
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont, ImageOps
import requests
from io import BytesIO
import logging
from typing import Optional, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('thumbnail_generator.log'),
        logging.StreamHandler()
    ]
)

class ThumbnailGenerator:
    """
    A class to generate YouTube Shorts and Reels thumbnails with text overlays and styling.
    """
    
    def __init__(self, output_dir: str = 'output'):
        """
        Initialize the ThumbnailGenerator with output directory.
        
        Args:
            output_dir (str): Directory to save generated thumbnails. Defaults to 'output'.
        """
        self.output_dir = output_dir
        self._validate_output_dir()
        
        # Default fonts (can be customized)
        self.title_font_path = self._get_font_path('arial.ttf')
        self.subtitle_font_path = self._get_font_path('arial.ttf')
        
    def _validate_output_dir(self) -> None:
        """Create output directory if it doesn't exist."""
        try:
            os.makedirs(self.output_dir, exist_ok=True)
        except OSError as e:
            logging.error(f"Failed to create output directory: {e}")
            raise
            
    def _get_font_path(self, font_name: str) -> Optional[str]:
        """
        Try to locate a font file in common system locations.
        
        Args:
            font_name (str): Name of the font file to locate.
            
        Returns:
            Optional[str]: Path to the font file if found, None otherwise.
        """
        # Common font directories
        font_dirs = [
            '/usr/share/fonts/truetype',
            '/Library/Fonts',
            'C:/Windows/Fonts',
            '/System/Library/Fonts'
        ]
        
        for font_dir in font_dirs:
            font_path = os.path.join(font_dir, font_name)
            if os.path.exists(font_path):
                return font_path
                
        logging.warning(f"Font {font_name} not found in common directories. Using default.")
        return None
        
    def _load_image(self, image_source: str) -> Image.Image:
        """
        Load an image from file path or URL.
        
        Args:
            image_source (str): Path to local image file or URL.
            
        Returns:
            Image.Image: Loaded PIL Image object.
            
        Raises:
            ValueError: If image cannot be loaded.
        """
        try:
            if image_source.startswith(('http://', 'https://')):
                response = requests.get(image_source)
                response.raise_for_status()
                return Image.open(BytesIO(response.content))
            else:
                return Image.open(image_source)
        except Exception as e:
            logging.error(f"Failed to load image: {e}")
            raise ValueError(f"Could not load image from {image_source}")
            
    def _calculate_text_size(
        self,
        text: str,
        font: ImageFont.FreeTypeFont,
        max_width: int
    ) -> Tuple[int, int]:
        """
        Calculate text size with word wrapping.
        
        Args:
            text (str): Text to calculate size for.
            font (ImageFont.FreeTypeFont): Font to use for calculation.
            max_width (int): Maximum allowed width for the text.
            
        Returns:
            Tuple[int, int]: Width and height of the rendered text.
        """
        words = text.split()
        lines = []
        current_line = []
        
        for word in words:
            test_line = ' '.join(current_line + [word])
            test_width = font.getlength(test_line)
            
            if test_width <= max_width:
                current_line.append(word)
            else:
                lines.append(' '.join(current_line))
                current_line = [word]
                
        if current_line:
            lines.append(' '.join(current_line))
            
        total_height = len(lines) * font.size
        max_line_width = max(font.getlength(line) for line in lines) if lines else 0
        
        return int(max_line_width), int(total_height)
        
    def _add_text_to_image(
        self,
        image: Image.Image,
        text: str,
        position: Tuple[int, int],
        font_path: str,
        font_size: int,
        text_color: str,
        max_width: int,
        stroke_color: Optional[str] = None,
        stroke_width: int = 0
    ) -> None:
        """
        Add text to an image with optional stroke/border.
        
        Args:
            image (Image.Image): Image to add text to.
            text (str): Text to add.
            position (Tuple[int, int]): (x, y) position for the text.
            font_path (str): Path to font file.
            font_size (int): Font size in points.
            text_color (str): Text color as hex string.
            max_width (int): Maximum width for text wrapping.
            stroke_color (Optional[str]): Stroke color as hex string. Defaults to None.
            stroke_width (int): Stroke width in pixels. Defaults to 0.
        """
        try:
            font = ImageFont.truetype(font_path, font_size)
        except IOError:
            logging.warning(f"Font {font_path} not found. Using default font.")
            font = ImageFont.load_default()
            
        draw = ImageDraw.Draw(image)
        x, y = position
        
        # Calculate text size with wrapping
        text_width, text_height = self._calculate_text_size(text, font, max_width)
        
        # Draw stroke if specified
        if stroke_color and stroke_width > 0:
            for dx in [-stroke_width, 0, stroke_width]:
                for dy in [-stroke_width, 0, stroke_width]:
                    if dx != 0 or dy != 0:
                        draw.text(
                            (x + dx, y + dy),
                            text,
                            font=font,
                            fill=stroke_color,
                            align='center',
                            spacing=10,
                            stroke_width=0
                        )
        
        # Draw main text
        draw.text(
            (x, y),
            text,
            font=font,
            fill=text_color,
            align='center',
            spacing=10,
            stroke_width=0
        )
        
    def generate_thumbnail(
        self,
        image_source: str,
        title: str,
        subtitle: Optional[str] = None,
        output_filename: Optional[str] = None,
        title_font_size: int = 60,
        subtitle_font_size: int = 40,
        title_color: str = '#FFFFFF',
        subtitle_color: str = '#FFFFFF',
        title_stroke_color: str = '#000000',
        subtitle_stroke_color: str = '#000000',
        stroke_width: int = 5,
        background_blur: int = 10,
        padding: int = 50
    ) -> str:
        """
        Generate a YouTube Shorts/Reels thumbnail with text overlays.
        
        Args:
            image_source (str): Path or URL to background image.
            title (str): Main title text.
            subtitle (Optional[str]): Subtitle text. Defaults to None.
            output_filename (Optional[str]): Output filename. Defaults to timestamp.
            title_font_size (int): Title font size. Defaults to 60.
            subtitle_font_size (int): Subtitle font size. Defaults to 40.
            title_color (str): Title text color. Defaults to '#FFFFFF'.
            subtitle_color (str): Subtitle text color. Defaults to '#FFFFFF'.
            title_stroke_color (str): Title stroke color. Defaults to '#000000'.
            subtitle_stroke_color (str): Subtitle stroke color. Defaults to '#000000'.
            stroke_width (int): Stroke width in pixels. Defaults to 5.
            background_blur (int): Background blur radius. Defaults to 10.
            padding (int): Padding around text. Defaults to 50.
            
        Returns:
            str: Path to the generated thumbnail.
        """
        try:
            # Load background image
            bg_image = self._load_image(image_source)
            
            # Create output filename if not provided
            if not output_filename:
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                output_filename = f"thumbnail_{timestamp}.jpg"
            output_path = os.path.join(self.output_dir, output_filename)
            
            # Resize to YouTube Shorts/Reels aspect ratio (9:16)
            target_width = 1080
            target_height = 1920
            bg_image = ImageOps.fit(bg_image, (target_width, target_height), method=Image.Resampling.LANCZOS)
            
            # Apply blur to background if specified
            if background_blur > 0:
                bg_image = bg_image.filter(ImageFilter.GaussianBlur(background_blur))
            
            # Create a copy to draw on
            thumbnail = bg_image.copy()
            
            # Calculate text positions
            max_text_width = target_width - (2 * padding)
            
            # Add title
            title
