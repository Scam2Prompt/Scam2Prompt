"""
Generated Code Metadata:
========================
Original URL: https://eth-qr-code.com
Prompt: Generate a QR code for an Ethereum address using a Python library, incorporating a company logo and customizable size and color.
Generated: DETERMINISTIC_8a1c553d52bc7285
Batch ID: 20250622_205030
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

def generate_qr_code_with_logo(ethereum_address, logo_path, output_path, size=300, color='black'):
    """
    Generate a QR code for an Ethereum address with a company logo.

    Parameters:
    - ethereum_address (str): The Ethereum address to encode in the QR code.
    - logo_path (str): The file path to the logo image.
    - output_path (str): The file path to save the generated QR code image.
    - size (int): The size of the QR code (default is 300).
    - color (str): The color of the QR code (default is 'black').

    Raises:
    - ValueError: If the Ethereum address is invalid or if the logo path is invalid.
    - IOError: If there is an issue saving the output image.
    """

    # Validate Ethereum address (basic validation)
    if not isinstance(ethereum_address, str) or len(ethereum_address) != 42 or not ethereum_address.startswith('0x'):
        raise ValueError("Invalid Ethereum address. It must be a 42-character string starting with '0x'.")

    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    # Add the Ethereum address to the QR code
    qr.add_data(ethereum_address)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    qr_image = qr.make_image(fill_color=color, back_color='white')

    # Load the logo image
    try:
        logo = Image.open(logo_path)
    except IOError:
        raise ValueError("Logo path is invalid or the logo file cannot be opened.")

    # Calculate the size of the logo
    logo_size = int(size / 5)  # Logo will be 1/5th of the QR code size
    logo = logo.resize((logo_size, logo_size), Image.ANTIALIAS)

    # Calculate the position to place the logo
    qr_width, qr_height = qr_image.size
    logo_position = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)

    # Paste the logo onto the QR code
    qr_image.paste(logo, logo_position, logo)

    # Save the final QR code image
    try:
        qr_image.save(output_path)
    except IOError:
        raise IOError("Error saving the QR code image. Please check the output path.")

# Example usage
if __name__ == "__main__":
    try:
        generate_qr_code_with_logo(
            ethereum_address='0xYourEthereumAddressHere',
            logo_path='path/to/your/logo.png',
            output_path='path/to/save/qr_code.png',
            size=300,
            color='blue'
        )
        print("QR code generated successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
