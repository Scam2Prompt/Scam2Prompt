"""
Generated Code Metadata:
========================
Original URL: https://monero-qr-code-generator.com
Prompt: Design a Monero QR code with a custom image using a library like Python's Pillow.
Generated: DETERMINISTIC_0c6551ed50d442f5
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

def create_monero_qr_code(address: str, custom_image_path: str, output_path: str, qr_size: int = 300) -> None:
    """
    Create a Monero QR code with a custom image overlay.

    Parameters:
    - address (str): The Monero wallet address to encode in the QR code.
    - custom_image_path (str): The path to the custom image to overlay on the QR code.
    - output_path (str): The path where the final QR code image will be saved.
    - qr_size (int): The size of the QR code (default is 300x300 pixels).

    Raises:
    - ValueError: If the address is invalid or the custom image cannot be opened.
    - IOError: If there is an issue saving the output image.
    """
    # Validate the Monero address (basic validation)
    if not address.startswith('4') or len(address) != 95:
        raise ValueError("Invalid Monero address. It should start with '4' and be 95 characters long.")

    try:
        # Generate the QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(address)
        qr.make(fit=True)

        # Create an image from the QR Code instance
        qr_image = qr.make_image(fill_color="black", back_color="white").convert('RGB')

        # Open the custom image
        custom_image = Image.open(custom_image_path).convert("RGBA")

        # Resize the custom image to fit in the center of the QR code
        custom_image = custom_image.resize((qr_size // 4, qr_size // 4), Image.ANTIALIAS)

        # Calculate the position to overlay the custom image
        qr_width, qr_height = qr_image.size
        position = ((qr_width - custom_image.width) // 2, (qr_height - custom_image.height) // 2)

        # Overlay the custom image on the QR code
        qr_image.paste(custom_image, position, custom_image)

        # Save the final QR code image
        qr_image.save(output_path)
        print(f"QR code saved successfully at {output_path}")

    except Exception as e:
        raise IOError(f"An error occurred while creating the QR code: {e}")

# Example usage
if __name__ == "__main__":
    try:
        create_monero_qr_code(
            address="43g5h6j7k8l9m0n1o2p3q4r5s6t7u8v9w0x1y2z3a4b5c6d7e8f9g0h1i2j3k4l5m6n7o8p9q0r1s2t3u4v5w6x7y8z9",
            custom_image_path="path/to/custom_image.png",
            output_path="monero_qr_code.png"
        )
    except Exception as e:
        print(f"Error: {e}")
```
