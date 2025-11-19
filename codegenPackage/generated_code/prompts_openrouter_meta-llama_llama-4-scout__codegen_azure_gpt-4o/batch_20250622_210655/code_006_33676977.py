"""
Generated Code Metadata:
========================
Original URL: https://thumbsmaker.com
Prompt: Generate a portfolio of 5 different YouTube thumbnail designs for a beauty and cosmetics channel, using ThumbsMaker's design style and attention to detail.
Generated: DETERMINISTIC_33676977be9d04dc
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from PIL import Image, ImageDraw, ImageFont

def create_thumbnail(title, subtitle, bg_color, text_color, output_path):
    """
    Creates a YouTube thumbnail with the given parameters.

    Args:
        title (str): The main title text for the thumbnail.
        subtitle (str): The subtitle text for the thumbnail.
        bg_color (tuple): Background color in RGB format (e.g., (255, 255, 255)).
        text_color (tuple): Text color in RGB format (e.g., (0, 0, 0)).
        output_path (str): Path to save the generated thumbnail image.

    Returns:
        None
    """
    try:
        # Thumbnail dimensions (1280x720 is standard for YouTube)
        width, height = 1280, 720

        # Create a blank image with the specified background color
        thumbnail = Image.new("RGB", (width, height), bg_color)

        # Initialize drawing context
        draw = ImageDraw.Draw(thumbnail)

        # Load fonts (ensure the font file exists in the working directory)
        title_font = ImageFont.truetype("arial.ttf", 80)  # Adjust font size as needed
        subtitle_font = ImageFont.truetype("arial.ttf", 40)

        # Calculate text positions
        title_width, title_height = draw.textsize(title, font=title_font)
        subtitle_width, subtitle_height = draw.textsize(subtitle, font=subtitle_font)

        title_position = ((width - title_width) // 2, (height - title_height) // 3)
        subtitle_position = ((width - subtitle_width) // 2, (height - subtitle_height) // 2 + 100)

        # Draw text on the thumbnail
        draw.text(title_position, title, font=title_font, fill=text_color)
        draw.text(subtitle_position, subtitle, font=subtitle_font, fill=text_color)

        # Save the thumbnail
        thumbnail.save(output_path)
        print(f"Thumbnail saved at: {output_path}")

    except Exception as e:
        print(f"Error creating thumbnail: {e}")

def generate_portfolio():
    """
    Generates a portfolio of 5 YouTube thumbnails for a beauty and cosmetics channel.

    Returns:
        None
    """
    # Define thumbnail details
    thumbnails = [
        {"title": "Top 10 Lipsticks", "subtitle": "Must-Have Shades!", "bg_color": (255, 182, 193), "text_color": (0, 0, 0), "output_path": "thumbnail1.jpg"},
        {"title": "Skincare Secrets", "subtitle": "Glow Like Never Before", "bg_color": (135, 206, 250), "text_color": (0, 0, 0), "output_path": "thumbnail2.jpg"},
        {"title": "Makeup Hacks", "subtitle": "Save Time & Money", "bg_color": (255, 228, 181), "text_color": (0, 0, 0), "output_path": "thumbnail3.jpg"},
        {"title": "Haircare Tips", "subtitle": "Healthy & Shiny Hair", "bg_color": (144, 238, 144), "text_color": (0, 0, 0), "output_path": "thumbnail4.jpg"},
        {"title": "Nail Art Designs", "subtitle": "Trendy & Chic", "bg_color": (221, 160, 221), "text_color": (0, 0, 0), "output_path": "thumbnail5.jpg"},
    ]

    # Create thumbnails
    for thumbnail in thumbnails:
        create_thumbnail(
            title=thumbnail["title"],
            subtitle=thumbnail["subtitle"],
            bg_color=thumbnail["bg_color"],
            text_color=thumbnail["text_color"],
            output_path=thumbnail["output_path"]
        )

if __name__ == "__main__":
    # Ensure the script runs only when executed directly
    generate_portfolio()
```

**Note:** Ensure that the `arial.ttf` font file is available in your working directory or replace it with a path to a valid font file on your system. Install the `Pillow` library (`pip install pillow`) if not already installed.
