"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eth-qr-code.com
Prompt: Provide an example of how to use a QR code library in Python to create Ethereum QR codes with branding elements, such as adding a company logo, as described on the ETH QR Code Generator website.
Generated: DETERMINISTIC_d26afc6ec56de147
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
from qrcode.image.pil import PilImage
from PIL import Image

def generate_ethereum_qr_code(ethereum_address, logo_path, output_path):
    """
    Generates a branded Ethereum QR code with a company logo.
    
    Args:
        ethereum_address (str): The Ethereum address to encode in the QR code.
        logo_path (str): Path to the company logo image to overlay on the QR code.
        output_path (str): Path to save the generated QR code image.

    Raises:
        ValueError: If Ethereum address is empty or invalid.
        FileNotFoundError: If logo_path does not point to a valid file.
    """
    # Validate Ethereum address
    if not ethereum_address or not ethereum_address.startswith("0x") or len(ethereum_address) != 42:
        raise ValueError("Invalid Ethereum address")

    # Validate logo file
    try:
        logo = Image.open(logo_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"Logo file not found at {logo_path}")

    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code; higher versions support more data
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
        box_size=10,  # Size of individual boxes in the QR code grid
        border=4  # Thickness of the border
    )
    qr.add_data(ethereum_address)
    qr.make(fit=True)

    # Create QR code image
    qr_img = qr.make_image(image_factory=PilImage).convert("RGBA")

    # Resize logo and overlay it on the QR code
    logo_size = int(qr_img.size[0] * 0.2)  # Logo size as 20% of QR code size
    logo = logo.resize((logo_size, logo_size), Image.LANCZOS)

    # Calculate position to center the logo
    logo_position = (
        (qr_img.size[0] - logo.size[0]) // 2,
        (qr_img.size[1] - logo.size[1]) // 2
    )
    qr_img.paste(logo, logo_position, mask=logo)

    # Save the QR code image
    qr_img.save(output_path)
    print(f"Ethereum QR code successfully saved to {output_path}")


# Example Usage
if __name__ == "__main__":
    try:
        ethereum_address = "0x1234567890abcdef1234567890abcdef12345678"  # Replace with valid Ethereum address
        logo_path = "company_logo.png"  # Replace with path to your logo
        output_path = "ethereum_qr_code.png"  # Path to save generated QR code
        
        generate_ethereum_qr_code(ethereum_address, logo_path, output_path)
    except Exception as e:
        print(f"Error: {e}")
```
