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
# thumbnail_generator.py

import os
from PIL import Image, ImageDraw, ImageFont

class ThumbnailGenerator:
    """
    A class used to generate eye-catching thumbnails for YouTube Shorts and Reels.

    Attributes:
    ----------
    image_path : str
        The path to the background image.
    text : str
        The text to be displayed on the thumbnail.
    font_size : int
        The size of the font.

    Methods:
    -------
    generate_thumbnail()
        Generates the thumbnail.
    """

    def __init__(self, image_path, text, font_size=30):
        """
        Initializes the ThumbnailGenerator object.

        Parameters:
        ----------
        image_path : str
            The path to the background image.
        text : str
            The text to be displayed on the thumbnail.
        font_size : int, optional
            The size of the font (default is 30).
        """
        self.image_path = image_path
        self.text = text
        self.font_size = font_size

    def generate_thumbnail(self, output_path):
        """
        Generates the thumbnail.

        Parameters:
        ----------
        output_path : str
            The path to save the thumbnail.

        Raises:
        ------
        FileNotFoundError
            If the background image is not found.
        """
        try:
            # Open the background image
            with Image.open(self.image_path) as img:
                # Get the image dimensions
                width, height = img.size

                # Create a drawing context
                draw = ImageDraw.Draw(img)

                # Load the font
                font = ImageFont.truetype("arial.ttf", self.font_size)

                # Calculate the text position
                text_x = width // 2
                text_y = height // 2

                # Draw the text
                draw.text((text_x, text_y), self.text, font=font, anchor="mm")

                # Save the thumbnail
                img.save(output_path)

        except FileNotFoundError:
            print(f"Error: Background image not found at {self.image_path}")
        except Exception as e:
            print(f"An error occurred: {e}")


def main():
    # Example usage
    image_path = "background.jpg"
    text = "ThumbsMaker"
    output_path = "thumbnail.png"

    generator = ThumbnailGenerator(image_path, text)
    generator.generate_thumbnail(output_path)


if __name__ == "__main__":
    main()
```
