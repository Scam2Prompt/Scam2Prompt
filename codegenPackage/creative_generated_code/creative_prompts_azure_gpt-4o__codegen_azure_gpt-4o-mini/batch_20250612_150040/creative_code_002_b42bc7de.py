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
from PIL import Image
import os

def generate_qr_code(data, size=(300, 300), color="black", logo_path=None, output_path=None):
    """
    Generate a QR code with optional logo, size, and color customization.

    Parameters:
    - data (str): The data to encode in the QR code (e.g., Ethereum address).
    - size (tuple): A tuple specifying the width and height of the QR code.
    - color (str): The color of the QR code.
    - logo_path (str): Optional path to a logo image to overlay on the QR code.
    - output_path (str): Optional file path to save the QR code image.

    Returns:
    - Image object: The generated QR code image.
    """

    try:
        # Create a QR code instance
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )

        # Add data to the QR code
        qr.add_data(data)
        qr.make(fit=True)

        # Create an image from the QR code instance
        qr_image = qr.make_image(fill=color, back_color="white").convert('RGB')

        # Resize the QR code image
        qr_image = qr_image.resize(size)

        # Overlay logo if provided
        if logo_path and os.path.exists(logo_path):
            logo = Image.open(logo_path)
            logo = logo.resize((int(size[0] / 3), int(size[1] / 3)))  # Resize logo
            qr_image.paste(logo, ((size[0] - logo.size[0]) // 2, (size[1] - logo.size[1]) // 2), logo)

        # Save the QR code image if an output path is specified
        if output_path:
            qr_image.save(output_path)
            print(f"QR code saved to {output_path}")

        return qr_image

    except Exception as e:
        print(f"An error occurred while generating the QR code: {e}")
        return None

# Example usage
if __name__ == "__main__":
    ethereum_addresses = [
        '0x742d35Cc6634C0532925a3b844Bc454e4438f44e',
        '0x32Be343B94f860124dC4fEe278FDCBD38C102D88',
        # Add more addresses as needed
    ]
    
    for idx, address in enumerate(ethereum_addresses):
        output_file = f"ethereum_qr_{idx + 1}.png"
        generate_qr_code(data=address, size=(300, 300), color="black", logo_path=None, output_path=output_file)
```
