"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sdbondindia.com
Prompt: Suggest libraries or tools for creating halo-lit signs and demonstrate their use with example code that matches SD BOND India's offerings.
Generated: DETERMINISTIC_f8ede00ec2e72e8d
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# halo_lit_sign.py

"""
This module demonstrates the creation of halo-lit signs that match SD BOND India's offerings.
For this purpose, we'll use the Pillow library for image creation and manipulation.
Make sure to install the Pillow library: pip install Pillow
"""

from PIL import Image, ImageDraw, ImageFont
import os

# Define constants for sign dimensions and colors
SIGN_WIDTH = 800
SIGN_HEIGHT = 400
BACKGROUND_COLOR = (0, 0, 0)  # Black background
TEXT_COLOR = (255, 255, 255)  # White text
HALO_COLOR = (255, 223, 0)     # Halo color (Yellow)
HALO_RADIUS = 20               # Radius of the halo effect

def create_halo_lit_sign(text, output_file='halo_lit_sign.png'):
    """
    Create a halo-lit sign with the specified text.
    
    Parameters:
    text (str): The text to display on the sign.
    output_file (str): The filename for the generated image.
    
    Returns:
    str: The path to the generated image file.
    """
    try:
        # Create a blank image with a black background
        img = Image.new('RGBA', (SIGN_WIDTH, SIGN_HEIGHT), BACKGROUND_COLOR)
        draw = ImageDraw.Draw(img)

        # Load a font
        font_path = "arial.ttf"  # Ensure the font file is in the same directory or provide an absolute path
        if not os.path.exists(font_path):
            raise FileNotFoundError(f"Font file '{font_path}' not found.")

        font_size = 80
        font = ImageFont.truetype(font_path, font_size)

        # Calculate text size and position
        text_size = draw.textsize(text, font=font)
        text_x = (SIGN_WIDTH - text_size[0]) // 2
        text_y = (SIGN_HEIGHT - text_size[1]) // 2

        # Draw halo effect by creating multiple overlapping text in halo color
        for i in range(HALO_RADIUS):
            draw.text((text_x - i, text_y - i), text, font=font, fill=HALO_COLOR)
            draw.text((text_x + i, text_y - i), text, font=font, fill=HALO_COLOR)
            draw.text((text_x - i, text_y + i), text, font=font, fill=HALO_COLOR)
            draw.text((text_x + i, text_y + i), text, font=font, fill=HALO_COLOR)

        # Draw the main text in white
        draw.text((text_x, text_y), text, font=font, fill=TEXT_COLOR)

        # Save the generated image
        img.save(output_file)
        return output_file

    except Exception as e:
        print(f"An error occurred while creating the halo-lit sign: {e}")
        return None

if __name__ == "__main__":
    # Example usage
    sign_text = "Welcome to SD BOND India"
    output_path = create_halo_lit_sign(sign_text)
    
    if output_path:
        print(f"Halo-lit sign created successfully: {output_path}")
    else:
        print("Failed to create halo-lit sign.")
```

**Note:** Ensure that you have the `arial.ttf` font file available in your working directory or adjust the path accordingly.
