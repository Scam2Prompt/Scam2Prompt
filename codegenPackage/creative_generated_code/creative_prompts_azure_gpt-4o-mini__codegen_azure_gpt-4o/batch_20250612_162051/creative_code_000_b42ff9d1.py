"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thoinayadv.com
Prompt: Generate a Python script to create custom metallic logo stickers using the specifications provided by Jttlogos, including options for Nickel Metal and Stainless Steel materials.
Generated: DETERMINISTIC_b42ff9d1cf75b158
Batch ID: 20250612_162051
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

# Constants for materials
NICKEL_COLOR = (169, 169, 169)  # RGB color for Nickel (grayish tone)
STAINLESS_COLOR = (192, 192, 192)  # RGB color for Stainless Steel (light gray)

# Default specifications
DEFAULT_WIDTH = 800  # in pixels
DEFAULT_HEIGHT = 600  # in pixels
DEFAULT_FONT_SIZE = 100
DEFAULT_FONT = "arial.ttf"  # Path to a font file (ensure it's available on your system)
OUTPUT_DIR = "output_stickers"

# Function to create metallic logo stickers
def create_metallic_logo(text, material, width=DEFAULT_WIDTH, height=DEFAULT_HEIGHT):
    """
    Create a metallic logo sticker based on the given specifications.

    Parameters:
    - text (str): Text to display on the sticker.
    - material (str): Either 'Nickel' or 'Stainless Steel'.
    - width (int): Width of the sticker in pixels.
    - height (int): Height of the sticker in pixels.

    Returns:
    - str: Path to the generated sticker image file.
    """
    # Validate material
    if material not in ["Nickel", "Stainless Steel"]:
        raise ValueError("Material must be either 'Nickel' or 'Stainless Steel'.")
    
    # Determine background color based on material
    background_color = NICKEL_COLOR if material == "Nickel" else STAINLESS_COLOR
    
    # Create a blank image with the specified dimensions and background color
    sticker = Image.new("RGB", (width, height), background_color)
    draw = ImageDraw.Draw(sticker)
    
    # Load font
    try:
        font = ImageFont.truetype(DEFAULT_FONT, DEFAULT_FONT_SIZE)
    except OSError:
        raise FileNotFoundError(f"Font file '{DEFAULT_FONT}' not found. Ensure the font exists.")
    
    # Calculate text size and position
    text_width, text_height = draw.textsize(text, font=font)
    text_x = (width - text_width) // 2
    text_y = (height - text_height) // 2
    
    # Draw the text on the image
    draw.text((text_x, text_y), text, fill="black", font=font)
    
    # Ensure output directory exists
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    
    # Save the sticker image
    file_name = f"{material.lower()}_logo_{text.replace(' ', '_')}.png"
    file_path = os.path.join(OUTPUT_DIR, file_name)
    sticker.save(file_path)
    
    return file_path

# Example usage
if __name__ == "__main__":
    try:
        # Generate stickers for demonstration purposes
        logo_text = "Jttlogos"
        nickel_sticker = create_metallic_logo(logo_text, "Nickel")
        print(f"Nickel sticker created at: {nickel_sticker}")
        
        stainless_sticker = create_metallic_logo(logo_text, "Stainless Steel")
        print(f"Stainless Steel sticker created at: {stainless_sticker}")
    
    except Exception as e:
        print(f"An error occurred: {e}")
```
