"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eth-qr-code.com
Prompt: Write Python code to generate a QR code for an Ethereum address using the features described on the ETH QR Code Generator website, including options for customizing size, color, and adding a logo.
Generated: DETERMINISTIC_35544ee7fdf3392c
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask
from PIL import Image
import os

def generate_eth_qr_code(
    eth_address, 
    output_file="eth_qr_code.png", 
    size=300, 
    color="black", 
    background_color="white", 
    logo_path=None
):
    """
    Generates a QR code for an Ethereum address with optional customization.
    
    Args:
        eth_address (str): Ethereum address to encode in the QR code.
        output_file (str): Path to save the generated QR code image.
        size (int): Size of the QR code (width/height in pixels).
        color (str): Foreground color of the QR code.
        background_color (str): Background color of the QR code.
        logo_path (str): Path to the logo image to embed at the center of the QR code (optional).
        
    Returns:
        None. The QR code is saved to the specified output file.
    """
    try:
        # Validate Ethereum address format (basic check)
        if not eth_address.startswith("0x") or len(eth_address) != 42:
            raise ValueError("Invalid Ethereum address format.")

        # Create QR code instance
        qr = qrcode.QRCode(
            version=1,  # Controls the size of the QR code
            error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction for logo embedding
            box_size=10,  # Size of each box in the QR code grid
            border=4,  # Border thickness around the QR code
        )
        qr.add_data(eth_address)
        qr.make(fit=True)

        # Customize QR code design
        img = qr.make_image(
            image_factory=StyledPilImage,
            module_drawer=RoundedModuleDrawer(),
            color_mask=SolidFillColorMask(back_color=background_color, front_color=color),
        )

        # Resize the QR code to the specified size
        img = img.resize((size, size), Image.ANTIALIAS)

        # Add logo if specified
        if logo_path and os.path.exists(logo_path):
            logo = Image.open(logo_path)

            # Adjust the logo size relative to the QR code size
            logo_size = size // 5  # Logo size is 1/5th of QR code size
            logo = logo.resize((logo_size, logo_size), Image.ANTIALIAS)

            # Calculate logo position
            logo_position = (
                (img.size[0] - logo.size[0]) // 2,
                (img.size[1] - logo.size[1]) // 2,
            )

            # Paste logo onto QR code
            img.paste(logo, logo_position, mask=logo)

        # Save the QR code image
        img.save(output_file)
        print(f"QR code successfully saved to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    eth_address = "0x1234567890abcdef1234567890abcdef12345678"
    generate_eth_qr_code(
        eth_address=eth_address,
        output_file="custom_eth_qr_code.png",
        size=400,
        color="blue",
        background_color="white",
        logo_path="logo.png"  # Replace with your logo file path
    )
```
