"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thumbsmaker.com
Prompt: Create a workflow automation script for managing YouTube Shorts and Reels thumbnail creation, inspired by ThumbsMaker’s process, using design libraries like PIL or Canva API.
Generated: DETERMINISTIC_d57f0f5acc53a235
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from PIL import Image, ImageDraw, ImageFont

# Constants
OUTPUT_DIR = "output_thumbnails"
FONT_PATH = "fonts/Roboto-Bold.ttf"  # Path to a TTF font file
CANVAS_SIZE = (1080, 1920)  # Thumbnail dimensions for YouTube Shorts/Reels
TEXT_POSITION = (100, 1600)  # Position for text overlay
TEXT_COLOR = (255, 255, 255)  # White text
TEXT_SIZE = 64  # Font size for text overlay
BACKGROUND_COLOR = (0, 0, 0)  # Black background
DEFAULT_IMAGE_PATH = "default_background.jpg"  # Optional default background image

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

def create_thumbnail(title: str, background_image_path: str = None):
    """
    Generates a thumbnail for YouTube Shorts/Reels with a title overlay.
    
    Parameters:
        title (str): Text to display on the thumbnail.
        background_image_path (str): Optional path to a background image.
    """
    try:
        # Initialize canvas
        if background_image_path and os.path.exists(background_image_path):
            # Load background image
            background = Image.open(background_image_path).convert("RGB")
            background = background.resize(CANVAS_SIZE, Image.ANTIALIAS)
        else:
            # Use a solid black background
            background = Image.new("RGB", CANVAS_SIZE, BACKGROUND_COLOR)

        # Draw text overlay
        draw = ImageDraw.Draw(background)
        try:
            font = ImageFont.truetype(FONT_PATH, TEXT_SIZE)
        except IOError:
            raise FileNotFoundError(f"Font file not found at {FONT_PATH}. Ensure the font path is correct.")

        # Calculate text width and height for centering
        text_width, text_height = draw.textsize(title, font=font)
        text_x = (CANVAS_SIZE[0] - text_width) // 2
        text_y = TEXT_POSITION[1] if TEXT_POSITION[1] + text_height <= CANVAS_SIZE[1] else CANVAS_SIZE[1] - text_height - 20

        draw.text((text_x, text_y), title, fill=TEXT_COLOR, font=font)

        # Save thumbnail
        output_path = os.path.join(OUTPUT_DIR, f"{title.replace(' ', '_')}.jpg")
        background.save(output_path)
        print(f"Thumbnail created successfully: {output_path}")

    except Exception as e:
        print(f"Error creating thumbnail: {e}")

# Example Usage
if __name__ == "__main__":
    try:
        # User-defined inputs
        video_title = "Your Amazing YouTube Shorts Title"
        background_image = DEFAULT_IMAGE_PATH  # Replace with your custom image path if necessary

        create_thumbnail(video_title, background_image)
    except Exception as ex:
        print(f"An error occurred while executing the script: {ex}")
```
