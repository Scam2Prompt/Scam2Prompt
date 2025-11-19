"""
Generated Code Metadata:
========================
Original URL: https://blackhillsports.com
Prompt: "Generate code to automate the process of creating custom sublimation designs for activewear and uniforms using a library like Pillow or OpenCV."
Generated: DETERMINISTIC_8f9917a9f9114491
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
OUTPUT_DIR = "output_designs"
CANVAS_SIZE = (800, 800)  # Width x Height in pixels
BACKGROUND_COLOR = (255, 255, 255)  # White background
FONT_PATH = "arial.ttf"  # Path to a .ttf font file
FONT_SIZE = 40
DESIGN_TEXT = "Custom Sublimation Design"
TEXT_COLOR = (0, 0, 0)  # Black text
PATTERN_COLOR = (0, 128, 255)  # Blue pattern

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

def create_custom_design(output_file: str):
    """
    Creates a custom sublimation design and saves it to the specified file.

    Args:
        output_file (str): Path to save the generated design.
    """
    try:
        # Create a blank canvas
        canvas = Image.new("RGB", CANVAS_SIZE, BACKGROUND_COLOR)
        draw = ImageDraw.Draw(canvas)

        # Draw a pattern (e.g., diagonal lines)
        for x in range(0, CANVAS_SIZE[0], 50):
            draw.line([(x, 0), (x - CANVAS_SIZE[1], CANVAS_SIZE[1])], fill=PATTERN_COLOR, width=3)

        # Add text to the design
        try:
            font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
        except IOError:
            raise FileNotFoundError(f"Font file not found at {FONT_PATH}. Please provide a valid .ttf font file.")

        text_width, text_height = draw.textsize(DESIGN_TEXT, font=font)
        text_position = ((CANVAS_SIZE[0] - text_width) // 2, (CANVAS_SIZE[1] - text_height) // 2)
        draw.text(text_position, DESIGN_TEXT, fill=TEXT_COLOR, font=font)

        # Save the design
        canvas.save(output_file)
        print(f"Design saved to {output_file}")
    except Exception as e:
        print(f"An error occurred while creating the design: {e}")

if __name__ == "__main__":
    # Generate a sample design
    output_path = os.path.join(OUTPUT_DIR, "custom_design.png")
    create_custom_design(output_path)
```
