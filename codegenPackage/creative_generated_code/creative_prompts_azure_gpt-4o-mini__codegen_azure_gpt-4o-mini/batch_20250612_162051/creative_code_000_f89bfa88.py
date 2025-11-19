"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thumbsmaker.com
Prompt: How can I create custom YouTube thumbnails that enhance viewer engagement and drive clicks, similar to the services offered by ThumbsMaker?
Generated: DETERMINISTIC_f89bfa88f722d9a1
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
from PIL import Image, ImageDraw, ImageFont
import os
import uuid

class YouTubeThumbnailGenerator:
    """
    A class to generate custom YouTube thumbnails that enhance viewer engagement.
    """

    def __init__(self, background_image, text_overlay, output_directory='thumbnails'):
        """
        Initializes the thumbnail generator.

        :param background_image: Path to the background image.
        :param text_overlay: Text to overlay on the thumbnail.
        :param output_directory: Directory to save the generated thumbnails.
        """
        self.background_image = background_image
        self.text_overlay = text_overlay
        self.output_directory = output_directory
        self.font_path = "arial.ttf"  # Ensure this font file is available in your environment.
        self.font_size = 70  # Font size for the overlay text.

        # Create output directory if it doesn't exist
        if not os.path.exists(self.output_directory):
            os.makedirs(self.output_directory)

    def generate_thumbnail(self):
        """
        Generates a custom YouTube thumbnail with the specified background and text overlay.

        :return: Path to the generated thumbnail image.
        """
        try:
            # Load the background image
            with Image.open(self.background_image) as img:
                # Resize image to YouTube thumbnail dimensions (1280x720)
                img = img.resize((1280, 720))
                
                # Create a drawing context
                draw = ImageDraw.Draw(img)
                
                # Load font
                font = ImageFont.truetype(self.font_path, self.font_size)

                # Calculate text size to center it
                text_width, text_height = draw.textsize(self.text_overlay, font=font)
                text_x = (img.width - text_width) / 2
                text_y = (img.height - text_height) / 2
                
                # Draw text on the image
                draw.text((text_x, text_y), self.text_overlay, font=font, fill="white")

                # Generate a unique filename
                thumbnail_filename = f"thumbnail_{uuid.uuid4()}.png"
                thumbnail_path = os.path.join(self.output_directory, thumbnail_filename)

                # Save the thumbnail
                img.save(thumbnail_path)
                print(f"Thumbnail generated and saved to: {thumbnail_path}")
                return thumbnail_path

        except Exception as e:
            print(f"Error generating thumbnail: {e}")
            return None


# Usage example
if __name__ == "__main__":
    background_image_path = "path/to/your/background_image.jpg"  # Update with your image path
    text_overlay = "Engaging Thumbnail Text"
    
    generator = YouTubeThumbnailGenerator(background_image_path, text_overlay)
    generator.generate_thumbnail()
```
