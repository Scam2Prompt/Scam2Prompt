"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alpha-digitalsolutions.com
Prompt: Write a Python script to automate the generation of social media ad designs, inspired by Alpha Digital Solutions' graphic design services.
Generated: DETERMINISTIC_d84cb5c32998f016
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
OUTPUT_DIR = "social_media_ads"
CANVAS_SIZE = (1080, 1080)  # Dimensions for the ad design (square)
BACKGROUND_COLOR = (255, 255, 255)  # White background
FONT_PATH = "arial.ttf"  # Path to the font file (replace with your desired font)
FONT_SIZE = 50
DEFAULT_MESSAGE = "Your Brand Here"
LOGO_PATH = "logo.png"  # Path to the logo file
OUTPUT_FORMAT = "PNG"

# Error handling for missing dependencies or files
if not os.path.exists(FONT_PATH):
    raise FileNotFoundError(f"Font file not found at '{FONT_PATH}'. Please provide a valid font path.")

if not os.path.exists(LOGO_PATH):
    raise FileNotFoundError(f"Logo file not found at '{LOGO_PATH}'. Please provide a valid logo path.")

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

def create_social_media_ad(message, output_filename):
    """
    Generates a social media ad design with the given message and saves it as a file.
    
    Args:
        message (str): The message to display on the ad.
        output_filename (str): The name of the output file (without extension).
    """
    # Create a blank canvas
    img = Image.new("RGB", CANVAS_SIZE, BACKGROUND_COLOR)
    draw = ImageDraw.Draw(img)
    
    # Load font
    try:
        font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
    except Exception as e:
        raise RuntimeError(f"Failed to load font: {e}")
    
    # Add text
    text_width, text_height = draw.textsize(message, font=font)
    text_position = ((CANVAS_SIZE[0] - text_width) // 2, (CANVAS_SIZE[1] - text_height) // 2)
    draw.text(text_position, message, fill=(0, 0, 0), font=font)
    
    # Add logo
    try:
        logo = Image.open(LOGO_PATH).convert("RGBA")
        logo.thumbnail((200, 200))  # Resize logo
        logo_position = (CANVAS_SIZE[0] - logo.width - 20, CANVAS_SIZE[1] - logo.height - 20)  # Bottom-right corner
        img.paste(logo, logo_position, logo)
    except Exception as e:
        raise RuntimeError(f"Failed to process logo: {e}")
    
    # Save the final design
    output_path = os.path.join(OUTPUT_DIR, f"{output_filename}.{OUTPUT_FORMAT.lower()}")
    img.save(output_path, OUTPUT_FORMAT)
    print(f"Ad saved to: {output_path}")


# Main function
def main():
    """
    Entry point of the script. Generates a sample ad design.
    """
    try:
        sample_message = DEFAULT_MESSAGE
        sample_output_filename = "sample_ad"
        
        print("Generating social media ad...")
        create_social_media_ad(sample_message, sample_output_filename)
        print("Ad generation complete.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
