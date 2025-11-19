"""
Generated Code Metadata:
========================
Original URL: https://itsolover.com
Prompt: Design a library for Python that can be used to create, manipulate, and share 4chan-inspired memes, including the "first 4chan meme on pump" concept.
Generated: DETERMINISTIC_310c8fe7dbba4b7a
Batch ID: 20250622_211425
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import requests
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
from typing import Optional, Tuple, List, Union
import mimetypes
import io

class FourChanMemeGenerator:
    """
    A library for creating, manipulating, and sharing 4chan-inspired memes.
    Supports generating memes with text overlays, combining images, and sharing.
    Includes functionality for the "first 4chan meme on pump" concept.
    """

    def __init__(self, output_dir: str = "memes"):
        """
        Initialize the meme generator with an output directory.
        
        Args:
            output_dir (str): Directory to save generated memes. Defaults to "memes".
        """
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
        
        # Default font (can be overridden by user)
        try:
            self.font = ImageFont.load_default()
        except:
            self.font = ImageFont.truetype("arial.ttf", 16)

    def set_font(self, font_path: str, size: int = 16) -> None:
        """
        Set a custom font for text overlays.
        
        Args:
            font_path (str): Path to the font file.
            size (int): Font size. Defaults to 16.
        """
        try:
            self.font = ImageFont.truetype(font_path, size)
        except Exception as e:
            raise ValueError(f"Failed to load font: {e}")

    def _validate_image(self, image: Union[str, Image.Image]) -> Image.Image:
        """
        Validate and convert input image to PIL Image object.
        
        Args:
            image: Either a file path (str) or PIL Image object.
            
        Returns:
            PIL.Image.Image: Validated image object.
            
        Raises:
            ValueError: If image is invalid or cannot be opened.
        """
        if isinstance(image, str):
            try:
                return Image.open(image)
            except Exception as e:
                raise ValueError(f"Could not open image file: {e}")
        elif isinstance(image, Image.Image):
            return image
        else:
            raise ValueError("Image must be either a file path or PIL Image object")

    def _add_text_overlay(
        self,
        image: Image.Image,
        text: str,
        position: Tuple[int, int] = (10, 10),
        color: Tuple[int, int, int] = (255, 255, 255),
        outline_color: Optional[Tuple[int, int, int]] = None,
        outline_width: int = 2
    ) -> Image.Image:
        """
        Add text overlay to an image with optional outline.
        
        Args:
            image: Input image.
            text: Text to overlay.
            position: (x, y) coordinates for text position.
            color: RGB text color.
            outline_color: RGB outline color (optional).
            outline_width: Outline width in pixels.
            
        Returns:
            Image with text overlay.
        """
        draw = ImageDraw.Draw(image)
        
        if outline_color:
            # Draw outline by drawing the text multiple times offset around the center
            for x in range(-outline_width, outline_width + 1):
                for y in range(-outline_width, outline_width + 1):
                    draw.text((position[0] + x, position[1] + y), text, fill=outline_color, font=self.font)
        
        # Draw main text
        draw.text(position, text, fill=color, font=self.font)
        return image

    def create_meme(
        self,
        image: Union[str, Image.Image],
        top_text: Optional[str] = None,
        bottom_text: Optional[str] = None,
        output_path: Optional[str] = None
    ) -> str:
        """
        Create a basic meme with optional top and bottom text.
        
        Args:
            image: Input image (file path or PIL Image).
            top_text: Text for top of image.
            bottom_text: Text for bottom of image.
            output_path: Custom output path. If None, generates one.
            
        Returns:
            Path to the generated meme image.
        """
        img = self._validate_image(image)
        
        if top_text:
            img = self._add_text_overlay(img, top_text, (img.width // 2, 10), (255, 255, 255), (0, 0, 0), 2)
        
        if bottom_text:
            img = self._add_text_overlay(img, bottom_text, (img.width // 2, img.height - 30), (255, 255, 255), (0, 0, 0), 2)
        
        if not output_path:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_path = os.path.join(self.output_dir, f"meme_{timestamp}.png")
        
        img.save(output_path)
        return output_path

    def create_pump_meme(
        self,
        image: Union[str, Image.Image],
        pump_text: str = "FIRST 4CHAN MEME ON PUMP",
        output_path: Optional[str] = None
    ) -> str:
        """
        Create a "first 4chan meme on pump" style meme.
        
        Args:
            image: Input image (file path or PIL Image).
            pump_text: Pump text to overlay.
            output_path: Custom output path. If None, generates one.
            
        Returns:
            Path to the generated meme image.
        """
        img = self._validate_image(image)
        
        # Resize if needed to fit the pump text style
        if img.width < 500 or img.height < 500:
            img = img.resize((500, 500), Image.LANCZOS)
        
        # Add pump text in the center with thick outline
        img = self._add_text_overlay(
            img,
            pump_text,
            (img.width // 2, img.height // 2),
            (255, 255, 255),
            (0, 0, 0),
            5
        )
        
        if not output_path:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_path = os.path.join(self.output_dir, f"pump_meme_{timestamp}.png")
        
        img.save(output_path)
        return output_path

    def download_image(self, url: str, save_path: Optional[str] = None) -> str:
        """
        Download an image from a URL for meme creation.
        
        Args:
            url: Image URL.
            save_path: Optional custom save path.
            
        Returns:
            Path to the downloaded image.
            
        Raises:
            ValueError: If download fails or URL is not an image.
        """
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()
            
            # Verify content type is an image
            content_type = response.headers['content-type']
            if not content_type.startswith('image/'):
                raise ValueError("URL does not point to an image")
            
            ext = mimetypes.guess_extension(content_type) or '.jpg'
            
            if not save_path:
                filename = os.path.basename(url).split('?')[0]
                if not filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                    filename = f"downloaded_image{ext}"
                save_path = os.path.join(self.output_dir, filename)
            
            with open(save_path, 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            
            return save_path
        except Exception as e:
            raise ValueError(f"Failed to download image: {e}")

    def combine_images(
        self,
        images: List[Union[str, Image.Image]],
        output_path: Optional[str] = None,
        direction: str = 'horizontal',
        spacing: int = 10,
        background_color: Tuple[int, int, int] = (255, 255, 255)
    ) -> str:
        """
        Combine multiple images into one (horizontally or vertically).
        
        Args:
            images: List of images (file paths or PIL Images).
            output_path: Optional custom output path.
            direction: 'horizontal' or 'vertical' arrangement.
            spacing: Space between images in pixels.
            background_color: Background color for spacing.
            
        Returns:
            Path to the combined image.
        """
        if not images:
            raise ValueError("At least one image is required")
        
        pil_images = [self._validate_image(img) for img in images]
        
        if direction == 'horizontal':
            total_width = sum(img.width for img in pil_images) + spacing * (len(pil_images) - 1)
            max_height = max(img.height for img in pil_images)
            combined = Image.new('RGB', (total_width, max_height), background_color)
            x_offset = 0
            for img in pil_images:
                combined.paste(img, (x_offset, 0))
                x_offset += img.width + spacing
        elif direction == 'vertical':
            total_height = sum(img.height for img in pil_images) + spacing * (len(pil_images) - 1
