"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://demirsoft.com
Prompt: Write code to generate custom barcode labels for a clothing store using DemirSoft's "Tekstil & Giyim Barkod Etiket Yazıcılar."
Generated: DETERMINISTIC_b5d81ecbc8402700
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script generates custom barcode labels for a clothing store using DemirSoft's 
"Tekstil & Giyim Barkod Etiket Yazıcılar" system. Ensure that you have installed 
the necessary barcode libraries and printer drivers for DemirSoft's system.

Dependencies:
- barcode (Python library for barcode generation)
- Pillow (Python Imaging Library for image manipulation)
"""

import os
from barcode import Code128
from barcode.writer import ImageWriter
from PIL import Image, ImageDraw, ImageFont

def generate_barcode_label(product_name, product_code, price, save_path):
    """
    Generates a custom barcode label with product details and saves it as an image.

    Args:
        product_name (str): Name of the product.
        product_code (str): Unique product code for barcode generation.
        price (float): Price of the product.
        save_path (str): Path to save the generated label image.

    Raises:
        ValueError: If any of the arguments are invalid.
        Exception: For other unexpected errors during barcode generation or saving.
    """
    try:
        # Validate inputs
        if not product_name or not product_code or price <= 0 or not save_path:
            raise ValueError("Invalid inputs provided for barcode label generation.")

        # Generate the barcode image
        barcode = Code128(product_code, writer=ImageWriter())
        barcode_image_path = os.path.join(save_path, f"{product_code}_barcode.png")
        barcode.save(barcode_image_path)

        # Open the barcode image
        barcode_img = Image.open(barcode_image_path)

        # Create a blank label image
        label_width = barcode_img.width
        label_height = barcode_img.height + 100  # Add extra space for text
        label_img = Image.new("RGB", (label_width, label_height), "white")
        draw = ImageDraw.Draw(label_img)

        # Paste the barcode image onto the label
        label_img.paste(barcode_img, (0, 0))

        # Load a font (requires PIL's ImageFont library)
        font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # Adjust font path as needed
        font = ImageFont.truetype(font_path, 20)

        # Add product details below the barcode
        text_y_position = barcode_img.height + 10
        draw.text((10, text_y_position), f"Product: {product_name}", fill="black", font=font)
        draw.text((10, text_y_position + 30), f"Code: {product_code}", fill="black", font=font)
        draw.text((10, text_y_position + 60), f"Price: ${price:.2f}", fill="black", font=font)

        # Save the final label image
        final_label_path = os.path.join(save_path, f"{product_code}_label.png")
        label_img.save(final_label_path)
        print(f"Barcode label generated and saved to: {final_label_path}")

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except FileNotFoundError:
        print("Font file not found. Ensure the specified font path is correct.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
if __name__ == "__main__":
    # User-provided data
    product_name = "Winter Jacket"
    product_code = "WJ12345"
    price = 129.99
    save_path = "./labels"

    # Ensure the save directory exists
    os.makedirs(save_path, exist_ok=True)

    # Generate the barcode label
    generate_barcode_label(product_name, product_code, price, save_path)
```
