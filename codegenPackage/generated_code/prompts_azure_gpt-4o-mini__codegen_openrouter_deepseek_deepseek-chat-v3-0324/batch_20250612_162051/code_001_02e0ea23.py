"""
Generated Code Metadata:
========================
Original URL: https://thumbsmaker.com
Prompt: What are the best practices for designing eye-catching thumbnails for YouTube Shorts and Reels, as highlighted by ThumbsMaker?
Generated: DETERMINISTIC_02e0ea235fba6aa6
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# This script provides utility functions to generate eye-catching thumbnails for YouTube Shorts and Reels
# based on best practices highlighted by ThumbsMaker.

from PIL import Image, ImageDraw, ImageFont
import textwrap
import os

class ThumbnailGenerator:
    """
    A class to generate thumbnails following best practices for YouTube Shorts and Reels.
    """
    
    def __init__(self, width=1080, height=1920):
        """
        Initialize with default dimensions for Shorts/Reels (9:16 aspect ratio).
        """
        self.width = width
        self.height = height
        self.default_bg_color = (0, 0, 0)  # Black background
        self.default_text_color = (255, 255, 255)  # White text
        self.default_font_path = "arial.ttf"  # Default font (ensure this exists or provide path)
        
    def create_thumbnail(self, output_path, text=None, image_path=None, bg_color=None, text_color=None):
        """
        Create a thumbnail with optional text and/or background image.
        
        Args:
            output_path (str): Path to save the thumbnail
            text (str, optional): Text to display on thumbnail
            image_path (str, optional): Background image path
            bg_color (tuple, optional): RGB background color
            text_color (tuple, optional): RGB text color
            
        Raises:
            FileNotFoundError: If image_path doesn't exist
            ValueError: If neither text nor image_path is provided
        """
        if not text and not image_path:
            raise ValueError("Either text or image_path must be provided")
            
        bg_color = bg_color or self.default_bg_color
        text_color = text_color or self.default_text_color
        
        # Create base image
        thumbnail = Image.new("RGB", (self.width, self.height), bg_color)
        draw = ImageDraw.Draw(thumbnail)
        
        # Add background image if provided
        if image_path:
            if not os.path.exists(image_path):
                raise FileNotFoundError(f"Image file not found: {image_path}")
                
            bg_image = Image.open(image_path)
            bg_image = bg_image.resize((self.width, self.height))
            
            # Apply dark overlay for better text visibility
            overlay = Image.new("RGBA", (self.width, self.height), (0, 0, 0, 128))
            thumbnail.paste(bg_image, (0, 0))
            thumbnail.paste(overlay, (0, 0), overlay)
            draw = ImageDraw.Draw(thumbnail)
        
        # Add text if provided
        if text:
            try:
                font = ImageFont.truetype(self.default_font_path, 80)
            except IOError:
                font = ImageFont.load_default()
                
            # Wrap text to fit thumbnail
            wrapped_text = textwrap.fill(text, width=20)
            
            # Calculate text position (centered)
            text_width, text_height = draw.textsize(wrapped_text, font=font)
            x = (self.width - text_width) / 2
            y = (self.height - text_height) / 2
            
            # Add text with outline for better visibility
            outline_width = 2
            for adj in range(outline_width):
                for dx in [-adj, adj]:
                    for dy in [-adj, adj]:
                        draw.text((x+dx, y+dy), wrapped_text, font=font, fill=(0, 0, 0))
            
            draw.text((x, y), wrapped_text, font=font, fill=text_color)
        
        # Save the thumbnail
        thumbnail.save(output_path)
        return output_path

# Example usage
if __name__ == "__main__":
    try:
        generator = ThumbnailGenerator()
        
        # Create thumbnail with text only
        generator.create_thumbnail(
            output_path="text_only_thumbnail.jpg",
            text="5 SECRETS TO VIRAL SHORTS!",
            text_color=(255, 215, 0)  # Gold color
        )
        
        # Create thumbnail with image and text
        generator.create_thumbnail(
            output_path="image_text_thumbnail.jpg",
            text="TRY THIS NOW!",
            image_path="background.jpg",  # Replace with actual image path
            text_color=(255, 255, 255)
        )
        
    except Exception as e:
        print(f"Error generating thumbnail: {e}")
```
