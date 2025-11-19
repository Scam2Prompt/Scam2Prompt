"""
Generated Code Metadata:
========================
Original URL: https://btc-qr.to
Prompt: Write a Python script to generate a QR code for a Bitcoin address using a library like `qrcode`. Include options to customize the color, size, and add a logo, similar to the features described on btc-qr.to.
Generated: DETERMINISTIC_d916342aa9a22703
Batch ID: 20250612_150440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import GappedSquareModuleDrawer, HorizontalBarsDrawer, VerticalBarsDrawer
from PIL import Image
import argparse
import os

def generate_qr_code(
    bitcoin_address: str, 
    output_file: str, 
    color: str = "#000000", 
    background_color: str = "#FFFFFF", 
    size: int = 200, 
    logo: str = None
):
    """
    Generate a QR code for a Bitcoin address.

    Args:
        bitcoin_address (str): The Bitcoin address to encode.
        output_file (str): The file path to save the QR code.
        color (str, optional): The color of the QR code. Defaults to "#000000".
        background_color (str, optional): The background color of the QR code. Defaults to "#FFFFFF".
        size (int, optional): The size of the QR code in pixels. Defaults to 200.
        logo (str, optional): The file path to a logo image. Defaults to None.
    """

    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=size // 21,
        border=4,
    )

    # Add data to the QR code instance
    qr.add_data(bitcoin_address)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img_1 = qr.make_image(fill_color=color, back_color=background_color)

    # Apply a style to the QR code
    # Uncomment to use a style
    # drawer = GappedSquareModuleDrawer()
    # img_1 = qr.make_image(image_factory=StyledPilImage, module_drawer=drawer, fill_color=color, back_color=background_color)

    if logo:
        # Check if logo file exists
        if not os.path.exists(logo):
            raise FileNotFoundError(f"Logo file '{logo}' not found.")

        # Open the logo image
        img_2 = Image.open(logo)

        # Calculate the position to paste the logo
        pos = ((img_1.size[0] - img_2.size[0]) // 2, (img_1.size[1] - img_2.size[1]) // 2)

        # Paste the logo onto the QR code
        img_1.paste(img_2, pos)

    # Save the image to a file
    img_1.save(output_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a QR code for a Bitcoin address.")
    parser.add_argument("bitcoin_address", help="The Bitcoin address to encode.")
    parser.add_argument("-o", "--output", help="The file path to save the QR code.", required=True)
    parser.add_argument("-c", "--color", help="The color of the QR code.", default="#000000")
    parser.add_argument("-b", "--background_color", help="The background color of the QR code.", default="#FFFFFF")
    parser.add_argument("-s", "--size", help="The size of the QR code in pixels.", type=int, default=200)
    parser.add_argument("-l", "--logo", help="The file path to a logo image.")
    args = parser.parse_args()

    try:
        generate_qr_code(
            args.bitcoin_address, 
            args.output, 
            args.color, 
            args.background_color, 
            args.size, 
            args.logo
        )
    except Exception as e:
        print(f"An error occurred: {e}")
```
