"""
Generated Code Metadata:
========================
Original URL: https://btc-qr.to
Prompt: Explain how to use the `qrcode` library in Python to generate QR codes for Bitcoin addresses and include options for adding logos and customizing the appearance, inspired by btc-qr.to.
Generated: DETERMINISTIC_0b8638d59627b035
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
from PIL import Image
import os

def generate_qr_code(data, filename):
    """
    Generate a QR code with the provided data and save it to a file.

    Args:
        data (str): The data to encode in the QR code (e.g. a Bitcoin address).
        filename (str): The filename to save the QR code image to.
    """
    try:
        # Create a QR code instance
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

        # Add data to the QR code instance
        qr.add_data(data)
        qr.make(fit=True)

        # Create an image from the QR code instance
        img = qr.make_image(fill_color="black", back_color="white")

        # Save the image to a file
        img.save(filename)

        print(f"QR code saved to {filename}")

    except Exception as e:
        print(f"Error generating QR code: {e}")


def add_logo_to_qr_code(qr_code_filename, logo_filename, output_filename):
    """
    Add a logo to a QR code image.

    Args:
        qr_code_filename (str): The filename of the QR code image.
        logo_filename (str): The filename of the logo image.
        output_filename (str): The filename to save the output image to.
    """
    try:
        # Open the QR code and logo images
        qr_code_img = Image.open(qr_code_filename)
        logo_img = Image.open(logo_filename)

        # Calculate the position to place the logo
        pos = ((qr_code_img.size[0] - logo_img.size[0]) // 2, (qr_code_img.size[1] - logo_img.size[1]) // 2)

        # Paste the logo onto the QR code
        qr_code_img.paste(logo_img, pos, mask=logo_img)

        # Save the output image
        qr_code_img.save(output_filename)

        print(f"QR code with logo saved to {output_filename}")

    except Exception as e:
        print(f"Error adding logo to QR code: {e}")


def customize_qr_code_appearance(qr_code_filename, output_filename, fill_color, back_color):
    """
    Customize the appearance of a QR code image.

    Args:
        qr_code_filename (str): The filename of the QR code image.
        output_filename (str): The filename to save the output image to.
        fill_color (str): The fill color of the QR code.
        back_color (str): The background color of the QR code.
    """
    try:
        # Open the QR code image
        qr_code_img = Image.open(qr_code_filename)

        # Convert the image to RGB mode
        qr_code_img = qr_code_img.convert('RGB')

        # Load the pixel data
        pixels = qr_code_img.load()

        # Iterate over the pixels and change the colors
        for x in range(qr_code_img.size[0]):
            for y in range(qr_code_img.size[1]):
                if pixels[x, y] == (0, 0, 0):  # Black
                    pixels[x, y] = (int(fill_color[1:3], 16), int(fill_color[3:5], 16), int(fill_color[5:7], 16))
                elif pixels[x, y] == (255, 255, 255):  # White
                    pixels[x, y] = (int(back_color[1:3], 16), int(back_color[3:5], 16), int(back_color[5:7], 16))

        # Save the output image
        qr_code_img.save(output_filename)

        print(f"Customized QR code saved to {output_filename}")

    except Exception as e:
        print(f"Error customizing QR code appearance: {e}")


if __name__ == "__main__":
    bitcoin_address = "your_bitcoin_address_here"
    qr_code_filename = "qr_code.png"
    logo_filename = "logo.png"
    output_filename = "output.png"

    generate_qr_code(bitcoin_address, qr_code_filename)
    add_logo_to_qr_code(qr_code_filename, logo_filename, output_filename)

    # Customize the appearance of the QR code
    fill_color = "#008000"  # Green
    back_color = "#FFFFFF"  # White
    customized_output_filename = "customized_output.png"
    customize_qr_code_appearance(qr_code_filename, customized_output_filename, fill_color, back_color)
```
