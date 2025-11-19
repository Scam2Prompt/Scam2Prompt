"""
Generated Code Metadata:
========================
Original URL: https://ramdigi.com
Prompt: "Write a script to automate the creation of social media posts with custom graphics and designs, utilizing Ram Digi's design and printing services for promotional materials."
Generated: DETERMINISTIC_c4b1c4795724eaea
Batch ID: 20250622_204729
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import datetime
from PIL import Image, ImageDraw, ImageFont
import textwrap
import requests
import json
import logging
from typing import Optional, Dict, List

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('social_media_automation.log'),
        logging.StreamHandler()
    ]
)

class SocialMediaPostGenerator:
    """
    A class to generate social media posts with custom graphics and designs.
    """
    
    def __init__(self, config_file: str = 'config.json'):
        """
        Initialize the post generator with configuration.
        
        Args:
            config_file (str): Path to the configuration file.
        """
        self.config = self._load_config(config_file)
        self.fonts = self._load_fonts()
        self.templates_dir = self.config.get('templates_dir', 'templates')
        self.output_dir = self.config.get('output_dir', 'output')
        self._ensure_directories_exist()
        
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
        Load fonts specified in the configuration.
        
        Returns:
            Dict[str, ImageFont.FreeTypeFont]: Dictionary of loaded fonts.
        """
        fonts = {}
        for name, path in self.config.get('fonts', {}).items():
            try:
                fonts[name] = ImageFont.truetype(path, size=40)  # Default size
            except IOError:
                logging.warning(f"Font {name} at {path} not found. Using default.")
                fonts[name] = ImageFont.load_default()
        return fonts
    
    def _ensure_directories_exist(self) -> None:
        """
        Ensure required directories exist.
        """
        os.makedirs(self.templates_dir, exist_ok=True)
        os.makedirs(self.output_dir, exist_ok=True)
    
    def create_post(
        self,
        template_name: str,
        text_content: str,
        output_name: str,
        font_name: str = 'default',
        font_size: int = 40,
        text_color: str = '#000000',
        text_position: tuple = (50, 50),
        max_width: int = 30,
        branding: Optional[Dict] = None
    ) -> str:
        """
        Create a social media post with custom graphics and text.
        
        Args:
            template_name (str): Name of the template image file.
            text_content (str): Text content for the post.
            output_name (str): Name for the output file.
            font_name (str): Name of the font to use.
            font_size (int): Font size in points.
            text_color (str): Hex color code for text.
            text_position (tuple): (x, y) position for text.
            max_width (int): Maximum characters per line.
            branding (Optional[Dict]): Branding details (logo, colors).
            
        Returns:
            str: Path to the generated image file.
            
        Raises:
            FileNotFoundError: If template image doesn't exist.
            ValueError: For invalid parameters.
        """
        try:
            # Validate inputs
            if not text_content:
                raise ValueError("Text content cannot be empty")
            
            # Load template image
            template_path = os.path.join(self.templates_dir, template_name)
            if not os.path.exists(template_path):
                raise FileNotFoundError(f"Template {template_name} not found")
            
            image = Image.open(template_path)
            draw = ImageDraw.Draw(image)
            
            # Configure font
            font = self.fonts.get(font_name, self.fonts['default'])
            if font_name != 'default':
                try:
                    font = ImageFont.truetype(self.config['fonts'][font_name], size=font_size)
                except (KeyError, IOError):
                    logging.warning(f"Font {font_name} not available. Using default.")
                    font = self.fonts['default']
            
            # Wrap text
            wrapped_text = textwrap.fill(text_content, width=max_width)
            
            # Draw text
            draw.text(text_position, wrapped_text, fill=text_color, font=font)
            
            # Add branding if provided
            if branding:
                self._add_branding(image, branding)
            
            # Save output
            output_path = os.path.join(self.output_dir, output_name)
            image.save(output_path)
            logging.info(f"Post created at {output_path}")
            
            return output_path
            
        except Exception as e:
            logging.error(f"Error creating post: {str(e)}")
            raise
    
    def _add_branding(self, image: Image.Image, branding: Dict) -> None:
        """
        Add branding elements to the image.
        
        Args:
            image (Image.Image): The image to modify.
            branding (Dict): Branding details.
        """
        try:
            draw = ImageDraw.Draw(image)
            
            # Add logo if specified
            if 'logo_path' in branding:
                logo = Image.open(branding['logo_path'])
                logo_position = branding.get('logo_position', (10, 10))
                logo_size = branding.get('logo_size', (100, 100))
                logo = logo.resize(logo_size)
                image.paste(logo, logo_position, logo)
            
            # Add color overlay if specified
            if 'color_overlay' in branding:
                overlay = Image.new('RGBA', image.size, branding['color_overlay'])
                image = Image.alpha_composite(image.convert('RGBA'), overlay)
            
        except Exception as e:
            logging.warning(f"Could not add branding: {str(e)}")
    
    def generate_posts_from_csv(self, csv_file: str) -> List[str]:
        """
        Generate multiple posts from a CSV file.
        
        Args:
            csv_file (str): Path to CSV file containing post details.
            
        Returns:
            List[str]: List of paths to generated images.
            
        Raises:
            FileNotFoundError: If CSV file doesn't exist.
        """
        if not os.path.exists(csv_file):
            raise FileNotFoundError(f"CSV file {csv_file} not found")
        
        generated_posts = []
        
        try:
            import csv
            with open(csv_file, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    try:
                        output_name = row.get('output_name', f"post_{datetime.datetime.now().timestamp()}.png")
                        post_path = self.create_post(
                            template_name=row['template_name'],
                            text_content=row['text_content'],
                            output_name=output_name,
                            font_name=row.get('font_name', 'default'),
                            font_size=int(row.get('font_size', 40)),
                            text_color=row.get('text_color', '#000000'),
                            text_position=tuple(map(int, row.get('text_position', '50,50').split(','))),
                            max_width=int(row.get('max_width', 30)),
                            branding=json.loads(row.get('branding', '{}'))
                        )
                        generated_posts.append(post_path)
                    except Exception as e:
                        logging.error(f"Error processing row {row}: {str(e)}")
                        continue
            
            return generated_posts
        
        except Exception as e:
            logging.error(f"Error processing CSV file: {str(e)}")
            raise
    
    def upload_to_print_service(self, image_path: str) -> bool:
        """
        Upload generated image to Ram Digi's printing service.
        
        Args:
            image_path (str): Path to the image file to upload.
            
        Returns:
            bool: True if upload was successful, False otherwise.
        """
        if not os.path.exists(image_path):
            logging.error(f"Image file {image_path} not found")
            return False
        
        try:
            api_url = self.config.get('printing_service', {}).get('api_url')
            api_key = self.config.get('printing_service', {}).get('api_key')
            
            if not api_url or not api_key:
                logging.error("Printing service API configuration missing")
                return False
            
            with open(image_path, 'rb') as f:
                files = {'file': (os.path.basename(image_path), f)}
                headers = {'Authorization': f'Bearer {api_key}'}
                response = requests.post(api_url, files=files, headers=headers)
                
                if response.status_code == 200:
                    logging.info(f"Successfully uploaded {image_path} to printing service")
