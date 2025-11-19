"""
Generated Code Metadata:
========================
Original URL: https://blackhillsports.com
Prompt: "Write a script to generate high-quality images of custom apparel products with embroidered or printed designs, using a library like ImageMagick or GraphicsMagick."
Generated: DETERMINISTIC_6e81b24742a80ee4
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

# Constants
OUTPUT_DIR = "output_images"
APPAREL_TEMPLATE = "apparel_template.png"  # Path to the base apparel template image
DESIGN_IMAGE = "design.png"  # Path to the design image (embroidered or printed)
FONT_PATH = "arial.ttf"  # Path to a font file for text overlay
TEXT_OVERLAY = "Custom Apparel"  # Text to overlay on the image
TEXT_POSITION = (50, 50)  # Position of the text overlay
TEXT_COLOR = (255, 255, 255)  # Color of the text overlay (white)
TEXT_SIZE = 40  # Font size for the text overlay

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_custom_apparel_image(template_path, design_path, output_path, text_overlay=None):
    """
    Generates a high-quality image of custom apparel with a design overlay.

    Args:
        template_path (str): Path to the base apparel template image.
        design_path (str): Path to the design image (embroidered or printed).
        output_path (str): Path to save the generated image.
        text_overlay (str, optional): Text to overlay on the image. Defaults to None.

    Raises:
        FileNotFoundError: If the template or design image is not found.
    """
    try:
        # Load the template image
        template = Image.open(template_path).convert("RGBA")
        
        # Load the design image
        design = Image.open(design_path).convert("RGBA")
        
        # Resize the design to fit the template (adjust as needed)
        design = design.resize((200, 200))  # Example size, adjust based on template
        
        # Paste the design onto the template
        template.paste(design, (100, 100), design)  # Position (100, 100) is an example
        
        # Add text overlay if provided
        if text_overlay:
            draw = ImageDraw.Draw(template)
            font = ImageFont.truetype(FONT_PATH, TEXT_SIZE)
            draw.text(TEXT_POSITION, text_overlay, fill=TEXT_COLOR, font=font)
        
        # Save the final image
        template.save(output_path, "PNG")
        print(f"Image saved successfully: {output_path}")
    
    except FileNotFoundError as e:
        print(f"Error: {e}. Please ensure the file paths are correct.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    output_file = os.path.join(OUTPUT_DIR, "custom_apparel.png")
    generate_custom_apparel_image(APPAREL_TEMPLATE, DESIGN_IMAGE, output_file, TEXT_OVERLAY)
```

### Notes:
- This script uses the `Pillow` library (a fork of PIL) for image manipulation. Ensure you have it installed (`pip install pillow`).
- Replace the constants (`APPAREL_TEMPLATE`, `DESIGN_IMAGE`, `FONT_PATH`, etc.) with actual file paths and values relevant to your use case.
- Adjust the design resizing and positioning logic based on your specific requirements.
