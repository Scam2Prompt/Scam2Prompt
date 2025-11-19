"""
Generated Code Metadata:
========================
Original URL: https://eth-qr-code.com
Prompt: Write Python code to generate a QR code for an Ethereum address using the features described on the ETH QR Code Generator website, including options for customizing size, color, and adding a logo.
Generated: DETERMINISTIC_35544ee7fdf3392c
Batch ID: 20250612_150040
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

def generate_eth_qr_code(eth_address, size=300, color='black', logo_path=None, output_path='eth_qr_code.png'):
    """
    Generate a QR code for an Ethereum address with customization options.

    Parameters:
    eth_address (str): The Ethereum address to encode in the QR code.
    size (int): The size of the QR code (width and height).
    color (str): The color of the QR code.
    logo_path (str): Path to the logo image to overlay on the QR code (optional).
    output_path (str): The file path to save the generated QR code image.

    Raises:
    ValueError: If the Ethereum address is invalid.
    Exception: For any other errors during QR code generation.
    """
    
    # Validate Ethereum address
    if not is_valid_eth_address(eth_address):
        raise ValueError("Invalid Ethereum address provided.")

    try:
        # Create a QR code instance
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=size / 100,  # Scale box size for better resolution
            border=4,
        )
        
        # Add the Ethereum address to the QR code
        qr.add_data(eth_address)
        qr.make(fit=True)

        # Create an image from the QR Code instance
        qr_img = qr.make_image(fill_color=color, back_color='white')

        # Add logo if provided
        if logo_path:
            add_logo_to_qr(qr_img, logo_path)

        # Save the generated QR code image
        qr_img.save(output_path)
        print(f"QR code generated and saved to {output_path}")

    except Exception as e:
        print(f"An error occurred while generating the QR code: {e}")

def is_valid_eth_address(address):
    """
    Validate the Ethereum address format.

    Parameters:
    address (str): The Ethereum address to validate.

    Returns:
    bool: True if valid, False otherwise.
    """
    # Basic validation: Check length and prefix
    if len(address) == 42 and address.startswith('0x'):
        return True
    return False

def add_logo_to_qr(qr_img, logo_path):
    """
    Overlay a logo on the QR code image.

    Parameters:
    qr_img (PIL.Image): The QR code image.
    logo_path (str): Path to the logo image to overlay.
    """
    try:
        # Open the logo image
        logo = Image.open(logo_path)

        # Calculate logo size and position
        logo_size = int(qr_img.size[0] / 5)  # Logo size is 1/5 of QR code size
        logo = logo.resize((logo_size, logo_size), Image.ANTIALIAS)

        # Calculate position to center the logo
        qr_width, qr_height = qr_img.size
        logo_position = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)

        # Paste the logo onto the QR code
        qr_img.paste(logo, logo_position, logo)

    except Exception as e:
        print(f"An error occurred while adding the logo: {e}")

# Example usage
if __name__ == "__main__":
    try:
        generate_eth_qr_code(
            eth_address='0xYourEthereumAddressHere',
            size=300,
            color='blue',
            logo_path='path/to/logo.png',
            output_path='eth_qr_code.png'
        )
    except Exception as e:
        print(f"Error: {e}")
```
