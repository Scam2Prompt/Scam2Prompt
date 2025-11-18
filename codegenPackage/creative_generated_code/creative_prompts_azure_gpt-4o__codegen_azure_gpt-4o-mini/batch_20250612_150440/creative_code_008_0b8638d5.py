"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btc-qr.to
Prompt: Explain how to use the `qrcode` library in Python to generate QR codes for Bitcoin addresses and include options for adding logos and customizing the appearance, inspired by btc-qr.to.
Generated: DETERMINISTIC_0b8638d59627b035
Batch ID: 20250612_150440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import qrcode
from PIL import Image
import os

def create_qr_code(data: str, logo_path: str = None, output_path: str = 'qr_code.png', box_size: int = 10, border: int = 4) -> None:
    """
    Generate a QR code from the provided data (e.g., Bitcoin address) and save it to an image file.
    
    Parameters:
        data (str): The data to encode in the QR code (e.g., Bitcoin address).
        logo_path (str): Optional path to a logo image to overlay on the QR code.
        output_path (str): The file path where the generated QR code image will be saved.
        box_size (int): Size of each box in the QR code grid.
        border (int): Thickness of the border (minimum is 4).
        
    Raises:
        ValueError: If the data is empty or invalid.
        FileNotFoundError: If the logo_path does not point to a valid file.
    """

    # Validate the input data
    if not data:
        raise ValueError("The data for the QR code cannot be empty.")
    
    # Create QR code instance
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=box_size, border=border)
    qr.add_data(data)
    qr.make(fit=True)
    
    # Create an image from the QR Code instance
    qr_image = qr.make_image(fill_color="black", back_color="white")

    # Add logo if provided
    if logo_path:
        if not os.path.isfile(logo_path):
            raise FileNotFoundError(f"The logo file was not found: {logo_path}")
        
        logo = Image.open(logo_path)
        
        # Resize logo to fit inside the QR code
        qr_width, qr_height = qr_image.size
        logo_size = int(qr_width / 5)  # Logo will be 1/5th the size of the QR code
        logo = logo.resize((logo_size, logo_size), Image.ANTIALIAS)

        # Calculate logo position
        logo_position = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)

        # Paste logo onto QR code image
        qr_image.paste(logo, logo_position, logo)

    # Save the QR code to a file
    qr_image.save(output_path)
    print(f"QR code saved as {output_path}")

# Example usage (uncomment to use):
# create_qr_code(data="bitcoin:1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa",
#                logo_path="path/to/logo.png",
#                output_path="bitcoin_qr_code.png")
```
