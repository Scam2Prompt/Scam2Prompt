"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btc-qr.to
Prompt: Write a Python script to generate a QR code for a Bitcoin address using a library like `qrcode`. Include options to customize the color, size, and add a logo, similar to the features described on btc-qr.to.
Generated: DETERMINISTIC_d916342aa9a22703
Batch ID: 20250612_150440
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

def generate_qr_code(data, logo_path=None, color="black", bg_color="white", size=10, logo_size=(50, 50)):
    """
    Generate a QR code with customizable options.

    Parameters:
    - data (str): The data to be encoded (e.g., a Bitcoin address).
    - logo_path (str): Path to the logo image file, if any (default is None).
    - color (str): QR code color (default is black).
    - bg_color (str): Background color (default is white).
    - size (int): Size of the QR code (default is 10).
    - logo_size (tuple): Size of the logo (default is (50, 50)).

    Returns:
    - Image object of the generated QR code.
    """
    
    try:
        # Create a QR code instance
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=size,
            border=4,
        )

        # Add data to the QR code
        qr.add_data(data)
        qr.make(fit=True)

        # Create an image from the QR code instance
        qr_image = qr.make_image(fill_color=color, back_color=bg_color)

        # If a logo is provided, overlay it on the QR code
        if logo_path:
            logo = Image.open(logo_path).convert("RGBA")
            logo = logo.resize(logo_size, Image.ANTIALIAS)

            # Calculate position to center the logo
            qr_image.paste(logo, ((qr_image.size[0] - logo.size[0]) // 2,
                                   (qr_image.size[1] - logo.size[1]) // 2), logo)

        return qr_image

    except Exception as e:
        print(f"Error generating QR code: {e}")
        return None

def save_qr_code(image, output_path):
    """
    Save the generated QR code image to a file.

    Parameters:
    - image (Image): The QR code image to save.
    - output_path (str): The path where the image will be saved.
    """
    try:
        if image:
            image.save(output_path)
            print(f"QR code saved to {output_path}")
        else:
            print("No image to save.")
    except Exception as e:
        print(f"Error saving QR code: {e}")

if __name__ == "__main__":
    # Example usage
    bitcoin_address = "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"  # Replace with your Bitcoin address
    logo_path = "path/to/logo.png"  # Replace with your logo path
    output_path = "bitcoin_qr_code.png"  # Output path for the QR code image

    # Generate QR code with custom options
    qr_image = generate_qr_code(bitcoin_address, logo_path=logo_path, color="blue", bg_color="yellow", size=10)

    # Save the generated QR code image
    save_qr_code(qr_image, output_path)
```

Make sure to replace `"path/to/logo.png"` with the actual path to your logo image. Ensure you have the required libraries installed by running:
```bash
pip install qrcode[pil] Pillow
```
