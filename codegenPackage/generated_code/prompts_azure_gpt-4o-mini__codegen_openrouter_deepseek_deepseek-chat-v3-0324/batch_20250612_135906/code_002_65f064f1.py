"""
Generated Code Metadata:
========================
Original URL: https://okayvc.com
Prompt: Write a Python script that automates the process of creating engaging content for social media, inspired by the content development strategies of Okay Visual Creations.
Generated: DETERMINISTIC_65f064f18821750a
Batch ID: 20250612_135906
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
import textwrap
from datetime import datetime, timedelta
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO
import json
import logging
from typing import List, Dict, Optional, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('social_media_automation.log'),
        logging.StreamHandler()
    ]
)

class SocialMediaContentGenerator:
    """
    A class to generate engaging social media content with images and captions.
    Inspired by Okay Visual Creations' content development strategies.
    """
    
    def __init__(self, config_file: str = 'config.json'):
        """
        Initialize the content generator with configuration.
        
        Args:
            config_file (str): Path to the configuration file.
        """
        self.config = self._load_config(config_file)
        self.fonts = self._load_fonts()
        self.content_ideas = self._load_content_ideas()
        self.quotes = self._load_quotes()
        
    def _load_config(self, config_file: str) -> Dict:
        """
        Load configuration from JSON file.
        
        Args:
            config_file (str): Path to the configuration file.
            
        Returns:
            Dict: Configuration dictionary.
            
        Raises:
            FileNotFoundError: If config file doesn't exist.
            json.JSONDecodeError: If config file is invalid JSON.
        """
        try:
            with open(config_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            logging.error(f"Config file {config_file} not found.")
            raise
        except json.JSONDecodeError:
            logging.error(f"Invalid JSON in config file {config_file}.")
            raise
    
    def _load_fonts(self) -> Dict[str, ImageFont.FreeTypeFont]:
        """
        Load fonts from configuration.
        
        Returns:
            Dict: Dictionary of loaded fonts.
        """
        fonts = {}
        try:
            for font_name, font_path in self.config['fonts'].items():
                fonts[font_name] = ImageFont.truetype(font_path, size=40)
            return fonts
        except Exception as e:
            logging.error(f"Error loading fonts: {e}")
            return {
                'default': ImageFont.load_default()
            }
    
    def _load_content_ideas(self) -> List[str]:
        """
        Load content ideas from file.
        
        Returns:
            List[str]: List of content ideas.
        """
        try:
            with open(self.config['content_ideas_file'], 'r') as f:
                return [line.strip() for line in f if line.strip()]
        except Exception as e:
            logging.warning(f"Could not load content ideas: {e}")
            return [
                "Behind the scenes of our creative process",
                "Tips for better content creation",
                "Our latest project showcase",
                "Industry trends you should know about",
                "Client success story"
            ]
    
    def _load_quotes(self) -> List[str]:
        """
        Load inspirational quotes from file.
        
        Returns:
            List[str]: List of quotes.
        """
        try:
            with open(self.config['quotes_file'], 'r') as f:
                return [line.strip() for line in f if line.strip()]
        except Exception as e:
            logging.warning(f"Could not load quotes: {e}")
            return [
                "Creativity is intelligence having fun.",
                "The only limit to your impact is your imagination and commitment.",
                "Design is not just what it looks like, design is how it works.",
                "Content is king, but engagement is queen, and she rules the house."
            ]
    
    def _get_random_image(self) -> Optional[Image.Image]:
        """
        Get a random image either from local directory or API.
        
        Returns:
            Optional[Image.Image]: PIL Image object or None if failed.
        """
        # Try local images first
        if os.path.exists(self.config['images_directory']):
            try:
                image_files = [
                    f for f in os.listdir(self.config['images_directory'])
                    if f.lower().endswith(('.png', '.jpg', '.jpeg'))
                ]
                if image_files:
                    random_image = random.choice(image_files)
                    return Image.open(os.path.join(self.config['images_directory'], random_image))
            except Exception as e:
                logging.warning(f"Could not load local image: {e}")
        
        # Fallback to API if configured
        if 'image_api' in self.config:
            try:
                response = requests.get(self.config['image_api']['url'], 
                                      params=self.config['image_api']['params'])
                response.raise_for_status()
                return Image.open(BytesIO(response.content))
            except Exception as e:
                logging.warning(f"Could not fetch image from API: {e}")
        
        return None
    
    def _add_text_to_image(self, image: Image.Image, text: str) -> Image.Image:
        """
        Add text overlay to an image.
        
        Args:
            image (Image.Image): Base image.
            text (str): Text to overlay.
            
        Returns:
            Image.Image: Image with text overlay.
        """
        try:
            draw = ImageDraw.Draw(image)
            
            # Calculate text position and size
            image_width, image_height = image.size
            max_text_width = image_width * 0.8
            font = self.fonts.get('primary', self.fonts['default'])
            
            # Wrap text
            wrapped_text = textwrap.fill(text, width=30)
            
            # Calculate text size
            text_bbox = draw.textbbox((0, 0), wrapped_text, font=font)
            text_width = text_bbox[2] - text_bbox[0]
            text_height = text_bbox[3] - text_bbox[1]
            
            # Position text
            x = (image_width - text_width) / 2
            y = (image_height - text_height) / 2
            
            # Add text with shadow effect
            shadow_color = (0, 0, 0, 128)
            draw.text((x+2, y+2), wrapped_text, font=font, fill=shadow_color)
            draw.text((x, y), wrapped_text, font=font, fill="white")
            
            return image
        except Exception as e:
            logging.error(f"Error adding text to image: {e}")
            return image
    
    def _generate_caption(self, content_type: str) -> str:
        """
        Generate a social media caption based on content type.
        
        Args:
            content_type (str): Type of content ('quote', 'tip', 'promo', etc.)
            
        Returns:
            str: Generated caption.
        """
        hashtags = " ".join(f"#{tag}" for tag in self.config['hashtags'])
        
        if content_type == 'quote':
            quote = random.choice(self.quotes)
            return f"{quote}\n\n{hashtags}"
        elif content_type == 'tip':
            tip = random.choice(self.content_ideas)
            return f"📌 Pro Tip: {tip}\n\nWhat's your favorite tip? Comment below! 👇\n\n{hashtags}"
        elif content_type == 'promo':
            return f"🚀 Exciting news coming soon! Stay tuned for updates.\n\n{hashtags}"
        else:
            idea = random.choice(self.content_ideas)
            return f"{idea}\n\n{hashtags}"
    
    def _save_content(self, image: Image.Image, caption: str, platform: str) -> Tuple[str, str]:
        """
        Save generated content to disk.
        
        Args:
            image (Image.Image): Generated image.
            caption (str): Generated caption.
            platform (str): Target platform ('instagram', 'twitter', etc.)
            
        Returns:
            Tuple[str, str]: Paths to saved image and caption files.
        """
        try:
            os.makedirs(self.config['output_directory'], exist_ok=True)
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            image_path = os.path.join(
                self.config['output_directory'],
                f"{platform}_post_{timestamp}.jpg"
            )
            caption_path = os.path.join(
                self.config['output_directory'],
                f"{platform}_post_{timestamp}.txt"
            )
            
            # Save image
            image.save(image_path, quality=95)
            
            # Save caption
            with open(caption_path, 'w') as f:
                f.write(caption)
            
            return image_path, caption_path
        except Exception as e:
            logging.error(f"Error saving content: {e}")
            raise
    
    def generate_post(self, platform: str = 'instagram', content_type: str = None) -> Tuple[str, str]:
        """
        Generate a complete social media post.
        
        Args:
            platform (str): Target platform ('instagram', 'twitter', etc.)
            content_type (str): Type of content to generate.
            
        Returns:
            Tuple[str, str]: Paths to saved image and caption files.
        """
        try:
            if not content_type:
                content_type = random.choice
