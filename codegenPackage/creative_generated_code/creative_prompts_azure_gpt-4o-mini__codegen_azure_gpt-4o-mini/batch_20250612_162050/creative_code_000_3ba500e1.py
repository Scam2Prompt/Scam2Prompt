"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://olaf-schirm.de
Prompt: Generate a Python script that creates a barcode clock using the Code128 format as described in Olaf Schirm's "TIME Code128" artwork.
Generated: DETERMINISTIC_3ba500e17cd14bae
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import barcode
from barcode.writer import ImageWriter
from PIL import Image, ImageDraw, ImageFont
import os

# Constants
FONT_PATH = "arial.ttf"  # Path to TTF font file for drawing text
BARCODE_FORMAT = 'code128'  # Barcode format
OUTPUT_DIR = 'barcodes'  # Directory to save barcode images
BATCH_SIZE = 60  # Number of barcodes to generate every minute

# Create the output directory if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_barcode(data: str, filename: str) -> None:
    """
    Generates a barcode image and saves it to a file.

    :param data: The data to encode in the barcode
    :param filename: The filename to save the barcode image as
    """
    try:
        # Create barcode
        code = barcode.get(BARCODE_FORMAT, data, writer=ImageWriter())
        # Save barcode image
        code.save(os.path.join(OUTPUT_DIR, filename))
    except Exception as e:
        print(f"Error generating barcode for {data}: {e}")

def draw_time_on_image(time_string: str, filename: str) -> None:
    """
    Draws the current time on a barcode image.

    :param time_string: The time string to draw on the image
    :param filename: The filename of the barcode image to modify
    """
    try:
        # Open the barcode image
        with Image.open(os.path.join(OUTPUT_DIR, filename)) as img:
            draw = ImageDraw.Draw(img)

            # Define font size and position
            font_size = 20
            font = ImageFont.truetype(FONT_PATH, font_size)
            text_width, text_height = draw.textsize(time_string, font=font)
            position = ((img.width - text_width) // 2, img.height - text_height - 10)

            # Draw the time on the image
            draw.text(position, time_string, fill="black", font=font)

            # Save the modified image
            img.save(os.path.join(OUTPUT_DIR, filename))
    except Exception as e:
        print(f"Error drawing time on image {filename}: {e}")

def create_barcode_clock() -> None:
    """
    Main function to create a barcode clock that generates barcodes every minute.
    """
    while True:
        # Get the current time
        current_time = time.strftime("%H:%M")
        barcode_data = f"T{current_time}"  # Prefix with 'T' as per the artwork specification
        barcode_filename = f"barcode_{current_time}.png"

        # Generate and save the barcode
        generate_barcode(barcode_data, barcode_filename)

        # Draw the current time on the barcode image
        draw_time_on_image(current_time, barcode_filename)

        # Wait until the next minute
        time.sleep(BATCH_SIZE)

if __name__ == "__main__":
    create_barcode_clock()
```

Make sure to have the necessary libraries installed before running the code:

```bash
pip install python-barcode pillow
```

Also, ensure that the `arial.ttf` font file is available in your working directory or adjust the `FONT_PATH` accordingly.
