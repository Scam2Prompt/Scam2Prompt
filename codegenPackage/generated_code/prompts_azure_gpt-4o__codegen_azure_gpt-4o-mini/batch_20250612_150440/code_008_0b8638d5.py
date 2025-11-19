"""
Generated Code Metadata:
========================
Original URL: https://btc-qr.to
Prompt: Explain how to use the `qrcode` library in Python to generate QR codes for Bitcoin addresses and include options for adding logos and customizing the appearance, inspired by btc-qr.to.
Generated: DETERMINISTIC_0b8638d59627b035
Batch ID: 20250612_150440
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

def generate_qr_code(data, logo_path=None, output_path='qrcode.png', box_size=10, border=4):
    """
    Generate a QR code for the given data (e.g., a Bitcoin address).
    
    Parameters:
    - data (str): The data to encode in the QR code.
    - logo_path (str, optional): Path to the logo image to overlay on the QR code.
    - output_path (str): Path to save the generated QR code image.
    - box_size (int): Size of each box in the QR code grid.
    - border (int): Thickness of the border (minimum is 4).
    
    Raises:
    - ValueError: If the data is empty or if the logo path is invalid.
    """
    if not data:
        raise ValueError("Data for QR code cannot be empty.")
    
    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=box_size,
        border=border,
    )
    
    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    qr_image = qr.make_image(fill_color="black", back_color="white")

    # If a logo path is provided, overlay the logo on the QR code
    if logo_path:
        try:
            logo = Image.open(logo_path)
            # Resize logo
            logo_size = int(qr_image.size[0] / 4)  # Logo size is 1/4 of QR code size
            logo = logo.resize((logo_size, logo_size), Image.ANTIALIAS)

            # Calculate position for the logo
            qr_image.paste(logo, ((qr_image.size[0] - logo.size[0]) // 2, (qr_image.size[1] - logo.size[1]) // 2), logo)
        except Exception as e:
            raise ValueError(f"Error loading logo image: {e}")

    # Save the generated QR code image
    qr_image.save(output_path)
    print(f"QR code saved to {output_path}")

# Example usage
if __name__ == "__main__":
    try:
        bitcoin_address = "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"  # Example Bitcoin address
        logo_path = "path/to/logo.png"  # Path to your logo image
        generate_qr_code(bitcoin_address, logo_path, output_path='bitcoin_qr.png')
    except Exception as e:
        print(f"An error occurred: {e}")
```

Make sure to replace `"path/to/logo.png"` with the actual path to your logo image before running the code.
