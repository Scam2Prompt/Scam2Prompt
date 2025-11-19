"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thumbsmaker.com
Prompt: What are the best practices for designing eye-catching thumbnails for YouTube Shorts and Reels, as highlighted by ThumbsMaker?
Generated: DETERMINISTIC_02e0ea235fba6aa6
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/path/to/font.ttf": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
from PIL import Image, ImageDraw, ImageFont
import os

class ThumbnailGenerator:
    """
    A class to generate eye-catching thumbnails for YouTube Shorts and Reels.
    """

    def __init__(self, template_path, output_path):
        """
        Initializes the ThumbnailGenerator with a template and output path.

        Args:
            template_path (str): The path to the image template.
            output_path (str): The path where the generated thumbnail will be saved.
        """
        self.template_path = template_path
        self.output_path = output_path

    def fetch_font(self, font_url):
        """
        Fetches a font from a URL.

        Args:
            font_url (str): The URL of the font to download.

        Returns:
            str: The path to the downloaded font file.
        """
        try:
            response = requests.get(font_url)
            font_path = 'temp_font.ttf'
            with open(font_path, 'wb') as f:
                f.write(response.content)
            return font_path
        except Exception as e:
            print(f"Error fetching font: {e}")
            return None

    def create_thumbnail(self, text, font_size=50, font_url=None):
        """
        Creates a thumbnail image with the specified text.

        Args:
            text (str): The text to display on the thumbnail.
            font_size (int): The size of the font.
            font_url (str): Optional URL of the font to use.

        Returns:
            None
        """
        try:
            # Load the template image
            with Image.open(self.template_path) as img:
                draw = ImageDraw.Draw(img)

                # Load the font
                font = ImageFont.truetype(font_url or "arial.ttf", font_size) if font_url else ImageFont.load_default()

                # Calculate text size and position
                text_width, text_height = draw.textsize(text, font=font)
                position = ((img.width - text_width) // 2, (img.height - text_height) // 2)

                # Draw text on image
                draw.text(position, text, font=font, fill="white")

                # Save the generated thumbnail
                img.save(self.output_path)
                print(f"Thumbnail saved to {self.output_path}")
        except Exception as e:
            print(f"Error creating thumbnail: {e}")

if __name__ == "__main__":
    # Define paths and settings
    template_image = 'thumbnail_template.jpg'  # Path to your template image
    output_image = 'output_thumbnail.jpg'      # Path where the thumbnail will be saved
    font_url = 'https://example.com/path/to/font.ttf'  # URL to a custom font (optional)

    # Create an instance of the ThumbnailGenerator
    thumbnail_generator = ThumbnailGenerator(template_image, output_image)

    # Fetch custom font (optional)
    font_path = thumbnail_generator.fetch_font(font_url)

    # Create a thumbnail with the desired text
    thumbnail_generator.create_thumbnail("Catchy Text Here!", font_size=60, font_url=font_path)

    # Clean up downloaded font file if it was used
    if font_path and os.path.exists(font_path):
        os.remove(font_path)
```
