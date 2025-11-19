"""
Generated Code Metadata:
========================
Original URL: https://olaf-schirm.de
Prompt: Generate a Python script that creates a barcode clock using the Code128 format as described in Olaf Schirm's "TIME Code128" artwork.
Generated: DETERMINISTIC_3ba500e17cd14bae
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import barcode
from barcode.writer import ImageWriter
from PIL import Image, ImageDraw, ImageFont
import datetime
import argparse
import os

# Define the Code128 barcode format
def create_barcode_clock(output_filename, clock_text):
    """
    Generate a barcode clock image using Code128 format.

    Args:
        output_filename (str): The filename to save the barcode image.
        clock_text (str): The text to encode in the barcode.

    Returns:
        None
    """
    # Create a Code128 barcode object
    barcode_object = barcode.Code128(
        clock_text, 
        writer=ImageWriter(), 
        quiet_zone=20
    )

    # Save the barcode to a file
    barcode_object.save(output_filename)

def create_clock_image(output_filename, barcode_filename):
    """
    Create a clock image with the barcode.

    Args:
        output_filename (str): The filename to save the clock image.
        barcode_filename (str): The filename of the barcode image.

    Returns:
        None
    """
    # Open the barcode image
    barcode_image = Image.open(f"{barcode_filename}.png")

    # Create a new image for the clock
    clock_image = Image.new('RGB', (barcode_image.width, barcode_image.height + 100), color = (73, 109, 137))

    # Paste the barcode image onto the clock image
    clock_image.paste(barcode_image, (0, 50))

    # Add text to the clock image
    draw = ImageDraw.Draw(clock_image)
    font = ImageFont.load_default()
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    draw.text((10, 10), current_time, fill=(255, 255, 0), font=font)

    # Save the clock image
    clock_image.save(output_filename)

def main():
    parser = argparse.ArgumentParser(description='Generate a barcode clock image')
    parser.add_argument('-o', '--output', help='Output filename', required=True)
    args = parser.parse_args()

    # Get the current time
    current_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

    # Create a barcode
    barcode_filename = "barcode"
    create_barcode_clock(barcode_filename, current_time)

    # Create a clock image
    create_clock_image(args.output, barcode_filename)

    # Remove the barcode image
    os.remove(f"{barcode_filename}.png")

if __name__ == "__main__":
    main()
```
