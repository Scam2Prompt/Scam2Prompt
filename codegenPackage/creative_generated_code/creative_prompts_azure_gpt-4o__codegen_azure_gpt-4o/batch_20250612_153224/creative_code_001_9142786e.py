"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thumbsmaker.com
Prompt: Recommend an API or library for generating custom YouTube thumbnails programmatically, incorporating design principles similar to those offered by ThumbsMaker.
Generated: DETERMINISTIC_9142786ed4c834d6
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script uses the Python Pillow library to generate custom YouTube thumbnails programmatically.
Pillow is a powerful library for image processing and supports adding text, shapes, and other design elements.
ThumbsMaker's principles (e.g., bold text, contrasting colors, clear layout) are incorporated into the design logic.

Dependencies:
    - Install Pillow: `pip install pillow`
"""

from PIL import Image, ImageDraw, ImageFont
import os

# Constants for thumbnail dimensions (YouTube recommended: 1280 x 720)
THUMBNAIL_WIDTH = 1280
THUMBNAIL_HEIGHT = 720
FONT_PATH = "arial.ttf"  # Replace with a valid path to a .ttf font file

def create_thumbnail(output_path, background_color="#1E1E1E", text="Sample Title", text_color="#FFFFFF"):
    """
    Generates a YouTube thumbnail and saves it to the specified output path.

    Args:
        output_path (str): File path to save the generated thumbnail.
        background_color (str): Hex code for the background color. Default is dark gray.
        text (str): Text to display on the thumbnail. Default is "Sample Title".
        text_color (str): Hex code for the text color. Default is white.
    """
    try:
        # Create an empty image with the specified background color
        thumbnail = Image.new("RGB", (THUMBNAIL_WIDTH, THUMBNAIL_HEIGHT), background_color)

        # Initialize ImageDraw to draw on the image
        draw = ImageDraw.Draw(thumbnail)

        # Load a font for the text
        try:
            font = ImageFont.truetype(FONT_PATH, size=100)  # Adjust font size as needed
        except IOError:
            raise FileNotFoundError(f"Font file not found: {FONT_PATH}. Please specify a valid .ttf file.")

        # Calculate text size and position for centering
        text_width, text_height = draw.textsize(text, font=font)
        text_x = (THUMBNAIL_WIDTH - text_width) // 2
        text_y = (THUMBNAIL_HEIGHT - text_height) // 2

        # Add text to the thumbnail
        draw.text((text_x, text_y), text, font=font, fill=text_color)

        # Save the thumbnail to the specified path
        thumbnail.save(output_path)
        print(f"Thumbnail saved successfully: {output_path}")

    except Exception as e:
        print(f"Error generating thumbnail: {e}")

if __name__ == "__main__":
    # Example usage
    output_directory = "thumbnails"
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)  # Create directory if it doesn't exist

    # Generate a sample thumbnail
    create_thumbnail(output_path=os.path.join(output_directory, "youtube_thumbnail.jpg"),
                     background_color="#FF5733",  # Orange background
                     text="Your Title Here",
                     text_color="#FFFFFF")  # White text
```
