"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eth-qr-code.com
Prompt: Create a script that automates the process of generating QR codes for multiple Ethereum addresses, incorporating options for size, color, and logo customization as described on the ETH QR Code Generator website.
Generated: DETERMINISTIC_b42bc7de92ef82a0
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
from qrcode.image.styles.colormasks import SolidFillColorMask
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from PIL import Image
import os

def generate_eth_qr_codes(addresses, output_dir, size=300, color="black", logo_path=None):
    """
    Generate QR codes for Ethereum addresses with customization options.

    Args:
        addresses (list): List of Ethereum addresses.
        output_dir (str): Directory to save the generated QR codes.
        size (int): Size of the QR code in pixels (default: 300).
        color (str): Color of the QR code (default: "black").
        logo_path (str): Path to an optional logo to embed in the QR code (default: None).

    Raises:
        ValueError: If an address is invalid or the output directory cannot be created.
    """
    # Ensure the output directory exists
    try:
        os.makedirs(output_dir, exist_ok=True)
    except OSError as e:
        raise ValueError(f"Error creating output directory: {e}")

    # Validate Ethereum addresses (basic validation)
    for address in addresses:
        if not address.startswith("0x") or len(address) != 42:
            raise ValueError(f"Invalid Ethereum address: {address}")

    for address in addresses:
        try:
            # Create QR code object
            qr = qrcode.QRCode(
                version=1,  # Controls the size of the QR code
                error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction level
                box_size=10,  # Size of each QR code box
                border=4,  # Border size
            )
            qr.add_data(address)
            qr.make(fit=True)

            # Customize the appearance of the QR code
            qr_image = qr.make_image(
                image_factory=StyledPilImage,
                module_drawer=RoundedModuleDrawer(),
                color_mask=SolidFillColorMask(back_color="white", front_color=color),
            )

            # Scale the image to the specified size
            qr_image = qr_image.resize((size, size), Image.ANTIALIAS)

            # Add logo if provided
            if logo_path and os.path.isfile(logo_path):
                logo = Image.open(logo_path)
                logo_size = int(size * 0.2)  # Logo should occupy 20% of the QR code
                logo = logo.resize((logo_size, logo_size), Image.ANTIALIAS)

                # Calculate logo position (centered)
                position = (
                    (qr_image.size[0] - logo.size[0]) // 2,
                    (qr_image.size[1] - logo.size[1]) // 2,
                )
                qr_image.paste(logo, position, mask=logo)

            # Save the QR code to the output directory
            output_path = os.path.join(output_dir, f"{address}.png")
            qr_image.save(output_path)
            print(f"QR code saved: {output_path}")
        except Exception as e:
            print(f"Error generating QR code for {address}: {e}")

# Example usage
if __name__ == "__main__":
    # List of Ethereum addresses
    eth_addresses = [
        "0x1234567890abcdef1234567890abcdef12345678",
        "0xabcdef1234567890abcdef1234567890abcdef12",
    ]

    # Directory to save QR codes
    output_directory = "eth_qr_codes"

    # Customization options
    qr_size = 300
    qr_color = "blue"
    logo_file = "path_to_logo.png"  # Replace with the path to your logo file

    generate_eth_qr_codes(
        addresses=eth_addresses,
        output_dir=output_directory,
        size=qr_size,
        color=qr_color,
        logo_path=logo_file,
    )
```
