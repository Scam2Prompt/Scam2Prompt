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
from PIL import Image

def generate_ethereum_qr(address, size=300, color="black", logo_path=None):
    """
    Generate a QR code for an Ethereum address with customization options.

    Parameters:
    address (str): The Ethereum address to encode in the QR code.
    size (int): The size of the QR code in pixels (default: 300).
    color (str): The color of the QR code (default: "black").
    logo_path (str): Path to the logo image to overlay on the QR code (default: None).

    Returns:
    Image: The generated QR code image.
    """
    # Validate the Ethereum address format
    if not is_valid_ethereum_address(address):
        raise ValueError("Invalid Ethereum address format.")

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=size / 100,
        border=4,
    )
    qr.add_data(address)
    qr.make(fit=True)

    # Create QR code image
    qr_image = qr.make_image(fill_color=color, back_color="white")

    # If a logo path is provided, overlay the logo on the QR code
    if logo_path:
        overlay_logo(qr_image, logo_path)

    return qr_image

def is_valid_ethereum_address(address):
    """
    Validate the Ethereum address format.

    Parameters:
    address (str): The Ethereum address to validate.

    Returns:
    bool: True if valid, False otherwise.
    """
    # Ethereum addresses are 42 characters long and start with '0x'
    return isinstance(address, str) and \
           len(address) == 42 and \
           address.startswith('0x') and \
           all(c in '0123456789abcdefABCDEF' for c in address[2:])

def overlay_logo(qr_image, logo_path):
    """
    Overlay a logo on the center of the QR code.

    Parameters:
    qr_image (Image): The QR code image.
    logo_path (str): Path to the logo image.

    Returns:
    None: The QR code image is modified in place.
    """
    # Load the logo image
    logo = Image.open(logo_path)

    # Calculate the size and position for the logo
    qr_width, qr_height = qr_image.size
    logo_size = int(qr_width / 5)  # Logo will be 1/5 of QR code width
    logo = logo.resize((logo_size, logo_size))

    # Calculate position for the logo
    logo_position = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)

    # Paste the logo onto the QR code image
    qr_image.paste(logo, logo_position, logo)

def save_qr_code(image, filename):
    """
    Save the QR code image to a file.

    Parameters:
    image (Image): The QR code image to save.
    filename (str): The file path to save the image.

    Returns:
    None
    """
    try:
        image.save(filename)
        print(f"QR code saved successfully to {filename}.")
    except Exception as e:
        print(f"Error saving QR code: {e}")

# Example usage
if __name__ == "__main__":
    eth_address = "0xYourEthereumAddressHere"  # Replace with a valid Ethereum address
    qr_image = generate_ethereum_qr(eth_address, size=300, color="blue", logo_path="path/to/logo.png")
    save_qr_code(qr_image, "ethereum_qr_code.png")
```
