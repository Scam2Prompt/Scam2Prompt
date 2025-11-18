"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eth-qr-code.com
Prompt: Write code to generate a QR code for an Ethereum address and export it as an image file, with options for customizing appearance as described on the ETH QR Code Generator website.
Generated: DETERMINISTIC_169e550d0be5a0ff
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
from PIL import Image
import os

def generate_eth_qr_code(eth_address, output_file, logo_path=None, border=4, fill_color="black", back_color="white"):
    """
    Generate a QR code for an Ethereum address and export it as an image file.

    :param eth_address: str - The Ethereum address to encode in the QR code.
    :param output_file: str - The path where the QR code image will be saved.
    :param logo_path: str or None - Optional path to a logo image to overlay on the QR code.
    :param border: int - Size of the border (minimum is 4).
    :param fill_color: str - Color of the QR code modules.
    :param back_color: str - Background color of the QR code.
    :raises ValueError: If the Ethereum address is invalid or output path is not writable.
    """
    
    # Validate Ethereum address (basic check)
    if not isinstance(eth_address, str) or len(eth_address) != 42 or not eth_address.startswith('0x'):
        raise ValueError("Invalid Ethereum address provided. It should start with '0x' and be 42 characters long.")
    
    # Create a QR Code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=border,
    )
    
    # Add the Ethereum address to the QR code
    qr.add_data(eth_address)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color=fill_color, back_color=back_color)

    # Overlay logo if provided
    if logo_path and os.path.exists(logo_path):
        try:
            logo = Image.open(logo_path)
            logo_size = 60  # Size of the logo
            logo = logo.resize((logo_size, logo_size))
            qr_width, qr_height = img.size
            logo_position = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)
            img.paste(logo, logo_position, logo)

        except Exception as e:
            raise RuntimeError(f"Error while processing logo: {str(e)}")

    # Save the generated QR code to the specified file
    try:
        img.save(output_file)
    except Exception as e:
        raise IOError(f"Unable to save QR code image to {output_file}: {str(e)}")

# Example usage:
# generate_eth_qr_code(
#     eth_address='0xYourEthereumAddressHere',
#     output_file='eth_qr_code.png',
#     logo_path='path_to_logo.png',
#     border=4,
#     fill_color='black',
#     back_color='white'
# )
```

In this code, ensure to replace `'0xYourEthereumAddressHere'` and `'path_to_logo.png'` with actual values when executing the function.
