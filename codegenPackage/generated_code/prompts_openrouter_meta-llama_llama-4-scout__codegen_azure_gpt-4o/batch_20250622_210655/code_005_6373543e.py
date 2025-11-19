"""
Generated Code Metadata:
========================
Original URL: https://thumbsmaker.com
Prompt: Recommend a suitable graphic design library or API for creating custom YouTube thumbnails, based on ThumbsMaker's design expertise and services offered.
Generated: DETERMINISTIC_6373543e8a983694
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script recommends a suitable graphic design library for creating custom YouTube thumbnails
based on ThumbsMaker's design expertise and services offered. It uses the Pillow library for image
manipulation and thumbnail creation, which is widely used and production-ready.
"""

# Import necessary libraries
from PIL import Image, ImageDraw, ImageFont
import os

def create_youtube_thumbnail(output_path, title="Sample Thumbnail", background_color=(255, 255, 255)):
    """
    Creates a custom YouTube thumbnail using the Pillow library.

    Args:
        output_path (str): Path to save the generated thumbnail image.
        title (str): Text to display on the thumbnail.
        background_color (tuple): RGB color for the thumbnail background.

    Returns:
        None
    """
    try:
        # Define thumbnail dimensions (YouTube recommended size: 1280x720)
        thumbnail_width = 1280
        thumbnail_height = 720

        # Create a blank image with the specified background color
        thumbnail = Image.new("RGB", (thumbnail_width, thumbnail_height), background_color)

        # Initialize drawing context
        draw = ImageDraw.Draw(thumbnail)

        # Load a font (ensure the font file exists in the working directory or provide a valid path)
        font_path = "arial.ttf"  # Replace with the path to your font file
        try:
            font = ImageFont.truetype(font_path, size=80)
        except IOError:
            raise FileNotFoundError(f"Font file not found at path: {font_path}")

        # Calculate text position to center it on the thumbnail
        text_width, text_height = draw.textsize(title, font=font)
        text_x = (thumbnail_width - text_width) // 2
        text_y = (thumbnail_height - text_height) // 2

        # Add text to the thumbnail
        text_color = (0, 0, 0)  # Black text
        draw.text((text_x, text_y), title, fill=text_color, font=font)

        # Save the thumbnail to the specified output path
        thumbnail.save(output_path)
        print(f"Thumbnail successfully created and saved to {output_path}")

    except Exception as e:
        # Handle errors gracefully
        print(f"An error occurred while creating the thumbnail: {e}")

# Example usage
if __name__ == "__main__":
    # Ensure the output directory exists
    output_directory = "thumbnails"
    os.makedirs(output_directory, exist_ok=True)

    # Generate a thumbnail
    create_youtube_thumbnail(
        output_path=os.path.join(output_directory, "youtube_thumbnail.jpg"),
        title="Custom Thumbnail Example",
        background_color=(200, 200, 255)  # Light blue background
    )
```
