"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fantom.de
Prompt: Create a Python script to automate the process of designing print media layouts, referencing Fantom Internet Dienst's print media services.
Generated: DETERMINISTIC_228d652300ed9762
Batch ID: 20250612_150040
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

# Constants for layout dimensions
PAGE_WIDTH = 2100       # Width in pixels (A4 size at 300 DPI)
PAGE_HEIGHT = 2970      # Height in pixels (A4 size at 300 DPI)
BACKGROUND_COLOR = (255, 255, 255)  # White background
FONT_COLOR = (0, 0, 0)  # Black font color

# Initialize font (path to a .ttf should be updated as per your environment)
FONT_PATH = "arial.ttf"
FONT_SIZE = 48

def create_layout(title, content, output_path):
    """
    Creates a print media layout with a title and content.
    
    Parameters:
    title (str): The title of the print media.
    content (str): The main content of the print media.
    output_path (str): The path where the generated layout image will be saved.
    
    Raises:
    ValueError: If title or content is empty.
    IOError: If there is an error saving the output image.
    """
    if not title or not content:
        raise ValueError("Title and content must be non-empty strings.")

    # Create a blank image for the layout
    layout_image = Image.new("RGB", (PAGE_WIDTH, PAGE_HEIGHT), BACKGROUND_COLOR)
    draw = ImageDraw.Draw(layout_image)

    # Load the font
    try:
        font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
    except IOError:
        raise IOError(f"Font file not found: {FONT_PATH}")

    # Draw the title
    title_width, title_height = draw.textsize(title, font=font)
    draw.text(((PAGE_WIDTH - title_width) / 2, 100), title, fill=FONT_COLOR, font=font)

    # Draw the content
    content_y_position = 200 + title_height
    for line in content.split('\n'):
        draw.text((100, content_y_position), line, fill=FONT_COLOR, font=font)
        content_y_position += font.getsize(line)[1]  # Move down for the next line

    # Save the resulting layout image
    try:
        layout_image.save(output_path)
        print(f"Layout saved successfully at {output_path}")
    except IOError as e:
        raise IOError(f"Failed to save the image: {str(e)}")

def main():
    """
    Main function to run the layout creation script.
    """
    # Sample title and content
    title = "Fantom Internet Dienst Print Media"
    content = "Enhance your business visibility with professional print media services.\n\nContact us for more details."
    
    output_path = "print_media_layout.png"

    try:
        create_layout(title, content, output_path)
    except (ValueError, IOError) as e:
        print(f"Error encountered: {str(e)}")

if __name__ == "__main__":
    main()
```
