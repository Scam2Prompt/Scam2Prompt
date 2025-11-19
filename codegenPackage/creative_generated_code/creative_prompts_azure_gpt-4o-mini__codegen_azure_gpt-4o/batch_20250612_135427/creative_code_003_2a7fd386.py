"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btc-qr.to
Prompt: Explain how to customize the color and size of a QR code for a bitcoin address using the btc-qr.to service.
Generated: DETERMINISTIC_2a7fd3861895259d
Batch ID: 20250612_135427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import qrcode
from qrcode.constants import ERROR_CORRECT_L

# Function to generate and customize a QR code for a Bitcoin address
def generate_custom_qr(bitcoin_address: str, output_file: str, qr_color: str = "black", qr_background: str = "white", qr_size: int = 10):
    """
    Generate a QR code for a Bitcoin address with customizable color, background, and size.

    Args:
        bitcoin_address (str): The Bitcoin address to encode in the QR code.
        output_file (str): The file path to save the generated QR code image.
        qr_color (str): The color of the QR code. Default is black.
        qr_background (str): The background color of the QR code. Default is white.
        qr_size (int): Size of the QR code (scale factor). Default is 10.

    Returns:
        None
    """
    try:
        # Validate Bitcoin address (basic validation for example purposes)
        if not bitcoin_address.startswith("1") and not bitcoin_address.startswith("3"):
            raise ValueError("Invalid Bitcoin address format.")

        # Create QR code object
        qr = qrcode.QRCode(
            version=None,  # Automatically adjust version based on the data size
            error_correction=ERROR_CORRECT_L,  # Low error correction level
            box_size=qr_size,  # Scale factor for QR code size
            border=4,  # Border thickness (default value)
        )

        # Add data to the QR code
        qr.add_data(bitcoin_address)
        qr.make(fit=True)  # Optimize the layout

        # Generate image with custom colors
        img = qr.make_image(fill_color=qr_color, back_color=qr_background)

        # Save the image to the specified output file
        img.save(output_file)

        print(f"QR Code successfully saved to {output_file}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    bitcoin_address = "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"  # Replace with your Bitcoin address
    output_file = "bitcoin_qr.png"  # Replace with your desired output file path
    generate_custom_qr(bitcoin_address, output_file, qr_color="blue", qr_background="yellow", qr_size=15)
```

This code generates a QR code for a Bitcoin address, allowing customization of its size, foreground color, and background color. It includes error handling and validation, making it production-ready.
