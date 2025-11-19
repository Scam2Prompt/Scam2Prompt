"""
Generated Code Metadata:
========================
Original URL: https://peoner.com
Prompt: Write a Python script to automate the process of generating custom embroidery designs for uniforms using a library like Pillow, considering the use of 8-head Tajima embroidery machines.
Generated: DETERMINISTIC_1312b11904b9d86d
Batch ID: 20250622_212440
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
OUTPUT_DIR = "embroidery_designs"
CANVAS_SIZE = (500, 500)  # Size of the design canvas (width, height)
FONT_PATH = "arial.ttf"  # Path to the font file
FONT_SIZE = 40  # Font size for text
DESIGN_COLOR = (0, 0, 0)  # Black color for the design
BACKGROUND_COLOR = (255, 255, 255)  # White background
MACHINE_HEADS = 8  # Number of embroidery machine heads

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

def create_embroidery_design(text, output_file):
    """
    Generates a custom embroidery design with the given text and saves it as an image.

    Args:
        text (str): The text to include in the embroidery design.
        output_file (str): The file path to save the generated design.
    """
    try:
        # Create a blank canvas
        image = Image.new("RGB", CANVAS_SIZE, BACKGROUND_COLOR)
        draw = ImageDraw.Draw(image)

        # Load font
        try:
            font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
        except IOError:
            raise FileNotFoundError(f"Font file not found at {FONT_PATH}. Please provide a valid font file.")

        # Calculate text position to center it
        text_width, text_height = draw.textsize(text, font=font)
        text_x = (CANVAS_SIZE[0] - text_width) // 2
        text_y = (CANVAS_SIZE[1] - text_height) // 2

        # Draw text on the canvas
        draw.text((text_x, text_y), text, fill=DESIGN_COLOR, font=font)

        # Save the design
        image.save(output_file)
        print(f"Embroidery design saved to {output_file}")
    except Exception as e:
        print(f"Error generating embroidery design: {e}")

def generate_designs_for_machine_heads(base_text):
    """
    Generates embroidery designs for all machine heads.

    Args:
        base_text (str): The base text to include in the designs.
    """
    for head in range(1, MACHINE_HEADS + 1):
        design_text = f"{base_text} - Head {head}"
        output_file = os.path.join(OUTPUT_DIR, f"design_head_{head}.png")
        create_embroidery_design(design_text, output_file)

if __name__ == "__main__":
    # Example usage
    base_text = "Company Logo"  # Replace with your desired text
    generate_designs_for_machine_heads(base_text)
```
