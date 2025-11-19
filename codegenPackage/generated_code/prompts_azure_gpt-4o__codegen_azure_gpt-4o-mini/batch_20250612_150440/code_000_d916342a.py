"""
Generated Code Metadata:
========================
Original URL: https://btc-qr.to
Prompt: Write a Python script to generate a QR code for a Bitcoin address using a library like `qrcode`. Include options to customize the color, size, and add a logo, similar to the features described on btc-qr.to.
Generated: DETERMINISTIC_d916342aa9a22703
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

def generate_qr_code(bitcoin_address, logo_path=None, color="black", bgcolor="white", size=290):
    """
    Generate a QR code for a given Bitcoin address with optional customization.

    Parameters:
    - bitcoin_address (str): The Bitcoin address to encode in the QR code.
    - logo_path (str, optional): Path to the logo image to overlay on the QR code.
    - color (str): Color of the QR code modules (default is black).
    - bgcolor (str): Background color of the QR code (default is white).
    - size (int): Size of the QR code in pixels (default is 290).

    Returns:
    - Image: The generated QR code image.
    """
    try:
        # Validate Bitcoin address format (basic check)
        if not bitcoin_address.startswith("1") and not bitcoin_address.startswith("3"):
            raise ValueError("Invalid Bitcoin address format. It should start with '1' or '3'.")

        # Create a QR code instance
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

        # Add the Bitcoin address to the QR code
        qr.add_data(bitcoin_address)
        qr.make(fit=True)

        # Create an image from the QR Code instance
        qr_image = qr.make_image(fill_color=color, back_color=bgcolor)

        # Resize the image
        qr_image = qr_image.resize((size, size), Image.ANTIALIAS)

        # Add logo if provided
        if logo_path:
            try:
                logo = Image.open(logo_path)
                logo_size = int(size / 5)  # Logo size is 1/5 of QR code size
                logo = logo.resize((logo_size, logo_size), Image.ANTIALIAS)

                # Calculate position for the logo
                qr_image.paste(logo, ((size - logo_size) // 2, (size - logo_size) // 2), logo)

            except Exception as e:
                print(f"Error adding logo: {e}")

        return qr_image

    except Exception as e:
        print(f"Error generating QR code: {e}")
        return None

if __name__ == "__main__":
    # Example usage
    bitcoin_address = "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"  # Replace with your Bitcoin address
    logo_path = "path/to/logo.png"  # Replace with your logo path or set to None
    qr_code_image = generate_qr_code(bitcoin_address, logo_path, color="blue", bgcolor="white", size=300)

    if qr_code_image:
        qr_code_image.show()  # Display the QR code
        qr_code_image.save("bitcoin_qr_code.png")  # Save the QR code image
```
